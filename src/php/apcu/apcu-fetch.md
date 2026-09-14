---
title: apcu_fetch
description: Recupera una variable almacenada en la caché
source_url: https://www.php.net/manual/es/function.apcu-fetch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apcu/functions/apcu-fetch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apcu
translation_status: ready
translation_revision: 804d8a054
order: 5060
---

apcu_fetch

Recupera una variable almacenada en la caché

## Descripción

```php
apcu_fetch(mixed $key, [bool $success]): mixed
```php

Recupera una entrada de la caché.

## Parámetros

`key`  
La clave `key` utilizada para almacenar el valor (con `apcu_store`). Si se pasa un array, entonces cada elemento es recuperado y devuelto.

`success`  
Definido como `true` en caso de éxito y `false` en caso de fallo.

## Valores devueltos

La variable o el array de variables almacenado en caso de éxito; `false` en caso de fallo.

## Historial de cambios

| Versión          | Descripción                             |
|------------------|-----------------------------------------|
| PECL apcu 3.0.17 | El parámetro `success` ha sido añadido. |

## Ejemplos

Un ejemplo con `apcu_fetch`

```
<?php
$bar = 'BAR';
apcu_store('foo', $bar);
var_dump(apcu_fetch('foo'));
?>

   
```php

El ejemplo anterior mostrará:

    string(3) "BAR"

## Véase también

apcu_store

apcu_delete

APCUIterator
