---
title: ZipArchive::locateName
description: Devuelve el índice de la entrada en el archivo
source_url: https://www.php.net/manual/es/ziparchive.locatename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/locatename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108400
---

ZipArchive::locateName

Devuelve el índice de la entrada en el archivo

## Descripción

```php
public ZipArchive::locateName(string $name, [int $flags]): int
```php

Localiza una entrada utilizando su nombre.

## Parámetros

`name`  
El nombre de la entrada a buscar

`flags`  
Los indicadores son especificados agregándoles OR a los siguientes valores, ó 0 para ninguno de ellos.

- `ZipArchive::FL_NOCASE`

- `ZipArchive::FL_NODIR`

## Valores devueltos

Devuelve el índice de la entrada en caso de tener éxito, o `false` si ocurre un error.

## Ejemplos

Crear un archivo y luego utilizarlo con `ZipArchive::locateName`

```
<?php
$file = 'testlocate.zip';

$zip = new ZipArchive;
if ($zip->open($file, ZipArchive::CREATE) !== TRUE) {
    exit('falló');
}

$zip->addFromString('entry1.txt', 'entry #1');
$zip->addFromString('entry2.txt', 'entry #2');
$zip->addFromString('dir/entry2d.txt', 'entry #2');

if ($zip->status !== ZipArchive::ER_OK) {
    echo "falló al escribir en el archivo zip\n";
}
$zip->close();

if ($zip->open($file) !== TRUE) {
    exit('falló');
}

echo $zip->locateName('entry1.txt') . "\n";
echo $zip->locateName('eNtry2.txt') . "\n";
echo $zip->locateName('eNtry2.txt', ZipArchive::FL_NOCASE) . "\n";
echo $zip->locateName('enTRy2d.txt', ZipArchive::FL_NOCASE|ZipArchive::FL_NODIR) . "\n";
$zip->close();

?>

   
```php

El ejemplo anterior mostrará:

    El ejemplo de arriba mostrará la salida:

    0

    1
    2
