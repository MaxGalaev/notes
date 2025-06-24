Проверка узлов кластера
```shell
etcdctl member list
```
Состояние узлов кластера
```shell
etcdctl endpoint status --cluster --write-out=table
```
Здоровье узлов кластера
```shell
etcdctl endpoint health --cluster
```
