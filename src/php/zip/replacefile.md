---
title: ZipArchive::replaceFile
description: Reemplaza fichero en el archivo ZIP con una ruta determinada
source_url: https://www.php.net/manual/es/ziparchive.replacefile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/replacefile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108460
---

ZipArchive::replaceFile

Reemplaza fichero en el archivo ZIP con una ruta determinada

## Descripción

```php
public ZipArchive::replaceFile(string $filepath, int $index, [int $start], [int $length], [int $flags]): bool
```php

Reemplaza fichero en el archivo ZIP con una ruta determinada.

> [!NOTE]
> Para una portabilidad máxima, se recomienda siempre utilizar barras oblicuas (`/`) como separador de directorio en los nombres de archivos zip.

## Parámetros

`filepath`  
La ruta del archivo a añadir.

`index`  
El índice del archivo a reemplazar, su nombre no ha cambiado.

`start`  
Para la copia parcial, posición de inicio.

`length`  
Para copia parcial, longitud a copiar, si `ZipArchive::LENGTH_TO_END` (0) se usa el tamaño del archivo, si `ZipArchive::LENGTH_UNCHECKED` se usa todo el archivo (comenzando desde `start`).

`flags`  
Máscara de bits compuesta por `ZipArchive::FL_ENC_GUESS`, `ZipArchive::FL_ENC_UTF_8`, `ZipArchive::FL_ENC_CP437`, `ZipArchive::FL_OPEN_FILE_NOW`. El comportamiento de estas constantes se describe en la página de [constantes ZIP](#zip.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0, PECL zip 1.22.1 | Se añadio `ZipArchive::FL_OPEN_FILE_NOW`. |
| 8.3.0, PECL zip 1.22.2 | Se añadieron `ZipArchive::LENGTH_TO_END` y `ZipArchive::LENGTH_UNCHECKED`. |

## Ejemplos

Este ejemplo abre un archivo ZIP `test.zip` y sustituye la entrada del índice 1 con `/path/to/index.txt`.

Abrir y reemplazar

```
<?php
$zip = new ZipArchive;
if ($zip->open('test.zip') === TRUE) {
    $zip->replaceFile('/path/to/index.txt', 1);
    $zip->close();
    echo 'ok';
} else {
    echo 'failed';
}
?>

   
```php

## Véase también

ZipArchive::addFile
