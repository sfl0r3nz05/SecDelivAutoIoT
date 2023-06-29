# Monitorización de Jenkins (Prometheus y Grafana)
## Configuración inicial
Lo primero de todo es poner en marcha los conteneodres de Jenkins, Prometheus y Grafana. En nuestro caso, vamos a añadir diferentes puertos a los contenedores ya que estamos utilizando los puertos en otro proyecto:
```powershell
docker run -d --name jenkins -p 8081:8080 -p 50000:50000 jenkins/jenkins:latest
docker run -d --name prometheus -p 9090:9090 prom/prometheus:latest
docker run -d --name grafana -p 3000:3000 grafana/grafana:latest
```

Una vez desplegados los contenedores, accedemos a `http://localhost:8081/` para acceder a Jenkins e instalamos el plugin `Prometheus metrics`. Una vez instalado el plugin, reiniciamos el contenedor docker:
```powershell
docker restart jenkins
```

## Configurar `prometheus.yml`
Tenemos que añadir el job de jenkins al archivo `prometheus.yml` del contenedor de prometheus.
```powershell
docker exec -it prometheus sh

tee -a /etc/prometheus/prometheus.yml <<EOF
  - job_name: jenkins
    metrics_path: /prometheus
    static_configs:
      - targets: ['172.19.0.1:8081']
EOF

docker restart prometheus
```
La ip `172.19.0.1` es la ip del gateway del network `secdelivautoiot` (que es el que utilizo en mi proyecto) y el puerto `8081` es el puerto de jenkins (`docker network inspect secdelivautoiot`). Si se está utilizando otro network de docker, hay que ejecutar el comando `docker network inspect <nombre-network>` y mirar la ip del gateway del network.

Al ejecutar estos comando, comprobamos que todo ha ido correcto accediendo a [http://localhost:9090/targets](http://localhost:9090/targets):
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Jenkins-Prometheus-targets.PNG" alt="http://localhost:9090/targets">

## Añadir dashboard en Grafana
1. Accede a Grafana [http://localhost:3000/login](http://localhost:3000/login) e inicia sesión con las credenciales `admin/admin`. La primera vez que accedes te pedirá cambiar de contraseña pero volveremos a poner la contraseña `admin` para simplificar.
2. En el meno de la izquierda, seleccionar `Connections`--> `Data sources` --> `Add data source` y de la lista seleccionar `Prometheus`. 
3. Se abrirá un menú de configuración del data source de prometheus y tenemos que completar el campo de "Prometheus server URL" con `http://172.19.0.1:9090`. Si al clickar en `Save & test` sale el mensaje `Successfully queried the Prometheus API.` es que la conexión se ha realizado correctamente.
4. En la parte superior de Grafana clickamos en el icono `+` y `Import dashboard`. Ahí, en el campo "Import via grafana.com" introducimos el ID del dashboard que queremos importar, en nuestro caso: `9964` y después cliclamos en `Load`. En el campo "Prometheus" se abre un desplegable y seleccionamos `Prometheus` y hacemos click en `Import`.

Una vez configurado, se nos abre el dashboard:
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Jenkins-Dashboard-1.PNG" alt="Primer dashboard de Jenkins">

Después de algunas ejecuciones del pipeline de Jenkins ([guía para configurar Jenkis](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/guias/Jenkins.md)) podemos ver los siguientes cambios en el dashboard para ver que obtiene métricas de Jenkin:
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Jenkins-Dashboard-2.PNG" alt="Segundo dashboard de Jenkins">

***
## Cambiar visualización de métricas en Grafana
En nuestro pipeline de Jenkins, tenemos 4 stages que queremos monitorizar el tiempo de ejecución:
- Analysis with SonarQube
- Build and Publish Image to Docker Hub
- Image Analysis with Trivy
- Deploy Image to ArgoCD

Esto es un ejemplo pero se puede ajustar a cualquier métrica que queramos monitorizar. Para poder visualizar el tiempo de ejecución de cada stage en Grafana, editamos un panel del dashboard (`...` --> `Edit`). Se abrirá la configuración del panel. En nuestro caso, las métricas que recibimos del tiempo de duración del job está en milisegundos, por lo que tenemos que tenemos que añadir una expresión (botón `+ Expression`) y añadimos la expresión de las métricas que queremos visualizar. En nuestro caso, para especificar el stage tenemos que añadir las opciones "stage" y "jenkins_job" especificando su valor y dividiéndolo por 1000 para obtener los segundos como se muestra en la imagen:
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Expresion%20Grafana.PNG" alt="Expression de Grafana">

Para mostrar en formato hh:mm:ss, en el menú de la derecha, hay que buscar `Standard options` --> `Unit` y cambiar el valor por `Time` --> `duration (hh:mm:ss)`.

Para cambiar el tipo de visualización, en el menú de la derecha en la parte superior hay un desplegable (en mi caso pone "stat"), al desplegarlo clicka en `Suggestions` y selecciona el que más te guste.

Esta sería la captura completa de la configuración del panel (en este caso el análisis de SonarQube pero el resto de los stages sería igual):
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Configuracion%20Panel%20Grafana.PNG" alt="Configuración del panel de Grafana">

Resultado final:
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Dashboard%20Completo%20Grafana.PNG" alt="Dashboard completo de Grafana">
