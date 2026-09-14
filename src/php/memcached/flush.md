---
title: Memcached::flush
description: Invalida todos los elementos del caché
source_url: https://www.php.net/manual/es/memcached.flush.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/flush.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46510
---

Memcached::flush

Invalida todos los elementos del caché

## Descripción

```php
public Memcached::flush([int $delay]): bool
```php

`Memcached::flush` invalida todos los elementos del caché, inmediatamente (por omisión), o después de un retraso de `delay` segundos. Tras una invalidación, ningún elemento será devuelto en respuesta a una orden de lectura (a menos que se almacene nuevamente bajo la misma clave, después de la operación de `Memcached::flush`). Esta operación no libera la memoria ocupada por los elementos existentes: esto se realizará gradualmente, con el almacenamiento de los nuevos elementos.

## Parámetros

`delay`  
El número de segundos de espera antes de la invalidación.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Utilice Memcached::getResultCode si es necesario.

## Ejemplos

Ejemplo con `Memcached::flush`

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

/* invalida todos los elementos en 10 segundos */
$m->flush(10);
?>

    
```php
