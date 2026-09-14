---
title: grapheme_strstr
description: Retorna la parte de una cadena a partir de una ocurrencia, insensible
  a mayúsculas/minúsculas
source_url: https://www.php.net/manual/es/function.grapheme-strstr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/grapheme/grapheme-strstr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 9a8c593c0
order: 39900
---

grapheme_strstr

Retorna la parte de una cadena a partir de una ocurrencia, insensible a mayúsculas/minúsculas

## Descripción

Estilo procedimental

```php
grapheme_strstr(string $haystack, string $needle, [bool $beforeNeedle], [string $locale]): string
```php

Retorna la parte de una cadena a partir de la primera ocurrencia de `needle` (sensible a mayúsculas/minúsculas), y hasta el final de la cadena (`needle` incluido).

## Parámetros

`haystack`  
La cadena a estudiar. Debe ser válida UTF-8.

`needle`  
La cadena a buscar. Debe ser válida UTF-8.

`beforeNeedle`  
Si `true`, `grapheme_strstr` retorna la parte de la `haystack` antes de la primera ocurrencia de la `needle` (excluyendo el `needle`).

`locale`  
La configuración regional a utilizar.

## Valores devueltos

Retorna la porción de la `haystack` o `false` si `needle` no es encontrado.

## Historial de cambios

| Versión | Descripción                                   |
|---------|-----------------------------------------------|
| 8.5.0   | Se ha añadido el parámetro opcional `locale`. |

## Ejemplos

Ejemplo con `grapheme_strstr`

```
<?php

$char_a_ring_nfd = "a\xCC\x8A";  // 'LATIN SMALL LETTER A WITH RING ABOVE' (U+00E5) forma de normalización "D"
$char_o_diaeresis_nfd = "o\xCC\x88"; // 'LATIN SMALL LETTER O WITH DIAERESIS' (U+00F6) forma de normalización "D"

print urlencode(grapheme_stristr( $char_a_ring_nfd . $char_o_diaeresis_nfd . $char_a_ring_nfd, $char_o_diaeresis_nfd));

?>

   
```php

El ejemplo anterior mostrará:

    o%CC%88a%CC%8A

      

## Véase también

`grapheme_stristr`, `grapheme_stripos`, `grapheme_strpos`, `grapheme_strripos`, `grapheme_strrpos`, [ Unicode Text Segmentation: Grapheme Cluster Boundaries ](http://unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries)
