# CI/CD Demo
En la demo se va a aprender a crear CI/CD pipeline con DroneCI y ArgoCD. Se utilizará DroneCI para ejecutar tests, publicar imágenes, y actualizar etiquetas de imagen en el repositorio de manifiesto. Y utilizaremos ArgoCD para Entrega Continua, sincronización de estados de la aplicaciones en el cluster de Kubernetes con los manifiestos mantenidos en el repositorio de Git.

![Arquitectura CICD Demo](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Aquitectura%20CICD%20Demo.png "Arquitectura CICD Demo")

## Prerequisitos
### [Instalr sevidor Drone para GitHub](https://docs.drone.io/server/provider/github/)
- Servidor Drone
  - [Instalación GitHub](https://docs.drone.io/server/provider/github/)
- Cluster K8s
  - minikube
- ArgoCD deployment
  - [Instalación todo en uno](https://argo-cd.readthedocs.io/en/stable/getting_started/#1-install-argo-cd)
- Cuenta de GitHub y DockerHub

## DroneCI
### Setup
Después de conectar GitHub con Drone, ya se puede seleccionar el repositorio. Después, clonar el repositorio, activarlo y navegar a `Repositories -> cicd-demo -> settings` y añadir los secretos:
- `docker_password`: cuenta de DockerHub.
- `docker_username`: contraseña de DockerHub.
- `ssh_key`: clave privada RSA codificada en base64 para acceder a GitHub.

## Referencias
- CI/CD Demo - [github.com](https://github.com/minghsu0107/cicd-demo)
