---
title: xattr_get
description: Obtener un atributo extendido
source_url: https://www.php.net/manual/es/function.xattr-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xattr/functions/xattr-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xattr
translation_status: ready
translation_revision: 8568bac07
order: 102010
---

xattr_get

Obtener un atributo extendido

## Descripción

```php
xattr_get(string $filename, string $name, [int $flags]): string
```php

Esta función obtiene el valor de un atributo extendido del archivo.

Los atributos extendidos tienen dos espacios de nombres diferentes: user y root. El espacio de nombres user está disponible para todos los usuarios, mientras que el espacio de nombres root solo está disponible para usuarios con privilegios de root. xattr opera sobre el espacio de nombres user por defecto, pero esto se puede cambiar con el parámetro `flags`.

## Parámetros

`filename`  
El archivo de la cual obtenemos el atributo.

`name`  
El nombre del atributo.

`flags`  
|  |  |
|----|----|
| `XATTR_DONTFOLLOW` | No sigue el enlace simbólico pero se puede operar en este. |
| `XATTR_ROOT` | Establece atributos en la raíz (segura) de espacio de nombres. Requiere privilegios de administrador. |

Banderas xattr soportadas

## Valores devueltos

Devuelve un string que contiene el valor o `false` si el atributo no existe.

## Ejemplos

Comprueba si el administrador del sistema firmó el archivo

```
<?php
$file = '/usr/local/sbin/some_binary';
$firma = xattr_get($file, 'Root signature', XATTR_ROOT);

/* ... Comprobar si la $firma es válida ... */

?>

    
```php

## Véase también

`xattr_list`, `xattr_set`, `xattr_remove`
