# Etapa 1: Flujo GitOps IoT GitLab
## CI
- Análisis de código fuente con SonarQube.
- Build de la imagen de la aplicación y pushear la imagen a GitLab Container Registry.
- Análisis del contenedor con Trivy.
- Enviar trigger al repositorio de configuración.

## CD
- Recibe el trigger del repositorio de la aplicación.
- Mediante ssh, despliega la aplicación del repositorio en argocd de la máquina virtual y se sincroniza.
