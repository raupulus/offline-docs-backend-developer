---
title: grapheme_substr
description: Devuelve una parte de un string
source_url: https://www.php.net/manual/es/function.grapheme-substr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/grapheme/grapheme-substr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 9a8c593c0
order: 39910
---

grapheme_substr

Devuelve una parte de un string

## Descripción

Estilo procedimental

```php
grapheme_substr(string $string, int $offset, [int $length], [string $locale]): string
```php

Devuelve una parte de un string.

## Parámetros

`string`  
El string a cortar. Debe ser UTF-8 y válido.

`offset`  
Posición de inicio en unidades de grafema por defecto. Si `offset` es estrictamente positivo, el string devuelto comenzará en la `offset` ésima posición en `string`, contando desde cero. Si `offset` es negativo, el string devuelto comenzará en la `offset` ésima unidad de grafema desde el final del string.

`length`  
El tamaño del sub-string a extraer, en unidades de grafema. Si `length` es dado y positivo, el string devuelto contendrá como máximo `length` grafemas, comenzando en `offset` (dependiendo del tamaño del string). Si `length` es proporcionado y es negativo, entonces se omitirán tantos grafemas desde el final del string (después de que la posición de inicio haya sido calculada, cuando `offset` también es negativo). Si `offset` denota una posición más allá del final del string, se devuelve un string vacío.

`locale`  
La configuración regional a utilizar.

## Valores devueltos

Devuelve la parte del string extraída de `string`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Se ha añadido el parámetro opcional `locale`. |
| 8.0.0 | La función ahora corrige sistemáticamente los desplazamientos fuera de límites a los límites del string. Anteriormente, `false` era devuelto en lugar de un string vacío en algunos casos. |

## Ejemplos

Ejemplo con `grapheme_substr`

```
<?php

$char_a_ring_nfd = "a\xCC\x8A";  // 'LATIN SMALL LETTER A WITH RING ABOVE' (U+00E5) normalization form "D"
$char_o_diaeresis_nfd = "o\xCC\x88"; // 'LATIN SMALL LETTER O WITH DIAERESIS' (U+00F6) normalization form "D"

print urlencode(grapheme_substr( "ao" . $char_a_ring_nfd . "bc" . $char_o_diaeresis_nfd . "O", 2, -1 ));
?>

   
```php

El ejemplo anterior mostrará:

    a%CC%8Abco%CC%88

      

## Véase también

`grapheme_extract`, [ Unicode Text Segmentation: Grapheme Cluster Boundaries ](http://unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries)
