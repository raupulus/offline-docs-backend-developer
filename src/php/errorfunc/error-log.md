---
title: error_log
description: Envía un mensaje de error al gestor de errores definido
source_url: https://www.php.net/manual/es/function.error-log.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/errorfunc/functions/error-log.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: errorfunc
translation_status: ready
translation_reviewed: false
translation_revision: 769812c12
order: 17630
---

error_log

Envía un mensaje de error al gestor de errores definido

## Descripción

```php
error_log(string $message, [int $message_type], [string $destination], [string $additional_headers]): bool
```php

Envía un mensaje de error al historial de errores del servidor web o a un fichero.

## Parámetros

`message`  
El mensaje de error que debe ser almacenado.

`message_type`  
Especifica el destino del mensaje de error. Los tipos posibles de mensajes son:

|  |  |
|----|----|
| 0 | `message` es enviado al historial PHP, que se basa en el historial del sistema o un fichero, dependiendo de la configuración de [error_log](#ini.error-log). Esta es la opción por omisión. |
| 1 | `message` es enviado por email a la dirección `destination`. Este es el único tipo que utiliza el cuarto parámetro `additional_headers`. |
| 2 | Ya no es una opción. |
| 3 | `message` es añadido al fichero `destination`. No se añade automáticamente una nueva línea (retorno de carro) al final de la cadena `message`. |
| 4 | `message` es enviado directamente al gestor de identificación SAPI. |

`error_log` tipos de registro

`destination`  
El destino. Esto depende del parámetro `message_type` descrito anteriormente.

`additional_headers`  
Los encabezados adicionales. Estos son utilizados cuando el parámetro `message_type` está definido a `1`. Este tipo de mensaje utiliza la misma función interna que la función `mail`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Si `message_type` es cero, entonces esta función siempre retorna `true`, independientemente de si el error pudo ser registrado en el registro de eventos.

## Historial de cambios

| Versión | Descripción                                               |
|---------|-----------------------------------------------------------|
| 8.0.0   | `destination` y `additional_headers` ahora son nullables. |

## Ejemplos

Ejemplos con `error_log`

```
<?php
// Envía una notificación por el historial del servidor web,
// si la conexión a la base de datos es imposible.
if (!Ora_Logon($username, $password)) {
  error_log("Base Oracle no disponible !", 0);
}

// Indicar al administrador, por email, que no hay más FOO
if (!($foo = allocate_new_foo())) {
  error_log("¡Ay!, No quedan más FOO disponibles !", 1,
  "operador@example.com");
}

// Otras maneras de llamar a error_log():
error_log("¡Gran error !", 3, "/var/tmp/mis-errors.log");
?>

    
```php

## Notas

> [!WARNING]
> La función `error_log` no es segura a nivel binario. El parámetro `message` será truncado por un carácter nulo.

> [!TIP]
> El parámetro `message` no debe contener caracteres nulos. Tenga en cuenta que el parámetro `message` puede ser enviado hacia un fichero, un correo, syslog, etc. Utilice las funciones apropiadas de conversión/escape, `base64_encode`, `rawurlencode` o `addslashes` antes de llamar a la función `error_log`.
