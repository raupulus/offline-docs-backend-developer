---
title: socket_strerror
description: Devuelve un string describiendo un mensaje de error
source_url: https://www.php.net/manual/es/function.socket-strerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-strerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 14dc7c473
order: 75870
---

socket_strerror

Devuelve un string describiendo un mensaje de error

## Descripción

```php
socket_strerror(int $error_code): string
```php

`socket_strerror` toma un código de error como argumento `error_code`. Este valor es frecuentemente devuelto por la función `socket_last_error`. La función devuelve el mensaje de error correspondiente.

> [!NOTE]
> Aunque los mensajes de error generados por la extensión socket estén en inglés, el sistema que gestiona los mensajes de esta función depende de la configuración local actual (`LC_MESSAGES`).

## Parámetros

`error_code`  
Un número de error de socket válido, como el producido por la función `socket_last_error`.

## Valores devueltos

Devuelve el mensaje de error asociado con el argumento `error_code`.

## Ejemplos

Ejemplo con `socket_strerror`

```
<?php
if (false == ($socket = @socket_create(AF_INET, SOCK_STREAM, SOL_TCP))) {
   echo "socket_create() ha fallado : razón : " . socket_strerror(socket_last_error()) . "\n";
}

if (false == (@socket_bind($socket, '127.0.0.1', 80))) {
   echo "socket_bind() ha fallado : razón : " . socket_strerror(socket_last_error($socket)) . "\n";
}
?>

    
```php

La salida esperada para el ejemplo anterior (suponiendo que se intenta ejecutar el script sin los derechos de Administrador) :

    socket_bind() ha fallado : razón : Permission denied

## Véase también

`socket_accept`, `socket_bind`, `socket_connect`, `socket_listen`, `socket_create`
