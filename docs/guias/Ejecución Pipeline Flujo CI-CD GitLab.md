# Flujo CI/CD GitLab
En esta guía vamos a ver cómo ejecutar un flujo CI/CD utilizando GitLab CI/CD des dos repositorios ([aplicación](https://gitlab.com/mikel-m/SecDelivAutoIoT) y [configuración](https://gitlab.com/mikel-m/configSecDelivAutoIoT)).

## Crear aplicación
Como lo que vamos a analizar es el flujo CI/CD, hemos creado una aplicación de prueba llamada `helloworld.py`:
```
# helloworld.py
from flask import Flask
import sys

app = Flask(__name__)

# Endpoint principal
@app.route('/')
def hello():
    return '¡Hola, mundo!'

# Endpoint para verificar el estado de salud
@app.route('/health')
def health_check():
    # Comprueba cualquier condición de salud aquí
    # Si todas las condiciones son correctas, devuelve un código de estado 200 "OK"
    # De lo contrario, devuelve un código de estado 500 "Internal Server Error"
    # Puedes personalizar las condiciones según las necesidades de tu aplicación
    if all_conditions_are_met():
        return '', 200
    else:
        return '', 500

def all_conditions_are_met():
    # Aquí puedes implementar tus propias condiciones de salud
    # Por ejemplo, verifica si todas las conexiones a bases de datos están activas,
    # si los servicios externos están disponibles, etc.
    # Si todas las condiciones son correctas, devuelve True; de lo contrario, False.
    return True

if __name__ == '__main__':
    # Obtén el puerto del argumento de línea de comandos o utiliza un valor predeterminado
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    # Inicia la aplicación Flask en el puerto especificado
    app.run(port=port)
```

```
# requirements.txt
flask
```

## Crear el archivo `.gitlab-ci.yml`
Lo primero que hay que hacer es crear el archivo `.gitlab-ci.yml` en los dos repositorios (uno en cada repositorio), que es el archivo que se encarga de ejecutar el pipeline y desencadenar las tareas cada vez que hay un cambio en el repositorio.

## GitLab CI/CD del repositorio de la aplicación
### Declarar los stages
GitLab CI/CD funciona por stages, que se puede describir como etapas del pipeline. En nuestro caso, vamos a tener 4 stages: check, build, analyze y deploy. Para declarar los stagen, tenemos que añadir lo siguiente al inicio del archivo `.gitlab-ci.yml`:
```
stages:
  - check
  - build
  - analyze
  - deploy
```
GitLab CI/CD se divide en jobs que se ejecutan dentro de cada stage. Nosotros vamos a realizar 4 jobs: sonarqube-check, release_dockerhub, trivy_dockerhub y trigger_second_repository.

### sonarqube-check
En nuestro caso, vamos a ejecutar el servidor de SonarQube en la misma máquina en la que está el runner de GitLab. Para crear un runner local de GitLab, hemos seguido las siguientes guías: [Instalación de GitLab Runner en Windows](https://docs.gitlab.com/runner/install/windows.html#installation) y [Reggistro de GitLab Runner en Windows](https://docs.gitlab.com/runner/register/index.html#windows).

Una vez registrado el runner localmente, desplegamos un contenedor docker con el servidor de SonarQube. Para ello, ejecutamos el siguiente comando en Visual Studio Code:
```powershell
docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest
```

Una vez corriendo el contenedor, accedos a la siguiente URL: [http://localhost:9000/](http://localhost:9000/). Te pedirá usuario y contraseña y la primera vez el usuario es `admin` y la contraseña es `admin`.

Lo primero que te saldrá será para crear un nuevo proyecto, en nuestro caso, seleccionamos GitLab. Nos pedirá el nombre de la configuración (que podemos poner el que queramos), GitLab API URL (que hay que poner `https://gitlab.com/api/v4`) y el token de acceso de GitLab. Para crear el token de acceso de GitLab, accedemos a nuestro repositorio de GitLab y en el menú de la izquierda desplegamos `Settings` y clicamos en `Access Tokens`, rellenamos los campos y seleccionamos el scope `api`. Al crear el token, copia el token (guardalo bien ya que una vez que salgas ya no podrás acceder al token) y pegalo en la configuración de sonarqube.

Una vez realizada la configuración te sale diferentes opciones para realizar el análisis. En nuestro caso, seleccionamos la opción `With GitLab CI/CD` y seguimos los pasos que pone. En nuesto caso, en el primer paso seleccionamos `Other` y creamos el archivo `sonar-project.properties` en el repositorio con el código que nos pone. Después añadimos las variables de entorno como nos pone. En el tercer paso nos pone un código de ejemplo que hay que poner en el archivo `.gitlab-ci.yml`. En nuestro caso, ponemos lo siguiente:
```
# Analizar código fuente con sonarqube
sonarqube-check:
  stage: check
  image: 
    name: sonarsource/sonar-scanner-cli:latest
    entrypoint: [""]
  variables:
    SONAR_USER_HOME: "${CI_PROJECT_DIR}/.sonar"  # Defines the location of the analysis task cache
    GIT_DEPTH: "0"  # Tells git to fetch all the branches of the project, required by the analysis task
  cache:
    key: "${CI_JOB_NAME}"
    paths:
      - .sonar/cache
  script: 
    - sonar-scanner
  tags:
    - SecDelivAutoIoT
```

Una vez hecho esto, el servido se queda esperando hasta que ejecutemos el pipeline con la ejecución del análisis de SonarQube. Al terminar el análisis, tendría que salir algo similar a lo siguiente:
<img src="" alt="Captura de análisis de SonarQube">

### release_dockerhub
El siguiente job sirve para generar la imagen de la aplicación del repositorio y registrarla en Docker Hub. Para ello añadimos el siguiente código al archivo `.gitlab-ci.yml`:
```
# Registrar la imagen en Docker Hub
release_dockerhub:
  stage: build
  tags:
    - SecDelivAutoIoT
  image:
    name: gcr.io/kaniko-project/executor:debug
    entrypoint: [""]
  script:
    - mkdir -p /kaniko/.docker
    - echo "{\"auths\":{\"https://index.docker.io/v1/\":{\"auth\":\"$(echo -n "${DOCKER_USERNAME}:${DOCKER_PASSWORD}" | base64 -w0)\"}}}" > /kaniko/.docker/config.json
    - >-
      /kaniko/executor
      --context "${CI_PROJECT_DIR}/"
      --dockerfile "${CI_PROJECT_DIR}/Dockerfile"
      --destination "${DOCKER_USERNAME}/${DOCKER_REPOSITORY}:${CI_COMMIT_SHORT_SHA}"
    - echo $DOCKER_USERNAME/$DOCKER_REPOSITORY:$CI_COMMIT_SHORT_SHA
```

Para generar la imagen, hay que adaptar el archivo el archivo `Dockerfile` según las necesidades de la aplicación. En nuestro caso, como es una aplicación de prueba, este es el contenido del archivo `Dockerfile`:
```
# Docker file helloworld.py
# Utiliza la imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de la aplicación al directorio de trabajo
COPY helloworld.py .

# Instala las dependencias si las hay
# RUN pip install <nombre_dependencia>
RUN pip install flask

# Expone el puerto en el que la aplicación está escuchando
EXPOSE 3000

# Ejecuta el comando para iniciar la aplicación
CMD [ "python", "helloworld.py" ]
```

La imagen genrada tiene una forma similar a: 
