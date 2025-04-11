### Стандартная настройка веб-сервера

#### Установка необходимых пакетов для сохранения правил
```shell
sudo apt install iptables-persistent netfilter-persistent
```

Настройки сохраняются в /etc/iptables/rules.v4
#### разрешаем 22 порт
```shell
iptables -A INPUT -p tcp --dport 22 -j ACCEPT 
```
#### разрешаем трафик для lo интерфейса
```shell
iptables -A INPUT -i lo -j ACCEPT
```
#### разрешаем icmp
```shell
iptables -A INPUT -p icmp -j ACCEPT
```
#### Разрешаем 80 и 443 порты
```shell
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
```
#### Разрешаем принимать ответы для наших соединений
```shell
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
```
#### Меняем политику по умолчанию на блокировку всех пакетов не соответствующих правилам выше
```shell
iptables -P INPUT DROP
```
#### Блокируем неугодный ip
```shell
iptables -I INPUT -s 192.168.2.42 -j DROP 
```

