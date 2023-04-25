# Drone vs Jenkins
## Drone CI vs Jenkins. Fight (video)
|                                     | **Drone CI**                                                        | **Jenkins**                                                                   |
|-------------------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Open Source                         | Sí (vesión pago: características adicionales)                                                       | Sí                                                                            |
| Autenticación                       | - Directamente con Git provider (por ejemplo Github).  - Tokens     | - Nombre de usuario y contraseña con el servidor Jenkins. - Contraseña        |
| Configuración           | Configuración mediante archivos YAML.                               | Configuración mediante interfaz de usuario.                                   |
| Webhooks                            | Se conecta con el usuario de Github y seleccionas los repositorios. | Tienes que añadir el repositorio manualmente mediante plugins y credenciales. |
| Entorno                             | En contenedores.                                                    | En el servidor.                                                               |
| Configuraciones (por ejemplo build) | Mediante archivo YAML (.drone.yml).                                 | Mediante interfaz de usuario.                                                 |
| MIRAR LO DE SECRETS                 |                                                                     |                                                                               |
| Docker                              | Sólo Docker, pero optimizado. (Para Docker la mejor opción)         | Opcional, pero lento. (Para Docker peor elección)                             |

## Time to migrate from Jenkins to Drone CI
|                                            | Drone                                                   | Jenkins                                          |
|--------------------------------------------|---------------------------------------------------------|--------------------------------------------------|
| Simplicidad                                | Más simple.                                             | Menos simple (aunque tiene más funciones).       |
| Velocidad                                  | Más rápido para detectar cambio de código.              | Más lento para detectar cambio de código.        |
| Facilidad de uso                           | Instalación e interfaz más sencilla.                    | Instalación e interfaz más compleja.             |
| Enfoque                                    | Usa metodologías modernas (contenedores).               | Usa metodologías antiguas.                       |
| Declarativo                                | Todo se configura a través de de archivos YAML simples. | Se configura a través de la interfaz de usuario. |
| Basado en contenedores y nativo de la nube | Cada paso es un contenedor aislado.                     | Todo se hace en el servidor Jenkins.             |

### Drone.io: Free vs Enterprise
|                        | **Feature**                  | **Free** | **Enterprise** |
|------------------------|------------------------------|:--------:|:--------------:|
| Source Code Management | GitHub                       |     ☑    |        ☑       |
|                        | GitHub Enterprise            |     ☑    |        ☑       |
|                        | GitLab                       |     ☑    |        ☑       |
| Data Storage           | Sqlite                       |     ☑    |        ☑       |
|                        | MySQL                        |          |        ☑       |
| Blob Storage           | Amazon S3                    |          |        ☑       |
|                        | Digital Ocean Spaces         |          |        ☑       |
| Platforms              | Linux x64                    |     ☑    |        ☑       |
|                        | Windows x86                  |     ☑    |        ☑       |
| Clustering             | Single Machine               |     ☑    |        ☑       |
|                        | Multi-Machine, Agents        |          |        ☑       |
|                        | Multi-Machine, Kubernetes    |          |        ☑       |
| Plugins and Extensions | Pipeline Plugins             |     ☑    |        ☑       |
|                        | Secret Extensions            |          |        ☑       |
|                        | Access Control Extensions    |          |        ☑       |
|                        | Configuration Extensions     |          |        ☑       |
| Secrets                | Encrypted                    |     ☑    |        ☑       |
|                        | External, AWS Secret Manager |          |        ☑       |
|                        | External, Kubernetes Secrets |          |        ☑       |
| Autoscaling            | Amazon EC2                   |          |        ☑       |
|                        | Digital Ocean                |          |        ☑       |
|                        | Google Compute               |          |        ☑       |

## Conclusión
Según por lo que se ha podido leer, Drone parece una mejor opción para un entorno de contenedores, ya que Drone se centra en la ejecución de pipelines dentro de contenedores. 

# Referencias
- Drone CI vs Jenkins. Fight!- Niklas Hole, Ole Anders Stokker - [youtube.com](https://www.youtube.com/watch?v=c9mhpFSDR7I&ab_channel=NDCConferences)
  - Drone CI vs Jenkins: Demo - [github.com](https://github.com/niklasmh/drone-vs-jenkins-demo)
- Why It’s Time to Migrate from Jenkins to Drone CI - [harness.io](https://www.harness.io/blog/why-migrate-from-jenkins-to-drone-ci)

# Artículos de interés
- Drone vs Jenkins - [knapsackpro.com](https://knapsackpro.com/ci_comparisons/drone/vs/jenkins)
- CICD Debates: Drone vs Jenkins - [rancher.cn](https://www.rancher.cn/drone-vs-jenkins)
