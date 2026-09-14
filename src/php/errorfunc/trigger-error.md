---
title: trigger_error
description: Desencadena un error de usuario
source_url: https://www.php.net/manual/es/function.trigger-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/errorfunc/functions/trigger-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: errorfunc
translation_status: ready
translation_reviewed: true
translation_revision: 72b70d7c3
order: 17710
---

trigger_error

Desencadena un error de usuario

## Descripción

```php
trigger_error(string $message, [int $error_level]): true
```php

`trigger_error` se utiliza para desencadenar un error de usuario. También puede ser utilizada en conjunción con un manejador de errores interno, o un manejador de errores de usuario que haya sido seleccionado como manejador de errores con `set_error_handler`.

`trigger_error` es práctico cuando se debe generar una respuesta particular durante la ejecución.

## Parámetros

`message`  
El mensaje de error designado para este error. Está limitado en longitud a 1024 bytes. Todos los caracteres después de los 1024 bytes serán ignorados.

`error_level`  
El tipo de error designado para este error. Solo funciona con la familia de constantes `E_USER_*` y será por omisión `E_USER_NOTICE`.

> [!WARNING]
> Pasar `E_USER_ERROR` como `error_level` está ahora deprecado. Lance una Exception o llame a `exit` en su lugar.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Esta función lanza una `ValueError` si el `error_level` no es uno de los `E_USER_ERROR`, `E_USER_WARNING`, `E_USER_NOTICE`, `E_USER_DEPRECATED`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Pasar `E_USER_ERROR` como `error_level` está ahora deprecado. Lance una Exception o llame a `exit` en su lugar. |
| 8.4.0 | La función tiene ahora un tipo de retorno `true` en lugar de `bool`. |
| 8.0.0 | La función lanza ahora una `ValueError` si se especifica un `error_level` inválido. Anteriormente, devolvía `false`. |

## Ejemplos

Ejemplo con `trigger_error`

Ver `set_error_handler` para un ejemplo más sustancial.

```
<?php
$password = $_POST['password'] ?? '';
if ($password === '') {
  trigger_error("Usar una contraseña vacía no es seguro", E_USER_WARNING);
}
$hash = password_hash($password, PASSWORD_DEFAULT);
?>

    
```php

## Notas

> [!WARNING]
> Las entidades HTML contenidas en el parámetro `message` no son escapadas. Utilice la función `htmlentities` en el mensaje si el error debe ser mostrado en un navegador.

## Véase también

`error_reporting`, `set_error_handler`, `restore_error_handler`, Las [constantes de nivel de error](#errorfunc.constants), El atributo `Deprecated`
