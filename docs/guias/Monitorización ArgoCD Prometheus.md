# Monitorización de ArgoCD con Prometheus
## Instalar Argocd
En mi caso, ya tenía instalado Argocd siguiendo esta [guía de instalación de ArgoCD](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/apuntes/Comandos%20ArgoCD.md).

## Vincular un repositorio principal a ArgoCD
ArgoCD usa la información de source y destination para monitorear continuamente el repositorio de Git en busca de cambios e implementarlos en el entorno de destino. Pongámoslo en acción aplicando los cambios:
```powershell
sudo cat <<EOF | kubectl apply -f -
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: workshop
  namespace: argocd
spec:
  destination:
    namespace: argocd
    server: https://kubernetes.default.svc
  project: default
  source:
    path: argoCD/
    repoURL: https://gitlab.com/mikel-m/configSecDelivAutoIoT.git
    targetRevision: main
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
EOF
```
Si da un error a la hora de ejecutarlo como el siguiente:
```powershell
WARN[0000] Unable to read /etc/rancher/k3s/k3s.yaml, please start server with --write-kubeconfig-mode to modify kube config permissions
error: error loading config file "/etc/rancher/k3s/k3s.yaml": open /etc/rancher/k3s/k3s.yaml: permission denied
```
Hay que ejecutar el siguiente comando y después ejecutar nuevamente el primer comando:
```powershell
sudo chmod +r /etc/rancher/k3s/k3s.yaml
```
Accedamos a la interfaz de usuario del servidor mediante el reenvío de puertos kubectl:
```powershell
kubectl port-forward service/argocd-server -n argocd 8080:443
```

## Referencias
- Deploying Prometheus and Grafana as Applications Using ArgoCD — Including Dashboards - [dzone.com](https://dzone.com/articles/deploying-prometheus-and-grafana-as-applications-u)
