
Чтобы посмотреть все api ресурсы зарегистрированные в кубере:
```shell
kubectl api-resources
```
Чтобы создать манифест с помощью ```kubectl``` 
```shell
kubectl run nginx --image nginx --dry-run=client -o yaml
```
Как можно запустить под для тестов
```shell
kubectl -n work run curl --rm -it --image=alpine/curl:8.14.1 -- /bin/sh
```
