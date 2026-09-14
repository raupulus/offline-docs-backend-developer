---
title: FilterIterator::accept
description: Comprueba si el elemento actual del iterador es aceptable
source_url: https://www.php.net/manual/es/filteriterator.accept.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/filteriterator/accept.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 82110
---

FilterIterator::accept

Comprueba si el elemento actual del iterador es aceptable

## Descripción

```php
public FilterIterator::accept(): bool
```php

Devuelve si el elemento actual del iterador es aceptable a través de este filtro.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si el elemento actual es aceptable, o `false` en caso contrario.

## Ejemplos

Ejemplo de `FilterIterator::accept`

```
<?php
// Este iterador filtra los valores con menos de 10 caracteres
class LengthFilterIterator extends FilterIterator {

    public function accept() {
        // Sólo acepta string con una longitud de 10 o mayor
        return strlen(parent::current()) >= 10;
    }

}

$arrayIterator = new ArrayIterator(array('test1', 'más de 10 caracteres'));
$lengthFilter = new LengthFilterIterator($arrayIterator);

foreach ($lengthFilter as $value) {
    echo $value . "\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    más de 10 caracteres
