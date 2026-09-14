---
title: ZipArchive::getExternalAttributesIndex
description: Obtener los atributos externos de una entrada definida por su índice
source_url: https://www.php.net/manual/es/ziparchive.getexternalattributesindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/getexternalattributesindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108290
---

ZipArchive::getExternalAttributesIndex

Obtener los atributos externos de una entrada definida por su índice

## Descripción

```php
public ZipArchive::getExternalAttributesIndex(int $index, int $opsys, int $attr, [int $flags]): bool
```php

Recuperar los atributos externos de una entrada definida por su índice.

## Parámetros

`index`  
El índice de la entrada.

`opsys`  
En caso de éxito, recibe el código del sistema operativo definido por una de las constantes ZipArchive::OPSYS\_.

`attr`  
En caso de éxito, recibe los atributos externos. El valor dependerá del sistema operativo.

`flags`  
Si flags se establece a `ZipArchive::FL_UNCHANGED`, se devuelven los atributos originales sin cambios.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Este ejemplo extrae todas las entradas de un archivo ZIP `test.zip` y asigna los permisos Unix tomados de los atributos externos.

Extraer todas las entradas con permisos Unix

```
<?php
$zip = new ZipArchive();
if ($zip->open('test.zip') === TRUE) {
    for ($idx=0 ; $s = $zip->statIndex($idx) ; $idx++) {
        if ($zip->extractTo('.', $s['name'])) {
            if ($zip->getExternalAttributesIndex($idx, $opsys, $attr)
                && $opsys==ZipArchive::OPSYS_UNIX) {
               chmod($s['name'], ($attr >> 16) & 0777);
            }
        }
    }
    $zip->close();
    echo "Ok\n";
} else {
    echo "KO\n";
}
?>

   
```php
