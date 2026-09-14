---
title: ini_get
description: Lee el valor de una opción de configuración
source_url: https://www.php.net/manual/es/function.ini-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/ini-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 911fe79de
order: 39050
---

ini_get

Lee el valor de una opción de configuración

## Descripción

```php
ini_get(string $option): string
```php

Devuelve el valor de la opción de configuración `varname` en caso de éxito.

## Parámetros

`option`  
El nombre de la opción de configuración.

## Valores devueltos

Devuelve el valor de la opción de configuración `varname` en caso de éxito, o un `string` vacío para los valores `null`. Devuelve `false` si la opción de configuración no existe.

## Ejemplos

Ejemplos con `ini_get`

```
<?php

/*
Nuestro archivo php.ini contiene las siguientes directivas:

display_errors = On
opcache.enable_cli = Off
post_max_size = 8M
*/

echo 'display_errors = ' . ini_get('display_errors') . "\n";
echo 'opcache.enable_cli = ' . (int) ini_get('opcache.enable_cli') . "\n";
echo 'post_max_size = ' . ini_get('post_max_size') . "\n";
echo 'post_max_size + 1 = ' . (rtrim(ini_get('post_max_size'), 'KMG') + 1) . "\n";
echo 'post_max_size in bytes = ' . ini_parse_quantity(ini_get('post_max_size'));

?>

    
```php

Resultado del ejemplo anterior es similar a:

    display_errors = 1
    opcache.enable_cli = 0
    post_max_size = 8M
    post_max_size+1 = 9
    post_max_size in bytes = 8388608

## Notas

> [!NOTE]
> Una directiva de configuración con el valor `off` será devuelta en forma de cadena vacía o "0" mientras que el valor `on` devolverá "`1`". Esta función también puede devolver el valor literal del archivo INI.

> [!NOTE]
> Varias directivas que tratan sobre tamaño de memoria, como [upload_max_filesize](#ini.upload-max-filesize), están almacenadas en el archivo `php.ini` con una notación corta. `ini_get` devuelve la cadena exacta almacenada en el archivo `php.ini` y *NO* su equivalente `int`. Aplicar operaciones aritméticas clásicas sobre estos valores no conducirá a nada bueno. La función `ini_parse_quantity` puede ser utilizada para convertir la notación abreviada en bytes.

> [!NOTE]
> `ini_get` no puede leer las opciones ini de tipo "array" como `pdo.dsn.*`, y devuelve `false` en este caso.

## Véase también

`get_cfg_var`, `ini_get_all`, `ini_parse_quantity`, `ini_restore`, `ini_set`
