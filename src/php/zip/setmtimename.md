---
title: ZipArchive::setMtimeName
description: Establece la hora de modificación de una entrada definida por su nombre
source_url: https://www.php.net/manual/es/ziparchive.setmtimename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/setmtimename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 963af75fa
order: 108580
---

ZipArchive::setMtimeName

Establece la hora de modificación de una entrada definida por su nombre

## Descripción

```php
public ZipArchive::setMtimeName(string $name, int $timestamp, [int $flags]): bool
```php

Establece la hora de modificación de una entrada definida por su nombre.

## Parámetros

`name`  
Nombre de la entrada.

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
    $zip->setMtimeName('text.txt', mktime(0,0,0,12,25,2019));
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

ZipArchive::setMtimeIndex
