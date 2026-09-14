---
title: php_ini_loaded_file
description: Obtiene la ruta de un archivo php.ini cargado
source_url: https://www.php.net/manual/es/function.php-ini-loaded-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/php-ini-loaded-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 39120
---

php_ini_loaded_file

Obtiene la ruta de un archivo php.ini cargado

## Descripción

```php
php_ini_loaded_file(): string
```php

Verifica si un archivo `php.ini` está cargado y obtiene su ruta.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La ruta del archivo `php.ini` cargado, o `false` si no se ha cargado ninguno.

## Ejemplos

Ejemplo con `php_ini_loaded_file`

```
<?php
$inipath = php_ini_loaded_file();

if ($inipath) {
    echo 'php.ini cargado : ' . $inipath;
} else {
    echo 'No se ha cargado ningún archivo php.ini';
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    php.ini cargado : /usr/local/php/php.ini

## Véase también

`php_ini_scanned_files`, `phpinfo`, [El archivo de configuración](#configuration.file)
