---
title: zend_thread_id
description: Devuelve un identificador único del hilo actual
source_url: https://www.php.net/manual/es/function.zend-thread-id.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/zend-thread-id.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: false
translation_revision: 8dd14a886
order: 39250
---

zend_thread_id

Devuelve un identificador único del hilo actual

## Descripción

```php
zend_thread_id(): int
```php

Esta función devuelve un identificador único para el hilo actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el identificador del hilo, en forma de `int`.

## Ejemplos

Ejemplo con `zend_thread_id`

```
<?php
$thread_id = zend_thread_id();

echo 'ID del hilo actual : ' . $thread_id;
?>

    
```php

Resultado del ejemplo anterior es similar a:

    ID del hilo actual : 7864

## Notas

> [!NOTE]
> Esta función solo está disponible si PHP ha sido compilado con soporte ZTS (`Zend Thread Safety`) y el modo de depuración (`--enable-debug`).
