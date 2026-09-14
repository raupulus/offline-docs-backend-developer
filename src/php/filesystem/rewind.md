---
title: rewind
description: Reemplaza el puntero de fichero al inicio
source_url: https://www.php.net/manual/es/function.rewind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/rewind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 24000
---

rewind

Reemplaza el puntero de fichero al inicio

## Descripción

```php
rewind(resource $stream): bool
```php

Reemplaza el puntero de fichero `stream` al inicio del flujo.

> [!NOTE]
> Si se ha abierto el fichero en modo de adición ("a" o "a+"), todos los datos que se escriban en este fichero serán siempre añadidos, sin importar la posición del puntero de fichero.

## Parámetros

`stream`  
El puntero de fichero debe ser válido y haber sido abierto correctamente por `fopen`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `rewind`

```
<?php
$handle = fopen('output.txt', 'r+');

fwrite($handle, 'Really long sentence.');
rewind($handle);
fwrite($handle, 'Foo');
rewind($handle);

echo fread($handle, filesize('output.txt'));

fclose($handle);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Foolly long sentence.

## Véase también

`fread`, `fseek`, `ftell`, `fwrite`
