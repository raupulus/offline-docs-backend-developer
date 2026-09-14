---
title: ZipArchive::setMtimeIndex
description: Establece el tiempo de modificación de una entrada definido por su índice
source_url: https://www.php.net/manual/es/ziparchive.setmtimeindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/setmtimeindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 963af75fa
order: 108570
---

ZipArchive::setMtimeIndex

Establece el tiempo de modificación de una entrada definido por su índice

## Descripción

```php
public ZipArchive::setMtimeIndex(int $index, int $timestamp, [int $flags]): bool
```php

Establece el tiempo de modificación de una entrada definido por su índice.

## Parámetros

`index`  
Índice de la entrada.

`timestamp`  
La hora de modificación (unix timestamp) del archivo.

`flags`  
Flags opcionales, sin usar por ahora.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Este ejemplo crea un archivo ZIP `test.zip` y añade al archivo `test.txt` con su fecha de modificación.

Archivar un fichero

```
<?php
$zip = new ZipArchive();
if ($zip->open('test.zip', ZipArchive::CREATE) === TRUE) {
    $zip->addFile('text.txt');
    $zip->setMtimeIndex(0, mktime(0,0,0,12,25,2019));
    $zip->close();
    echo "Ok\n";
} else {
    echo "KO\n";
}
?>

   
```php

## Notas

> [!NOTE]
> Esta función sólo está disponible si se construye con libzip ≥ 1.0.0.

## Véase también

ZipArchive::setMtimeName
