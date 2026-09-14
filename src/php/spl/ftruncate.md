---
title: SplFileObject::ftruncate
description: Trunca el archivo a una longitud dada
source_url: https://www.php.net/manual/es/splfileobject.ftruncate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/ftruncate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84470
---

SplFileObject::ftruncate

Trunca el archivo a una longitud dada

## Descripción

```php
public SplFileObject::ftruncate(int $size): bool
```php

Trunca el archivo a `size` bytes.

## Parámetros

`size`  
El tamaño a truncar.

> [!NOTE]
> Si `size` es más grande que el fichero este es extendido con bytes null.
>
> Si `size` es más pequeño que el archivo, los datos extra se perderán.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de SplFileObject::ftruncate

```
<?php
// Crea un fichero conteniendo "Hola Mundo!"
$file = new SplFileObject("/tmp/ftruncate", "w+");
$file->fwrite("Hola Mundo!");

// Truncar a 4 bytes
$file->ftruncate(4);

// Rebobina y leer los datos
$file->rewind();
echo $file->fgets();
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Hola

## Véase también

`ftruncate`
