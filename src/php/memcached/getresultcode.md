---
title: Memcached::getResultCode
description: Devuelve el código de resultado de la última operación
source_url: https://www.php.net/manual/es/memcached.getresultcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/getresultcode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 976425d4f
order: 46600
---

Memcached::getResultCode

Devuelve el código de resultado de la última operación

## Descripción

```php
public Memcached::getResultCode(): int
```php

`Memcached::getResultCode` devuelve una de las constantes `Memcached::RES_*` que indica el estado del resultado de la última operación.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El código de resultado de la última operación Memcached.

## Ejemplos

Ejemplo con `Memcached::getResultCode`

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

$m->add('foo', 'bar');
if ($m->getResultCode() == Memcached::RES_NOTSTORED) {
    /* ... */
}
?>

    
```php
