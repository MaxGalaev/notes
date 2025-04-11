### Установка через APT
```shell
sudo apt install ansible
```
### Чтобы отключить запрос на фингерпринт надо добавить в конфиг строку
```
[defaults]
host_key_checking = false
```
### Описание
Дефолтный список хостов берется из
```
/etc/ansible/hosts
```
Конфиг лежит в 
```
/etc/ansible/ansible.cfg
```
