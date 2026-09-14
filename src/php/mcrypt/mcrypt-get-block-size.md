---
title: mcrypt_get_block_size
description: Devuelve el tamaño de bloques de un cifrado
source_url: https://www.php.net/manual/es/function.mcrypt-get-block-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-get-block-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45860
---

mcrypt_get_block_size

Devuelve el tamaño de bloques de un cifrado

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_get_block_size(int $cipher): int
```php

```php
mcrypt_get_block_size(string $cipher, string $mode): int
```

El primer prototipo se utiliza cuando PHP está compilado con la biblioteca libmcrypt 2.2.x, el segundo cuando está compilado con libmcrypt 2.4.x o 2.5.x.

`mcrypt_get_block_size` sirve para leer el tamaño de bloques del cifrado `cipher` (en combinación con un modo de cifrado).

Se recomienda utilizar la función `mcrypt_enc_get_block_size`, ya que utiliza el recurso devuelto por `mcrypt_module_open`.

## Parámetros

`cipher`  
Una de las constantes `MCRYPT_ciphername`, o el nombre del algoritmo como cadena.

`mode`  
Una de las constantes `MCRYPT_MODE_modename`, o una de las siguientes cadenas: "ecb", "cbc", "cfb", "ofb", "nofb" o "stream".

## Valores devueltos

Lee el tamaño de bloque, en forma de un `int`.

## Ejemplos

Ejemplo con `mcrypt_get_block_size`

Este ejemplo muestra cómo utilizar esta función cuando PHP está compilado con libmcrypt 2.4.x y 2.5.x.

```php
<?php
echo mcrypt_get_block_size('tripledes', 'ecb'); // 8
?>

   
```

## Véase también

mcrypt_get_key_size

mcrypt_enc_get_block_size

mcrypt_encrypt
