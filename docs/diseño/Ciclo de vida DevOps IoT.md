# Ciclo de vida DevOps para dispositivos IoT
## Ciclo de Vida General
1. Planificación: se define un conjunto mínimo de funcionalidades que aportan valor en cada iteración y los criterios de aceptación a cumplir.
2. Desarrollo: desarrollo del software del proyecto. Estos desarrollos avanzan en pequeños procesos en el ciclo de desarrollo. Al mismo tiempo, empiezas a definirlas pruebas que deberás realizar a tu pieza para asegurar que cumple con la especificación funcional.
3. Construcción: construir la aplicación con la integración de varios códigos que hicieron en la fase de desarrollo. Creación de los artefactos que componen el software.
4. Pruebas: ejecución de las pruebas para verificar el correcto funcionamiento de todas las características del proyecto.
5. Lanzamiento: una vez la aplicación pasó las pruebas funcionales y de integración, se podrá crear una versión del software.
6. Operación: asegurarse de que no existan comportamientos raros e inadecuados, errores que se pedan encontrar en la producción.
7. Monitoreo: establecer cuáles son los parámetros a vigilar de la aplicación. Recopilar toda la información recogida a lo largo de un periodo de tiempo para realizar los ajustes necesarios en la siguiente fase de planificación.

<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Ciclo%20de%20Vida%20DevOps.png">

## Mi Ciclo de Vida
1. Planificación: los desarrolladores y el equipo de DevOps trabajan juntos para planificar y priorizar el trabajo de desarrollo de la aplicación.
2. Desarrollo: los desarrolladores realizan cambios en el código de la aplicación y lo suben al repositorio de GitLab.
3. Construcción: GitLab CI/CD desencadena la ejecución de los flujos de trabajo definidos en “.gitlab-ci.yml” para el build, test y deploy de la imagen.
4. Pruebas: GitLab CI/CD ejecuta las pruebas de seguridad definidas en el flujo de trabajo para verificar la seguridad del código.
5. Lanzamiento: si las pruebas de seguridad son exitosas, GitLab CI/CD construirá la imagen del contenedor y la almacenará en GitLab Container Registry.
6. Operación: GitLab CI/CD notifica a ArgoCD para que construya e implemente la imagen en el cluster Kubernetes de la Raspberry Pi.
7. Monitoreo: Se utiliza una solución de monitoreo para supervisar la aplicación en producción, detectar problemas y recopilar información sobre el rendimiento de la aplicación.

<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Ciclo%20de%20Vida%20DevOps%20IoT.svg" alt="Ciclo de vida DevOps para dispositivos IoT">

## Referencias
- Introducción al Ciclo de Vida de DevOps - [kranio.io](https://www.kranio.io/blog/introduccion-al-ciclo-de-vida-de-devops)
