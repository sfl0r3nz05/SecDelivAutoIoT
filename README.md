# Secure delivery automation over monitored IoT infrastructures
Este proyecto pretende automatizar la Integración Continua y el Despliegue Continuo de forma segura de aplicaciones sobre dispositivos IoT y Android siguiendo la metodología GitOps diseñada en los [diseños de la arquitectura](https://github.com/sfl0r3nz05/SecDelivAutoIoT/tree/master/docs/dise%C3%B1o) tanto para GitLab como para Jenkins.

## Overview
En la siguiente imagen se puede ver la idea general que siguen los flujos que hemos diseñado, separando tanto los repositorios como la parte de la Integración Continua (CI) y el Despliegue Continuo (CD):
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Overview.svg" alt="Overview">

## Diseño
Estos son los flujos que hemos diseñado tanto para dispositivos IoT como para dispositivos Android utilizando las herramientas de GitLab CI/CD y Jenkins en cada caso.
### IoT
Para esta arquitectura, hemos diseñado dos flujos según las necesidades: utilizando GitLab CI/CD y utilizando Jenkins.

Para GitLab CI/CD, hemos creado dos repositorios (aplicación y configuración). En el repositorio de la aplicación se realiza el análisis del código fuente del repositorio en busca de vulnerabilidades y mejorar la calidad del código. Luego se genera la imagen docker y se registra en Docker Hub. Una vez registrada, se analiza esa imagen en busca de vulnerabilidades. Y por último, se despliega la imagen en ArgoCD que está alojado en una máquina virtual.

Para Jenkins, el flujo sigue la misma idea solo que uilizando dos pipelines de Jenkins en vez de GitLab CI/CD. En este caso, también se utilizan dos repositorios (aplicación y configuración) que se definen cada uno en un pipeline.

En los siguientes enlaces puedes ver los diseños del flujo con GitLab y con Jenkins:
- [Flujo con GitLab](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/dise%C3%B1o/2.1%20Arquitectura%20Flujo%20GitOps%20IoT%20GitLab.md)
- [Flujo con Jenkins](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/dise%C3%B1o/2.3%20Arquitectura%20Flujo%20GitOps%20IoT%20Jenkins.md)

### Android
Para dispositivos Android, también hemos realizado el diseño utilizando GitLab CI/CD y Jenkins.

Como en el caso de IoT, también vamos a utilizar dos repositorios (aplicación y configuración). En este caso, el flujo sigue la misma idea que en IoT de analizar el código fuente, generar la imagen de la aplicación, analizar esa imagen y desplegarla en ArgoCD.

En los siguientes enlaces puedes ver los diseños del flujo con GitLab y con Jenkins:
- [Flujo con GitLab](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/dise%C3%B1o/2.2%20Arquitectura%20Flujo%20GitOps%20Android%20GitLab.md)
- [Flujo con Jenkins](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/dise%C3%B1o/2.4%20Arquitectura%20Flujo%20GitOps%20Android%20Jenkins.md)

## Tabla de herramientas de seguridad
| **Herramienta**    | **Descripción**                                                                                                                                                                                                                                 | **OWASP**               | **NIST**                                                   | **Open Source** | **Lenguaje**                                           | **Docker** |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|--------------------------------------------------------|-------------|----------------------------------------------------|--------|
| SonarQube      | SonarQube es una herramienta de análisis de calidad de código y seguridad que permite a los desarrolladores mejorar la calidad del código y detectar vulnerabilidades de seguridad temprano en el ciclo de vida del desarrollo de software. | Sí                  | No (explícitamente)                                    | Sí          | ☑Python <br> ☑JavaScript <br> ☑Java | Sí     |
| Trivy          | Trivy es un escáner de vulnerabilidades de imágenes de contenedores de código abierto que puede integrarse en pipelines de CI/CD para identificar vulnerabilidades en imágenes de contenedores.                                             | No (explícitamente) | No, pero sí Common Vulnerabilities and Exposures (CVE) | Sí          | ☑Python <br> ☑JavaScript <br> ☑Java | Sí     |
| Sysdig Falco   | Falco es una herramienta de detección de amenazas de seguridad para entornos de contenedores que utiliza reglas personalizadas para alertar sobre actividades sospechosas.                                                                  | No (explícitamente) | No (explícitamente)                                    | Sí          | Examina los contenedores                           | Sí     |
| Anchore Engine | Anchore Engine es una plataforma de seguridad de contenedores que ofrece escaneo de imágenes, análisis de vulnerabilidades, políticas personalizadas y monitoreo continuo de vulnerabilidades.                                              | No (explícitamente) | No (explícitamente)                                    | Sí          | ☑Python <br> ☑JavaScript <br> ☑Java | Sí     |

## Implementación
Para la implementación de estos flujos, hemos creado las siguientes guías para seguir paso a paso la implementación de los flujos descritos.
### IoT
- **GitLab**: Para el flujo de GitLab en dispositivos IoT, hemos creado la siguiente [guía para la implementación del flujo en GitLab CI/CD](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/guias/Ejecuci%C3%B3n%20Pipeline%20Flujo%20CI-CD%20GitLab.md).
- **Jenkins**: Para el flujo de Jenkins en dispositivos IoT, hemos creado la siguiente [guía para la implementación del flujo en Jenkins](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/guias/Ejecuci%C3%B3n%20Pipeline%20Flujo%20CI-CD%20Jenkins.md).

### Android
- **GitLab**: Para el flujo de GitLab en dispositivos Android, hemos creado la siguiente _guía para la implementación del flujo en GitLab CI/CD_.

- **Jenkins**: Para el flujo de Jenkins en dispositivos Android, hemos creado la siguiente _guía para la implementación del flujo en Jenkins_.

En el caso de Android, sigue en desarrollo por lo que no hay ninguna guía de implementación.

## Monitorización
Para la parte de la monitorización, hemos utilizado la herramienta de Prometheus para recopilar las métricas y la herramienta Grafana para la visualización de las métricas.
### GitLab
Para la implementación de las herramientas de monitorización de GitLab CI/CD, hemos creado la siguiente [guía para la monitorización del flujo de GitLab CI/CD](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/guias/Monitorizaci%C3%B3n%20GitLab%20Prometheus%20Grafana.md).
### Jenkins
Para la implementación de las herramientas de monitorización de Jenkins, hemos creado la siguinete [guía para la monitorización del flujo de Jenkins](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/guias/Monitorizaci%C3%B3n%20Jenkins%20Prometheus%20Grafana.md).
