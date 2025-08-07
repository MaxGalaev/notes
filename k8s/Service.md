`Service` используется для балансировки и распределения нагрузки на несколько подов. В манифесте сервиса в разделе спецификации указываются метки подов на которые будет направляться трафик.

Как `Service` определяет на какие `ip` адреса направлять трафик? Под капотом создается такая сущность как `enpdoint`, который в себе содержит все `ip`:`port` всех подов, подподающих под селектор, поэтому имя `service` и `endpoint` совпадают. 

### Манифест
```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-nginx-service
  namespace: work
  labels:
    app.kubernetes.io/name: nginx
    app.kubernetes.io/version: 1.27.5
spec:
  selector: # Метки подов на которые будет распределяться трафик
    app.kubernetes.io/name: nginx
    app.kubernetes.io/version: 1.27.5
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
    name: http
```

`Service` бывают нескольких типов:
- `ClusterIP` - используется по умолчанию

`Service` не дает доступ к вашему приложению снаружи кластера. Для проверки `Service` можно настроить `port-forward`, он используется только для тестов.
```shell
kubectl -n work port-forward svc/my-nginx-service 8080:80
```
