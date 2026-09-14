---
title: php_strip_whitespace
description: Devuelve la fuente sin comentarios ni espacios en blanco
source_url: https://www.php.net/manual/es/function.php-strip-whitespace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/php-strip-whitespace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: f9c4a68ef
order: 47150
---

php_strip_whitespace

Devuelve la fuente sin comentarios ni espacios en blanco

## Descripción

```php
php_strip_whitespace(string $filename): string
```php

Devuelve el código fuente PHP del argumento `filename` habiendo eliminado los comentarios así como los espacios. Esto puede ser útil para comparar la cantidad de código con la cantidad de comentarios en su código. Esto equivale a utilizar el comando `php -w` desde la [línea de comandos](#features.commandline).

## Parámetros

`filename`  
Ruta hacia el fichero PHP.

## Valores devueltos

El código fuente limpiado será devuelto en caso de éxito o una cadena vacía en caso de fallo.

> [!NOTE]
> Esta función respeta el valor de la directiva INI [short_open_tag](#ini.short-open-tag).

## Ejemplos

Ejemplo con `php_strip_whitespace`

```
<?php
// Comentario PHP aquí

/*
 * Otro comentario PHP
 */

echo        php_strip_whitespace(__FILE__);
// Los saltos de línea son considerados como espacios y por lo tanto también son eliminados:
do_nothing();
?>

    
```php

El ejemplo anterior mostrará:

    <?php
     echo php_strip_whitespace(__FILE__); do_nothing(); ?>

        

Observe que los comentarios PHP ya no están presentes, al igual que los espacios y los saltos de línea después del primer `echo`.
