---
title: Ds\Set::add
description: Añade valores a la secuencia
source_url: https://www.php.net/manual/es/ds-set.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 9e0f03ac3
order: 15760
---

Ds\Set::add

Añade valores a la secuencia

## Descripción

```php
public Ds\Set::add(mixed ...$values): void
```php

Añade todos los valores dados al conjunto que no hayan sido ya añadidos.

> [!NOTE]
> Los valores de tipo `object` son soportados. Si un objeto implementa `Ds\Hashable`, la igualdad será determinada por la función `equals` del objeto. Si un objeto no implementa `Ds\Hashable`, los objetos deben ser referencias a la misma instancia para ser considerados iguales.

> [!CAUTION]
> Todas las comparaciones son estrictas (tipo y valor).

## Parámetros

`values`  
Los valores a añadir a la secuencia.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Set::add` utilizando enteros

```
<?php
$set = new \Ds\Set();

$set->add(1);
$set->add(1);
$set->add(2);
$set->add(3);

// Las comparaciones estrictas no tratarían estos valores de la misma manera que int(1)
$set->add("1");
$set->add(true);

var_dump($set);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Set)#1 (5) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
      [3]=>
      string(1) "1"
      [4]=>
      bool(true)
    }

Ejemplo de `Ds\Set::add` utilizando objetos

```
<?php
class HashableObject implements \Ds\Hashable
{
    /**
     * Un valor arbitrario a utilizar como valor de hash. No define la igualdad.
     */
    private $value;

    public function __construct($value)
    {
        $this->value = $value;
    }

    public function hash()
    {
        return $this->value;
    }

    public function equals($obj): bool
    {
        return $this->value === $obj->value;
    }
}

$set = new \Ds\Set();

$obj = new \ArrayIterator([]);

// Añadir la misma instancia varias veces solo añadirá la primera.
$set->add($obj);
$set->add($obj);

// Añadir varias instancias del mismo objeto añadirá todas las instancias.
$set->add(new \stdClass());
$set->add(new \stdClass());

// Añadir varias instancias de objetos hashables iguales solo añadirá la primera.
$set->add(new \HashableObject(1));
$set->add(new \HashableObject(1));
$set->add(new \HashableObject(2));
$set->add(new \HashableObject(2));

var_dump($set);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Set)#1 (5) {
      [0]=>
      object(ArrayIterator)#2 (1) {
        ["storage":"ArrayIterator":private]=>
        array(0) {
        }
      }
      [1]=>
      object(stdClass)#3 (0) {
      }
      [2]=>
      object(stdClass)#4 (0) {
      }
      [3]=>
      object(HashableObject)#5 (1) {
        ["value":"HashableObject":private]=>
        int(1)
      }
      [4]=>
      object(HashableObject)#6 (1) {
        ["value":"HashableObject":private]=>
        int(2)
      }
    }
