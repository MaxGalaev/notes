Я продолжаю открывать для себя линукс, во всем его противоречии.
Казалось бы простая задача по смене порта ssh демона на кастомный превращается в увлекательный квест в мире сервисов и сокетов, по крайней мере в Ubuntu.
После того как я поменял директиву Port 22 на Port 222 в /etc/ssh/sshd_config и попытался рестартануть сервис sshd, оказалось что такого сервиса нет)
Команда sudo systemctl status ssh выводит:
```
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/usr/lib/systemd/system/ssh.service; disabled; preset: enabled)
     Active: active (running) since Thu 2025-02-27 10:17:31 UTC; 6min ago
TriggeredBy: ● ssh.socket
       Docs: man:sshd(8)
             man:sshd_config(5)
    Process: 1319 ExecStartPre=/usr/sbin/sshd -t (code=exited, status=0/SUCCESS)
   Main PID: 1321 (sshd)
      Tasks: 1 (limit: 1064)
     Memory: 3.4M (peak: 4.3M)
        CPU: 132ms
     CGroup: /system.slice/ssh.service
             └─1321 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"
```
Это позволяет нам понять что мы имеем дело не с сервисом, а с сокетом. Оказывается в Ubuntu начиная с версии 22.10 OpenSSH сервер перешел на работу с systemd socket activation.


