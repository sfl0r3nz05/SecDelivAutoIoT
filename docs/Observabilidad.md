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

### Conclusión
las métricas y las alertas son piezas fundamentales en la monitorización de una aplicación. Proporcionan información sobre la salud y el rendimiento de tus servicios.

## Referencias
- DevOps For The Desperate A Hands-On Survival Guide - [bibis.ir](https://bibis.ir/science-books/programming/2022/Devops%20For%20The%20Desperate%20A%20Hands-On%20Survival%20Guide%20by%20Bradley%20Smith_bibis.ir.pdf)
- Observability vs Monitoring in DevOps - [about.gitlab.com](https://about.gitlab.com/blog/2022/06/14/observability-vs-monitoring-in-devops/)
