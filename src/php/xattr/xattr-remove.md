---
title: xattr_remove
description: Elimina un atributo extendido
source_url: https://www.php.net/manual/es/function.xattr-remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xattr/functions/xattr-remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xattr
translation_status: ready
translation_revision: 14af302c9
order: 102030
---

xattr_remove

Elimina un atributo extendido

## Descripción

```php
xattr_remove(string $filename, string $name, [int $flags]): bool
```php

Esta función elimina un atributo extendido del archivo.

Los atributos extendidos tienen dos espacios de nombres diferentes: user y root. El espacio de nombres user está disponible para todos los usuarios, mientras que el espacio de nombres root solo está disponible para usuarios con privilegios de root. xattr opera sobre el espacio de nombres user por defecto, pero esto se puede cambiar con el parámetro `flags`.

## Parámetros

`filename`  
El archivo del que se elimina el atributo.

`name`  
El nombre del atributo a eliminar.

`flags`  
|  |  |
|----|----|
| `XATTR_DONTFOLLOW` | No sigue el enlace simbólico pero se puede operar en este. |
| `XATTR_ROOT` | Establece atributos en la raíz (segura) de espacio de nombres. Requiere privilegios de administrador. |

Banderas xattr soportadas

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Elimina todos los atributos extendidos de un archivo

```
<?php
$file = 'some_file';
$attributes = xattr_list($file);

foreach ($attributes as $attr_name) {
    xattr_remove($file, $attr_name);
}
?>

    
```php

## Véase también

`xattr_list`, `xattr_set`, `xattr_get`
