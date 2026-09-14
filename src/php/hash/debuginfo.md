---
title: HashContext::__debugInfo
description: Devuelve información de depuración sobre el contexto de hash
source_url: https://www.php.net/manual/es/hashcontext.debuginfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/hashcontext/debuginfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_revision: ed4d79bee
order: 29390
---

HashContext::\_\_debugInfo

Devuelve información de depuración sobre el contexto de hash

## Descripción

```php
public HashContext::__debugInfo(): array
```php

Este método no está pensado para ser llamado directamente; es invocado por `var_dump` y funciones relacionadas al inspeccionar una instancia de `HashContext`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array asociativo con información de depuración. Contiene una clave `algo` que almacena el nombre del algoritmo de hash en uso por el contexto.

## Ejemplos

Ejemplo de HashContext::\_\_debugInfo

```
<?php
$ctx = hash_init('sha256');
var_dump($ctx);
?>

   
```php

El ejemplo anterior mostrará:

    object(HashContext)#1 (1) {
      ["algo"]=>
      string(6) "sha256"
    }

## Véase también

hash_init

var_dump
