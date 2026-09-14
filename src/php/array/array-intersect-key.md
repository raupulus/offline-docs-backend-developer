---
title: array_intersect_key
description: Calcula la intersección de dos arrays utilizando las claves para la comparación
source_url: https://www.php.net/manual/es/function.array-intersect-key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-intersect-key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: c84024092
order: 5340
---

array_intersect_key

Calcula la intersección de dos arrays utilizando las claves para la comparación

## Descripción

```php
array_intersect_key(array $array, array ...$arrays): array
```php

`array_intersect_key` devuelve un array que contiene todas las entradas del array `array` que contienen claves presentes en todos los arrays pasados como argumentos.

## Parámetros

`array`  
El array que contiene las claves maestras a verificar.

`arrays`  
Arrays a comparar.

## Valores devueltos

Devuelve un array asociativo que contiene todas las entradas del array `array` cuyas claves están presentes en todos los argumentos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función puede ser llamada ahora con un solo parámetro. Anteriormente, al menos dos parámetros eran necesarios. |

## Ejemplos

Ejemplo con `array_intersect_key`

```
<?php
$array1 = array('azul'  => 1, 'rojo'  => 2, 'verde'  => 3, 'violeta' => 4);
$array2 = array('verde' => 5, 'azul' => 6, 'amarillo' => 7, 'cian'   => 8);

var_dump(array_intersect_key($array1, $array2));
?>

    
```php

El ejemplo anterior mostrará:

    array(2) {
      ["azul"]=>
      int(1)
      ["verde"]=>
      int(3)
    }

En este ejemplo, se puede ver que solo las claves `'azul'` y `'verde'` están presentes en ambos arrays y por lo tanto, son devueltas. Note también que los valores para las claves `'azul'` y `'verde'` difieren entre los dos arrays. No obstante, aún corresponden porque solo las claves son verificadas. Los valores devueltos son los del array `array1`.

Las dos claves desde los pares `clave => valor` son consideradas iguales solo si `(string) $clave1 === (string) $clave2`. En otras palabras, se realiza un análisis estricto del tipo, por lo que la representación en forma de string debe ser exactamente la misma.

## Véase también

`array_diff`, `array_udiff`, `array_diff_assoc`, `array_diff_uassoc`, `array_udiff_assoc`, `array_udiff_uassoc`, `array_diff_key`, `array_diff_ukey`, `array_intersect`, `array_intersect_assoc`, `array_intersect_uassoc`, `array_intersect_ukey`
