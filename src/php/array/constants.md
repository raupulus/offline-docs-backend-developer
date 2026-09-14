---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/array.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_revision: e50e79746
order: 5130
---

## Constantes predefinidas

Las constantes listadas aquí están siempre disponibles en PHP.

`CASE_LOWER` (`int`)  
`CASE_LOWER` se utiliza con `array_change_key_case` y sirve para convertir todos los índices de un array en minúsculas. Este es también el comportamiento por omisión de `array_change_key_case`. A partir de PHP 8.2.0, solo los caracteres ASCII serán convertidos.

`CASE_UPPER` (`int`)  
`CASE_UPPER` se utiliza con `array_change_key_case` y sirve para convertir todos los índices de un array en mayúsculas. A partir de PHP 8.2.0, solo los caracteres ASCII serán convertidos.

Constantes de ordenación:

`SORT_ASC` (`int`)  
`SORT_ASC` se utiliza con `array_multisort` para ordenar en orden ascendente.

`SORT_DESC` (`int`)  
`SORT_DESC` se utiliza con `array_multisort` para ordenar en orden descendente.

Otras constantes de ordenación:

`SORT_REGULAR` (`int`)  
`SORT_REGULAR` compara normalmente los valores de una ordenación.

`SORT_NUMERIC` (`int`)  
`SORT_NUMERIC` compara numéricamente los valores de una ordenación.

`SORT_STRING` (`int`)  
`SORT_STRING` compara alfabéticamente los valores de una ordenación.

`SORT_LOCALE_STRING` (`int`)  
`SORT_LOCALE_STRING` se utiliza para comparar alfabéticamente los valores de una ordenación, utilizando la configuración local actual.

`SORT_NATURAL` (`int`)  
`SORT_NATURAL` se utiliza para comparar los elementos como strings, utilizando un "orden natural" como lo hace la función `natsort`.

`SORT_FLAG_CASE` (`int`)  
`SORT_FLAG_CASE` puede ser combinado (con el operador OR a nivel de bits) con `SORT_STRING` o `SORT_NATURAL` para ordenar strings sin tener en cuenta la casilla. A partir de PHP 8.2.0, solo la conversión ASCII en función de la casilla será realizada.

Banderas de filtro:

`ARRAY_FILTER_USE_KEY` (`int`)  
`ARRAY_FILTER_USE_KEY` se utiliza con `array_filter` para pasar cada clave como primer argumento a la función de retrollamada proporcionada.

`ARRAY_FILTER_USE_BOTH` (`int`)  
`ARRAY_FILTER_USE_BOTH` se utiliza con `array_filter` para pasar el valor y la clave a la función de retrollamada proporcionada.

<!-- -->

`COUNT_NORMAL` (`int`)  

`COUNT_RECURSIVE` (`int`)  

`EXTR_OVERWRITE` (`int`)  

`EXTR_SKIP` (`int`)  

`EXTR_PREFIX_SAME` (`int`)  

`EXTR_PREFIX_ALL` (`int`)  

`EXTR_PREFIX_INVALID` (`int`)  

`EXTR_PREFIX_IF_EXISTS` (`int`)  

`EXTR_IF_EXISTS` (`int`)  

`EXTR_REFS` (`int`)
