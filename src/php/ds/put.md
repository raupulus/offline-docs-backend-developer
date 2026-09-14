---
title: Ds\Map::put
description: Asocia una clave a un valor
source_url: https://www.php.net/manual/es/ds-map.put.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/put.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15040
---

Ds\Map::put

Asocia una clave a un valor

## Descripción

```php
public Ds\Map::put(mixed $key, mixed $value): void
```php

Asocia una `clave` a un `valor`, sobrescribiendo una asociación previa si existe.

> [!NOTE]
> Las claves de tipo `object` son soportadas. Si un objeto implementa `Ds\Hashable`, la igualdad será determinada por la función `equals` del objeto. Si un objeto no implementa `Ds\Hashable`, los objetos deben ser referencias a la misma instancia para ser considerados iguales.

> [!NOTE]
> Asimismo, se puede utilizar la sintaxis de array para asociar valores por clave, por ejemplo `$map["clave"] = $valor`.

> [!CAUTION]
> Atención al uso de la sintaxis de array. Las claves escalares serán coercionadas a enteros por el motor. Por ejemplo, `$map["1"]` intentará acceder a `int(1)`, mientras que `$map->get("1")` buscará correctamente la clave de string.
>
> Ver [arrays](#language.types.array).

## Parámetros

`key`  
La clave a asociar al valor.

`value`  
El valor a asociar a la clave.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Map::put`

```
<?php
$map = new \Ds\Map();

$map->put("a", 1);
$map->put("b", 2);
$map->put("c", 3);

print_r($map);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Map Object
    (
        [0] => Ds\Pair Object
            (
                [key] => a
                [value] => 1
            )

        [1] => Ds\Pair Object
            (
                [key] => b
                [value] => 2
            )

        [2] => Ds\Pair Object
            (
                [key] => c
                [value] => 3
            )

    )

Ejemplo de `Ds\Map::put` utilizando objetos como clave

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

$map = new \Ds\Map();

$obj = new \ArrayIterator([]);

// Utilizar la misma instancia varias veces sobrescribirá el valor anterior.
$map->put($obj, 1);
$map->put($obj, 2);

// Utilizar varias instancias del mismo objeto creará nuevas asociaciones.
$map->put(new \stdClass(), 3);
$map->put(new \stdClass(), 4);

// Utilizar varias instancias de objetos iguales sobrescribirá los valores anteriores.
$map->put(new \HashableObject(1), 5);
$map->put(new \HashableObject(1), 6);
$map->put(new \HashableObject(2), 7);
$map->put(new \HashableObject(2), 8);

var_dump($map);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Map)#1 (5) {
      [0]=>
      object(Ds\Pair)#7 (2) {
        ["key"]=>
        object(ArrayIterator)#2 (1) {
          ["storage":"ArrayIterator":private]=>
          array(0) {
          }
        }
        ["value"]=>
        int(2)
      }
      [1]=>
      object(Ds\Pair)#8 (2) {
        ["key"]=>
        object(stdClass)#3 (0) {
        }
        ["value"]=>
        int(3)
      }
      [2]=>
      object(Ds\Pair)#9 (2) {
        ["key"]=>
        object(stdClass)#4 (0) {
        }
        ["value"]=>
        int(4)
      }
      [3]=>
      object(Ds\Pair)#10 (2) {
        ["key"]=>
        object(HashableObject)#5 (1) {
          ["value":"HashableObject":private]=>
          int(1)
        }
        ["value"]=>
        int(6)
      }
      [4]=>
      object(Ds\Pair)#11 (2) {
        ["key"]=>
        object(HashableObject)#6 (1) {
          ["value":"HashableObject":private]=>
          int(2)
        }
        ["value"]=>
        int(8)
      }
    }
