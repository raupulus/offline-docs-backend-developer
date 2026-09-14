---
title: mcrypt_enc_get_algorithms_name
description: Devuelve el nombre del algoritmo de cifrado
source_url: https://www.php.net/manual/es/function.mcrypt-enc-get-algorithms-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-enc-get-algorithms-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45720
---

mcrypt_enc_get_algorithms_name

Devuelve el nombre del algoritmo de cifrado

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_enc_get_algorithms_name(resource $td): string
```php

`mcrypt_enc_get_algorithms_name` devuelve el nombre de el algoritmo utilizado por `td`.

## Parámetros

`td`  
El recurso de cifrado.

## Valores devueltos

Devuelve el nombre del algoritmo actual, en forma de `string`

## Ejemplos

Ejemplo con `mcrypt_enc_get_algorithms_name`

```
<?php
     $td = mcrypt_module_open (MCRYPT_CAST_256, '', MCRYPT_MODE_CFB, '');
     echo mcrypt_enc_get_algorithms_name($td). "\n";

     $td = mcrypt_module_open ('cast-256', '', MCRYPT_MODE_CFB, '');
     echo mcrypt_enc_get_algorithms_name($td). "\n";
     ?>

   
```php

El ejemplo anterior mostrará:

    CAST-256
    CAST-256
