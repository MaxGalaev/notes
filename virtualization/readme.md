Proxmox это платформа виртуализации. Все средства автоматизации крутятся вокруг создания и использования VM templates. 
Template можно создать руками на основе любого дистрибутива после установки и настройки ОС, а можно использовать Packer.
Packer сделает эталонный образ, на основе которого можно разворачивать VM. Конфигурация для Packer описывается в файле.
После работы Packer, на выходе получаем готовую Template. При этом, все равно надо руками задавать такие параметры 
как имя машины, ssh-ключи, пользователей и т.д. Эту проблему решает cloud-init. Cloud-init работает со всеми популярными 
облаками, а также с Proxmox. Cloud-init запускается еще до старта сети.


