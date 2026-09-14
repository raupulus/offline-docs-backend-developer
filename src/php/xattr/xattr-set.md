---
title: xattr_set
description: Establece un atributo extendido
source_url: https://www.php.net/manual/es/function.xattr-set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xattr/functions/xattr-set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xattr
translation_status: ready
translation_revision: 14af302c9
order: 102040
---

xattr_set

Establece un atributo extendido

## Descripción

```php
xattr_set(string $filename, string $name, string $value, [int $flags]): bool
```php

Esta función establece el valor de un atributo extendido del archivo.

Los atributos extendidos tienen dos espacios de nombres diferentes: user y root. El espacio de nombres user está disponible para todos los usuarios, mientras que el espacio de nombres root solo está disponible para usuarios con privilegios de root. xattr opera sobre el espacio de nombres user por defecto, pero esto se puede cambiar con el parámetro `flags`.

## Parámetros

`filename`  
El archivo en el que se establece el atributo.

`name`  
El nombre del atributo extendido. Este atributo se crea si no existe o reemplazado si ya existe. Puede cambiar este comportamiento mediante el uso de los parámetros `flags`.

`value`  
El valor del atributo.

`flags`  
|  |  |
|----|----|
| `XATTR_CREATE` | La función falla si el atributo extendido ya existe. |
| `XATTR_REPLACE` | La función falla si el atributo extendido no existe. |
| `XATTR_DONTFOLLOW` | No sigue el enlace simbólico pero se puede operar en este. |
| `XATTR_ROOT` | Establece atributos en la raíz (segura) de espacio de nombres. Requiere privilegios de administrador. |

Banderas xattr soportadas

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Establece atributos extendidos en archivo `.wav`

```
<?php
$file = 'my_favourite_song.wav';
xattr_set($file, 'Artist', 'Someone');
xattr_set($file, 'My ranking', 'Good');
xattr_set($file, 'Listen count', '34');

/* ... other code ... */

printf("You've played this song %d times", xattr_get($file, 'Listen count'));
?>

    
```php

## Véase también

`xattr_get`, `xattr_remove`
