# Jenkins
## Instalación
En Visual Studio Code he ejecutado el siguiente comando para descargar la imagen Docker de Jenkins:
```
docker pull jenkins/jenkins
```

Una vez descargada la imagen Docker de Jenkins, se ejecuta el siguiente comando para ejecutar la imagen en un contenedor Docker:
```
docker run -d -p 8080:8080 -p 50000:50000 jenkins/jenkins
```
Con socket docker:
```
docker run -d \
  -p 8080:8080 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -u root \
  --name jenkins \
  jenkins/jenkins:lts
```

### Cambio de nombre del conetenedor
Al iniciar el contenedor, el nombre del contenedor es `charming_mayer`. Entonces para cambiar el nombre del contenedor a `jenkins` ejecutar el siguiente comando:
```
docker rename charming_mayer jenkins
```

## Primeros pasos de Jenkins
Al acceder a `localhost:8080` te pide una contraseña de Jenkins. Para saber la contraseña, hay que ejecutar lo siguiente para poder acceder a la contraseña dentro del contenedor:
```
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

## Configurar pipeline Jenkins
Para poder utilizar el archivo `Jenkinsfile` en el pipeline de Jenkin, hay que entrar en la configuración del pipeline y poner los siguientes ajustes:
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Configuraci%C3%B3n%20Pipeline%20Jenkins.PNG">

## SonarQube
En mi caso, estoy ejecutando Sonarqube y Jenkins en contenedores distintos en mi host (ya están creados). Entonces lo primero de todo hay que crear el network y añadir Sonarqube y Jenkins a un network de docker:
```
docker network create secdelivautoiot
docker network connect secdelivautoiot jenkins
docker network connect secdelivautoiot sonarqube
```

### Configuración global
`Administrar Jenkins` --> `System` --> `SonarQube servers`:
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Configuraci%C3%B3n%20Global%20SonarQube.PNG">

### Primera ejecución del pipeline
Para la primera ejecución del pipeline, hay que descargar sonarqube. Yo he cambiado el nombre a la carpeta de sonarqueb una vez descomprimida para facilitar el nombre a sonar-scanner:
```
// Analisis SonarQube
stage('sonarqube-check') {
  steps {
    // Descargar SonarQube en el directorio del workspace
    sh 'curl -o sonarqube.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.8.0.2856-linux.zip'
    sh 'unzip /var/jenkins_home/workspace/SecDelivAutoIoT/sonarqube.zip'
    // Cambiar el nombre de la carpeta a sonar-scanner
    sh 'mv /var/jenkins_home/workspace/SecDelivAutoIoT/sonar-scanner-4.8.0.2856-linux /var/jenkins_home/workspace/SecDelivAutoIoT/sonar-scanner'

    // Ejecutar SonarQube Scanner
    withSonarQubeEnv('sonarqube') {
      sh "/var/jenkins_home/workspace/SecDelivAutoIoT/sonar-scanner/bin/sonar-scanner"
    }
  }
}
```
Una vez ejecutado esta primera vez, ya tendremos el workspace configurado para ejecutar lo siguiente a partir de ahora:
```
stage('sonarqube-check') {
  steps {
    // Ejecutar SonarQube Scanner
    withSonarQubeEnv('sonarqube') {
      sh "/var/jenkins_home/workspace/SecDelivAutoIoT/sonar-scanner/bin/sonar-scanner"
    }
  }
}
```

## Push Docker Hub
Para poder contruir y pushear una imagen a Docker Hub, tenemos que descargar los plugins de `Docker` y `Docker pipeline`. Una vez hecho esto, Tenmos que añadir el siguiente stage al archivo `Jenkinsfile`:
```
stage('Build and Publish Image to Docker Hub') {
  steps {
    script {
      docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
        git 'https://gitlab.com/mikel-m/SecDelivAutoIoT.git'
        docker.build('mikelm98/secdelivautoiot').push('latest')
      }
    }
  }
}
```

## Plugins instalados
- GitLab Plugin
- SonarQube Scanner for Jenkins
- Docker Pipeline
- Docker
