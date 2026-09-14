---
title: tmpfile
description: Crea un fichero temporal
source_url: https://www.php.net/manual/es/function.tmpfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/tmpfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 65bea242c
order: 24060
---

tmpfile

Crea un fichero temporal

## Descripción

```php
tmpfile(): resource
```php

Crea un fichero temporal con un nombre único, abierto en escritura, lectura y binario (`w+b`), y devuelve un puntero de fichero.

Este fichero será automáticamente borrado cuando sea cerrado (por ejemplo, al llamar a la función `fclose`, o cuando no haya más referencias al gestor de fichero devuelto por la función `tmpfile`), o cuando el script finalice.

> [!CAUTION]
> Si el script termina de manera inesperada, es posible que el fichero temporal no sea eliminado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un puntero de fichero, idéntico al devuelto por la función `fopen`, para el nuevo fichero o `false` si ocurre un error.

## Ejemplos

Ejemplo con `tmpfile`

```
<?php
$temp = tmpfile();
fwrite($temp, "Escritura en el fichero temporal");
fseek($temp, 0);
echo fread($temp, 1024);
fclose($temp); // esto borrará el fichero
?>

    
```php

El ejemplo anterior mostrará:

    Escritura en el fichero temporal

## Véase también

`tempnam`, `sys_get_temp_dir`
