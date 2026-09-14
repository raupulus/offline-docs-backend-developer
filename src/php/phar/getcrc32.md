---
title: PharFileInfo::getCRC32
description: Retorna el código CRC32 o levanta una excepción si el CRC no ha sido
  verificado
source_url: https://www.php.net/manual/es/pharfileinfo.getcrc32.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharFileInfo/getCRC32.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 64770
---

PharFileInfo::getCRC32

Retorna el código CRC32 o levanta una excepción si el CRC no ha sido verificado

## Descripción

```php
public PharFileInfo::getCRC32(): int
```php

Retorna la suma de verificación `crc32` del fichero dentro del archivo Phar.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La suma de verificación `crc32` del fichero dentro del archivo Phar.

## Errores/Excepciones

Levanta una excepción `BadMethodCallException` si el CRC32 del fichero no ha sido verificado aún. Esto no ocurre normalmente, ya que el CRC es verificado al abrir el fichero en modo lectura o escritura.

## Ejemplos

Ejemplo con `PharFileInfo::getCRC32`

```
<?php
try {
    $p = new Phar('/ruta/versus/mon.phar', 0, 'mon.phar');
    $p['monfichier.txt'] = 'salut';
    $file = $p['monfichier.txt'];
    echo $file->getCRC32();
} catch (Exception $e) {
    echo 'La escritura de mon.phar.phar ha fallado: ', $e;
}
?>

    
```php

El ejemplo anterior mostrará:

    3633523372
