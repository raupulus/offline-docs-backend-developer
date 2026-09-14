---
title: msg_receive
description: Recibe un mensaje desde una cola de mensajes
source_url: https://www.php.net/manual/es/function.msg-receive.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/msg-receive.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: true
translation_revision: fd2f14b2e
order: 73470
---

msg_receive

Recibe un mensaje desde una cola de mensajes

## Descripción

```php
msg_receive(SysvMessageQueue $queue, int $desired_message_type, int $received_message_type, int $max_message_size, mixed $message, [bool $unserialize], [int $flags], [int $error_code]): bool
```php

`msg_receive` recibe el primer mensaje de la cola `queue`, cuyo tipo está especificado por `desired_message_type`.

## Parámetros

`queue`  
Descriptor de recurso de cola de mensajes

`desired_message_type`  
Si `desired_message_type` vale 0, se devuelve el primer mensaje de la cola. Si `desired_message_type` vale más que 0, entonces se devolverá el primer mensaje de ese tipo. Si `desired_message_type` vale menos que 0, se devolverá el primer mensaje de la cola cuyo tipo sea inferior o igual al valor absoluto de `desired_message_type`. Si no hay mensajes que cumplan los criterios, el script esperará a que llegue un mensaje de ese tipo a la cola. Este bloqueo puede evitarse especificando la opción `MSG_IPC_NOWAIT` en el parámetro `flags`.

`received_message_type`  
El tipo de mensaje recibido se almacenará en este parámetro.

`max_message_size`  
El tamaño máximo de mensaje se establece mediante `max_message_size`; si el mensaje de la cola es más grande que este tamaño, la función fallará (a menos que se utilice una opción `flags`, descrita a continuación).

`message`  
El mensaje recibido se almacenará en el parámetro `message`, a menos que haya habido errores al recibir el mensaje.

`unserialize`  
Cuando esto es cierto, el mensaje se trata como si hubiera sido serializado con el mismo mecanismo que el módulo de sesión. El mensaje será entonces deserializado y devuelto al script. Esto permitirá recibir fácilmente arrays u objetos complejos en su script, enviados por otros scripts PHP, o, si se utiliza WDDX, desde cualquier fuente compatible con WDDX.

Si `unserialize` vale `false`, el mensaje se devolverá intacto, sin modificar los valores binarios.

`flags`  
El parámetro `flags` permite pasar opciones para configurar las llamadas msgrcv. Por omisión, vale 0, pero se pueden especificar una o varias opciones combinándolas con el operador OR.

|  |  |
|----|----|
| `MSG_IPC_NOWAIT` | Si no hay mensajes del tipo `desired_message_type`, se devuelve inmediatamente y no se espera. La función fallará y devolverá un entero correspondiente a `MSG_ENOMSG`. |
| `MSG_EXCEPT` | Al utilizar esta opción en combinación con un tipo `desired_message_type` superior a 0, la función leerá el primer mensaje que no sea del tipo solicitado por `desired_message_type`. |
| `MSG_NOERROR` | Si el mensaje es más grande que `max_message_size`, esta opción truncará el mensaje al tamaño de `max_message_size` y no reportará errores. |

Opciones de la función `msg_receive`

`errorcode`  
Si la función falla, el parámetro opcional `error_code` se establecerá al valor de la variable del sistema errno.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

Al recibir un mensaje con éxito, la cola se actualiza de la siguiente manera: `msg_lrpid` toma el valor del identificador de proceso del proceso llamante, `msg_qnum` se decrementa en 1 y `msg_rtime` toma la fecha y hora actuales.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `queue` ahora espera una `SysvMessageQueue`; anteriormente, se esperaba un `resource`. |

## Véase también

msg_remove_queue

msg_send

msg_stat_queue

msg_set_queue
