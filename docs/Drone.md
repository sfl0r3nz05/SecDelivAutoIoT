# Drone
Aunque la idea de un demonio al que se puede conectar por medio de sockets no le gustó mucho a la gente de coreos, esto abre la puerta a que un contenedor pueda crear contenedores en tiempo de ejecución, y este es el principio subyacente detrás de Drone.io.

El concepto de flujo se mantiene igual que en otras herramientas de integración continua, se definen un conjunto de pasos secuenciales que representan un estado en la aplicación:

- Clonado: se obtiene una copia del código fuente desde el Sistema de Control de Versiones.
- Pruebas: se ejecutan el conjunto de pruebas automáticas al código fuente, usualmente pruebas unitarias, de integración y punto a punto.
- Construcción: se construye un artefacto con el estado actual de la aplicación.
- Almacenamiento: se almacena el artefacto en un Repositorio de Artefactos.
- Despliegue: se actualiza la versión de los servidores a la nueva versión construida.

![Flujo de CI-CD por Drone](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Flujo%20de%20CI-CD%20por%20Drone.jpg "Flujo de CI-CD por Drone")

Sin pretender haber implementado a conformidad Continuous Integration, Continuous Delivery y Continuous Deployment, podemos decir que con este flujo estamos cumpliendo grandes prácticas de DevOps: las pruebas son el epicentro del Continuous Integration, el Repositorio de Artefactos se convierte en el centro del Continuous Delivery, y el despliegue de estos nuevos artefactos es el núcleo del Continuous Delivery.

El concepto más importante de Drone es que cada paso de flujo se ejecuta en un contenedor con un volumen compartido donde se almacena el código fuente, lo cual nos brinda flexibilidad, portabilidad y ligereza, también reduce ampliamente los tiempos de configuración de la herramienta, pues no es necesario realizar configuraciones adicionales por tecnología o lenguaje de programación.

Conceptos más relevantes de Drone:
1. **La fase de clonado**: no es obligatoria, pero en ella podemos definir las configuraciones para clonar el proyecto.
2. **El flujo**: depende en cada caso (Pruebas, Construcción/Almacenamiento, Despliegue y Notificación).
3. **Los plugins**: las fases de construcción, despliegue y notificación utilizan plugins para facilitar el proceso.
4. **La ejecución condicional**: el paso de despliegue solo se utiliza cuando es llamado desde la rama env/production.
5. **Los secretos**: información confidencial, como las credenciales de acceso al registry de docker y el acceso al cluster de kubernetes son ocultadas y manejadas por el manejador de secretos de drone.

## Características de Drone
- Open-source, desarrollado por una enorme comunidad.
- Fácil de instalar y mantener.
- Basado en Docker, todo corre en containers.
- Integraciones nativas de Github, Gitlab, Bitbucket…
- Adopta configuración basada en yaml, adoptando el principio de canalización como código.
- Fácilmente escalable.
- Incluye muchos plugins de trabajo mantenidos por la comunidad.

### Conclusiones
Drone es una herramienta robusta para implementación de prácticas DevOps relacionadas con la integración contínua, el despliegue contínuo y la entrega contínua.

Al ser Container Native, Drone puede ejecutarse directamente como un servicio dentro del orquestador de contenedores.

## Referencias
- Drone.io como motor de CI/CD - [medium.com](https://medium.com/ingenier%C3%ADa-en-tranqui-finanzas/drone-io-como-motor-de-ci-cd-32a8d714320d)
- Goodbye Jenkins: How Drone Simplifies CI/CD for Engineering Teams Everywhere - [boom.co](https://boom.co/blogs/drone-ci-for-engineering-teams/)
