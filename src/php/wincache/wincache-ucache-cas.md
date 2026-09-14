---
title: wincache_ucache_cas
description: Compara la variable con el valor antiguo y le asigna un nuevo valor a
  este
source_url: https://www.php.net/manual/es/function.wincache-ucache-cas.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-ucache-cas.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: ed710737e
order: 101710
---

wincache_ucache_cas

Compara la variable con el valor antiguo y le asigna un nuevo valor a este

## Descripción

```php
wincache_ucache_cas(string $key, int $old_value, int $new_value): bool
```php

Compara la variable asociada con la `key` con `old_value` y si coincide entonces asigna el `new_value` a este.

## Parámetros

`key`  
El parámetro `key` que se utiliza para almacenar la variable en la caché. `key` distingue mayúsculas de minúsculas.

`old_value`  
Valor anterior de la variable apuntada por `key` en la memoria caché del usuario. El valor debe ser de tipo `long`, en caso contrario la función devuelve `false`.

`new_value`  
El nuevo valor que se asignará a la variable indicada por la `key` si se encuentra una coincidencia. El valor debe ser de tipo `long`, en caso contrario la función devolverá `false`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Usando `wincache_ucache_cas`

```
<?php
wincache_ucache_set('counter', 2922);
var_dump(wincache_ucache_cas('counter', 2922, 1));
var_dump(wincache_ucache_get('counter'));
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    int(1)

## Véase también

`wincache_ucache_inc`, `wincache_ucache_dec`
