---
title: AppendIterator::append
description: Añade un iterador
source_url: https://www.php.net/manual/es/appenditerator.append.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/appenditerator/append.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 81000
---

AppendIterator::append

Añade un iterador

## Descripción

```php
public AppendIterator::append(Iterator $iterator): void
```php

Añade un iterador.

## Parámetros

`iterator`  
El iterador a añadir.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de AppendIterator::append

```
<?php
$array_a = new ArrayIterator(array('a', 'b', 'c'));
$array_b = new ArrayIterator(array('d', 'e', 'f'));

$iterator = new AppendIterator;
$iterator->append($array_a);
$iterator->append($array_b);

foreach ($iterator as $current) {
    echo $current;
}
?>

    
```php

El ejemplo anterior mostrará:

    abcdef

## Véase también

AppendIterator::\_\_construct
