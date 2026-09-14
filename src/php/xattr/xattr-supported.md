---
title: xattr_supported
description: Comprueba si soporta los atributos extendidos del sistema de archivos
source_url: https://www.php.net/manual/es/function.xattr-supported.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xattr/functions/xattr-supported.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xattr
translation_status: ready
translation_revision: 14af302c9
order: 102050
---

xattr_supported

Comprueba si soporta los atributos extendidos del sistema de archivos

## Descripción

```php
xattr_supported(string $filename, [int $flags]): bool
```php

Esta función comprueba si el sistema de archivos que contenía el fichero dado soporta los atributos extendidos. Es necesario tener acceso de lectura al archivo.

## Parámetros

`filename`  
La ruta del archivo de prueba.

`flags`  
|  |  |
|----|----|
| `XATTR_DONTFOLLOW` | No sigue el enlace simbólico pero se puede operar en este. |

Banderas xattr soportadas

## Valores devueltos

Esta función devuelve `true` si sistema de archivo soporta los atributos extendidos, `false` si no soporta y `null` si no se puede determinar (Por ejemplo ruta incorrecta o le faltan permisos al archivo).

## Ejemplos

Ejemplo de `xattr_supported`

El siguiente código comprueba si se pueden utilizar los atributos extendidos.

```
<?php
$file = 'some_file';

if (xattr_supported($file)) {
    /* ... make use of some xattr_* functions ... */
}

?>

    
```php

## Véase también

`xattr_get`, `xattr_list`
