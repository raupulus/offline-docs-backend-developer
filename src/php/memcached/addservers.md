---
title: Memcached::addServers
description: Añade múltiples servidores al grupo
source_url: https://www.php.net/manual/es/memcached.addservers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/addservers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46370
---

Memcached::addServers

Añade múltiples servidores al grupo

## Descripción

```php
public Memcached::addServers(array $servers): bool
```php

`Memcached::addServers` añade los servidores `servers` al grupo de servidores. Cada entrada en `servers` debe ser un array, conteniendo el nombre de host, y opcionalmente su peso. No se establece ninguna conexión con el servidor en este momento.

El mismo servidor puede aparecer múltiples veces en el grupo, ya que no se realiza ninguna verificación de duplicación. Esto no es recomendado. En su lugar, es preferible utilizar el argumento `weight` para aumentar el peso del servidor.

## Parámetros

`array`  
Un array de servidores a añadir.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcached::addServers`

```
<?php
$m = new Memcached();

$servers = array(
    array('mem1.domain.com', 11211, 33),
    array('mem2.domain.com', 11211, 67)
);
$m->addServers($servers);
?>

    
```php

## Véase también

Memcached::addServer, Memcached::resetServerList
