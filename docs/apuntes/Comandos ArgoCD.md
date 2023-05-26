# ArgoCD
## Instalación ArgoCD
### ArgoCD
```
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

### Instalar ArgoCD CLI
```
curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
sudo install -m 555 argocd-linux-amd64 /usr/local/bin/argocd
rm argocd-linux-amd64
```

### Port Forwarding
```
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

### Login Using The CLI
```
argocd admin initial-password -n argocd
argocd login <ARGOCD_SERVER>
```
***

## Create app
```
argocd app create <nombre-app> --repo https://gitlab.com/user/repository.git --path <ruta-yaml-configuración> --dest-server https://kubernetes.default.svc --dest-namespace argocd
```
- `--path` es la ruta donde está la configuración YAML, en nuestro caso de ejemplo, dento de la carpeta _kubernetes_, por lo que habría que poner `--path kubernetes`.
- `--dest-server https://kubernetes.default.svc`es el cluster de K3s que se va a desplegar, en este caso, el cluster local.
- `--dest-namespace argocd` es el namespace en el que se va a desplegar, por defecto es _default_, pero en mis pruebas he puesto _argocd_.

### Sincronizar app
```
argocd app sync <nombre-app>
```

### Desplegar app desde ArgoCD en la Raspberry Pi
```
argocd app create <nombre-app> --repo https://gitlab.com/user/repository.git --path . --dest-server https://<ip-raspberry-pi> --dest-namespace <namespace-raspberry-pi>
```

## Add repo
Hay que crear un Token de acceso en GitLab
```
sudo argocd repo add https://gitlab.com/user/repository.git --password <token-de-acceso>
```

## Referencias
- Getting Started (ArgoCD) - [argo-cd.readthedocs.io](https://argo-cd.readthedocs.io/en/stable/getting_started/)
