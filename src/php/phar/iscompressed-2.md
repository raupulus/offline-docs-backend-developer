---
title: PharFileInfo::isCompressed
description: Indica si la entrada está comprimida
source_url: https://www.php.net/manual/es/pharfileinfo.iscompressed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharFileInfo/isCompressed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64840
---

PharFileInfo::isCompressed

Indica si la entrada está comprimida

## Descripción

```php
public PharFileInfo::isCompressed([int $compression]): bool
```php

Este método determina si un fichero dentro de un archivo Phar está comprimido con una de las compresiones Gzip o Bzip2.

## Parámetros

`compression`  
Una de las compresiones `Phar::GZ` o `Phar::BZ2`, sin compresión por omisión.

## Valores devueltos

`true` si el fichero dentro del archivo está comprimido, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción                      |
|---------|----------------------------------|
| 8.0.0   | `compression` ahora es nullable. |

## Ejemplos

Un ejemplo con `PharFileInfo::isCompressed`

```
<?php
try {
    $p = new Phar('/ruta/versus/mon.phar', 0, 'mon.phar');
    $p['monfichier.txt'] = 'salut';
    $p['monfichier2.txt'] = 'salut';
    $p['monfichier2.txt']->setCompressedGZ();
    $file = $p['monfichier.txt'];
    $file2 = $p['monfichier2.txt'];
    var_dump($file->isCompressed());
    var_dump($file2->isCompressed());
} catch (Exception $e) {
    echo 'La creación/modificación de mon.phar ha fallado: ', $e;
}
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)

## Véase también

`PharFileInfo::getCompressedSize`, `PharFileInfo::decompress`, `PharFileInfo::compress`, `Phar::decompress`, `Phar::compress`, `Phar::canCompress`, `Phar::isCompressed`, `Phar::getSupportedCompression`, `Phar::decompressFiles`, `Phar::compressFiles`
