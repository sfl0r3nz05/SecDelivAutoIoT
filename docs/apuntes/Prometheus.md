# Prometheus
Prometheus es un conjunto de herramientas de supervisión y alerta de sistemas de código abierto, originalmente desarrollado en SoundCloud. Prometheus recopila y almacena sus métricas como datos de series temporales, es decir, la información de las métricas se almacena con la marca de tiempo en la que se registró, junto con pares clave-valor opcionales llamados etiquetas.

## Características
- Modelo de datos multidimensional con datos de series temporales identificados por nombre de métrica y pares clave/valor.
- Sin dependencia del almacenamiento distribuido; los nodos de un solo servidor son autónomos.
- La recopilación de series temporales se realiza a través de un modelo de extracción a través de HTTP.
- Los objetivos se descubren a través del descubrimiento de servicios o la configuración estática.
- Múltiples modos de soporte de gráficos y tableros.

## ¿Qué son las métricas?
En términos sencillos, las métricas son medidas numéricas. Serie temporal significa que los cambios se registran a lo largo del tiempo. Lo que los usuarios quieren medir difiere de una aplicación a otra.

Las métricas juegan un papel importante para comprender por qué su aplicación funciona de cierta manera. Supongamos que está ejecutando una aplicación web y descubre que la aplicación es lenta. Necesitará cierta información para saber qué está pasando con su aplicación.

## ¿Cuándo es adecuado?
Prometheus funciona bien para registrar cualquier serie temporal númerica pura. Se adapta tanto a la supervisión centrada en máquinas como a la supervisión de arquitecturas de servicios altamente dinámicas. En un mundo de microservicios, su capacidad de recopilación y consulta de datos multidimensionales es una fortaleza particular.

## Tipos de métricas
- **Contador**: es una métrica acumulativa que representa un contador único y monótonamente creciente cuyo valor sólo puede aumentar o reiniciarse a cero. Por ejemplo, puedes usar un contador para representar el número de solicitudes atendidas, tareas completadas o errores.
- **Medidor**: es una métrica que representa un único valor numérico que puede aumentar o disminuir arbritariamente. Los medidores se utilizan típicamente para valores medidos como temperaturas o uso actual de memoria, pero también para "contar" que pueden aumentar o disminuir, como el número de solicitudes concurrentes.
- **Histograma**: toma muestras de observaciones (generalmente cosas como la duración de las solicitudes o el tamaño de las respuestas) y las cuenta en compartimiento configurables. También proporciona una suma de todos los valores observados.
- **Resumen**: similar a un histograma, un resumen toma muestras de observaciones (generalmente cosas como la duración de solicitudes y el tamaño de las respuestas). Si bien también proporciona un recuento total de las observaciones y una suma de todos los valores observados, calcula cuantiles configurables en una ventana de tiempo deslizante.

***
# Métricas Flujos 
## Métricas del repositorio de GitLab
- Número de commits
- Ramas
- Pull requests

## Métricas de flujo de trabajo
- Duración de cada job del piepline
- Tiempo de ejecución total
- Número de construcciones exitosas o fallidas

## Métricas de SonarQube
- Número de problemas de seguridad detectados
- Cobertura de pruebas

## Métricas de Docker Hub
- Número de imágener almacenadas
- Tamaño total de las imágenes

## Métricas de Trivy
- Vulnerabilidades detectadas

## Métricas ArgoCD
- Tiempo de implementación
- Número de implementaciones exitosas o fallidas

## Métricas de K3s
- Uso de recursos
- Escalabilidad
- Latencia de los pods

## Referencias
- Prometheus Docs - [prometheus.io](https://prometheus.io/docs/introduction/overview/)
