# Monitorización de ArgoCD con Prometheus
## Instalar Argocd
En mi caso, ya tenía instalado Argocd siguiendo esta [guía de instalación de ArgoCD](https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/apuntes/Comandos%20ArgoCD.md).

Lo primero será desplegar la aplicación `workshop` en ArgoCD ejecutando el siguiente comando:
```powershell
cat <<EOF | kubectl apply -f -
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
    repoURL: https://github.com/naturalett/continuous-delivery
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
Una vez desplegado la aplicación workshop, accede a la interfaz de ArgoCD para comprobar el despliegue de la aplicación o ejecuta el siguiente comando para 

## Referencias
- Deploying Prometheus and Grafana as Applications Using ArgoCD — Including Dashboards - [dzone.com](https://dzone.com/articles/deploying-prometheus-and-grafana-as-applications-u)
