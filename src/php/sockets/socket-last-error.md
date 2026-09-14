---
title: socket_last_error
description: Lee el último error generado por un socket
source_url: https://www.php.net/manual/es/function.socket-last-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-last-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: e50e79746
order: 75720
---

socket_last_error

Lee el último error generado por un socket

## Descripción

```php
socket_last_error([Socket $socket]): int
```php

Si una instancia de `Socket` es pasada a esta función, el último error que haya sido generado por este socket será devuelto. Si `socket` es `null`, el último código de error generado es devuelto. Este comportamiento es particularmente práctico para funciones como `socket_create` que no devuelven un socket en caso de fallo, y `socket_select` que puede fallar sin razón directamente relacionada con el socket. El código de error puede ser transmitido a `socket_strerror` que devuelve un mensaje de error legible.

Si no ha ocurrido ningún error, o si el error ha sido eliminado con la función `socket_clear_error`, esta función devolverá `0`.

## Parámetros

`socket`  
Una instancia de `Socket` creada por `socket_create`.

## Valores devueltos

Devuelve el código de error asociado al socket.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |
| 8.0.0 | `socket` ahora es nullable. |

## Ejemplos

Ejemplo con `socket_last_error`

```
<?php
$socket = @socket_create(AF_INET, SOCK_STREAM, SOL_TCP);

if ($socket === false) {
    $errorcode = socket_last_error();
    $errormsg = socket_strerror($errorcode);

    die("Imposible crear el socket : [$errorcode] $errormsg");
}
?>

    
```php

## Notas

> [!NOTE]
> `socket_last_error` no borra el código de error. Utilice en su lugar la función `socket_clear_error` para ello.
