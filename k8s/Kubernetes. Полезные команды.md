
Чтобы посмотреть все api ресурсы зарегистрированные в кубере:
```shell
kubectl api-resources
```
Чтобы создать манифест с помощью ```kubectl``` 
```shell
kubectl run nginx --image nginx --dry-run=client -o yaml
```
