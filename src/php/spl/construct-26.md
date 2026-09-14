---
title: SplFixedArray::__construct
description: Construye un nuevo SplFixedArray
source_url: https://www.php.net/manual/es/splfixedarray.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfixedarray/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84650
---

SplFixedArray::\_\_construct

Construye un nuevo

SplFixedArray

## Descripción

```php
public SplFixedArray::__construct([int $size])
```php

Inicializa un array fijo con un número de valores `null` iguales al argumento `size`.

## Parámetros

`size`  
El tamaño del array de tamaño fijo. Espera un número comprendido entre `0` y `PHP_INT_MAX`.

## Errores/Excepciones

Lanza una excepción `ValueError` cuando `size` es negativo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Ahora lanza una excepción `ValueError` cuando `size` es negativo. Anteriormente, se lanzaba una `InvalidArgumentException`. |

## Ejemplos

Ejemplo con `SplFixedArray::__construct`

```
<?php
$array = new SplFixedArray(5);

$array[1] = 2;
$array[4] = "foo";

foreach($array as $v) {
  var_dump($v);
}
?>

    
```php

El ejemplo anterior mostrará:

    NULL
    int(2)
    NULL
    NULL
    string(3) "foo"
