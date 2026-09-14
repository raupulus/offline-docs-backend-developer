---
title: PharFileInfo::isCRCChecked
description: Determina si el fichero tiene un CRC verificado
source_url: https://www.php.net/manual/es/pharfileinfo.iscrcchecked.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharFileInfo/isCRCChecked.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64830
---

PharFileInfo::isCRCChecked

Determina si el fichero tiene un CRC verificado

## Descripción

```php
public PharFileInfo::isCRCChecked(): bool
```php

Este método determina si un fichero dentro de un archivo Phar tiene un CRC verificado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si el fichero tiene un CRC verificado, `false` en caso contrario.

## Ejemplos

Un ejemplo con `PharFileInfo::isCRCChecked`

```
<?php
try {
    $p = new Phar('/ruta/al/mon.phar', 0, 'mon.phar');
    $p['monfichier.txt'] = 'hola';
    $file = $p['monfichier.txt'];
    var_dump($file->isCRCChecked());
} catch (Exception $e) {
    echo 'La creación/modificación de mon.phar ha fallado: ', $e;
}
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
