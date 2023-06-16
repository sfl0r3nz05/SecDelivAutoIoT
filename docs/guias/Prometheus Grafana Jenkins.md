# Configuración Prometheus y Grafana (GitLab)
## Configuración inicial
Lo primero de todo es poner en marcha los conteneodres de Jenkins, Prometheus y Grafana. En nuestro caso, vamos a añadir diferentes puertos a los contenedores ya que estamos utilizando los puertos en otro proyecto:
```powershell
docker run -d --name jenkins -p 8083:8080 -p 50001:50000 jenkins/jenkins:latest
docker run -d --name prometheus -p 9091:9090 prom/prometheus
docker run -d --name grafana -p 3001:3000 grafana/grafana
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
      - targets: ['172.17.0.1:8083']
EOF

docker restart prometheus
```
La ip `172.17.0.1` es la ip del gateway del network bridge y el puerto `8083` es el puerto de jenkins (`docker network inspect bridge`).

Al ejecutar estos comando, comprobamos que todo ha ido correcto accediendo a [http://localhost:9091/targets](http://localhost:9091/targets):
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Jenkins-Prometheus-targets.PNG" alt="http://localhost:9091/targets">

## Añadir dashboard en Grafana
1. Accede a Grafana [http://localhost:3001/login](http://localhost:3001/login) e inicia sesión con las credenciales `admin/admin`. La primera vez que accedes te pedirá cambiar de contraseña pero volveremos a poner la contraseña `admin` para simplificar.
2. Clicka en el icono "+" de la parte superior y "New dashboard". Se abrirá un  menú y hay que clickar en "+ Add visualization".
3. Se abrirá un mnú para seleccionar el data source. En la parte inferior, hay que clickar en "Configure a new data source" y de las opciones que sale, seleccionar "Prometheus".
