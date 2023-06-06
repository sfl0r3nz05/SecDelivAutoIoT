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

## Plugins instalados
- GitLab Plugin
- SonarQube Scanner for Jenkins
- Slack Notification
