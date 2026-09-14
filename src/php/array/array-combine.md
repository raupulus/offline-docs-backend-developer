---
title: array_combine
description: Crea un array a partir de dos otros arrays
source_url: https://www.php.net/manual/es/function.array-combine.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-combine.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 2e60c5134
order: 5190
---

array_combine

Crea un array a partir de dos otros arrays

## Descripción

```php
array_combine(array $keys, array $values): array
```php

Crea un `array`, donde las claves son los valores de `keys`, y los valores son los valores de `values`.

## Parámetros

`keys`  
Array de claves a utilizar. Los valores ilegales para las claves serán convertidos en `string`.

`values`  
`Array` de valores a utilizar

## Valores devueltos

Devuelve el `array` combinado.

## Errores/Excepciones

A partir de PHP 8.0.0, lanza un error de tipo `ValueError` si el número de elementos de `keys` y de `values` no coinciden. Anteriormente, lanzaba una advertencia de nivel `E_WARNING`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `array_combine` ahora lanza un error de tipo `ValueError` si el número de elementos para cada array es desigual; anteriormente se devolvía `false` en su lugar. |

## Ejemplos

Ejemplo con `array_combine`

```
<?php
$a = array('green', 'red', 'yellow');
$b = array('avocado', 'apple', 'banana');
$c = array_combine($a, $b);

print_r($c);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [green] => avocado
        [red] => apple
        [yellow] => banana
    )

## Véase también

`array_merge`, `array_walk`, `array_values`, `array_map`
