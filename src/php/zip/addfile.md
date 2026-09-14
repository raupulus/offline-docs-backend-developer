---
title: ZipArchive::addFile
description: Añade un fichero al archivo ZIP para la ruta dada
source_url: https://www.php.net/manual/es/ziparchive.addfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/addfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108150
---

ZipArchive::addFile

Añade un fichero al archivo ZIP para la ruta dada

## Descripción

```php
public ZipArchive::addFile(string $filepath, [string $entryname], [int $start], [int $length], [int $flags]): bool
```php

Añade un fichero al archivo ZIP par la ruta dada.

> [!NOTE]
> Para una portabilidad máxima, se recomienda siempre utilizar barras oblicuas (`/`) como separador de directorio en los nombres de archivos zip.

## Parámetros

`filename`  
La ruta del fichero a añadir.

`entryname`  
Si corresponde, este es el nombre local dentro del archivo ZIP que reemplazará el `filepath`.

`start`  
Para la copia parcial, posición de inicio.

`length`  
Para copia parcial, longitud a copiar, si `ZipArchive::LENGTH_TO_END` (0) se usa el tamaño del archivo, si `ZipArchive::LENGTH_UNCHECKED` se usa todo el archivo (comenzando desde `start`).

`flags`  
Máscara de bits compuesta por `ZipArchive::FL_OVERWRITE`, `ZipArchive::FL_ENC_GUESS`, `ZipArchive::FL_ENC_UTF_8`, `ZipArchive::FL_ENC_CP437`, `ZipArchive::FL_OPEN_FILE_NOW`. El comportamiento de estas constantes se describe en la página de [constantes ZIP](#zip.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL zip 1.18.0 | Se añadio `flags`. |
| 8.3.0, PECL zip 1.22.1 | Se añadio `ZipArchive::FL_OPEN_FILE_NOW`. |
| 8.3.0, PECL zip 1.22.2 | Se añadieron `ZipArchive::LENGTH_TO_END` y `ZipArchive::LENGTH_UNCHECKED`. |

## Ejemplos

Este ejemplo abre un archivo ZIP `test.zip` y añade el fichero `/path/to/index.txt`. como `newname.txt`.

Abrir y extraer

```
<?php
$zip = new ZipArchive;
if ($zip->open('test.zip') === TRUE) {
    $zip->addFile('/path/to/index.txt', 'newname.txt');
    $zip->close();
    echo 'ok';
} else {
    echo 'failed';
}
?>

     
```php

## Notas

> [!NOTE]
> Cuando un fichero es añadido al archivo, PHP bloqueará el fichero. El bloqueo se desbloqueará cuando el objeto `ZipArchive` finalice, ya sea a través de ZipArchive::close o el objeto `ZipArchive` sea destruido. Esto puede impedir que se pueda eliminar el archivo que se está añadiendo hasta después de que el bloqueo haya sido liberado.

## Véase también

ZipArchive::replaceFile
