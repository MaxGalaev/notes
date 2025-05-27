docker compose позвоялет управлять связанным набором контейнеров, каждый из которых представляет один сервис проекта. Управление представляет собой сборку, запуск с учетом зависимостей и конфигурацию. Конфигурация описывается в compose.yml и лежит в корне проекта.

Пример compose.yml из официальной документации:
```yml
services:
  frontend: # имя сервиса, может быть любым
    image: example/webapp #образ из которого будет стартовать контейнер
    ports:
      - "443:8043"
    networks: # сети, к которым будет подключен контейнер
      - front-tier
      - back-tier
    configs:
      - httpd-config
    secrets:
      - server-certificate

  backend:
    image: example/database
    volumes: # волюмы, которые будут подключены к контейнеру
      - db-data:/etc/data
    networks:
      - back-tier

volumes: # создание волюмов, которые можно подключить к контейнерам
  db-data:
    driver: flocker
    driver_opts:
      size: "10GiB"

configs:
  httpd-config:
    external: true

secrets:
  server-certificate:
    external: true

networks:
  # The presence of these objects is sufficient to define them
  front-tier: {}
  back-tier: {}
```
