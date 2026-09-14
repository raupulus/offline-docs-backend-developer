---
title: grapheme_extract
description: Extrae un grupo de grafemas de una cadena UTF-8
source_url: https://www.php.net/manual/es/function.grapheme-extract.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/grapheme/grapheme-extract.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 2245ff665
order: 39820
---

grapheme_extract

Extrae un grupo de grafemas de una cadena UTF-8

## Descripción

Estilo procedimental

```php
grapheme_extract(string $haystack, int $size, [int $type], [int $offset], [int $next]): string
```php

Esta función extrae una secuencia de grupos de grafemas por defecto de un texto en UTF-8.

## Parámetros

`haystack`  
La cadena a estudiar.

`size`  
El número máximo de elementos, en función de `type`, a devolver.

`type`  
Define el tipo de unidades indicadas por el parámetro `size`:

GRAPHEME_EXTR_COUNT (por defecto): `size` es el número de grupos de grafemas a extraer., GRAPHEME_EXTR_MAXBYTES: `size` es el número de bytes a devolver., GRAPHEME_EXTR_MAXCHARS: `size` es el número de caracteres UTF-8 a devolver.

`offset`  
La posición de inicio en `haystack`, expresada en bytes. Debe ser positiva, nula o inferior al tamaño de `haystack` en bytes, o un valor negativo, que contaría desde el final de `haystack`. Si `offset` no corresponde al primer byte de un carácter UTF-8 válido, la posición de inicio será desplazada al siguiente byte válido.

`next`  
Referencia a una variable que recibirá la próxima posición de inicio válida. Cuando la función termina, esto puede ser una posición que está más allá del tamaño de la cadena.

## Valores devueltos

Una cadena que comienza en la posición `offset` y termina en el límite válido de un grafema, y que se ajusta a las condiciones `size` y `type` especificadas, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                                              |
|---------|----------------------------------------------------------|
| 7.1.0   | Se añadió el soporte para valores negativos en `offset`. |

## Ejemplos

Ejemplo con `grapheme_extract`

```
<?php

$char_a_ring_nfd = "a\xCC\x8A";  // 'LATIN SMALL LETTER A WITH RING ABOVE' (U+00E5) normalization form "D"
$char_o_diaeresis_nfd = "o\xCC\x88"; // 'LATIN SMALL LETTER O WITH DIAERESIS' (U+00F6) normalization form "D"

print urlencode(grapheme_extract( $char_a_ring_nfd . $char_o_diaeresis_nfd, 1, GRAPHEME_EXTR_COUNT, 2));

?>

   
```php

El ejemplo anterior mostrará:

    o%CC%88

      

## Véase también

`grapheme_substr`, [ Unicode Text Segmentation: Grapheme Cluster Boundaries ](http://unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries)
