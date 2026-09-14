---
title: apcu_sma_info
description: Devuelve información sobre la Asignación de Memoria Compartida de APCu
source_url: https://www.php.net/manual/es/function.apcu-sma-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apcu/functions/apcu-sma-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apcu
translation_status: ready
translation_revision: 804d8a054
order: 5090
---

apcu_sma_info

Devuelve información sobre la Asignación de Memoria Compartida de APCu

## Descripción

```php
apcu_sma_info([bool $limited]): array
```php

Devuelve información sobre la Asignación de Memoria Compartida de APCu.

## Parámetros

`limited`  
Cuando el valor `false` es pasado (por omisión) a este argumento, la función `apcu_sma_info` devuelve información detallada sobre cada segmento.

## Valores devueltos

Un array de datos sobre la Asignación de Memoria Compartida; `false` en caso de fallo.

## Ejemplos

Un ejemplo con `apcu_sma_info`

```
<?php
print_r(apcu_sma_info());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [num_seg] => 1
        [seg_size] => 31457280
        [avail_mem] => 31448408
        [block_lists] => Array
            (
                [0] => Array
                    (
                        [0] => Array
                            (
                                [size] => 31448408
                                [offset] => 8864
                            )

                    )

            )

    )

## Véase también

Directivas de configuración de APCu
