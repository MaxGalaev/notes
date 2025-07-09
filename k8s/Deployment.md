В основном для разворачивания приложений используюется такая сущность как Deployment, которая в себя включает ReplicaSet и стратегию развертывания. 

Пример:
```yaml
apiVersion: apps/v1
kind: Deployment                                          # 1
metadata:
  name: my-nginx
spec:
  replicas: 3                                             # 2
  minReadySeconds: 15
  selector:
    matchLabels:
      app: nginx
  strategy:
    type: RollingUpdate              # Стратегия обновления
    rollingUpdate: 
      maxUnavailable: 1              # Удалять поды по одному
      maxSurge: 1                    # Макс кол-во подов за одно добавление
  template:                                               # 6
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - image: nginx
          imagePullPolicy: Always                         # 8
          name: nginx
          ports:
            - containerPort: 80

```

Есть 2 стратегии обновления
Дефолтная - Rolling Update, постепенная замена старых подов на новые.
Вторая - Recreate, сначала удаляются все старые поды, а затем поднимаются новые.

Первая стратегия - без остновки работы приложения, вторая - с небольшим даунтаймом.

Для выкатки новой версии приложения нужно изменить что-то в template секции, чаще всего это образ. 

Если что-то пошло не так, мы всегда можем откатиться на предыдущие ревизии приложения. 