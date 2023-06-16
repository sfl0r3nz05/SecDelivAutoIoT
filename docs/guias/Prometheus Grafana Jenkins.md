# Configuración Prometheus y Grafana (GitLab)
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
      - targets: ['172.17.0.1:8081']
EOF

docker restart prometheus
```
La ip `172.17.0.1` es la ip del gateway del network bridge y el puerto `8083` es el puerto de jenkins (`docker network inspect bridge`).

Al ejecutar estos comando, comprobamos que todo ha ido correcto accediendo a [http://localhost:9090/targets](http://localhost:9090/targets):
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Jenkins-Prometheus-targets.PNG" alt="http://localhost:9090/targets">

## Añadir dashboard en Grafana
1. Accede a Grafana [http://localhost:3000/login](http://localhost:3000/login) e inicia sesión con las credenciales `admin/admin`. La primera vez que accedes te pedirá cambiar de contraseña pero volveremos a poner la contraseña `admin` para simplificar.
2. En el meno de la izquierda, seleccionar `Connections`--> `Data sources` --> `Add data source` y de la lista seleccionar `Prometheus`. 
3. Se abrirá un menú de configuración del data source de prometheus y tenemos que completar el campo de "Prometheus server URL" con `http://172.17.0.1:9090`. Si al clickar en `Save & test` sale el mensaje `Successfully queried the Prometheus API.` es que la conexión se ha realizado correctamente.
4. En la parte superior de Grafana clickameo en el icono `+` y `Import dashboard`. Ahí, en el campo "Import via grafana.com" introducimos el ID del dashboard que queremos importar, en nuestro caso: `9964` y después cliclamos en `Load`. En el campo "Prometheus" se abre un desplegable y seleccionamos `Prometheus` y hacemos click en `Import`.

una vez configurado, se nos abre el dashboard:
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Jenkins-Dashboard-1.PNG" alt="Primer dashboard de Jenkins">
