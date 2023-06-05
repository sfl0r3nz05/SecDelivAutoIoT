# Secure delivery automation over monitored IoT infrastructures

- This repository is under development by [@mikel-m](mikelmorillo98@gmail.com) and [@sfl0r3nz05](sfigueroa@ceit.es).

<!--
![image](https://user-images.githubusercontent.com/6643905/221798180-3fbb2e2d-5d3c-45d5-b670-da783c05b06f.png)
-->

## Contenido
### Estructura
- [Estado del Arte](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/Estado%20del%20Arte.md)
- [Herramientas para análisis de seguridad](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/Herramientas%20para%20an%C3%A1lisis%20de%20seguridad.md)
- [Repositorio con los diseños](https://github.com/sfl0r3nz05/SecDelivAutoIoT/tree/master/docs/dise%C3%B1o)
- [Métricas de monitorización](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/M%C3%A9tricas%20de%20monitorizaci%C3%B3n.md)
- [Repositorio con apuntes propios](https://github.com/sfl0r3nz05/SecDelivAutoIoT/tree/master/docs/apuntes)

### Repositorios de GitLab
- [Repositorio de la aplicación](https://gitlab.com/mikel-m/SecDelivAutoIoT)
- [Repositorio de configuración](https://gitlab.com/mikel-m/configSecDelivAutoIoT)

### Repositorio de GitHub
- [Repositorio de GitHub](https://github.com/sfl0r3nz05/SecDelivAutoIoT)

### [Documentación de flujos](https://github.com/sfl0r3nz05/SecDelivAutoIoT/tree/master/docs/Domumentacion-Flujos)
- [Etapa 1: Flujo GitOps IoT GitLab](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/Domumentacion-Flujos/Etapa%201-Flujo%20GitOps%20IoT%20GitLab.md)

## Proyecto
Este proyecto pretende automatizar la Integración Continua y el Despliegue Continuo de forma segura de aplicaciones siguiendo las arquitecturas diseñadas en los [diseños](https://github.com/sfl0r3nz05/SecDelivAutoIoT/tree/master/docs/dise%C3%B1o). En este momento estamos utilizando una aplicación simpe en Python pero el objetivo es poder utilizar también aplicaciones Android.

### Etapa 1
En esta primera etapa se define implementa el flujo de CI en el [repositorio de GitLab de la aplicación](https://gitlab.com/mikel-m/SecDelivAutoIoT).
1. Se analiza el código fuente con SonarQube.
2. Se registra la imagen en GitLab Container Registry.
3. Se analiza la imagen con Trivy.
4. Se envía un trigger al [repositorio de GitLab de la configuración](https://gitlab.com/mikel-m/configSecDelivAutoIoT).

Una vez enviado el trigger al repositorio de GitLab de configuración, 
