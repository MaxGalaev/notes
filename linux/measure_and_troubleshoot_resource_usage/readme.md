### Нагрузка, производительность, траблшутинг

### Теория:

### Практика:

Проверяем версию системы

```shell
lsb_release -a
```

Проверяем кто в системе и насколько грузит
 
```shell
w
```

Проверяем информацию о сетевой нагрузке

```shell
netstat -i 
netstat -s
```

Проверяем открытые файлы

```shell
lsof
```

Проверяем процессы и нагрузку

```shell
ps aux
top
```

Для сбора информации используется набор утилит sysstat

 - sar: collects and reports system activity information;
 - iostat: reports CPU utilization and disk I/O statistics;
 - tapestat: reports statistics for tapes connected to the system;
 - mpstat: reports global and per-processor statistics;
 - pidstat: reports statistics for Linux tasks (processes);
 - sadf: displays data collected by sar in various formats;
 - cifsiostat: reports I/O statistics for CIFS filesystems.  

Если нам нужно собрать информацию прямо сейчас в онлайне используется утилита sar.
Например, мы хотим собирать информацию по процессору каждую секунду 3 раза
```shell
sar -u 1 3 # процессор
sar -r 1 3 # память
sar -S 1 3 # swap
sar -b 1 3 # диск
```

В основном sar используется для сбора данных по крону.
