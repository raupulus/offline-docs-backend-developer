---
title: apcu_delete
description: Elimina una variable almacenada en caché
source_url: https://www.php.net/manual/es/function.apcu-delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apcu/functions/apcu-delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apcu
translation_status: ready
translation_reviewed: false
translation_revision: 804d8a054
order: 5020
---

apcu_delete

Elimina una variable almacenada en caché

## Descripción

```php
apcu_delete(mixed $key): mixed
```php

Elimina una variable almacenada en caché.

## Parámetros

`key`  
Una clave (`key`) empleada para almacenar el valor como un `string` para una única clave, o como un `array` de strings para varias claves, o como un `object` `APCUIterator`.

## Valores devueltos

Si `key` es una `array`, se devuelve una `array` indexada de las claves. De lo contrario, se devuelve `true` en caso de éxito, o `false` en caso de fallo.

## Ejemplos

Un ejemplo de`apcu_delete`

```
<?php
$bar = 'BAR';
apcu_store('foo', $bar);
apcu_delete('foo');
// obviamente, esto no es útil de esta forma

// Alternativamente, borrar varias claves.
apcu_delete(['foo', 'bar', 'baz']);

// O utilizar un Iterator con una expresión regular.
apcu_delete(new APCUIterator('#^myprefix_#'));
?>

   
```php

## Véase también

apcu_store

apcu_fetch

apcu_clear_cache

APCUIterator
