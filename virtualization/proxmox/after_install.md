### Настройка репозиториев для Proxmox 8 и выше
```shell
sudo nano /etc/apt/sources.list.d/pve-enterprise.list
```

```
#deb https://enterprise.proxmox.com/debian/pve bookworm enterprise
deb http://download.proxmox.com/debian/pve bookworm pve-no-subscription
deb http://security.debian.org/debian-security bookworm-security main contrib
```

```shell
sudo nano /etc/apt/sources.list.d/ceph.list
```

For Ceph Quincy

```
deb http://download.proxmox.com/debian/ceph-reef bookworm no-subscription
```

### Добавление токена для Ansible

Галочку Privilege Separation нужно убрать

```
TokenID: root@pam!ansible
Secret: 502c98c6-adab-4afd-a26b-8b9297b110b8
```
