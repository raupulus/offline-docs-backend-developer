---
title: wincache_ucache_info
description: Recupera información sobre los datos almacenados en la caché del usuario
source_url: https://www.php.net/manual/es/function.wincache-ucache-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-ucache-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: b95d28e6e
order: 101780
---

wincache_ucache_info

Recupera información sobre los datos almacenados en la caché del usuario

## Descripción

```php
wincache_ucache_info([bool $summaryonly], [string $key]): array
```php

Recupera información sobre los datos almacenados en la caché del usuario.

## Parámetros

`summaryonly`  
Controla si el array devuelto contiene información sobre las entradas de caché individuales junto con el resumen caché del usuario.

`key`  
La clave de una entrada en la caché del usuario. Si se especifica a continuación, el array devuelto contendrá información sólo acerca de que la entrada de caché. Si no se especifica y `summaryonly` es establecido a `false` entonces el array devuelto contendrá información sobre todas las entradas en la caché.

## Valores devueltos

Array de metadatos sobre caché de usuario o `false` si ocurre un error

El array devuelto por esta función contiene los siguientes elementos:

- `total_cache_uptime` - tiempo total en segundos que el caché de usuario ha sido activo
- `total_item_count` - número total de elementos que están actualmente en la caché del usuario
- `is_local_cache` - true si el caché es de metadatos para una instancia de caché local, false si los metadatos es para el la caché global
- `total_hit_count` - número de veces que los datos se han servido de la memoria caché
- `total_miss_count` - número de veces que los datos no se han encontrado en la caché
- `ucache_entries` - un array que contiene la información sobre todos los elementos almacenados en caché:
  - `key_name` - nombre de la clave que se utiliza para almacenar los datos
  - `value_type` - tipo de valor almacenado por la clave
  - `use_time` - tiempo en segundos desde el fichero ha sido visitado en la caché de código de operación
  - `last_check` - tiempo en segundos desde el fichero ha sido chequeado para modificaciones
  - `is_session` - indica si los datos son una variable de sesión
  - `ttl_seconds` - el tiempo restante de los datos a vivir en la memoria caché, 0 significa infinito
  - `age_seconds` - tiempo transcurrido desde el momento que los datos han sido añadidos en la caché
  - `hitcount` - número de veces que los datos se han servido de la memoria caché

## Ejemplos

Usar `wincache_ucache_info`

```
<?php
wincache_ucache_get('green');
wincache_ucache_set('green', 2922);
wincache_ucache_get('green');
wincache_ucache_get('green');
wincache_ucache_get('green');
print_r(wincache_ucache_info());
?>

    
```php

El ejemplo anterior mostrará:

    Array
    ( ["total_cache_uptime"] => int(0)
      ["is_local_cache"] => bool(false)
      ["total_item_count"] => int(1)
      ["total_hit_count"] => int(3)
      ["total_miss_count"] => int(1)
      ["ucache_entries"] => Array(1)
        ( [1] => Array(6)
          (
            ["key_name"] => string(5) "green"
            ["value_type"] => string(4) "long"
            ["is_session"] => int(0)
            ["ttl_seconds"] => int(0)
            ["age_seconds"] => int(0)
            ["hitcount"] => int(3)
           )
        )
    )

## Véase también

`wincache_fcache_meminfo`, `wincache_ocache_fileinfo`, `wincache_ocache_meminfo`, `wincache_rplist_meminfo`, `wincache_rplist_fileinfo`, `wincache_refresh_if_changed`, `wincache_ucache_meminfo`, `wincache_scache_info`, `wincache_scache_meminfo`
