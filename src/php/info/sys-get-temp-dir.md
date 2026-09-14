---
title: sys_get_temp_dir
description: Devuelve la ruta del directorio utilizado para los ficheros temporales
source_url: https://www.php.net/manual/es/function.sys-get-temp-dir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/sys-get-temp-dir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: false
translation_revision: 8dd14a886
order: 39230
---

sys_get_temp_dir

Devuelve la ruta del directorio utilizado para los ficheros temporales

## Descripción

```php
sys_get_temp_dir(): string
```php

Devuelve la ruta del directorio PHP donde se almacenan los ficheros temporales por defecto.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la ruta del directorio temporal.

## Ejemplos

Ejemplo con `sys_get_temp_dir`

```
<?php
// Creación de un fichero temporal en el directorio
// de ficheros temporales, utilizando la función sys_get_temp_dir()
$temp_file = tempnam(sys_get_temp_dir(), 'Tux');

echo $temp_file;
?>

    
```php

Resultado del ejemplo anterior es similar a:

    C:\Windows\Temp\TuxA318.tmp

## Véase también

`tmpfile`, `tempnam`
