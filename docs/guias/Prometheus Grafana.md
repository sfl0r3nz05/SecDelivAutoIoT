# Configuración Prometheus y Grafana
## Configuración inicial
Vamos a utilizar los archivos del repositorio [mvisonneau/gitlab-ci-pipelines-exporter](https://github.com/mvisonneau/gitlab-ci-pipelines-exporter/tree/main) de github. Lo primero que tenemos que hacer es clonar el repositorio y dirigirnos a la carpera `gitlab-ci-pipelines-exporter/examples/quickstart`:
```powershell
git clone https://github.com/mvisonneau/gitlab-ci-pipelines-exporter.git
cd gitlab-ci-pipelines-exporter/examples/quickstart
```
En Ubuntu habría que ejecutar el siguiente comando:
```powershell
sed -i 's/<your_token>/xXF_xxjV_xxyzxzz/' gitlab-ci-pipelines-exporter.yml
```
Pero como yo estaba utilizando el powershell de Visual Studio Code, he ejecutado el siguiente comando:
```powershell
(Get-Content -Path "gitlab-ci-pipelines-exporter.yml") -replace "<your_token>", "xXF_xxjV_xxyzxzz" | Set-Content -Path "gitlab-ci-pipelines-exporter.yml"
```
Para ejecutar este paso, hay que crear un token de acceso en GitLab con el permiso de `read_api` y sustituirlo por `<your_token>`. Aún así, hay que añadir el token de acceso en el archivo `docker-compose.yml` en el campo `GCPE_GITLAB_TOKEN` y en el archivo `gitlab-ci-pipelines-exporter.yml` en el apartado de `gitlab:` --> `token:`.

En mi caso, he creado un network en docker llamado `secdelivautoiot` para que se comuniquen entre sí los contenedores, para ello aádimos el campo `network` en cada job de `docker-compose.yml` y añadimos el nombre del network. Antes de ejecutar el comando de docker-compose, hay que añadir el repositorio de GitLab que se quieren medir las métricas (en mi caso mikel-m/SecDelivAutoIoT). Entonces los archivos quedarías así:
***
### `docker-compose.yml`
```
---
version: '3.8'
services:
  gitlab-ci-pipelines-exporter:
    image: quay.io/mvisonneau/gitlab-ci-pipelines-exporter:v0.5.5
    # You can comment out the image name and use the following statement
    # to build the image against the current version of the repository
    # build: ../..
    ports:
      - 8080:8080
    environment:
      GCPE_GITLAB_TOKEN: <gitlab-token>
      GCPE_CONFIG: /etc/gitlab-ci-pipelines-exporter.yml
      GCPE_INTERNAL_MONITORING_LISTENER_ADDRESS: tcp://127.0.0.1:8082
    volumes:
      - type: bind
        source: ./gitlab-ci-pipelines-exporter.yml
        target: /etc/gitlab-ci-pipelines-exporter.yml
    networks:
      - secdelivautoiot

  prometheus:
    image: docker.io/prom/prometheus:v2.44.0
    ports:
      - 9090:9090
    links:
      - gitlab-ci-pipelines-exporter
    volumes:
      - ./prometheus/config.yml:/etc/prometheus/prometheus.yml
    networks:
      - secdelivautoiot

  grafana:
    image: docker.io/grafana/grafana:9.5.2
    ports:
      - 3000:3000
    environment:
      GF_AUTH_ANONYMOUS_ENABLED: 'true'
      GF_INSTALL_PLUGINS: grafana-polystat-panel,yesoreyeram-boomtable-panel
    links:
      - prometheus
    volumes:
      - ./grafana/dashboards.yml:/etc/grafana/provisioning/dashboards/default.yml
      - ./grafana/datasources.yml:/etc/grafana/provisioning/datasources/default.yml
      - ./grafana/dashboards:/var/lib/grafana/dashboards
    networks:
      - secdelivautoiot

networks:
  secdelivautoiot:
    driver: bridge
```

### `gitlab-ci-pipelines-exporter.yml`
```
---
log:
  level: debug

gitlab:
  url: https://gitlab.com
  token: <gitlab-token>

# Pull jobs related metrics on all projects
project_defaults:
  pull:
    pipeline:
      jobs:
        enabled: true

projects:
  - name: mikel-m/SecDelivAutoIoT
    # Pull environments related metrics prefixed with 'stable' for this project
    pull:
      environments:
        enabled: true
        name_regexp: '^stable.*'

```

### `prometheus/config.yml`
```
global:
  scrape_interval:     15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'gitlab-ci-pipelines-exporter'
    scrape_interval: 10s
    scrape_timeout: 5s
    static_configs:
      - targets: ['gitlab-ci-pipelines-exporter:8080']
```

### `grafana/datasources.yml`
```
datasources:
- name: 'prometheus'
  type: 'prometheus'
  access: 'proxy'
  org_id: 1
  url: 'http://prometheus:9090'
  is_default: true
  version: 1
  editable: true
```
***

Una vez ya teniendo todo configurado, podemos ejecutar el comando docker-compose:
```powershell
docker-compose up -d
```
Y tendrá que salir esto:
```powershell
Creating quickstart_gitlab-ci-pipelines-exporter_1 ... done
Creating quickstart_prometheus_1                   ... done
Creating quickstart_grafana_1                      ... done
```
Y si se ejecuta el comando `docker ps` se tendría que ver esto:
```powershell
9b7f4bb8d3a0   grafana/grafana:9.5.2                                    "/run.sh"                43 minutes ago   Up 4 minutes   0.0.0.0:3000->3000/tcp              quickstart_grafana_1
4c45e5e9eb70   prom/prometheus:v2.44.0                                  "/bin/prometheus --c…"   43 minutes ago   Up 4 minutes   0.0.0.0:9090->9090/tcp              quickstart_prometheus_1
f2071a0fb1bf   quay.io/mvisonneau/gitlab-ci-pipelines-exporter:v0.5.5   "/usr/local/bin/gitl…"   44 minutes ago   Up 4 minutes   0.0.0.0:8080->8080/tcp              quickstart_gitlab-ci-pipelines-exporter_1
```

Si entras en [http://localhost:9090/targets](http://localhost:9090/targets) tendría que salir algo así:
<br>************ INSERTAR CAPTURA ************

Y para acceder al dashboard del pipeline de grafana, tienes que acceder a [http://localhost:3000/d/gitlab_ci_pipelines](http://localhost:3000/d/gitlab_ci_pipelines) y tendría que salir algo así:
<br>************ INSERTAR CAPTURA ************

Si se quiere acceder al dashboard de los jobs, tienes que acceder a [http://localhost:3000/d/gitlab_ci_jobs](http://localhost:3000/d/gitlab_ci_jobs) y tendría que salir algo así:
<br>************ INSERTAR CAPTURA ************

## Referencias
- Example usage of gitlab-ci-pipelines-exporter with Prometheus & Grafana - [github.com](https://github.com/mvisonneau/gitlab-ci-pipelines-exporter/tree/main/examples/quickstart)
