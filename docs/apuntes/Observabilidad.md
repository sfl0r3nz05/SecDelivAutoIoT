# Observabilidad
La observabilidad es un atributo de un sistema, en lugar de algo que hace. Es la capacidad de un sistema para ser monitoreado, rastreado y analizado. Cualquier aplicación digna de producción debe ser observable. Su objetivo principal al observar un sistema es discernir lo que está haciendo internamente. Esto se logra mediante el análisis de salidas del sistema como métricas, trazas y registros.

El monitoreo es cualquier acción que implica registrar, analizar y alertar sobre métricas predefinidas para comprender el estado actual de un sistema. Un sistema observable debe hacer lo posible por responder a dos preguntas principales: "¿Qué?" y "¿Por qué?". "¿Qué?" se refiere a un síntoma de una aplicación o servicio durante un periodo de tiempo específico, mientras que "¿Por qué?" busca las razones detrás del síntoma.

### Métricas
Ya que deseas adaptar tus métricas a la felicidad del usuario, deberías usar un patrón común para alinear todas tus aplicaciones. Este enfoque es siempre bueno al instrumentar tus servicios, ya que permitir que cada aplicación tenga su propia versión única de métricas dificulta mucho el diagnóstico.

#### Señales de Oro
Las Señales de Oro son cuatro métricas que nos ayudan a entender la salud de un microservicio.
- **Latencia**: es el tiempo que tarda un servicio en procesar una solicitud.
- **Tráfico**: es la cantidad de solicitudes que una aplicación está recibiendo.
- **Errores**: es el número de errores que una aplicación está reportando (como un servidor web que informa de errores 500).
- **Saturación**: es cuán lleno está un servicio. Para una señal de saturación se puede medir el uso de la CPU para determinar cuánto margen de maniobra queda en el sistema antes de que la aplicación o el host se vuelvan lentos o no respondan.

Un microservicio típicamente es una aplicación poco aclopada a otros servicios en tu plataforma. Está diseñado para enfocarse únicamente en uno o dos aspectos de tu dominio general.

### Alertas
Las métricas y gráficos sólo constituyen la mitad de una solución de monitoreo. Cuando tu aplicación decide dar un paseo por un acantilado, alguien o algo necesita saberlo. Si un Pod muere en un Deployment, Kubernetes simplemente lo remplaza con uno nuevo. Pero si el Pod sigue reiniciándose, alguien debe abordarlo, y es ahí donde entran en juego las alertas y notificaciones.

¿Qué constituye una buena alerta? Además de una alerta para cada una de las Señales de Oro de tu aplicación, es posible que necesites una alerta entoeno a una métrica clave para monitorear. Cuando esto sucede, ten en cuenta un par de pautas a seguir al crear alertas: no establezca límites demasiados bajos y evitar alertas que no sean accionables.

### ¿Por qué centrarse en la observabilidad?
Enfocarse en la observabilidad puede ayudar a reducir el tiempo medio de resolución (MTTR), lo que resulta en interrupciones más cortas, mejor rendimiento de la aplicación y una experiencia del cliente mejorada. La observabilidad también es importante para los interesados no técnicos y las unidades de negocios. La observabilidad puede proporcionar una mejor visión del rendimiento de los KPI (Indicadores Clave de Rendimiento), así como opciones de autoservicio para diferentes equipos.

El software y las aplicaciones modernas dependen en gran medida de ofrecer buena experiencia de usuario (UX). El monitoreo de métricas estáticas no siempre contará la historia completa sobre la UX o el rendimiento del sistema. Puede haber problemas graves acechando detrás de paneles de métricas aparentemente saludables.

### Métricas clave de observabilidad
Para las organizaciones que han decidido implementar herramientas de observabilidad, el siguiente paso es identificar los objetivos principales de la observabilidad y cómo se puede implementar mejor en toda su pila de tecnologías:
- Registros: información y eventos.
- Métricas: medidas de métricas específicas y datos de rendimiento.
- rastreo: registro del rendimiento de las solicitudes de extremo a extremo durante la ejecución.

Datos y pilares adicionales de observabilidad incluyen:
- rastreo de errores: registros más detallados con agregación de información.
- Perfilado continuo: evaluación del rendimiento detallado del código.
- Monitoreo de usuario reales (RUM): comprensión del rendimiento de la aplicación desde la perspectiva de un usuario real.

### Diferencia entre monitoreo y observabilidad
El monitoreo es la práctica de recopilar y analizar datos de una aplicación o sistema para detectar y diagnosticar problemas. Esto se logra a través de la recopilación de métricas y registros, la configuración de alertas y visualización de gráficos y paneles de control.

Por otro lado, la observabilidad se refiere a la capacidad de un sistema para ser monitoreado, rastreado y analizado. Se trata de un enfoque más amplio y proactivo que busca comprender el comportamineto interno del sistema y su rendimiento en el mundo real.

## Métricas de monitorización
- **Plazo para modificaciones**: es el tiempo transcurrido entre el momento en que se confirma un cambio de código en la rama troncal y el momento en que se encuentra listo para implementar. Por ejemplo, cuando el código supera todas las pruebas necesarias previas a la publicación.
- **Tasa de errores por modificaciones**: es el porcentaje de cambios realizados en el código que requieren una corrección inmediata u otras soluciones tras haber pasado a producción.
- **Frecuencia de implementación**: es fundamental saber con qué frecuencia se implementa código nuevo en la fase de produción para poder medir el éxito de DevOps.
- **Tiempo medio de recuperación (MTTR)**: mide el tiempo que se tarda en recuperarse de una interrupción parcial del servicio o de un fallo total.
- **Tiempo medio de detección (MTTD)**: es el tiempo promedio transcurrido desde que comienza un incidente hasta que se descubre.
- **Duración del ciclo**: es el tiempo que un equipo dedica a trabajar en un elemento hasta que está listo para lanzarse.
- **Porcentaje de código cubierto**: mide la proporción de código sujeto a pruebas automatizadas.
- **Disponibilidad de la aplicación**: mide la proporción del tiempo en que una aplicación está completamente funcional y accesible para satisfacer las necesidades de los usuarios finales.

### Cómo medir, utilizar y mejorar las métricas de DevOps
- **Plazo para modificaciones**: la automatización de pruebas, el desarrollo basado en troncos y el trabajo en lotes pequeños son elementos clave para mejorar los plazos.
- **Tasa de errores por modificaciones**: las mismas prácticas que contribuyen a acortar los plazos (automatización de pruebas, desarrollo basado en troncos y trabajo en lotes pequeños) se asocian a una reducción de las tasas de errores por modificación.
- **Frecuencia de implementación**: la capacidad de implementar bajo demanda requiere una canalización de implementación automatizada que incorpore los mecanismos automatizados de pruebas y que minimice la necesidad de intervención humana.
- **Tiempo medio de recuperación (MTTR)**: la capacidad de recuperarse de un error depende de la capacidad de identificar rápidamente cuándo se produce un error e implementar una corrección o revisión de los cambios que han provocado ese error. Por lo general, esto se lleva a cabo supervisando continuamente el estado del sistema y alertando al equipo de operaciones en caso de que se produzca algún error.
- **Duración del ciclo**: los informes de duración del ciclo permiten a los responsables de proyectos establecer una referencia en la canalización de desarrollo que pueda servir para evaluar procesos futuros.

## Four Key Metrics
- **Frecuencia de Implementación**: rastrea la frecuencia de las implementaciones no solo en producción, sino también en los entornos de prueba y ensayo.
- **Plazo de Ejecución para Cambios**: es el tiempo que se tarda entre el momento en que se pide un cambio de código hasta que se ejecuta correctamente en producción.
- **Tiempo Medio de Restauración**: es el tiempo medio que se necesita para volver al servicio cuando ha habido un fallo en la producción.
- **Tasa de Fallo de Cambio**: consiste en la relación entre cambios que han fallado y los cambios exitosos en un servicio.

## ¿Qué es KPI?
Un KPI (Key Performance Indicator, Indicador Clave de Rendimiento) es una métrica para medir el rendimiento y el éxito de un proceso, proyecto o actividad en una organización. En DevOps, los KPI se utilizan para medir la eficacia de las prácticas y herramientas DevOps en términos de velocidad, calidad y eficiencia de entrega de software. Por ejemplo, algunos KPI comunes en DevOps incluyen el tiempo promedio de entrega de nuevas versiones, la tasa de éxito de las implementaciones, el tiempo de recuperación de incidentes...

Los KPI son importantes en DevOps porque permiten a los equipos de desarrollo y operaciones identificar áreas de mejora, tomar decisiones informadas y realizar ajustes en tiempo real para optimizar procesos y mejorar el rendimiento general del equipo y la organización.

## Conclusión
Las métricas y las alertas son piezas fundamentales en la monitorización de una aplicación. Proporcionan información sobre la salud y el rendimiento de tus servicios. La capacidad de medir y supervisar el rendimiento mediante las diferentes métricas permite a los equipos acelerar en velocidad y aumentar su calidad.

## Referencias
- DevOps For The Desperate A Hands-On Survival Guide - [bibis.ir](https://bibis.ir/science-books/programming/2022/Devops%20For%20The%20Desperate%20A%20Hands-On%20Survival%20Guide%20by%20Bradley%20Smith_bibis.ir.pdf)
- Observability vs Monitoring in DevOps - [about.gitlab.com](https://about.gitlab.com/blog/2022/06/14/observability-vs-monitoring-in-devops/)
- Métricas de DevOps - [atlassian.com](https://www.atlassian.com/es/devops/frameworks/devops-metrics)
- 9 key DevOps metrics for success - [dynatrace.com](https://www.dynatrace.com/news/blog/devops-metrics-for-success/)
- ¿Cómo medir el éxito de DEVOPS a través de las FOUR KEY METRICS? - [youtube.com](https://www.youtube.com/watch?v=FKDzAGYzePs&list=TLPQMDMwNTIwMjNOb3RT_ME9Sg&index=3&ab_channel=SENTRIO)

# Prometheus: Monitorización de Métricas
Prometheus es un conjunto de herramientas de monitoreo y alerta de sistemas de código abierto. Prometheus recopila y almacena sus métricas como datos de series temporales, es decir, la información de las métricas se almacena con la marca de tiempo en la que se registró, junto con pares clave-valor opcionales denominados etiquetas.

## Características
- Modelo de datos multidimensional con datos de series temporales identificados por nombre de métrica y pares clave/valor.
- Sin dependencia del almacenamiento distribuido; los nodos de un solo servidor son autónomos.
- La recopilación de series temporales se realiza a través de un modelo de extracción a través de HTTP.
- Los objetivos se descubren a través del descubrimiento de servicios o la configuración estática.
- Múltiples modos de soporte de gráficos y tableros.

## ¿Qué son las métricas?
En términos sencillos, las métricas son medidas numéricas. Serie temporal significa que los cambios se registran a lo largo del tiempo. Lo que los usuarios quieren medir difiere de una aplicación a otra.

Las métricas juegan un papel importante para comprender por qué su aplicación funciona de cierta manera. Supongamos que está ejecutando una aplicación web y descubre que la aplicación es lenta. Necesitará cierta información para saber qué está pasando con su aplicación. Por ejemplo, la aplicación puede volverse lenta cuando la cantidad de solicitudes es alta. Si tiene la métrica de recuento de solicitudes, puede detectar el motivo y aumentar la cantidad de servidores para manejar la carga.

## Referencias
- Desarrollo e Implementación de una Arquitectura DevOps - [dspace.ups.edu.ec](https://dspace.ups.edu.ec/bitstream/123456789/21675/1/UPS-CT009520.pdf)
- Prometheus - [prometheus.io](https://prometheus.io/docs/introduction/overview/)
