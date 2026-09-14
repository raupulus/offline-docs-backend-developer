---
title: array_search
description: Busca en un array la primera clave asociada al valor
source_url: https://www.php.net/manual/es/function.array-search.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-search.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 2e60c5134
order: 5570
---

array_search

Busca en un array la primera clave asociada al valor

## Descripción

```php
array_search(mixed $needle, array $haystack, [bool $strict]): int
```php

Busca `needle` en `haystack`.

## Parámetros

`needle`  
El valor a buscar.

> [!NOTE]
> Si `needle` es un `string`, la comparación se realiza respetando la casilla.

`haystack`  
El array.

`strict`  
Si el tercer argumento `strict` es `true`, entonces `array_search` buscará elementos *idénticos* en `haystack`. Esto significa que esta función realizará una [comparación estricta del tipo](#language.types) de `needle` en `haystack`, y que los objetos provienen de la misma instancia.

## Valores devueltos

Devuelve la clave para `needle` si es encontrada en el array, `false` en caso contrario.

Si `needle` es encontrado más de una vez en `haystack`, la primera clave coincidente es devuelta. Para encontrar todas las claves correspondientes, utilice en su lugar la función `array_keys` con el argumento opcional `filter_value`.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Ejemplos

Ejemplo con `array_search`

```
<?php
$array = array(0 => 'blue', 1 => 'red', 2 => 'green', 3 => 'red');

$key = array_search('green', $array); // $key = 2;
print_r($key);

$key = array_search('red', $array);   // $key = 1;
print_r($key);
?>

    
```php

## Véase también

`array_keys`, `array_values`, `array_key_exists`, `in_array`
