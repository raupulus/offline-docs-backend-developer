---
title: ob_get_status
description: Lee el estado del búfer de salida
source_url: https://www.php.net/manual/es/function.ob-get-status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/functions/ob-get-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: false
translation_revision: af7044e82
order: 59830
---

ob_get_status

Lee el estado del búfer de salida

## Descripción

```php
ob_get_status([bool $full_status]): array
```php

`ob_get_status` devuelve información sobre el estado del búfer de salida de alto nivel o de todos los búferes de salida si `full_status` está definido como `true`.

## Parámetros

`full_status`  
`true` para devolver todos los búferes de salida. Si es `false` o no está definido, solo se devolverá el estado del búfer de salida de alto nivel.

## Valores devueltos

Si el parámetro `full_status` está omitido o es igual a `false`, se devuelve un array simple que contiene información sobre el estado del nivel de salida activo.

Si el parámetro `full_status` es igual a `true`, se devuelve un array con un elemento para cada nivel de búfer de salida activo. El nivel de salida se utiliza como clave del array superior y cada elemento del array es a su vez otro array que contiene información sobre un nivel de salida activo.

Se devuelve un array vacío si la memoria intermedia de salida no está activada.

\
**Elementos devueltos por la función `ob_get_status`**\
**Clave:** name\
**Valor:** Nombre del gestor de salida activo (ver los valores de retorno de `ob_list_handlers` para más detalles)\
**Clave:** type\
**Valor:** `0` (gestor interno) o `1` (gestor proporcionado por el usuario)\
**Clave:** flags\
**Valor:** Máscara de bits de los indicadores definidos por la función `ob_start`, el tipo de gestor de salida (ver arriba) y el estado del proceso de memoria intermedia ([ `PHP_OUTPUT_HANDLER_*` ](#outcontrol.constants.flags-returned-by-handler) constantes). Si el gestor ha procesado con éxito el búfer y no ha devuelto `false`, `PHP_OUTPUT_HANDLER_STARTED` y `PHP_OUTPUT_HANDLER_PROCESSED` estarán definidos. Si el gestor ha fallado al procesar el búfer o ha devuelto `false`, `PHP_OUTPUT_HANDLER_STARTED` y `PHP_OUTPUT_HANDLER_DISABLED` estarán definidos.\
**Clave:** level\
**Valor:** Nivel de anidación de la salida (a partir de cero). Tenga en cuenta que el valor devuelto para el mismo nivel por la función `ob_get_level` está desplazado en uno. El primer nivel es `0` para `ob_get_status`, y `1` para `ob_get_level`.\
**Clave:** chunk_size\
**Valor:** Tamaño del fragmento en bytes. Definido por la función `ob_start` o [output_buffering](#ini.output-buffering) si está activado y su valor está definido como un entero positivo\
**Clave:** buffer_size\
**Valor:** Tamaño del búfer de salida en bytes\
**Clave:** buffer_used\
**Valor:** Tamaño de los datos en el búfer de salida en bytes (el mismo que el valor de retorno entero de `ob_get_length`)\

## Ejemplos

Array devuelto cuando el parámetro `full_status` es igual a `true`

    Array
    (
        [type] => 0
        [flags] => 112
        [level] => 2
        [chunk_size] => 0
        [buffer_size] => 16384
        [buffer_used] => 1024
    )

Array devuelto cuando el parámetro `full_status` es igual a `true`

    Array
    (
        [0] => Array
            (
                [name] => default output handler
                [type] => 0
                [flags] => 112
                [level] => 1
                [chunk_size] => 0
                [buffer_size] => 16384
                [buffer_used] => 2048
            )

        [1] => Array
            (
                [name] => URL-Rewriter
                [type] => 0
                [flags] => 112
                [level] => 2
                [chunk_size] => 0
                [buffer_size] => 16384
                [buffer_used] => 1024
            )

    )

## Véase también

`ob_get_level`, `ob_list_handlers`, `ob_get_length`, `ob_start`
