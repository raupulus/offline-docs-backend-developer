---
title: mcrypt_get_iv_size
description: Retorna el tamaño del VI utilizado por un par cifrado/modo
source_url: https://www.php.net/manual/es/function.mcrypt-get-iv-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-get-iv-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45880
---

mcrypt_get_iv_size

Retorna el tamaño del VI utilizado por un par cifrado/modo

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_get_iv_size(string $cipher, string $mode): int
```php

`mcrypt_get_iv_size` retorna el tamaño del vector de inicialización (VI). Si el algoritmo no utiliza un vector de inicialización, se retorna cero.

Es más útil utilizar la función `mcrypt_enc_get_iv_size`, ya que utiliza el recurso retornado por `mcrypt_module_open`.

## Parámetros

`cipher`  
Una de las constantes `MCRYPT_ciphername`, o el nombre del algoritmo como cadena.

`mode`  
Una de las constantes `MCRYPT_MODE_modename`, o una de las siguientes cadenas: "ecb", "cbc", "cfb", "ofb", "nofb" o "stream".

El VI es ignorado en modo ECB, ya que este modo no lo requiere. Debe tener el mismo VI (punto de partida) durante el cifrado y el descifrado, de lo contrario, el cifrado fallará.

## Valores devueltos

Retorna el tamaño del vector de inicialización (VI), en bytes. En caso de error, la función retorna `false`. Si el vector de inicialización no es necesario, se retorna 0.

## Ejemplos

Ejemplo con `mcrypt_get_iv_size`

```
<?php
echo mcrypt_get_iv_size(MCRYPT_CAST_256, MCRYPT_MODE_CFB) . "\n";

echo mcrypt_get_iv_size('des', 'ecb') . "\n";
?>

   
```php

## Véase también

mcrypt_get_block_size

mcrypt_enc_get_iv_size

mcrypt_create_iv
