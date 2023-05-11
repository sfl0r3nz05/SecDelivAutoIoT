# Jenkins
## ¿Qué es Jenkins?
Jenkins es un servidor de automatización de código abierto y autocontenido que se puede utilizar para automatizar todo tipo de tareas relacionadas con la construcción, prueba, entrega o implementación de software. La funcionalidad principal de Jenkins radica en su capacidad para automatizar tareas repetitivas relacionadas con la compilación, prueba y despliegue de software. Actúa como un servidor que se integra con sistemas de control de versiones como Git, y puede ser configurado para ejecutar una serie de pasos o tareas definidas por el usuario (pipeline).

Los trabajos en Jenkins pueden ser configurados para ejecutarse en respuesta a eventos específicos, como cambios en el repositorio de código fuente. La herramienta permite la ejecución de la ejecución de pruebas automatizadas, la generación de informes, la notificación de resultados y la gestión de despliegues en distintos entornos.

Su popularidad se debe en gran medida a su flexibilidad, escalabilidad y soporte activo de la comunidad de desarrolladores, lo que lo convierte en una opción popular para la automatización de procesos de desarrollo de software.

## ¿Por qué usar Jenkins?
- Los commit son desarrollados y verificados. Ya no es necesario corregir todo el código, sino solo la parte que está mal.
- Se conocen los resultados de las pruebas de cambios a lo largo de la ejecución.
- Automatiza el despliegue y los testeos, lo cual ahorra tiempo y evita errores.
- Los ciclos de desarrollo son más rápidos.

## Funcionamiento de Jenkins
- El desarrollador crea un commit de código en determinado repositorio.
- Jenkins hace comprobaciones cada cierto tiempo para encontrar los cambios.
- Una vez que se detectan las modificacionescompila el código y prepara un build. Si el build falla, se informa al equipo. Si funciona, se despliega el servidor de testeo.
- Luego de la prueba, se genera un feedback y se le notifica al personal.
- El proceso se repite de forma periódica.
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Funcionamiento-de-Jenkins-min.png" alt="Funcionamiento de Jenkins">

### Ventajas
- Fácil de configurar y personalizar.
- Gran versatilidad por sus plugins.
- Muestra los errores en el código y las pruebas.
- Detecta y resuelve problemas de manera rápida.
- Todo se hace de forma automática.
- Entrega el código de forma instantánea y genera un informe después del despliegue.

## Referencias
- Documentación de usuario de Jenkins - [jenkins.io](https://www.jenkins.io/doc/)
- ¿Para qué sirve Jenkins? - [bambu-mobile.com](https://www.bambu-mobile.com/para-que-sirve-jenkins/#:~:text=Funcionamiento%20de%20Jenkins-,%C2%BFQu%C3%A9%20es%20Jenkins%3F,la%20entrega%20de%20nuevas%20versiones.)
