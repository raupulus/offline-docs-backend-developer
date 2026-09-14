---
title: filter_var_array
description: Obtiene múltiple variables y opcionalmente las filtra
source_url: https://www.php.net/manual/es/function.filter-var-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filter/functions/filter-var-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filter
translation_status: ready
translation_reviewed: false
translation_revision: 627f933cf
order: 24220
---

filter_var_array

Obtiene múltiple variables y opcionalmente las filtra

## Descripción

```php
filter_var_array(array $array, [array $options], [bool $add_empty]): array
```php

Valida un `array` asociativo de valores usando los filtros de validación `FILTER_VALIDATE_*`, filtros de saneación `FILTER_SANITIZE_*`, o filtros definidos por el usuario

## Parámetros

`array`  
Un array asociativo que contiene los datos a filtrar.

`options`  
Ya sea un `array` asociativo de opciones, o el filtro que se aplicará a cada entrada, que puede ser un filtro de validación mediante el uso de una de las constantes `FILTER_VALIDATE_*` o un filtro de saneamiento mediante el uso de una de las constantes `FILTER_SANITIZE_*`.

La array de opciones es un array asociativo donde la clave corresponde a una clave en la matriz de datos `array` y el valor asociado es el filtro a aplicar a esta entrada, o un array asociativo que describe cómo y qué filtro se debe aplicar a esta entrada.

El array asociativo que describe cómo se debe aplicar un filtro debe contener la clave `'filter'` cuyo valor asociado es el filtro a aplicar, que puede ser uno de las constantes `FILTER_VALIDATE_*`, `FILTER_SANITIZE_*`, `FILTER_UNSAFE_RAW`, o `FILTER_CALLBACK`. Opcionalmente, puede contener la clave `'flags'`, que especifica los indicadores que se aplican al filtro, y la clave `'options'`, que especifica las opciones que se aplican al filtro.

`add_empty`  
Añade claves faltantes como `null` al valor devuelto.

## Valores devueltos

En caso de éxito un array que contiene los valores de las variables que se han pedido o `false` en caso de fallo. El valor del array será `false` si el filtro falla o `null` si la variable no está definida.

## Ejemplos

Ejemplo de `filter_var_array`

```
<?php

$data = [
    'product_id' => 'libgd<script>',
    'component'  => '10',
    'versions'   => '2.0.33',
    'testscalar' => ['2', '23', '10', '12'],
    'testarray'  => '2',
];

$filters = [
    'product_id'   => FILTER_SANITIZE_ENCODED,
    'component'    => [
        'filter'   => FILTER_VALIDATE_INT,
        'flags'    => FILTER_FORCE_ARRAY,
        'options'  => [
            'min_range' => 1,
            'max_range' => 10,
        ],
    ],
    'versions'     => [
        'filter' => FILTER_SANITIZE_ENCODED
    ],
    'testscalar'   => [
        'filter' => FILTER_VALIDATE_INT,
        'flags'  => FILTER_REQUIRE_SCALAR,
    ],
    'testarray'    => [
        'filter' => FILTER_VALIDATE_INT,
        'flags'  => FILTER_FORCE_ARRAY,
    ],
    'doesnotexist' => FILTER_VALIDATE_INT,
];

var_dump(filter_var_array($data, $filters));

?>

   
```php

El ejemplo anterior mostrará:

    array(6) {
      ["product_id"]=>
      string(17) "libgd%3Cscript%3E"
      ["component"]=>
      array(1) {
        [0]=>
        int(10)
      }
      ["versions"]=>
      string(6) "2.0.33"
      ["testscalar"]=>
      bool(false)
      ["testarray"]=>
      array(1) {
        [0]=>
        int(2)
      }
      ["doesnotexist"]=>
      NULL
    }

## Véase también

filter_input_array

filter_var

filter_input

Filtros de validación

FILTER_VALIDATE\_

\*

Filtros de saneación

FILTER_SANITIZE\_

\*
