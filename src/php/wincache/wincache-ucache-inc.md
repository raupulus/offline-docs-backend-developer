---
title: wincache_ucache_inc
description: Incrementa el valor asociado a la clave
source_url: https://www.php.net/manual/es/function.wincache-ucache-inc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-ucache-inc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: ed710737e
order: 101770
---

wincache_ucache_inc

Incrementa el valor asociado a la clave

## Descripción

```php
wincache_ucache_inc(string $key, [int $inc_by], [bool $success]): mixed
```php

Incrementa el valor asociado a la `key` por 1 o como se especifica por `inc_by`.

## Parámetros

`key`  
La `key` que se utiliza para almacenar la variable en la caché. `key` distingue mayúsculas de minúsculas.

`inc_by`  
El valor por el cual la variable asociada con la `key` será incrementada. Si el argumento es un número de punto flotante se truncará al integer más cercano. La variable asociada con la `key` debe ser de tipo `long`, de lo contrario la función falla y devuelve `false`.

`success`  
Se establecerá en `true` en caso de éxito y `false` en caso de error.

## Valores devueltos

Devuelve el valor incrementado en caso de éxito y `false` en caso de error.

## Ejemplos

Usando `wincache_ucache_inc`

```
<?php
wincache_ucache_set('counter', 1);
var_dump(wincache_ucache_inc('counter', 2921, $success));
var_dump($success);
?>

    
```php

El ejemplo anterior mostrará:

    int(2922)
    bool(true)

## Véase también

`wincache_ucache_dec`, `wincache_ucache_cas`
