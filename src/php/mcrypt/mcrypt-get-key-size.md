---
title: mcrypt_get_key_size
description: Devuelve el tamaño de la clave de cifrado
source_url: https://www.php.net/manual/es/function.mcrypt-get-key-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-get-key-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45890
---

mcrypt_get_key_size

Devuelve el tamaño de la clave de cifrado

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_get_key_size(int $cipher): int
```php

```php
mcrypt_get_key_size(string $cipher, string $mode): int
```

La primera sintaxis utiliza libmcrypt 2.2.x, y la segunda libmcrypt 2.4.x o posterior.

`mcrypt_get_key_size` se utiliza para obtener el tamaño de la clave del cifrado `cipher`.

Es más interesante utilizar la función `mcrypt_enc_get_key_size` ya que utiliza el recurso devuelto por la función `mcrypt_module_open`.

## Parámetros

`cipher`  
Una de las constantes `MCRYPT_ciphername`, o el nombre del algoritmo como cadena.

`mode`  
Una de las constantes `MCRYPT_MODE_modename`, o una de las siguientes cadenas: "ecb", "cbc", "cfb", "ofb", "nofb" o "stream".

## Valores devueltos

Devuelve el tamaño máximo soportado para una clave del algoritmo, en bytes o `false` si ocurre un error.

## Ejemplos

Ejemplo con `mcrypt_get_key_size`

```php
<?php
echo mcrypt_get_key_size('tripledes', 'ecb');
?>

   
```

El ejemplo anterior muestra el uso de la función cuando ha sido compilada con la biblioteca 2.4.x o 2.5.x.

El ejemplo anterior mostrará:

    24

## Véase también

mcrypt_get_block_size

mcrypt_enc_get_key_size

mcrypt_encrypt
