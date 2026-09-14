---
title: stream_get_wrappers
description: Lista los gestores de flujo
source_url: https://www.php.net/manual/es/function.stream-get-wrappers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-get-wrappers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: adc94ff1a
order: 88000
---

stream_get_wrappers

Lista los gestores de flujo

## Descripción

```php
stream_get_wrappers(): array
```php

`stream_get_wrappers` lee la lista de los gestores de flujo disponibles en el sistema actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`stream_get_wrappers` devuelve un array indexado que contiene el nombre de todos los gestores de flujo disponibles en el sistema.

## Ejemplos

Ejemplo con `stream_get_wrappers`

```
<?php
print_r(stream_get_wrappers());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => php
        [1] => file
        [2] => http
        [3] => ftp
        [4] => compress.bzip2
        [5] => compress.zlib
    )

Verificación de la existencia de un gestor de flujo

```
<?php
// Verificación de la existencia de un gestor de flujo bzip2
if (in_array('compress.bzip2', stream_get_wrappers())) {
    echo 'compress.bzip2:// soporte activo.';
} else {
    echo 'compress.bzip2:// soporte inactivo.';
}
?>

    
```php

## Véase también

stream_wrapper_register
