# Instalación ArgoCD
En esta guía vamos a explicar cómo instalar ArgoCD en la máquina virtual donde vamos a desplegar las aplicaciones.

## Instalación ArgoCD
Para instalar ArgoCD, hay que ejecutar los siguientes comandos:
```powershell
sudo kubectl create namespace argocd
sudo kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

también vamos a crear un namespace, que es donde vamos a desplegar la aplicación:
```powershell
sudo kubectl create namespace secdelivautoiot
```

## Acceder a la API de ArgoCD
Para acceder a ArgoCD, hay que ejecutar el siguiente comando:
```powershell
sudo kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
```

Y para saber a qué puerto tenemos que acceder en el navegador, ejecutamos el siguiente comando y nos fijamos en la línea de `service/argocd-server`:
```powershell
sudo kubectl get all -n argocd
```

En nuestro caso, nos sale esto:
``` powershell
service/argocd-server                             LoadBalancer   10.43.179.226   <pending>     80:30361/TCP,443:32261/TCP   30m
```
Por lo que en el navegador tenemos que acceder a [http://\<ip-maquina-virtual\>:\<puerto-argocd-server\>](http://\<ip-maquina-virtual\>:32261), que en nuestro caso es el puerto 32261.

## Login en ArgoCD
Para acceder a ArgoCD, tenemos que ejecutar el siguiente comando para obtener la contraseña inicial de ArgoCD:
```powershell
argocd admin initial-password -n argocd
```

Una vez obtenida la contraseña, iniciamos sesión desde la línea de comandos ejecutando el siguiente comando:
```powershell
argocd login localhost:32261 --insecure --username admin --password <contraseña-inicial>
```

Al iniciar sesión, si se quiere cambiar la contraseña, ejecuta el siguiente comando:
```powershell
argocd account update-password
```

## Acceder a la interfaz de ArgoCD
Una vez todo listo, en el navegador, introduce la ip de la máquina virtual y el puerto mostrado anteriormente ([http://\<ip-maquina-virtual\>:\<puerto-argocd-server\>](http://\<ip-maquina-virtual\>:32261)) e introduces el usuario `admin` y la contraseña que hayas introducido con el cambio de contraseña.
<img src="https://github.com/sfl0r3nz05/SecDelivAutoIoT/blob/master/docs/images/Captura%20Menu%20ArgoCD.PNG" alt="Menu ArgoCD">

## Referencias
- ArgoCD - Getting Started - [argo-cd.readthedocs.io](https://argo-cd.readthedocs.io/en/stable/getting_started/)
