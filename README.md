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

### Guías
- [Repositorio con las guías](https://github.com/sfl0r3nz05/SecDelivAutoIoT/tree/master/docs/guias)

### Repositorios de GitLab
- [Repositorio de la aplicación](https://gitlab.com/mikel-m/SecDelivAutoIoT)
- [Repositorio de configuración](https://gitlab.com/mikel-m/configSecDelivAutoIoT)

### Repositorio de GitHub
- [Repositorio de GitHub](https://github.com/sfl0r3nz05/SecDelivAutoIoT)

### Registro de imágenes
- GitLab Container Registry: [mikel-m/secdelivautoiot](https://gitlab.com/mikel-m/SecDelivAutoIoT/container_registry/4192474)
- Docker Hub: [mikelm98/secdelivautoiot](https://hub.docker.com/repository/docker/mikelm98/secdelivautoiot/general)

### [Documentación de flujos](https://github.com/sfl0r3nz05/SecDelivAutoIoT/tree/master/docs/Domumentacion-Flujos)
- [Etapa 1: Flujo GitOps IoT GitLab](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/Domumentacion-Flujos/Etapa%201-Flujo%20GitOps%20IoT%20GitLab.md)

***

## Proyecto
Este proyecto pretende automatizar la Integración Continua y el Despliegue Continuo de forma segura de aplicaciones siguiendo la metodología GitOps diseñada en los [diseños de la arquitectura](https://github.com/sfl0r3nz05/SecDelivAutoIoT/tree/master/docs/dise%C3%B1o).

## Descripción
Los flujos que hemos diseñado se han realizado para dispositivos IoT y para dispositivos Android.
### IoT
Para esta arquitectura, hemos diseñado dos flujos según las necesidades: utilizando GitLab CI/CD y utilizando Jenkins.

Para GitLab CI/CD, hemos creado dos repositorios (aplicación y configuración). En el repositorio de la aplicación se realiza el análisis del código fuente del repositorio en busca de vulnerabilidades y mejorar la calidad del código. Luego se genera la imagen docker y se registra en Docker Hub. Una vez subida, se analiza esa imagen en busca de vulnerabilidades. Y por último, se despliega la imagen en ArgoCD.

Para Jenkins, el flujo sigue la misma idea solo que uilizando dos pipelines de Jenkins en vez de GitLab CI/CD. En este caso, también se utilizan dos repositorios (aplicación y configuración) que se definen cada uno en un pipeline.

En los siguientes enlaces puedes ver los diseños del flujo con GitLab y con Jenkins:
- [Flujo con GitLab](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/dise%C3%B1o/2.1%20Arquitectura%20Flujo%20GitOps%20IoT%20GitLab.md)
- [Flujo con Jenkins](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/dise%C3%B1o/2.3%20Arquitectura%20Flujo%20GitOps%20IoT%20Jenkins.md)

### Android

## Overview
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Overview.svg" alt="Overview">

## Implementación
Para la implementación de estos flujo, hemos creado las siguientes guías para seguir paso a paso la implementación de los flujos descritos.
### GitLab
Para el flujo de GitLab, hemos creado la siguiente [guía para la implementación del flujo en GitLab CI/CD](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/guias/Ejecuci%C3%B3n%20Pipeline%20Flujo%20CI-CD%20GitLab.md).
### Jenkins
Para el flujo de Jenkins, hemos creado la siguiente [guía para la implementación del flujo en Jenkins](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/guias/Ejecuci%C3%B3n%20Pipeline%20Flujo%20CI-CD%20Jenkins.md).

## Monitorización
