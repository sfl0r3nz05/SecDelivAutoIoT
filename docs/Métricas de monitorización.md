# Métricas de monitorización
A continuación se presenta una tabla con las métricas que se pueden tener en cuenta a la hora de monitorizar el proyecto.

| **Métrica**                  | **Descripción**                                                                                          |
|------------------------------|----------------------------------------------------------------------------------------------------------|
| Frecuencia de commits        | Cantidad de veces que los desarrolladores hacen commit en un periodo determinado.                        |
| Tiempo de latencia           | Tiempo que tarda desde que un desarrollador hace un commit hasta que GitLab CI/CD comienza a trabajar.   |
| Tiempo de construcción       | Tiempo que tarda GitLab CI/CD en construir la imagen del contenedor.                                     |
| Tiempo de prueba             | Tiempo que tardan las pruebas de seguridad en ejecutarse.                                                |
| Cobertura de prueba          | Porcentaje de código que se prueba durante las pruebas de seguridad.                                     |
| Tiempo de espera             | Tiempo que transcurre desde el final de GitLab CI/CD hasta el inicio de ArgoCD.                          |
| Frecuencia de implementación | Cantidad de veces que se implementa la aplicación en el clúster de Kubernetes en un periodo determinado. |
| Tiempo de implementación     | Tiempo que tarda ArgoCD en implementar la nueva imagen en el clúster de Kubernetes.                      |

## Referencias
- Observabilidad - [github.com](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/Observabilidad.md)
