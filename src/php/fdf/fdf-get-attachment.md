---
title: fdf_get_attachment
description: Extrae un fichero integrado en un documento FDF
source_url: https://www.php.net/manual/es/function.fdf-get-attachment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fdf/functions/fdf-get-attachment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fdf
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 22430
---

fdf_get_attachment

Extrae un fichero integrado en un documento FDF

## Descripción

```php
fdf_get_attachment(resource $fdf_document, string $fieldname, string $savepath): array
```php

Extrae el fichero `fieldname` subido a través del campo `"file selection"`, luego lo almacena en el fichero `savepath`.

## Parámetros

`fdf_document`  
El gestor de documento FDF, devuelto por la función `fdf_create`, la función `fdf_open` o la función `fdf_open_string`.

`fieldname`  

`savepath`  
Puede ser el nombre de un fichero o bien un directorio en el cual el fichero subido será creado bajo su nombre original. Cualquier fichero ya existente con el mismo nombre será sobrescrito.

> [!NOTE]
> Parece que no hay otra manera de conocer el nombre del fichero subido que almacenarlo en un directorio con `savepath` y luego leer su nombre en el directorio.

## Valores devueltos

El array devuelto contiene los siguientes campos:

- `path` - ruta de almacenamiento del directorio

- `size` - tamaño del fichero almacenado en bytes

- `type` - Tipo MIME del fichero, si fue proporcionado en el documento FDF

## Ejemplos

Almacenamiento de un fichero subido

```
<?php
$fdf = fdf_open_string($HTTP_FDF_DATA);
$data = fdf_get_attachment($fdf, "filename", "/tmpdir");
echo "El fichero subido es almacenado en $data[path]";
?>

   
```php
