# Diseño de arquitectura de Flujo GitOps para dispositivos IoT en el contexto de GitLab
Un pipeline de CI/CD automatiza su proceso de entrega de software. El pipeline crea código, ejecuta pruebas (CI) e implementa de manera segura una nueva versión de la aplicación (CD). Los pipelines automáticos eliminan errores manuales. Con CI, cada cambio en el código desencadena una secuencia automatizada de compilación y prueba para el proyecto determinado. CD incluye la implementación de la infraestructura.

## Diseño
### Componentes
Identificar los componentes clave para implementar GitOps en el entorno IoT.
- Repositorio GitLab: es el repositorio donde se almacenará el código fuente de la aplicación.
- Raspberry Pi con K3s: es el dispositivo IoT que se encargará de la gestión del cluster Kubernetes y la ejecución de la infraestructura.
- ArgoCD: es el agente CI/CD que se encarga de la implementación de la aplicación y la configuración de la infraestructura en el cluster Kubernetes.
- Herramienta de análisis de seguridad: es la herramienta (o las herramientas) que se utilizará para el análisis de la seguridad del código.

### Flujo de trabajo
1. Los desarrolladores realizan cambios en el código de la aplicación y lo suben al repositorio de GitLab.
2. GitLab CI/CD desencadena la ejecución de los flujos de trabajo definidos en “.gitlab-ci.yml” para el build, test y deploy de la aplicación.
3. ArgoCD se encarga de la implementación de la aplicación y la configuración de la infraestructura en el cluster Kubernetes de la Raspberry Pi.
4. ArgoCD ejecuta los chequeos de seguridad (herramientas de análisis de seguridad).
5. Si las pruebas son exitosas, la aplicación se despliega automáticamente en producción.

### [Diseño de arquitectura](https://learn.microsoft.com/es-es/azure/architecture/example-scenario/gitops-aks/gitops-blueprint-aks#scenario-4-use-gitops-with-argo-cd-github-actions-and-aks-to-implement-cicd)
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/gitops-ci-cd-argo-cd.png" alt="GitOps CI/CD ArgoCD">

<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Flujo%20GitOps%20IoT%20GitLab.PNG" alt="Flujo GitOps IoT GitLab">

## Referencias
- Diseño, desarrollo e implementación de una arquitectura GitOps - [dspace.ups.edu.ec](https://dspace.ups.edu.ec/bitstream/123456789/22397/1/UPS-CT009712.pdf)
- GitOps para Azure Kubernetes Service - [learn.microsoft.com](https://learn.microsoft.com/es-es/azure/architecture/example-scenario/gitops-aks/gitops-blueprint-aks)
