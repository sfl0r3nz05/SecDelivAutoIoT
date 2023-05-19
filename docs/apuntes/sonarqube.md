# SonarQube
## sonar-project.properties
El fichero `sonar-project.properties` sirve para configurar y personalizar el análisis estático del código fuente realizado por SonarQube. Este archivo de propiedades permite especificar diferentes parámetros y ajustes que son utilizados por SonarQube durante el análisis.

Estas son algunas de las configuraciones:
1. **Información del proyecto**: Se puede proporcionar información básica sobre el proyecto (nombre, versión, descripción...)
2. **Ubicación del código fuente**: Se puede indicar la ruta o las rutas de los archivos de código fuente que se deben analizar.
3. **Exclusiones**: Se pueden especificar patrones de exclusión para archivos o directorios que no deben ser analizados.

El archivo "sonar-project.properties" se coloca en la raíz del proyecto y es leído por SonarQube durante el análisis. Proporciona una forma estructurada y configurable de definir las opciones de análisis para cada proyecto, lo que permite adaptar el análisis de SonarQube a las necesidades específicas de cada proyecto y equipo de desarrollo.

## Variables de entorno
### SonarQube Token
Es una variable de entorno utilizada en la configuración de integración continua (CI) para autenticar y autorizar el análisis de código con SonarQube. Cuando se realiza un análisis con SonarQube, se necesita un token de acceso válido para identificar y autenticar el proyecto que está siendo analizado. El token se utiliza para establecer una conexión segura entre el servidor de SonarQube y la instancia de CI. Al configurar y proporcionar el valor de `SONAR_TOKEN`, se asegura que solo los proyectos autorizados y con los permisos adecuados puedan realizar análisis en la instancia de SonarQube, manteniendo la seguridad y control del sistema.

### SonarQube URL
Es una variable de entorno utilizada en la configuración de integración continua (CI) para especificar la URL o la dirección del servidor de SonarQube al que se debe conectar durante el análisis de código. Cuando se realiza un análisis con SonarQube, es necesario indicar la ubicación del servidor de SonarQube para enviar los resultados del análisis y obtener las métricas y recomendaciones correspondientes. Al configurar y proporcionar el valor de SONAR_HOST_URL, se establece la conexión correcta entre el sistema de CI y el servidor de SonarQube, lo que permite enviar los resultados del análisis y recibir información detallada sobre la calidad del código.

## .gitlab-ci.yml
```
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
  allow_failure: true
```

### script
En la parte del script, se ejecuta el comando `sonar-scanner`. Este comando invoca al cliente de SonarQube, que se encarga de realizar el análisis estático del código fuente del proyecto y enviar los resultados al servidor de SonarQube especificado.

Durante la ejecución de `sonar-scanner`, ocurren los siguientes pasos:
1. El cliente de SonarQube analiza los archivos de código fuente presentes en el proyecto según las configuraciones definidas en el archivo `sonar-project.properties`.
2. El cliente de SonarQube recopila diversas métricas y datos relacionados con la calidad del código, como la complejidad, las reglas de calidad violadas, las duplicaciones de código...
3. Los resultados del análisis se empaquetan y envían al servidor de SonarQube especificado en la variable de entorno `SONAR_HOST_URL`. El servidor de SonarQube procesa los resultados y almacena la información en su base de datos.
4. Una vez finalizado el análisis y la carga de datos en el servidor de SonarQube, se puede acceder a los resultados a través de la interfaz web de SonarQube. Estos resultados incluyen información sobre la calidad del código, problemas identificados, métricas y recomendaciones para mejorar la calidad y el rendimiento del código.

### image
Se utiliza para especificar la imagen de Docker que se utilizará para ejecutar el análisis con SonarQube. Al especificar la imagen de Docker que contiene el cliente de línea de comandos de SonarQube, se asegura que el job tenga acceso a las herramientas necesarias para realizar el análisis del código. La imagen sonarsource/sonar-scanner-cli proporciona una configuración predefinida y lista para usar del cliente de SonarQube, lo que simplifica el proceso de análisis y asegura la compatibilidad con SonarQube.
- `name: sonarsource/sonar-scanner-cli:latest`: Indica el nombre de la imagen de Docker que se utilizará para este job. En este caso, se utiliza la imagen `sonarsource/sonar-scanner-cli` proporcionada por SonarSource, que contiene el cliente de línea de comandos (CLI) de SonarQube.
- `entrypoint: [""]`:  Anula cualquier comando de entrada predeterminado especificado en la imagen Docker.

### variables
- `SONAR_USER_HOME: "${CI_PROJECT_DIR}/.sonar"`: Esta variable define la ubicación del directorio de caché de tareas de análisis. `${CI_PROJECT_DIR}` es una variable de entorno proporcionada por GitLab que apunta al directorio raíz del proyecto en el repositorio. `${CI_PROJECT_DIR}/.sonar` se utiliza para almacenar información y datos relacionados con el análisis de código, como la configuración, los resultados anteriores y otros archivos de caché.
- `GIT_DEPTH: "0"`: Esta variable se utiliza para configurar la profundidad de clonación del repositorio Git durante el análisis. Al establecer `GIT_DEPTH` en "0", se indica a Git que descargue todo el historial del repositorio, incluyendo todas las ramas y commits. Esto es necesario para que el análisis de SonarQube pueda tener acceso a todo el código fuente del proyecto y realizar un análisis completo y preciso.

### cache
La sección `cache` sirve para configurar el almacenamiento en caché de los resultados del análisis realizados por SonarQube. Esto permite que los resultados del análisis se guarden en caché y se reutilicen en ejecuciones posteriores del job, lo que puede acelerar el proceso de análisis. Cuando se ejecuta el job de SonarQube, los resultados del análisis se almacenan en el directorio `.sonar/cache`. En ejecuciones posteriores del mismo job, si la caché con la misma clave aún existe, GitLab recupera los datos almacenados en la caché en lugar de realizar un análisis completo nuevamente.
- `key: "${CI_JOB_NAME}"`: Especifica una clave única para identificar y diferenciar la caché de este job de otros jobs en el pipeline. La variable `${CI_JOB_NAME}` hace referencia al nombre del job actual en el pipeline.
- `paths`: Define los directorios o archivos que se deben almacenar en caché. En este caso, se almacena en caché el directorio `.sonar/cache`, que es el directorio donde SonarQube guarda los archivos y datos relacionados con la caché de análisis.
