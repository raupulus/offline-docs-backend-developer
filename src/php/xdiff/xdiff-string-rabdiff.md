---
title: xdiff_string_rabdiff
description: Hace una comparación binaria de dos strings utilizando el algoritmo polinomial
  de huella digital (fingerprinting) de Rabin
source_url: https://www.php.net/manual/es/function.xdiff-string-rabdiff.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-string-rabdiff.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_reviewed: false
translation_revision: 480cc8a9e
order: 102260
---

xdiff_string_rabdiff

Hace una comparación binaria de dos strings utilizando el algoritmo polinomial de huella digital (fingerprinting) de Rabin

## Descripción

```php
xdiff_string_rabdiff(string $old_data, string $new_data): string
```php

Hace una comparación binaria de dos strings utilizando el algoritmo de huella digital polinomial de Rabin implementado por [libxdiff](http://www.xmailserver.org/xdiff-lib.html). En comparación con `xdiff_string_bdiff`, este algoritmo generalmente produce diferencias más pequeñas y opera más rápido, manteniendo la compatibilidad total con `xdiff_string_bpatch` y `xdiff_file_bpatch` para la aplicación de parches.

Esta función puede utilizarse tanto con datos de texto como binarios. Los datos de comparación pueden aplicarse posteriormente para recrear la nueva versión a partir de la anterior.

Para obtener más información sobre el algoritmo, vea la [documentación de libxdiff](https://www.xmailserver.org/xdiff-lib.html).

## Parámetros

`old_data`  
El primer string que contiene los datos binarios "antiguos".

`new_data`  
El segundo string que contiene los "nuevos" datos binarios.

## Valores devueltos

Devuelve un string binario de comparación que contiene las diferencias entre los datos antiguos y nuevos, o `false` si ocurre un error.

## Ejemplos

Creación de una diferencia binaria entre dos cadenas

```
     
<?php
$old = file_get_contents('file_v1.txt');
$new = file_get_contents('file_v2.txt');

$diff = xdiff_string_rabdiff($old, $new);
file_put_contents('patch.rdiff', $diff);
?>

    
```php

## Véase también

`xdiff_string_bdiff`, `xdiff_string_bpatch`, `xdiff_file_bpatch`
