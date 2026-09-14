---
title: SplFileObject::getFlags
description: Obtener las flags de SplFileObject
source_url: https://www.php.net/manual/es/splfileobject.getflags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/getflags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84520
---

SplFileObject::getFlags

Obtener las flags de SplFileObject

## Descripción

```php
public SplFileObject::getFlags(): int
```php

Obtiene las flags establecidas en una instancia de SplFileObject como un `int`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `int` que representa las flags.

## Ejemplos

Ejemplo de SplFileObject::getFlags

```
<?php
$file = new SplFileObject(__FILE__, "r");

if ($file->getFlags() & SplFileObject::SKIP_EMPTY) {
    echo "Saltando líneas vacías\n";
} else {
    echo "Sin saltar líneas vacías\n";
}

$file->setFlags(SplFileObject::SKIP_EMPTY);

if ($file->getFlags() & SplFileObject::SKIP_EMPTY) {
    echo "Saltando líneas vacías\n";
} else {
    echo "Sin saltar líneas vacías\n";
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Sin saltar líneas vacías
    Saltando líneas vacías

## Véase también

SplFileObject::setFlags
