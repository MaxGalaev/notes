#Теория:
Есть root и все остальные. У root uid = 0
Все пользователи описаны в файле /etc/passwd
Все группы и кто в них входит /etc/group
Пароли хранятся в /etc/shadow

# Кто в системе в онлайне
w
who
whoami
id $(whoami)

# Создание и удаление нового пользователя
adduser alex
deluser alex

# Изменение пароля пользователя
passwd alex

# Добавление пользователя в группу
usermod -a -G sudo alex

