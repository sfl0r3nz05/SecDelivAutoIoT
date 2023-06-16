# Jenkins
## Instalación
Lo primero que hay que hacer es generar el contenedor de jenkins con socket docker, para poder generar imágenes docker y poder subirlo a Docker Hub:
```powershell
docker run -d \
  -p 8080:8080 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -u root \
  --name jenkins \
  jenkins/jenkins:latest
```
O también de esta forma (lo mismo que el comando de arriba):
```powershell
docker run -d -p 8080:8080 -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -u root --name jenkins jenkins/jenkins:latest
```

### Cambio de nombre del conetenedor (opcional)
Al iniciar el contenedor, el nombre del contenedor es `charming_mayer`. Entonces para cambiar el nombre del contenedor a `jenkins` ejecutar el siguiente comando:
```powershell
docker rename charming_mayer jenkins
```

## Primeros pasos de Jenkins
Al acceder a `localhost:8080` te pide una contraseña de Jenkins. Para saber la contraseña, hay que ejecutar lo siguiente para poder acceder a la contraseña dentro del contenedor:
```powershell
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

## Configurar pipeline Jenkins
Para poder utilizar el archivo `Jenkinsfile` del repositorio de GitLab en el pipeline de Jenkin, hay que entrar en la configuración del pipeline y poner los siguientes ajustes:
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Configuraci%C3%B3n%20Pipeline%20Jenkins.PNG">

## SonarQube
En mi caso, estoy ejecutando Sonarqube y Jenkins en contenedores distintos en mi host (ya están creados). Entonces lo primero de todo hay que crear el network y añadir Sonarqube y Jenkins a un network de docker:
```powershell
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
stage('Analysis with SonarQube') {
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
// Analisis SonarQube
stage('Analysis with SonarQube') {
  steps {
    // Ejecutar SonarQube Scanner
    withSonarQubeEnv('sonarqube') {
      sh "/var/jenkins_home/workspace/SecDelivAutoIoT/sonar-scanner/bin/sonar-scanner"
    }
  }
}
```

## Push Docker Hub
Lo primero de todo, tenemos que instalar docker en el contenedor de Jenkins. Para eso, ejecutamos el siguiente comando para acceder al contenedor desde Visual Studio Code:
```powershell
docker exec -it -u 0 jenkins bash
```
Una vez dentro del contenedor instalamos docker con los siguientes comandos:
```powershell
apt-get update
apt-get install -y docker.io
```

Una vez instalado docker en el contenedor de Jenkins, para poder contruir y pushear una imagen a Docker Hub, tenemos que descargar los plugins de `Docker` y `Docker pipeline`. También hay que añadir las credenciales de Docker Hub con el usuario y contraseña. Una vez hecho esto, tenemos que añadir el siguiente stage al archivo `Jenkinsfile`:
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

## Analisis con Trivy
Al igual que hicimos anteriormente con docker, aquí también tenemos que instalar trivy en el contenedor de jenkins. Para ello, ejecutamos el de nuevo el siguiente comando en Visual Studio Code para acceder al contenedor:
```powershell
docker exec -it -u 0 jenkins bash
```
Una vez dentro, ejecutamos los siguientes comandos pra instalar trivy:
```powershell
apt-get update
apt-get install -y wget apt-transport-https gnupg lsb-release
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | apt-key add -
echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | tee -a /etc/apt/sources.list.d/trivy.list
apt-get update
apt-get install -y trivy
```
Una vez instalado, hay que añadir el siguiente stage para analizar la imagen con trivy:
```
// Analisis de imagen de Docker Hub con Trivy
stage('Image Analysis with Trivy') {
  steps {
    script {
      def imageName = 'mikelm98/secdelivautoiot:latest'
      def trivyReport = 'trivy-report.json'
                    
      // Descargar la imagen desde Docker Hub
      docker.image(imageName).pull()
                    
      // Ejecutar el escaneo de Trivy en la imagen
      sh "trivy image ${imageName} --format json --output ${trivyReport}"
                    
      // Publicar el informe de Trivy como artefacto en Jenkins
      archiveArtifacts artifacts: trivyReport, onlyIfSuccessful: false
    }
  }
}
```

## Desplegar imagen en ArgoCD
Para poder desplegar la imagen en ArgoCd desde el pipeline de Jenkins, hay que añadir el siguiente stage en el `Jenkinsfile`:
```
// Desplegar imagen a ArgoCD de la máquina virtual
stage('Deploy Image to ArgoCD') {
  steps {
    script {
      docker.image('ubuntu:latest').inside {
        sh 'apt-get update && apt-get install -y openssh-client sshpass'
        sh 'sshpass -p "$ARGOCD_PASSWORD_MV" ssh -o StrictHostKeyChecking=no $ARGOCD_USER_MV@$ARGOCD_IP_MV "argocd login localhost:32261 --insecure --username $ARGOCD_USERNAME --password $ARGOCD_PASSWORD"'
        sh 'sshpass -p "$ARGOCD_PASSWORD_MV" ssh -o StrictHostKeyChecking=no $ARGOCD_USER_MV@$ARGOCD_IP_MV "argocd app create secdelivautoiot --repo https://gitlab.com/mikel-m/SecDelivAutoIoT.git --path kubernetes --dest-server https://kubernetes.default.svc --dest-namespace secdelivautoiot"'
        sh 'sshpass -p "$ARGOCD_PASSWORD_MV" ssh -o StrictHostKeyChecking=no $ARGOCD_USER_MV@$ARGOCD_IP_MV "argocd app sync secdelivautoiot"'
      }
    }
  }
}
```
Para añadir las variables de entorno, `Administrar Jenkins` --> `System` y buscar el apartado de `Propiedades globales` y activar la opción `Variables de entorno`. Se despliega una lista y ahí puedes añadir el nombre de la variable y el valor.

## Plugins instalados
- GitLab Plugin
- SonarQube Scanner for Jenkins
- Docker Pipeline
- Docker

# Referencias
- Docker Pipeline plugin - [docs.cloudbees.com](https://docs.cloudbees.com/docs/cloudbees-ci/latest/pipelines/docker-workflow)
