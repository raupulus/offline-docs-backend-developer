---
title: msg_send
description: Envía un mensaje a una cola
source_url: https://www.php.net/manual/es/function.msg-send.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/msg-send.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: false
translation_revision: fd2f14b2e
order: 73490
---

msg_send

Envía un mensaje a una cola

## Descripción

```php
msg_send(SysvMessageQueue $queue, int $message_type, string $message, [bool $serialize], [bool $blocking], [int $error_code]): bool
```php

`msg_send` envía el mensaje `message` de tipo `message_type` (que DEBE ser mayor que 0) a la cola de mensajes identificada por `queue`.

## Parámetros

`queue`  
La cola de mensajes

`message_type`  
El tipo del mensaje (DEBE ser mayor que 0)

`message`  
El cuerpo del mensaje

> [!NOTE]
> Si `serialize` está definido como `false`, DEBE ser del tipo: `string`, `int`, `float` o `bool`. En otros casos se emitirá un aviso.

`serialize`  
El parámetro opcional `serialize` controla el método de envío del mensaje `message`. `serialize` tiene por omisión el valor `true` lo que significa que el mensaje `message` será serializado utilizando el mismo mecanismo que el utilizado por las sesiones, antes de ser enviado a la cola de mensajes. Esto permite enviar arrays y objetos complejos a otros scripts PHP, o bien, si se utiliza la extensión WDDX, intercambiar mensajes con clientes compatibles WDDX.

`blocking`  
Si el mensaje es demasiado grande para ser almacenado por la cola, su script esperará hasta que otro proceso lea de la cola un mensaje, y libere suficiente espacio para su mensaje. Este es el modo bloqueante: puede evitar este modo utilizando el parámetro `blocking` con el valor `false`: en este caso, `msg_send` retornará inmediatamente `false` si el mensaje es demasiado grande para la cola. Asignará entonces al parámetro `error_code` el valor de `MSG_EAGAIN`, indicando que debería intentar enviar su mensaje de nuevo, un poco más tarde.

`error_code`  
Si la función falla, el código de error opcional será definido con el valor de la variable del sistema errno.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

Al enviar con éxito un mensaje, la cola se actualiza de la siguiente manera: `msg_lrpid` toma el valor del identificador de proceso del proceso llamante, `msg_qnum` se incrementa en 1 y `msg_rtime` toma la fecha y hora actual.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `queue` ahora espera una `SysvMessageQueue`; anteriormente, se esperaba un `resource`. |

## Véase también

msg_remove_queue

msg_receive

msg_stat_queue

msg_set_queue
