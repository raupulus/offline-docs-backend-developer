---
title: wincache_ucache_exists
description: Comprueba si una variable existe en la caché del usuario
source_url: https://www.php.net/manual/es/function.wincache-ucache-exists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-ucache-exists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: ed710737e
order: 101750
---

wincache_ucache_exists

Comprueba si una variable existe en la caché del usuario

## Descripción

```php
wincache_ucache_exists(string $key): bool
```php

Comprueba si una variable con la `key` existe en la caché de usuario o no.

## Parámetros

`key`  
La `key` que se utiliza para almacenar la variable en la caché. `key` distingue mayúsculas de minúsculas.

## Valores devueltos

Devuelve `true` si la variable con la `key` existe, en caso contrario devuelve `false`.

## Ejemplos

Usando `wincache_ucache_exists`

```
<?php
if (!wincache_ucache_exists('green'))
    wincache_ucache_set('green', 1);
var_dump(wincache_ucache_exists('green'));
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)

## Véase también

`wincache_ucache_set`, `wincache_ucache_add`, `wincache_ucache_get`, `wincache_ucache_clear`, `wincache_ucache_delete`, `wincache_ucache_meminfo`, `wincache_ucache_info`
