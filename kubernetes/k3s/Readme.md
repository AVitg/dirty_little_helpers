## on Ubuntu 22 lts fresh install: / 2023_05

### pods not coming up after first reboot
- follow no"k3s install guide
- everything works fine, after reboot local path or so does not come up.
- do below as per [1]

create  /etc/systemd/network/50-flannel.link
```
[Match]
OriginalName=flannel*

[Link]
MACAddressPolicy=none
```


[1]
https://wiki.archlinux.org/title/Kubernetes#Pods_cannot_communicate_when_using_Flannel_CNI_and_systemd-networkd

### getting error (:8080 unreachable, when deploying helm charts)
as per: https://wiki.archlinux.org/title/Kubernetes#Pods_cannot_communicate_when_using_Flannel_CNI_and_systemd-networkd
```
kubectl config view --raw > ~/.kube/config
```


### cconecting to dashboard
- create token
```
 sudo k3s kubectl -n kubernetes-dashboard create token admin-user
```
- run proxy??
```
sudo k3s kubectl proxy 
```
- forward
```
kubectl -n kubernetes-dashboard port-forward  kubernetes-dashboard-POD__ID  8443:8443
```
- connect using https