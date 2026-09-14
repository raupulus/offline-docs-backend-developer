---
title: wincache_ucache_dec
description: Disminuye el valor asociado a la clave
source_url: https://www.php.net/manual/es/function.wincache-ucache-dec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-ucache-dec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: ed710737e
order: 101730
---

wincache_ucache_dec

Disminuye el valor asociado a la clave

## Descripción

```php
wincache_ucache_dec(string $key, [int $dec_by], [bool $success]): mixed
```php

Disminuye el valor asociado a la `key` por 1 o como se especifica por `dec_by`.

## Parámetros

`key`  
El parámetro `key` que se utiliza para almacenar la variable en la caché. `key` distingue mayúsculas de minúsculas.

`dec_by`  
El valor de la variable asociada por el que conseguirá que `key` disminuya. Si el argumento es un número de punto flotante se truncará al integer más cercano. La variable asociada con la `key` debe ser de tipo `long`, en caso contrario la función falla y devolverá `false`.

`success`  
Será establecido a `true` en caso de éxito y `false` en caso de error.

## Valores devueltos

Devuelve el valor decrementado en caso de éxito y `false` en caso de error.

## Ejemplos

Usando `wincache_ucache_dec`

```
<?php
wincache_ucache_set('counter', 1);
var_dump(wincache_ucache_dec('counter', 2923, $success));
var_dump($success);
?>

    
```php

El ejemplo anterior mostrará:

    int(2922)
    bool(true)

## Véase también

`wincache_ucache_inc`, `wincache_ucache_cas`
