# Herramientas para análisis de seguridad

- Aqua: <https://www.aquasec.com/products/container-vulnerability-scanning/>
- Snyk: <https://snyk.io/product/container-vulnerability-management/>
- Twistlock: <https://www.cloudfoundry.org/the-foundry/twistlock/>
- Sysdig Secure: <https://sysdig.com/use-cases/container-and-kubernetes-security/>
- Anchore Engine: <https://anchore.com/container-vulnerability-scanning/>
- Clair: <https://www.redhat.com/es/topics/containers/what-is-clair>
- Qualys Container Security: <https://www.qualys.com/apps/container-security/>
- Prisma Cloud: <https://www.paloaltonetworks.es/prisma/cloud/container-security>
- Docker Bench Security: <https://github.com/docker/docker-bench-security>
- Trivy: <https://github.com/aquasecurity/trivy>
- kube-bench: <https://github.com/aquasecurity/kube-bench>
- OpenSCAP: <https://www.open-scap.org/>


| **Herramienta**    | **Descripción**                                                                                                                                                                                                                                 | **OWASP**               | **NIST**                                                   | **Open Source** | **Lenguaje**                                           | **Docker** |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|--------------------------------------------------------|-------------|----------------------------------------------------|--------|
| Sysdig Falco   | Falco es una herramienta de detección de amenazas de seguridad para entornos de contenedores que utiliza reglas personalizadas para alertar sobre actividades sospechosas.                                                                  | No (explícitamente) | No (explícitamente)                                    | Sí          | Examina los contenedores                           | Sí     |
| Anchore Engine | Anchore Engine es una plataforma de seguridad de contenedores que ofrece escaneo de imágenes, análisis de vulnerabilidades, políticas personalizadas y monitoreo continuo de vulnerabilidades.                                              | No (explícitamente) | No (explícitamente)                                    | Sí          | ☑Python <br> ☑JavaScript <br> ☑Java | Sí     |
| Trivy          | Trivy es un escáner de vulnerabilidades de imágenes de contenedores de código abierto que puede integrarse en pipelines de CI/CD para identificar vulnerabilidades en imágenes de contenedores.                                             | No (explícitamente) | No, pero sí Common Vulnerabilities and Exposures (CVE) | Sí          | ☑Python <br> ☑JavaScript <br> ☑Java | Sí     |
| SonarQube      | SonarQube es una herramienta de análisis de calidad de código y seguridad que permite a los desarrolladores mejorar la calidad del código y detectar vulnerabilidades de seguridad temprano en el ciclo de vida del desarrollo de software. | Sí                  | No (explícitamente)                                    | Sí          | ☑Python <br> ☑JavaScript <br> ☑Java | Sí     |
