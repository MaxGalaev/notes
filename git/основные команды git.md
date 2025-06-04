1. Как отменить последний коммит
```shell
git reset HEAD~ # удаляем только коммит
git reset --hard HEAD~ # удаляем коммит и изменения
```
1. Как удалить ветку в локальном репозитории
```shell
git branch -D name
```
3. Как удалить ветку в удаленном репозитории
```shell
git push origin --delete repo_name
```
3. Как создать новую ветку
```shell
git branch -b name
```
4. Как удалить изменения в файлах и в индексе
```shell
git restore filename
```
5. Как удалить изменения только в индексе
```shell
git restore --staged filename
```
6. Как удалить файлы из индекса не удаляя из папки
```shell
git rm --cached file.go 
```
7. Как посмотреть состояние удаленных репозиториев
```shell
git remote -v 
```
