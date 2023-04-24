# Estado del Arte
En el contexto de los dispositivos IoT actuales y las tecnologías IoT emergentes, la automatización de la entrega segura a través de la infraestructura IoT monitorizada es un área de investigación importante para garantizar la seguridad, privacidad y fiabilidad en el proceso de entrega de valor. Los conceptos basado en la nube, como sistemas basados en microservicios y contenedores, se utilizan para abordar las necesidades de la próxima generación de IoT, y se utiliza un ecosistema DevOps para automatizar la entrega segura de aplicaciones altamente distribuidas.

En este proyecto, se llevará a cabo una etapa de Integración Continua enfocada en la seguridad utilizando herramientas compatibles con frameworks como OWASP o NIST para la implementación de chequeos de seguridad de dispositivos IoT. Además, se aplicará GitOps para la Integración Continua, acelerando la entrega de valor y evitar procesos manuales. El software se entregará en dispositivos IoT que soportan infraestructuras basadas en K3s, como Raspberry Pi y Beaglebones, y se monitorizará el cluster utilizando herramientas de monitorización como DataDog. La solución de automatización se implementará tanto en un entorno GitLab como en uno basado en Drones.

## Marco Teórico
Antes de empezar con el trabajo de Fin de Grado es importante realizar el Marco Teórico de los temas que se van a tratar. En este trabajo, el Marco Teórico se centrará en el análisis y descripción de los siguientes temas: el framework NIST, la metodología GitOps, Kubernetes (K3s), Dynamic Feature Modules y Drone CI.

En este Marco Teórico, se describirá detalladamente cada uno de los temas, analizando su relevancia, su funcionamiento y su aplicación en el desarrollo de software. Se examinarán las ventajas y desventajas de cada tecnología y se investigará su impacto en el desarrollo de software en términos generales.

### NIST
El framework es una metodología con un enfoque para reducir el riesgo vinculado a las amenazas cibernéticas que puedan comprometer la seguridad de la información, y está compuesto por tres partes: el Núcleo del Framework, los Niveles de Implementación y los Perfiles del framework.

La gestión de riesgos es el proceso continuo de identificación, evaluación y respuesta al riesgo. Para gestionar el riesgo, las organizaciones deben comprender la probabilidad de que ocurra un evento y los posibles impactos resultantes. Con esta información, las organizaciones pueden determinar el nivel aceptable de riesgo para lograr sus objetivos organizacionales y pueden expresar esto como su tolerancia al riesgo.

Las siguientes cinco funciones básicas del framework no están destinadas a formar una ruta serial o conducir a un estado final estático. Por el contrario, las funciones deben realizarse concurrentemente y continuamente para formar una cultura operativa que aborde el riesgo dinámico de seguridad cibernética.
- Identificar: desarrolla una comprensión organizacional para administrar el riesgo de seguridad cibernética para sistemas, personas, activos, datos y capacidades. Las actividades en la Función Identificar son fundamentales para el uso efectivo del Marco.
- Proteger: desarrollar e implementar medidas de seguridad adecuadas para garantizar la entrega de servicios críticos. La Función Proteger admite la capacidad de limitar o contener el impacto de un posible evento de seguridad cibernética.
- Detectar: desarrollar e implementar actividades apropiadas para identificar la ocurrencia de un evento de seguridad cibernética. La Función Detectar permite el descubrimiento oportuno de eventos de seguridad cibernética.
- Responder: Las actividades en la Función Identificar son fundamentales para el uso efectivo del framework. La Función Responder respalda la capacidad de contener el impacto de un posible incidente de seguridad cibernética.
- Recuperar: Desarrollar e implementar actividades apropiadas para mantener los planes de resiliencia y restablecer cualquier capacidad o servicio que se haya visto afectado debido a un incidente de seguridad cibernética. La Función Recuperar admite la recuperación oportuna a las operaciones normales para reducir el impacto de un incidente de seguridad cibernética.

Los siguientes pasos ilustran cómo una organización podría utilizar el Marco para crear un nuevo programa de seguridad cibernética o mejorar un programa existente. Estos pasos deben repetirse según sea necesario para mejorar continuamente la seguridad cibernética.
- Paso 1: Priorización y Alcance: la organización identifica sus objetivos empresariales o de misión y las prioridades organizacionales de alto nivel. Con esta información, la organización toma decisiones estratégicas con respecto a las implementaciones de seguridad cibernética y determina el alcance de los sistemas y activos que respaldan la línea o proceso comercial seleccionado.
- Paso 2: Orientación: una vez que se ha determinado el alcance del programa de seguridad cibernética para la línea de negocio o el proceso, la organización identifica los sistemas y activos relacionados, los requisitos reglamentarios y el enfoque de riesgo general. La organización luego consulta las fuentes para identificar las amenazas y vulnerabilidades aplicables a esos sistemas y activos.
- Paso 3: Crear un Perfil Actual: la organización desarrolla un Perfil Actual en que indica qué resultados de Categoría y Subcategoría del Núcleo del Marco se están logrando actualmente.
- Paso 4: Realizar una evaluación de riesgos: la organización analiza el entorno operativo para discernir la probabilidad de un evento de seguridad cibernética y el impacto que el evento podría tener en la organización.
- Paso 5: Crear un Perfil Objetivo: la organización crea un Perfil Objetivo que se centra en la evaluación de las Categorías y Subcategorías del Marco que describen los resultados deseados de seguridad cibernética de la organización.
- Paso 6: Determinar, analizar y priorizar brechas: la organización compara el Perfil Actual y el Perfil Objetivo para determinar las brechas. A continuación, crea un plan de acción priorizado para abordar las brechas para lograr los resultados en el Perfil Objetivo.
- Paso 7: Implementar plan de acción: la organización determina qué acciones tomar para abordar las brechas, si las hay, identificadas en el paso anterior y luego ajusta sus prácticas actuales de seguridad cibernética para lograr el Perfil Objetivo.

### Metodología GitOps
Un sistema administrado por GitOps debe tener su estado deseado expresado de forma declarativa. En este contexto, un sistema se define como uno o más entornos de tiempo de ejecución que consisten en recursos bajo administración, los agentes de administración dentro de cada tiempo de ejecución y las políticas para controlar el acceso y la administración de repositorios, implementaciones y tiempos de ejecución.

El estado deseado significa que usted representa la forma en que desea que funcione el sistema en un "estado final", que será el estado final alcanzado por los cambios realizados por el entorno de GitOps. El estado deseado debe ser declarativo. El estado de un sistema se almacena como un conjunto de declaraciones sin procedimientos sobre cómo se logrará ese estado.
- Versionado e inmutable: un ejemplo es Git porque cada cambio se rastrea en una nueva versión sin alterar las versiones anteriores. Por lo tanto, puede volver a una versión anterior mientras conserva una auditoría de todos los cambios que se han realizado.
- Pull automático: Los agentes de software de GitOps comprueban el estado deseado extrayendo declaraciones del almacén de estado a intervalos regulares, lo que significa tanto sondear como extraer.
- Reconciliación Continua: Este principio refleja directamente las funciones de los controladores de Kubernetes, pero GitOps lo aplica a toda una aplicación o pila de infraestructura en lugar de solo a un objeto. Si hay una diferencia entre el estado deseado y el estado en ejecución, se reconcilian cambiando el estado en ejecución.

#### GitOps y CI/CD
CI/CD es una de las prácticas destacadas en el movimiento DevOps. Los principales conceptos atribuidos a CI/CD son integración continua, entrega continua e implementación continua.

La integración continua crea y prueba nuevos cambios de código y los fusiona en un repositorio compartido de forma regular. La entrega continua se refiere a la automatización de la publicación de cambios en los entornos de desarrollo/escenario y preproducción. Luego, los cambios se implementan en producción. También automatiza los pasos manuales que ralentizan la entrega de aplicaciones. El propósito de la entrega continua es implementar código nuevo con un esfuerzo mínimo. La implementación continua lleva la entrega continua un paso más allá, implementando los cambios en la producción real.

### Kubernetes para IoT (K3s)
Como nunca he utilizado Kubernetes, he tenido que aprender desde cero. Para ello, he instalado K3s (distribución liviana de Kubernetes) en la Raspberry Pi que vamos a utilizar y coger soltura con los comandos básicos. ëstos son algunos de lo comandos básicos de Kubernetes:
- Lista de los nodos del cluster: `kubectl get nodes`
- Lista de los pods: `kubectl get pods`
- Lista de deployments: `kubectl get deployments`
- Eliminar pod (por ejemplo, nginx): `kubectl delete pod nginx`
- Acceder al pod (por ejemplo, nginx): `kubectl exec -it nginx -- sh`
- Aplicar el contenido del fichero deployment.yaml: `kubectl apply -f deployment.yaml`
- Eliminar pod del fichero deployment.yaml: `kubectl delete -f deployment.yaml`

### Dynamic Feature Modules
Google Play usa su paquete de aplicaciones para generar y publicar APK optimizados para la configuración del dispositivo de cada usuario, de modo que descarguen solo el código y los recursos que necesitan para ejecutar su aplicación. A través de Dynamic Delivery, los usuarios pueden descargar e instalar las funciones dinámicas de la aplicación a pedido después de que ya hayan instalado el APK base de su aplicación. Como resultado, el tamaño de descarga inicial de su aplicación es menor y los usuarios no necesitan funciones ni código sin usar en sus dispositivos.

Los Dynamic Feature Modules permiten separar ciertas funciones y recursos del módulo base de su aplicación e incluirlos en su paquete de aplicaciones. Los usuarios pueden descargar e instalar estos módulos más adelante a pedido después de que ya hayan instalado el APK base de la aplicación mediante Dynamic Delivery.

### Drone
Aunque la idea de un demonio al que se puede conectar por medio de sockets no le gustó mucho a la gente de coreos, esto abre la puerta a que un contenedor pueda crear contenedores en tiempo de ejecución, y este es el principio subyacente detrás de Drone.io. El concepto de flujo se mantiene igual que en otras herramientas de integración continua, se definen un conjunto de pasos secuenciales que representan un estado en la aplicación:
- Clonado: se obtiene una copia del código fuente desde el Sistema de Control de Versiones.
- Pruebas: se ejecutan el conjunto de pruebas automáticas al código fuente, usualmente pruebas unitarias, de integración y punto a punto.
- Construcción: se construye un artefacto con el estado actual de la aplicación.
- Almacenamiento: se almacena el artefacto en un Repositorio de Artefactos.
- Despliegue: se actualiza la versión de los servidores a la nueva versión construida.

El concepto más importante de Drone es que cada paso de flujo se ejecuta en un contenedor con un volumen compartido donde se almacena el código fuente, lo cual nos brinda flexibilidad, portabilidad y ligereza, también reduce ampliamente los tiempos de configuración de la herramienta, pues no es necesario realizar configuraciones adicionales por tecnología o lenguaje de programación.

Conceptos más relevantes de Drone:
1. La fase de clonado: no es obligatoria, pero en ella podemos definir las configuraciones para clonar el proyecto.
2. El flujo: depende en cada caso (Pruebas, Construcción/Almacenamiento, Despliegue y Notificación).
3. Los plugins: las fases de construcción, despliegue y notificación utilizan plugins para facilitar el proceso.
4. La ejecución condicional: el paso de despliegue solo se utiliza cuando es llamado desde la rama env/production.
5. Los secretos: información confidencial, como las credenciales de acceso al registry de Docker y el acceso al cluster de Kubernetes son ocultadas y manejadas por el manejador de secretos de Drone.

Características de Drone:
- Open-source, desarrollado por una enorme comunidad.
- Fácil de instalar y mantener.
- Basado en Docker, todo corre en containers.
- Integraciones nativas de Github, Gitlab, Bitbucket…
- Adopta configuración basada en yaml, adoptando el principio de canalización como código.
- Fácilmente escalable.
- Incluye muchos plugins de trabajo mantenidos por la comunidad.

### Herramientas para el análisis de seguridad
Hoy en día, cada vez es más y más la demanda de aplicaciones y con ello, el aumento del riesgo de recibir ataques cibernéticos. Por eso es necesario proteger a los usuarios de estos ataques. Para ello es importante el uso de herramientas de análisis de vulnerabilidades para mejorar la seguridad en el ciclo de vida de las aplicaciones e intentar reducir el riesgo de vulnerabilidades del código.

En este apartado, he realizado una búsqueda de herramientas de análisis de seguridad centrándome en si cumplen con los frameworks de OWASP y NIST, si son open source, si pueden analizar los lenguajes de Python, JavaScript y Java, y si se pueden utilizar con Docker y lo he plasmado en la siguiente tabla:

| **Herramienta**    | **OWASP**               | **NIST**                                                   | **Open Source** | **Lenguaje**                                           | **Docker** |
|----------------|---------------------|--------------------------------------------------------|-------------|----------------------------------------------------|--------|
| Sysdig Falco   | No | No                        | Sí          | Examina los contenedores                           | Sí     |
| Anchore Engine | No  | No    | Sí          | ☑Python <br> ☑JavaScript <br> ☑Java | Sí     |
| Trivy          | No  | Sí (CVE) | Sí          | ☑Python <br> ☑JavaScript <br> ☑Java | Sí     |
| SonarQube      | Sí                  | No                               | Sí          | ☑Python <br> ☑JavaScript <br> ☑Java | Sí     |


A continuación, te presento una breve descripción de las herramientas encontradas:
- Sysdig Falco: Falco es una herramienta de detección de amenazas de seguridad para entornos de contenedores que utiliza reglas personalizadas para alertar sobre actividades sospechosas.
- Anchore Engine: Anchore Engine es una plataforma de seguridad de contenedores que ofrece escaneo de imágenes, análisis de vulnerabilidades, políticas personalizadas y monitoreo continuo de vulnerabilidades.
- Trivy: Trivy es un escáner de vulnerabilidades de imágenes de contenedores de código abierto que puede integrarse en pipelines de CI/CD para identificar vulnerabilidades en imágenes de contenedores.
- SonarQube: SonarQube es una herramienta de análisis de calidad de código y seguridad que permite a los desarrolladores mejorar la calidad del código y detectar vulnerabilidades de seguridad temprano en el ciclo de vida del desarrollo de software.

### Instalación de K3s en la Raspberry Pi
1. Editar el fichero `/boot/cmdline.txt` y añadir `cgroup_memory=1 cgroup_enable=memory` al final de la línea. Para ello, hay que ejecutar el siguiente comando:
  <pre>sudo nano /boot/cmdline.txt</pre>
  y agregar la línea de configuración como se indica a continuación:
  <pre>console=serial0,115200 console=tty1 root=PARTUUID=32cbd588-02 rootfstype=ext4 fsck.repair=yes rootwait cgroup_memory=1 cgroup_enable=memory</pre>
  Guardar el fichero y reiniciar la Raspberry Pi con el siguiente comando:
  <pre>sudo reboot</pre>
2. Una vez que la Raspberry Pi se haya reiniciado, hay que instalar K3s utilizando el siguiente comando:
  <pre>curl -sfL https://get.k3s.io | sh -</pre>
  Este comando descarga el instalador de K3s y lo ejecuta en la Raspberry Pi para poder instalar la última versión de K3s.
3. Verificar que el servicio K3s se haya iniciado correctamente ejecutando el siguiente comando:
  <pre>sudo systemctl status k3s</pre>
  Este comando te muestra el estado actual del servicio K3s.

![Captura de pantalla del comando systemctl status k3s](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Captura%20systemctl%20status%20k3s.PNG "Captura de pantalla del comando systemctl status k3s")

Con estos pasos, ya estaría instalado K3s en la Raspberry Pi y se podrá empezar a utilizar para desplegar las aplicaciones. Para asegurarse de que se ha creado el master correctamente, se puede ejecutar el comando `sudo kubectl get nodes` para ver que único nodo que hay es el master que hemos creado en nuestra Raspberry Pi.

![Captura de pantalla del comando kubectl get nodes](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Captura%20kubectl%20get%20nodes.PNG "Captura de pantalla del comando kubectl get nodes")

## Referencias
- NIST - [docs.google.com](https://docs.google.com/document/d/1iaeQo4RI6FsqoR_ak5dra9uTT4lBzNNG5_q1vTTV4FQ/edit?usp=sharing)
- Path to GitOps - [docs.google.com](https://docs.google.com/document/d/1cQVQnBXhqUqchH6cduWlR-XAzE-J54NWOAIZiWnAUzI/edit?usp=sharing)
- Comandos Kubernetes - [docs.google.com](https://docs.google.com/document/d/17oqf-fs8zGtcK8HAqN-noJb3ieDhng8IU2jVlHn4szk/edit?usp=sharing)
- Dynamic Feature Modules - [docs.google.com](https://docs.google.com/document/d/1u63gvovECQCgJC11MDEmeK97YB2baPo4iMmVReCSDoY/edit?usp=sharing)
- Drone - [docs.google.com](https://docs.google.com/document/d/1FBuLXEVjFFJTJMBXZCvo8goJtY7uiDihltpgQfIYWcA/edit?usp=sharing)
- Herramientas para análisis de seguridad - [docs.google.com](https://docs.google.com/document/d/1k63yvoXLnqFfAu6gcZQnnGlKwYWnQsdRIm0FtNNzz5U/edit?usp=sharing)
- Kubernetes tutorial - Install Kubernetes on Raspberry Pi fast in 2022 - [youtube.com](https://www.youtube.com/watch?v=rOXkutK8ANc&ab_channel=AndrewMalkov)
