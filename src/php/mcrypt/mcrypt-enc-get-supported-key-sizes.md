---
title: mcrypt_enc_get_supported_key_sizes
description: Devuelve un array que contiene los tamaños de clave admitidos por un
  algoritmo
source_url: https://www.php.net/manual/es/function.mcrypt-enc-get-supported-key-sizes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-enc-get-supported-key-sizes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45770
---

mcrypt_enc_get_supported_key_sizes

Devuelve un array que contiene los tamaños de clave admitidos por un algoritmo

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_enc_get_supported_key_sizes(resource $td): array
```php

`mcrypt_enc_get_supported_key_sizes` lee los tamaños de clave soportados por el algoritmo actual del recurso de cifrado `td`.

## Parámetros

`td`  
El recurso de cifrado.

## Valores devueltos

Devuelve un array que contiene los tamaños de clave soportados por el algoritmo designado por `td`. Si devuelve un array vacío, es que todas las claves entre 1 y `mcrypt_enc_get_key_size` son admitidas por el algoritmo.

## Ejemplos

Ejemplo con `mcrypt_enc_get_supported_key_sizes`

```
<?php
    $td = mcrypt_module_open('rijndael-256', '', 'ecb', '');
    var_dump(mcrypt_enc_get_supported_key_sizes($td));
?>

   
```php

El ejemplo anterior mostrará:

    array(3) {
      [0]=>
      int(16)
      [1]=>
      int(24)
      [2]=>
      int(32)
    }
