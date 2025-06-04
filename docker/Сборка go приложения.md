Особенности сборки go приложений

В результате сборки мы получаем один бинарный файл, который лучше положить куда-нибудь откуда его легко вызвать просто по имени, например в ```/usr/bin/```

Так как мы получаем один бинарный файл и нам больше ничего не нужно, имеет смысл использовать так называемую multi-stage сборку, когда в одном докерфайле есть несколько этапов, результаты работы которых могут передаваться между собой.
Пример конфига из оф документации:
```Dockerfile
# syntax=docker/dockerfile:1
FROM golang:1.24 AS build
WORKDIR /src
COPY <<EOF /src/main.go
package main

import "fmt"

func main() {
  fmt.Println("hello, world")
}
EOF
RUN go build -o /bin/hello ./main.go

FROM scratch
COPY --from=build /bin/hello /bin/hello
CMD ["/bin/hello"]
```

Часто для запуска приложения используют облегченные или совсем пустые образы типа scratch, чтобы на выходе получить по сути только бинарник, что существенно сокращает размер итогового образа. Но тут есть несколько нюансов. Во первых, при сборке go приложению нужно указать чтобы все нербходимые зависимости были включены в итоговый файл, а не подгружались динамически, иначе так как у нас в образе ничего больше нет, приложение не запустится. Также можно использовать специальные образы для go приложений, которые содержат необходимые зависимости, но при этом они не сильно больше весят чем scratch образы. 
Пример такого конфига для multi-stage сборки веб-сервера caddy:
```Dockerfile
FROM golang:1.24 AS builder
COPY caddy /caddy/
RUN useradd -u 10001 --shell /usr/sbin/nologin -m caddy && mkdir -p /home/caddy && chown -R caddy:caddy /home/caddy 
WORKDIR /caddy/cmd/caddy
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o /usr/bin/caddy

FROM gcr.io/distroless/static:nonroot
WORKDIR /usr/bin/
COPY --from=builder /usr/bin/caddy ./ 
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder --chown=caddy:caddy /home/caddy* /home/caddy/
COPY Caddyfile /etc/caddy/
USER caddy
EXPOSE 80 443
CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile"]
```
