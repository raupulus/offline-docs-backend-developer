---
title: wincache_ucache_clear
description: Elimina todo el contenido de la caché del usuario
source_url: https://www.php.net/manual/es/function.wincache-ucache-clear.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-ucache-clear.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: 709e2ce20
order: 101720
---

wincache_ucache_clear

Elimina todo el contenido de la caché del usuario

## Descripción

```php
wincache_ucache_clear(): bool
```php

Borra o elimina todos los valores almacenados en la caché del usuario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Usando `wincache_ucache_clear`

```
<?php
wincache_ucache_set('green', 1);
wincache_ucache_set('red', 2);
wincache_ucache_set('orange', 4);
wincache_ucache_set('blue', 8);
wincache_ucache_set('cyan', 16);
$array1 = array('green', 'red', 'orange', 'blue', 'cyan');
var_dump(wincache_ucache_get($array1));
var_dump(wincache_ucache_clear());
var_dump(wincache_ucache_get($array1));
?>

    
```php

El ejemplo anterior mostrará:

    array(5) { ["green"]=> int(1)
               ["red"]=> int(2)
               ["orange"]=> int(4)
               ["blue"]=> int(8)
               ["cyan"]=> int(16) }
    bool(true)
    bool(false)

## Véase también

`wincache_ucache_set`, `wincache_ucache_add`, `wincache_ucache_delete`, `wincache_ucache_get`, `wincache_ucache_exists`, `wincache_ucache_meminfo`, `wincache_ucache_info`
