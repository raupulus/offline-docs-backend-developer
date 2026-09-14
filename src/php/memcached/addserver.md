---
title: Memcached::addServer
description: Añade un servidor al grupo
source_url: https://www.php.net/manual/es/memcached.addserver.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/addserver.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46360
---

Memcached::addServer

Añade un servidor al grupo

## Descripción

```php
public Memcached::addServer(string $host, int $port, [int $weight]): bool
```php

`Memcached::addServer` añade el servidor indicado al grupo de servidores. No se establece ninguna conexión en ese momento, pero si se utiliza la clave de distribución por hash consistente (a través de `Memcached::DISTRIBUTION_CONSISTENT` o `Memcached::OPT_LIBKETAMA_COMPATIBLE`), ciertas estructuras internas van a ser actualizadas. Por lo tanto, si es necesario añadir varios servidores, se recomienda utilizar Memcached::addServers para que la actualización ocurra una sola vez.

El mismo servidor puede aparecer varias veces en el grupo, ya que no se realiza ninguna búsqueda de duplicados. Esto no es recomendado: en su lugar, utilice el argumento `weight` para aumentar el peso de un servidor en la selección.

## Parámetros

`host`  
El nombre de host del servidor memcache. Si el nombre de host no es válido, las operaciones sobre los datos van a definir el código de resultado `Memcached::RES_HOST_LOOKUP_FAILURE`. Desde la versión 2.0.0b1, este argumento también puede especificar la ruta hacia un socket Unix, por ejemplo; `/ruta/hacia/memcached.sock` para utilizar el socket de dominio Unix, y en este caso, el argumento `port` también debe ser definido a `0`.

`port`  
El puerto en el que memcache funciona. Generalmente, es `11211`. Desde la versión 2.0.0b1, defina este argumento a `0` cuando se utilicen sockets de dominio Unix.

`weight`  
El peso del servidor relativamente al peso total de todos los servidores. Esto controla la probabilidad de que un servidor sea seleccionado durante las operaciones. Esta opción solo se utiliza con la distribución consistente, y generalmente, esto corresponde al total de memoria disponible en este servidor.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcached::addServer`

```
<?php
$m = new Memcached();

/* Añade dos servidores, y el segundo es dos veces
   más solicitado que el primero */
$m->addServer('mem1.domain.com', 11211, 33);
$m->addServer('mem2.domain.com', 11211, 67);
?>

    
```php

## Véase también

Memcached::addServers, Memcached::resetServerList
