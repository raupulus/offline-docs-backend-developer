---
title: xattr_list
description: Obtener una lista de atributos extendidos
source_url: https://www.php.net/manual/es/function.xattr-list.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xattr/functions/xattr-list.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xattr
translation_status: ready
translation_revision: 8e2cfbdce
order: 102020
---

xattr_list

Obtener una lista de atributos extendidos

## Descripción

```php
xattr_list(string $filename, [int $flags]): array
```php

Esta función obtiene una lista de nombres de los atributos extendidos de un archivo.

Los atributos extendidos tienen dos espacios de nombres diferentes: user y root. El espacio de nombres user está disponible para todos los usuarios, mientras que el espacio de nombres root solo está disponible para usuarios con privilegios de root. xattr opera sobre el espacio de nombres user por defecto, pero esto se puede cambiar con el parámetro `flags`.

## Parámetros

`filename`  
La ruta del archivo.

`flags`  
|  |  |
|----|----|
| `XATTR_DONTFOLLOW` | No sigue el enlace simbólico pero se puede operar en este. |
| `XATTR_ROOT` | Establece atributos en la raíz (segura) de espacio de nombres. Requiere privilegios de administrador. |

Banderas xattr soportadas

## Valores devueltos

Esta función devuelve un array con los nombres de los atributos extendidos.

## Ejemplos

Imprime los nombres de todos los atributos extendidos del archivo

```
<?php
$file = 'some_file';
$root_attributes = xattr_list($file, XATTR_ROOT);
$user_attributes = xattr_list($file);

echo "Atributos Root: \n";
foreach ($root_attributes as $attr_name) {
    printf("%s\n", $attr_name);
}

echo "\n Atributos usuario: \n";
foreach ($user_attributes as $attr_name) {
    printf("%s\n", $attr_name);
}

?>

    
```php

## Véase también

`xattr_get`
