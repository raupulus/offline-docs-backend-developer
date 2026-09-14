---
title: socket_create_listen
description: Abre un socket en un puerto para aceptar conexiones
source_url: https://www.php.net/manual/es/function.socket-create-listen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-create-listen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: dfd68fd22
order: 75630
---

socket_create_listen

Abre un socket en un puerto para aceptar conexiones

## Descripción

```php
socket_create_listen(int $port, [int $backlog]): Socket
```php

`socket_create_listen` crea una nueva instancia de `Socket`, de tipo `AF_INET`, en espera en *todas* las interfaces locales, para el puerto `port`.

`socket_create_listen` sirve para simplificar la creación de nuevos sockets destinados a estar en espera, y aceptar nuevas conexiones.

## Parámetros

`port`  
El puerto que debe ser escuchado en todas las interfaces.

`backlog`  
El parámetro `backlog` define el tamaño máximo de la cola de conexiones en espera. `SOMAXCONN` puede ser utilizada como valor para el parámetro `backlog`. Consulte `socket_listen` para más detalles.

## Valores devueltos

`socket_create_listen` devuelve una nueva instancia de `Socket` en caso de éxito y `false` en caso de error. El código de error generado puede ser obtenido llamando a la función `socket_last_error`. Este código de error puede ser pasado a la función `socket_strerror` para obtener un mensaje de error legible por humanos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Ahora lanza un ValueError cuando `port` es menor que 0 o mayor que 65535. |
| 8.4.0 | El valor por omisión de `backlog` es ahora `SOMAXCONN`. Anteriormente, era `128`. |
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `Socket`; anteriormente, se devolvía un `resource`. |

## Notas

> [!NOTE]
> Si se desea crear un socket que solo escuche ciertas interfaces, debe utilizarse `socket_create`, `socket_bind` y `socket_listen`.

## Véase también

`socket_create`, `socket_create_pair`, `socket_bind`, `socket_listen`, `socket_last_error`, `socket_strerror`
