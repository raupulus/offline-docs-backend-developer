---
title: apcu_cache_info
description: Recupera la información almacenada en la memoria APCu
source_url: https://www.php.net/manual/es/function.apcu-cache-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apcu/functions/apcu-cache-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apcu
translation_status: ready
translation_revision: 184764a63
order: 4980
---

apcu_cache_info

Recupera la información almacenada en la memoria APCu

## Descripción

```php
apcu_cache_info([bool $limited]): array
```php

Recupera la información almacenada y los metadatos del almacén de datos de la APCu.

## Parámetros

`limited`  
Si el parámetro `limited` es `true`, el valor devuelto excluirá la lista individual de entradas de la memoria caché. Esto es útil cuando se intentan optimizar las llamadas para la recopilación de estadísticas.

## Valores devueltos

Array de datos en caché (y metadatos) o `false` si ocurre un error

> [!NOTE]
> `apcu_cache_info` hará una advertencia si no puede recuperar los datos de la caché del APCu. Esto suele ocurrir cuando el APCu no está activado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL apcu 3.0.11 | El parámetro `limited` fué introducido. |
| PECL apcu 3.0.16 | La opción "`filehits`" para el parámetro `cache_type` fué introducido. |

## Ejemplos

Un ejemplo de `apcu_cache_info`

```
<?php
print_r(apcu_cache_info());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [num_slots] => 2000
        [ttl] => 0
        [num_hits] => 9
        [num_misses] => 3
        [start_time] => 1123958803
        [cache_list] => Array
            (
                [0] => Array
                    (
                        [filename] => /path/to/apcu_test.php
                        [device] => 29954
                        [inode] => 1130511
                        [type] => file
                        [num_hits] => 1
                        [mtime] => 1123960686
                        [creation_time] => 1123960696
                        [deletion_time] => 0
                        [access_time] => 1123962864
                        [ref_count] => 1
                        [mem_size] => 677
                    )
                [1] => Array (...iterates for each cached file)
    )

## Véase también

APCu configuration directives

APCUIterator::getTotalSize

APCUIterator::getTotalHits

APCUIterator::getTotalCount
