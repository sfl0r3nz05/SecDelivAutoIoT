# Diseño de arquitectura de Flujo GitOps para dispositivos Android en el contexto de GitLab
## Diseño
### Componentes
Identificar los componenetes clave para implementar GitOps en el entorno Android:
- Repositorio GitLab: es el repositorio donde se almacenará el código fuente de la aplicación y la configuración.
- GitLab CI/CD: es la herramienta que se encargará de la Integración Continua.
- Raspberry Pi con K3s: es el dispositivo IoT que se encargará de la gestión del cluster de Kubernetes y la ejecución de la infraestructura.
- ArgoCD: es el agente que se encarga de la implementación de la implementación de la aplicación y la configuración de la infraestructura en el cluster de Kubernetes.
- Herramienta de análisis de seguridad: es la herramienta (o herramientas) que se utilizará para el análisis (o chequeo) de la seguridad del código (por ejemplo, SonarQube).
- Play Store: es la tienda de Android donde se subirá la aplicación.

### Flujo de trabajo
1. Los desarrolladores realizan cambios en el código de la aplicación y lo suben al repositorio de GitLab.
2. GitLab CI/CD desencadena la ejecución de los flujos de trabajo definidos en “.gitlab-ci.yml” para el build, test y deploy de la aplicación. Aquí es donde se compilará la aplicación y generará el APK.
3. ArgoCD se encarga de la implementación de la aplicación y la configuración de la infraestructura en el cluster de Kubernetes de la Raspberry Pi.
4. ArgoCD ejecuta los chequeos de seguridad (herramientas de análisis de seguridad).
5. Si las pruebas son exitosas, ArgoCD construirá la imagen en el cluster de Kubernetes.
6. La aplicación se publicará en la Play Store.

### Diseño
<img src="" alt="Diseño arquitectura GitOps Android GitLab">

## Referencias
- Diseño, desarrollo e implementación de una arquitectura GitOps - [dspace.ups.edu.ec](https://dspace.ups.edu.ec/bitstream/123456789/22397/1/UPS-CT009712.pdf)
- GitOps para Azure Kubernetes Service - [learn.microsoft.com](https://learn.microsoft.com/es-es/azure/architecture/example-scenario/gitops-aks/gitops-blueprint-aks)
- Explaining GitOps: How does it work? - [youtube.com](https://www.youtube.com/watch?v=dIaX5IhRqkI&ab_channel=DevOpsJourney)


_[Se puede utilizar dos repositorios en vez de uno sólo. Uno para el código fuente y el otro para la configuración.]_
