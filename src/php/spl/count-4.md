---
title: GlobIterator::count
description: Lee el número de directorios y ficheros
source_url: https://www.php.net/manual/es/globiterator.count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/globiterator/count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: d51166ca1
order: 82350
---

GlobIterator::count

Lee el número de directorios y ficheros

## Descripción

```php
public GlobIterator::count(): int
```php

Lee el número de directorios y ficheros encontrados por la expresión Glob.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El número de directorios y ficheros se devuelve como un `int`.

## Ejemplos

Ejemplo con GlobIterator::count

```
<?php
$iterator = new GlobIterator('*.xml');

printf("Encontrados %d elemento(s)\r\n", $iterator->count());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Matched 8 item(s)

## Véase también

GlobIterator::\_\_construct, `count`, `glob`
