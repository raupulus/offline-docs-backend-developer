---
title: Phar::isCompressed
description: Devuelve Phar::GZ o PHAR::BZ2 si el archivo completo está comprimido
  (.tar.gz/tar.bz, etc)
source_url: https://www.php.net/manual/es/phar.iscompressed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/isCompressed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 64210
---

Phar::isCompressed

Devuelve Phar::GZ o PHAR::BZ2 si el archivo completo está comprimido (.tar.gz/tar.bz, etc)

## Descripción

```php
public Phar::isCompressed(): int
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Devuelve Phar::GZ o PHAR::BZ2 si el archivo completo está comprimido (.tar.gz/tar.bz, etc). Los archivos phar basados en Zip no pueden ser comprimidos como archivo, y este método siempre devolverá `false` si se consulta un archivo phar basado en Zip.

## Parámetros

No se admiten argumentos.

## Valores devueltos

`Phar::GZ`, `Phar::BZ2` o `false`.

## Ejemplos

Ejemplo con `Phar::isCompressed`

```
<?php
try {
    $phar1 = new Phar('monphar.zip.phar');
    var_dump($phar1->isCompressed());
    $phar2 = new Phar('monpharnoncompresse.tar.phar');
    var_dump($phar2->isCompressed());
    $phar2->compress(Phar::GZ);
    var_dump($phar2->isCompressed() == Phar::GZ);
} catch (Exception $e) {
}
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(false)
    bool(true)

## Véase también

`PharFileInfo::getCompressedSize`, `PharFileInfo::isCompressed`, `PharFileInfo::decompress`, `PharFileInfo::compress`, `Phar::decompress`, `Phar::compress`, `Phar::canCompress`, `Phar::compressFiles`, `Phar::decompressFiles`, `Phar::getSupportedCompression`
