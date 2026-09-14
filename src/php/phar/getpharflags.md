---
title: PharFileInfo::getPharFlags
description: Devuelve los flags del archivo Phar
source_url: https://www.php.net/manual/es/pharfileinfo.getpharflags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharFileInfo/getPharFlags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64810
---

PharFileInfo::getPharFlags

Devuelve los flags del archivo Phar

## Descripción

```php
public PharFileInfo::getPharFlags(): int
```php

Este método devuelve los flags establecidos en el manifiesto para un Phar. Siempre devolverá `0` en su implementación actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Los flags Phar (siempre `0` en su implementación actual)

## Ejemplos

Un ejemplo con `PharFileInfo::getPharFlags`

```
<?php
try {
    $p = new Phar('/ruta/versus/mon.phar', 0, 'mon.phar');
    $p['monfichier.txt'] = 'hola';
    $file = $p['monfichier.txt'];
    var_dump($file->getPharFlags());
} catch (Exception $e) {
    echo 'No puede crear/modificar mon.phar: ', $e;
}
?>

    
```php

El ejemplo anterior mostrará:

    int(0)
