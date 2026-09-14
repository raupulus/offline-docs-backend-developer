---
title: mcrypt_list_modes
description: Lista todos los modos de cifrado soportados
source_url: https://www.php.net/manual/es/function.mcrypt-list-modes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-list-modes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45910
---

mcrypt_list_modes

Lista todos los modos de cifrado soportados

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_list_modes([string $lib_dir]): array
```php

Lista todos los modos de cifrado de `lib_dir`.

## Parámetros

`lib_dir`  
Especifica el directorio donde se encuentran todos los modos. Si se omite, se utiliza el valor de la directiva `mcrypt.modes_dir` en el `php.ini`.

## Valores devueltos

Devuelve un array con todos los modos soportados.

## Ejemplos

Ejemplo con `mcrypt_list_modes`

```
<?php
$modes = mcrypt_list_modes();

foreach ($modes as $mode) {
    echo "$mode <br />\n";
}
?>

   
```php

El ejemplo anterior mostrará todos los modos soportados en el directorio por omisión. Si el modo no está definido por la directiva `mcrypt.modes_dir` del `php.ini`, se utilizará el directorio por omisión de mcrypt (el directorio `/usr/local/lib/libmcrypt`).
