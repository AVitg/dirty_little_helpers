## on Ubuntu 22 lts fresh install: / 2023_05
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
