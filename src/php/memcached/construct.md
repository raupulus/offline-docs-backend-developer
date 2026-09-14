---
title: Memcached::__construct
description: Crea un objeto Memcached
source_url: https://www.php.net/manual/es/memcached.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: c49d175bb
order: 46420
---

Memcached::\_\_construct

Crea un objeto Memcached

## Descripción

```php
public Memcached::__construct([string $persistent_id], [callable $callback], [string $connection_str])
```php

Crea un objeto Memcached que representa la conexión al servidor memcache.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`persistent_id`  
Por omisión, las instancias Memcached son destruidas al final de la petición. Para crear un objeto que persiste entre las peticiones, utilice el argumento `persistent_id` para especificar un identificador único para la instancia. Todos los objetos creados con el mismo identificador `persistent_id` compartirán la misma conexión.

`callback`  
```php
callback(Memcached $memcached, string $persistent_id): void
```

El parámetro `callback` es llamado cuando se establece la conexión. Debe ser un `callable` PHP válido que reciba el objeto `Memcached` como su primer parámetro, y `persistent_id` como el segundo.

`connection_str`  
Este parámetro se utiliza para pasar opciones de conexión adicionales a los servidores memcache, como el peso de un servidor en un clúster.

## Ejemplos

Creación de un objeto Memcached

```php
<?php
/* Creación de un objeto clásico */
$m = new Memcached();
echo get_class($m);

/* Creación de un objeto persistente */
$m2 = new Memcached('story_pool');
$m3 = new Memcached('story_pool');

/* Ahora $m2 y $m3 comparten la misma conexión */
?>

    
```
