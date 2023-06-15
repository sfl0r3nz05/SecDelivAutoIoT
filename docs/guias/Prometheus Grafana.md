# Configuración Prometheus y Grafana
## Configuración Prometheus
Hay que crear el archivo `prometheus.yml` y añadir lo siguiente:
```
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'gitlab'
    metrics_path: '/-/metrics'
    static_configs:
      - targets: ['<ip-maquina-local>:8080']
```

También hay que crear el archivo `grafana.ini`. Esta es una configuración básica del archivo:
```
[paths]
data = /var/lib/grafana
logs = /var/log/grafana
plugins = /var/lib/grafana/plugins
provisioning = /etc/grafana/provisioning

[server]
http_port = 3000
domain = localhost

[database]
type = sqlite3
path = /var/lib/grafana/grafana.db

[auth.anonymous]
enabled = true

[auth.basic]
enabled = false

[auth.github]
enabled = false

[metrics]
enabled = true
interval_seconds = 10
```

Por último, hay qye crear el archivo `docker-compose.yml` para desplegar los contenedores de Prometheus y Grafana:
```
version: '3'
services:
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - 9090:9090

  grafana:
    image: grafana/grafana
    volumes:
      - ./grafana.ini:/etc/grafana/grafana.ini
    ports:
      - 3000:3000
```

Para desplegar los contenedores, hay que ejecutar el siguiente comando:
```
docker-compose up -d
```

Para acceder a Prometheus, hay que introducir `http://localhost:9090/` en el navegador. Y para acceder a Grafana, hay que introducir `http://localhost:3000/` en el navegador.

## Inicio de Grafana
Lo primero, hay que iniciar sesión en Grafana. Para ello hay que introducir el usuario y la contraseña `admin/admin`. Una vez que se haya iniciado sesión, hay que agregar un nuevo panel de Grafana haciendo clic en el botón "+" (icono en la parte superior) y seleccionando "Panel vacío".
