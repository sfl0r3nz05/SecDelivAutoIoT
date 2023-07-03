# Calificación de herramientas de seguridad
## SonarQube
### Descripción
SonarQube es una herramienta de análisis de calidad de código y seguridad que permite a los desarrolladores mejorar la calidad del código y detectar vulnerabilidades de seguridad temprano en el ciclo de vida del desarrollo de software.

### Diseño


### Implementación
Para ejecutar SonarQube, tenemos que desplegar el contenedor Docker con SonarQube en la misma máquina que el runner de GitLab. Para crear un runner local de GitLab, hemos seguido las siguientes guías: [Instalación de GitLab Runner en Windows](https://docs.gitlab.com/runner/install/windows.html#installation) y [Reggistro de GitLab Runner en Windows](https://docs.gitlab.com/runner/register/index.html#windows).

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
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Captura%20Analisis%20SonarQube.PNG" alt="Captura de análisis de SonarQube">

## MobsSF Scan
### Descripción
Mobile Security Framework (MobSF) es una plataforma de pruebas de seguridad móvil de código abierto que permite a los desarrolladores evaluar la seguridad de aplicaciones Android. MobSF se utiliza para realizar análisis estático y dinámico de aplicaciones móviles con el objetivo de identificar vulnerabilidades y mejorar la seguridad de la aplicación.

### Diseño


### Implementación
Para realizar el análisis del repositorio, simplemente tendremos que añadir este job al archivo `.gitlab-ci.yml`:
```
# Analizar código fuente con MobSF
mobsfscan-check:
  stage: check
  tags:
    - SecDelivAutoIoT
  image: python
  before_script:
    - pip install --upgrade pip
    - pip3 install --upgrade mobsfscan
  script:
    - mobsfscan .
```
Este es una captura de un ejemplo que tendría que salir al ejecutar el análisis:
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Captura%20Pipeline%20MobSF.PNG" alt="Captura de un análisis de MobSF">
