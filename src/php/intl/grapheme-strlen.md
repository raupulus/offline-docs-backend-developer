---
title: grapheme_strlen
description: Lee la longitud de una cadena en número de grafemas
source_url: https://www.php.net/manual/es/function.grapheme-strlen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/grapheme/grapheme-strlen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: e7d502fec
order: 39860
---

grapheme_strlen

Lee la longitud de una cadena en número de grafemas

## Descripción

Estilo procedimental

```php
grapheme_strlen(string $string): int
```php

Lee la longitud de una cadena en número de grafemas (y no en bytes o caracteres).

## Parámetros

`string`  
La cadena a medir. Debe ser una cadena UTF-8 válida.

## Valores devueltos

La longitud de la cadena en caso de éxito, `null` o `false` en caso de fallo.

## Ejemplos

Ejemplo con `grapheme_strlen`

```
<?php

$char_a_ring_nfd = "a\xCC\x8A";  // 'LATIN SMALL LETTER A WITH RING ABOVE' (U+00E5) forma normalizada "D"
$char_o_diaeresis_nfd = "o\xCC\x88"; // 'LATIN SMALL LETTER O WITH DIAERESIS' (U+00F6) forma normalizada "D"

print grapheme_strlen( 'abc' . $char_a_ring_nfd . $char_o_diaeresis_nfd . $char_a_ring_nfd);

?>

   
```php

El ejemplo anterior mostrará:

    6

      

## Véase también

[ Unicode Text Segmentation: Grapheme Cluster Boundaries ](http://unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries), `iconv_strlen`, `mb_strlen`, `strlen`
