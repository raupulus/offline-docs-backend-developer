---
title: Countable::count
description: Cuenta el número de elementos de un objeto
source_url: https://www.php.net/manual/es/countable.count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/countable/count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 527e9b11a
order: 3120
---

Countable::count

Cuenta el número de elementos de un objeto

## Descripción

```php
public Countable::count(): int
```php

Este método se ejecuta cuando el `value` para `count` es un objeto que implementa `Countable`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El número contado, en forma `int`.

## Ejemplos

Ejemplo con `Countable::count`

```
<?php

class Counter implements Countable
{
    private $count = 0;

    public function count(): int
    {
        return ++$this->count;
    }
}

$counter = new Counter;

for ($i = 0; $i < 10; ++$i) {
    echo "He sido contado " . count($counter) . " veces\n";
}

?>

   
```php

Resultado del ejemplo anterior es similar a:

    He sido contado 1 veces
    He sido contado 2 veces
    He sido contado 3 veces
    He sido contado 4 veces
    He sido contado 5 veces
    He sido contado 6 veces
    He sido contado 7 veces
    He sido contado 8 veces
    He sido contado 9 veces
    He sido contado 10 veces
