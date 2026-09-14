---
title: GearmanClient::addServer
description: Añade un servidor de tareas al cliente
source_url: https://www.php.net/manual/es/gearmanclient.addserver.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/addserver.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 24890
---

GearmanClient::addServer

Añade un servidor de tareas al cliente

## Descripción

```php
public GearmanClient::addServer([string $host], [int $port], [bool $setupExceptionHandler]): bool
```php

Añade un servidor de tareas a una lista de servidores que pueden ser utilizados para realizar una tarea. No se realiza ninguna entrada/salida en un socket aquí; el servidor es simplemente añadido a la lista.

## Parámetros

`host`  
El nombre de host del servidor de trabajos.

`port`  
El puerto del servidor de trabajos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Añadir dos servidores

```
<?php

## Crea nuestro objeto cliente.
$gmclient= new GearmanClient();

## Añade dos servidores de tareas, el primero escuchando en el puerto por omisión, 4730
$gmclient->addServer("10.0.0.1");
$gmclient->addServer("10.0.0.2", 7003);

?>

   
```php

## Véase también

GearmanClient::addServers
