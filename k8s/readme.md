### Основные понятия Кубера

Кластер Кубера состоит из 2-х типов нод: master node и worker node. И тех и тех может быть больше одной.
Сервисы работающие на master node называются control plane. Сама master node используется только для административных задач. Контейнеры запускаются только на worker node.
Компоненты control plane могут запускаться на любой машине в коастере, однако обычно все запускается на одном сервере.

### Минимальный набор компонентов кластера:
- Control plane
  - apiserver
  - controller-manager
  - kube-scheduller
  - etcd
- Worker-nodes
  - kubelet
  - kube-proxy
### Master node
1) etcd - распределенное key-value хранилище. Хранит всю информацию о кластере и его обьектах.
2) kube-apiserver - точка входа для всех запросов в кластер. Только он может что-то менять в кластере. Отвечает за авторизацию и аутентификацию.
3) kube-controller-manager - приводит состояние кластера к желаемому. Включает в себя множество других сервисов.
4) kube-scheduller - распределяет контейнеры по нодам
### Worker node
1) Runtime контейнеров: Docker, Containerd(по умолчанию), CRI-O  
2) kubelet - основной компонент на каждой рабочей ноде кластера. Управляет жизненным циклом локально работающего контейнера. Рапортует apiserver об изменениях.
3) kube-proxy - отвечает за сетевое взаимодействие контейнеров. Конфигурирует правила iptables.

### Абстракции Кубернетиса
1) pod - минимальная единица запуска. Состоит из дного или нескольких контейнеров и работает с ними как с единым целым. Контейнеры с поде имееют общий сетевой неймспейс. Нет пода - нет контейнера. 
Минимальный конфиг пода: 
```yml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: nginx-container
    image: nginx
```

2) labels - произвольная пара ключ:значение, добавляемая к ресурсу для дальнейшей выборки по определенным правилам, которые назывются селекторами. Под может иметь несколько labels. Labels обычно прикрепляются к ресурсам в момент создания, но могут быть добавлены и потом. 
Спецификация пода с лейблами:
```yml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  labels:
    environment: prod
    app: nginx
spec:
  containers:
  - name: nginx-container
    image: nginx
```
3) ReplicaSet - обеспечивает поддержание постоянной работы подов, гарантирует что поды всегда запущены, в случае падения ноды создаст новые реплики подов на других нодах, обеспечивает горизонтальное масштабироввание подов.
Спецификация ReplicaSet:
```yml
apiVersion: v1
kind: ReplicaSet
metadata:
  name: nginx
  labels:
    app: nginx
    cluster: prod
spec:
  replicas: 3
  selector:
    matchlabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx 
```
