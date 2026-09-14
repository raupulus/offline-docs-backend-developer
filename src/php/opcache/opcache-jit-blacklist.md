---
title: opcache_jit_blacklist
description: Excluye una función de la compilación JIT
source_url: https://www.php.net/manual/es/function.opcache-jit-blacklist.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/opcache/functions/opcache-jit-blacklist.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: opcache
translation_status: ready
translation_revision: 3c36a56c9
order: 58630
---

opcache_jit_blacklist

Excluye una función de la compilación JIT

## Descripción

```php
opcache_jit_blacklist(Closure $closure): void
```php

Esta función excluye una función particular de la compilación JIT cuando se utiliza Tracing JIT. La función se especifica usando una `Closure`.

> [!WARNING]
> Las partes de la función que ya fueron compiladas por JIT no se ven afectadas y seguirán siendo compiladas por JIT.

## Parámetros

`closure`  
La función a excluir, representada como un callable de primera clase. También es posible pasar una función anónima, en cuyo caso la propia función anónima será excluida.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo básico de `opcache_jit_blacklist`

```
<?php
function foo() {
    $x = 1;
    $x += 0;
    ++$x;
    var_dump($x);
}
opcache_jit_blacklist(foo(...));
foo();
?>

   
```php

## Véase también

opcache_invalidate

opcache_reset
