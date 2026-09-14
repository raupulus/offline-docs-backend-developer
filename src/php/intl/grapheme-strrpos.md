---
title: grapheme_strrpos
description: Encuentra la posición del último grafema
source_url: https://www.php.net/manual/es/function.grapheme-strrpos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/grapheme/grapheme-strrpos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: 2583cd865
order: 39890
---

grapheme_strrpos

Encuentra la posición del último grafema

## Descripción

Estilo procedimental

```php
grapheme_strrpos(string $haystack, string $needle, [int $offset], [string $locale]): int
```php

Encuentra la posición del último grafema, realizando una búsqueda sensible a mayúsculas y minúsculas.

## Parámetros

`haystack`  
La cadena a estudiar. Debe estar en formato UTF-8 válido.

`needle`  
La cadena a buscar. Debe estar en formato UTF-8 válido.

`offset`  
El argumento `offset` permite especificar la posición en la `haystack` donde comienza la búsqueda, expresada en grafemas (y no en octetos o caracteres). La posición devuelta siempre se da con respecto al inicio de `haystack`, independientemente del valor de `offset`.

El parámetro opcional offset permite especificar la posición en `haystack` donde comienza la búsqueda, expresada como un desplazamiento en grafemas (y no en bytes o caracteres). Si `offset` es negativo, se interpreta con respecto al final de la cadena. La posición devuelta siempre se da con respecto al inicio de `haystack`, independientemente del valor de offset. La búsqueda se realiza de derecha a izquierda, buscando la primera aparición de `needle` a partir del grupo de grafemas seleccionado.

`locale`  
La configuración regional a utilizar.

## Valores devueltos

Devuelve la posición en forma de entero. Si `needle` no es encontrado, `grapheme_strrpos` devuelve `false`.

## Historial de cambios

| Versión | Descripción                                   |
|---------|-----------------------------------------------|
| 8.5.0   | Se ha añadido el parámetro opcional `locale`. |

## Ejemplos

Ejemplo con `grapheme_strrpos`

```
<?php
$char_a_ring_nfd = "a\xCC\x8A";  // 'LATIN SMALL LETTER A WITH RING ABOVE' (U+00E5) forma normalizada "D"
$char_o_diaeresis_nfd = "o\xCC\x88"; // 'LATIN SMALL LETTER O WITH DIAERESIS' (U+00F6) forma normalizada "D"

print grapheme_strrpos( $char_a_ring_nfd . $char_o_diaeresis_nfd . $char_o_diaeresis_nfd, $char_o_diaeresis_nfd);
?>

   
```php

El ejemplo anterior mostrará:

    2

      

## Véase también

`grapheme_stripos`, `grapheme_stristr`, `grapheme_strpos`, `grapheme_strripos`, `grapheme_strstr`, [ Unicode Text Segmentation: Grapheme Cluster Boundaries ](http://unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries)
