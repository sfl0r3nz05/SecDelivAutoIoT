# Configuración Prometheus y Grafana (GitLab)
## Configuración inicial
Lo primero de todo es poner en marcha los conteneodres de Jenkins, Prometheus y Grafana:
```powershell
docker run -d --name jenkins -p 8081:8080 -p 50000:50000 jenkins/jenkins:latest
docker run -d --name prometheus -p 9090:9090 prom/prometheus
docker run -d --name grafana -p 3000:3000 grafana/grafana
```

Una vez desplegados los contenedores, accedemos a `http://localhost:8081/` para acceder a Jenkins e instalamos el plugin `Prometheus metrics`. Una vez instalado el plugin, reiniciamos el contenedor docker:
```powershell
docker restart jenkins
```

## Configurar `prometheus.yml`
Como nostros ya tenemos el contenedor de prometheus desplegado de otro proyecto, añadimos al archivo `prometheus/config.yml` (en otros proyectos es `prometheus.yml`)el siguiente job:
```
  - job_name: jenkins
    metrics_path: /prometheus
    static_configs:
      - targets: ['jenkins:8081']
```

Una vez añadido, hacemos `docker-compose restart` para aplicar los cambios:
```powershell
docker-compose restart
```
