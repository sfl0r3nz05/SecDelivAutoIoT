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
Se ejecuta el comando `sonar-scanner`. Este comando invoca al cliente de SonarQube, que se encarga de realizar el análisis estático del código fuente del proyecto y enviar los resultados al servidor de SonarQube especificado.

Durante la ejecución de `sonar-scanner`, ocurren los siguientes pasos:
1. El cliente de SonarQube analiza los archivos de código fuente presentes en el proyecto según las configuraciones definidas en el archivo `sonar-project.properties`.
2. El cliente de SonarQube recopila diversas métricas y datos relacionados con la calidad del código, como la complejidad, las reglas de calidad violadas, las duplicaciones de código...
3. Los resultados del análisis se empaquetan y envían al servidor de SonarQube especificado en la variable de entorno `SONAR_HOST_URL`. El servidor de SonarQube procesa los resultados y almacena la información en su base de datos.
4. Una vez finalizado el análisis y la carga de datos en el servidor de SonarQube, se puede acceder a los resultados a través de la interfaz web de SonarQube. Estos resultados incluyen información sobre la calidad del código, problemas identificados, métricas y recomendaciones para mejorar la calidad y el rendimiento del código.
