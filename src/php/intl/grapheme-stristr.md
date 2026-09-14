---
title: grapheme_stristr
description: Devuelve la parte de una cadena a partir de una ocurrencia
source_url: https://www.php.net/manual/es/function.grapheme-stristr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/grapheme/grapheme-stristr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 9a8c593c0
order: 39850
---

grapheme_stristr

Devuelve la parte de una cadena a partir de una ocurrencia

## Descripción

Estilo procedimental

```php
grapheme_stristr(string $haystack, string $needle, [bool $beforeNeedle], [string $locale]): string
```php

Devuelve la parte de `haystack` a partir de la primera ocurrencia de `needle` (`needle` incluido) (insensible a mayúsculas/minúsculas), y hasta el final de la `haystack`.

## Parámetros

`haystack`  
La cadena a estudiar. Debe ser válida UTF-8.

`needle`  
La cadena a buscar. Debe ser válida UTF-8.

`beforeNeedle`  
Si `true`, `grapheme_stristr` devuelve la parte de `haystack` antes de la primera ocurrencia (`needle` excluido).

`locale`  
La configuración regional a utilizar.

## Valores devueltos

Devuelve una porción de `haystack`, o `false` si `needle` no es encontrado.

## Historial de cambios

| Versión | Descripción                                   |
|---------|-----------------------------------------------|
| 8.5.0   | Se ha añadido el parámetro opcional `locale`. |

## Ejemplos

Ejemplo con `grapheme_stristr`

```
<?php

$char_a_ring_nfd  = "a\xCC\x8A";  // 'LATIN SMALL LETTER A WITH RING ABOVE' (U+00E5)  forma normalizada "D"
$char_o_diaeresis_nfd  = "o\xCC\x88"; // 'LATIN SMALL LETTER O WITH DIAERESIS' (U+00F6) forma  normalizada "D"
$char_O_diaeresis_nfd =  "O\xCC\x88"; // 'LATIN CAPITAL LETTER O WITH DIAERESIS' (U+00D6) forma  normalizada "D"

print  urlencode(grapheme_stristr( $char_a_ring_nfd . $char_o_diaeresis_nfd .  $char_a_ring_nfd, $char_O_diaeresis_nfd));

?>

   
```php

El ejemplo anterior mostrará:

    o%CC%88a%CC%8A

      

## Véase también

`grapheme_stripos`, `grapheme_strpos`, `grapheme_strripos`, `grapheme_strrpos`, `grapheme_strstr`, [ Unicode Text Segmentation: Grapheme Cluster Boundaries ](http://unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries)
