---
title: SplFileObject::key
description: Obtiene el número de línea
source_url: https://www.php.net/manual/es/splfileobject.key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84550
---

SplFileObject::key

Obtiene el número de línea

## Descripción

```php
public SplFileObject::key(): int
```php

Obtener el número de línea.

> [!NOTE]
> Este nñumero puede no ser reflejado en la línea actual en el fichero si el método SplFileObject::setMaxLineLen es usado para leer posiciones fijas de el fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de línea actual.

## Ejemplos

Ejemplo de SplFileObject::key

```
<?php
$file = new SplFileObject("lipsum.txt");
foreach ($file as $line) {
    echo $file->key() . ". " . $line;
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    0. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    1. Duis nec sapien felis, ac sodales nisl.
    2. Lorem ipsum dolor sit amet, consectetur adipiscing elit.

SplFileObject::key ejemplo con SplFileObject::setMaxLineLen

```
<?php
$file = new SplFileObject("lipsum.txt");
$file->setMaxLineLen(20);
foreach ($file as $line) {
    echo $file->key() . ". " . $line . "\n";
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    0. Lorem ipsum dolor s
    1. it amet, consectetu
    2. r adipiscing elit.
    3.

    4. Duis nec sapien fel
    5. is, ac sodales nisl
    6. .

    7. Lorem ipsum dolor s
    8. it amet, consectetu
    9. r adipiscing elit.

## Véase también

SplFileObject::current, SplFileObject::seek, SplFileObject::next, SplFileObject::rewind, SplFileObject::valid
