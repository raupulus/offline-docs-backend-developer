---
title: IntlChar::enumCharTypes
description: Enumera todos los puntos de código con sus categorías generales Unicode
source_url: https://www.php.net/manual/es/intlchar.enumchartypes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/enumchartypes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40780
---

IntlChar::enumCharTypes

Enumera todos los puntos de código con sus categorías generales Unicode

## Descripción

```php
public static IntlChar::enumCharTypes(callable $callback): void
```php

Enumera eficientemente todos los puntos de código con sus categorías generales Unicode. Esto es útil para construir estructuras de datos, para enumerar todos los puntos de código asignados, etc.

Para cada rango de puntos de código contiguos con una categoría general dada ("tipo de carácter"), se llama a la función `callback`. Los rangos adyacentes tienen tipos diferentes. La norma Unicode garantiza que el valor numérico del tipo es 0..31.

## Parámetros

`callback`  
La función que debe ser llamada para cada rango de puntos de código contiguos con la misma categoría general. Se le pasarán los tres argumentos siguientes: `int` `$start` - El punto de código de inicio del rango, `int` `$end` - El punto de código de fin del rango, `int` `$name` - El tipo de carácter (una de las constantes `IntlChar::CHAR_CATEGORY_*`)

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Enumera un rango de ejemplo de puntos de código

```
    
<?php
IntlChar::enumCharTypes(function($start, $end, $type) {
    printf("U+%04x through U+%04x are in category %d\n", $start, $end, $type);
});
?>

   
```php

El ejemplo anterior mostrará:

        
    U+0000 through U+0020 are in category 15
    U+0020 through U+0021 are in category 12
    U+0021 through U+0024 are in category 23
    U+0024 through U+0025 are in category 25
    U+0025 through U+0028 are in category 23
    U+0028 through U+0029 are in category 20
    U+0029 through U+002a are in category 21
    U+002a through U+002b are in category 23
    U+002b through U+002c are in category 24
    U+002c through U+002d are in category 23
    U+002d through U+002e are in category 19
    U+002e through U+0030 are in category 23
    U+0030 through U+003a are in category 9
    ...
