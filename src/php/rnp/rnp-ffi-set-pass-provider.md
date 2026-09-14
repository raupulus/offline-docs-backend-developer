---
title: rnp_ffi_set_pass_provider
description: Define la función de retrollamada del proveedor de contraseña
source_url: https://www.php.net/manual/es/function.rnp-ffi-set-pass-provider.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-ffi-set-pass-provider.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72150
---

rnp_ffi_set_pass_provider

Define la función de retrollamada del proveedor de contraseña

## Descripción

```php
rnp_ffi_set_pass_provider(RnpFFI $ffi, callable $password_callback): bool
```php

Define la función de retrollamada del proveedor de contraseña. Esta función puede solicitar la contraseña en una entrada estándar (si el script PHP se ejecuta en un entorno de línea de comandos), mostrar un cuadro de diálogo GUI o proporcionar la contraseña de todas las maneras posibles. Las contraseñas solicitadas se utilizan para cifrar o descifrar las claves secretas o realizar operaciones de cifrado/descifrado simétricas.

## Parámetros

`ffi`  
El objeto FFI retornado por `rnp_ffi_create`.

`password_callback`  
La función que debe ser llamada para cada solicitud de contraseña. Tiene la siguiente firma:

```php
password_callback(string $key_fp, string $pgp_context, string $password): bool
```

`$key_fp` - La huella de la clave, si corresponde. Puede estar vacío., `$pgp_context` - Cadena que describe por qué se solicita la clave., `$password` - Referencia de cadena donde debe almacenarse la contraseña proporcionada. La función de retrollamada debe devolver `true` si la contraseña se ha establecido correctamente o `false` si ocurre un error.

## Valores devueltos

Devuelve `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de una función de retrollamada simple

```php
<?php
function password_callback(string $key_fp, string $pgp_context, string &$password)
{
    $password = "password";

    return true;
}

$ffi = rnp_ffi_create('GPG', 'GPG');

rnp_ffi_set_pass_provider($ffi, 'password_callback');

      
```
