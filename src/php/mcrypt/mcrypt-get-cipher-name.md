---
title: mcrypt_get_cipher_name
description: Lee el nombre del cifrado utilizado
source_url: https://www.php.net/manual/es/function.mcrypt-get-cipher-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-get-cipher-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45870
---

mcrypt_get_cipher_name

Lee el nombre del cifrado utilizado

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_get_cipher_name(int $cipher): string
```php

```php
mcrypt_get_cipher_name(string $cipher): string
```

`mcrypt_get_cipher_name` devuelve el nombre del cifrado utilizado.

`mcrypt_get_cipher_name` toma el número de cifrado (con libmcrypt 2.2.x) o toma el nombre del cifrado (con libmcrypt 2.4.x) como argumento, y devuelve el nombre del cifrado, o `false`, si no existe.

## Parámetros

`cipher`  
Una de las constantes `MCRYPT_ciphername`, o el nombre del algoritmo como cadena.

## Valores devueltos

Esta función devuelve el nombre del cipher o `false` si el cipher no existe.

## Ejemplos

Ejemplo con `mcrypt_get_cipher_name`

```php
<?php
$cipher = MCRYPT_TripleDES;

echo mcrypt_get_cipher_name($cipher);
?>

   
```

El ejemplo anterior mostrará:

    3DES
