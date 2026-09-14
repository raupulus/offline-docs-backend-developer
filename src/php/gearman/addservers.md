---
title: GearmanClient::addServers
description: Añade una lista de servidores de tareas al cliente
source_url: https://www.php.net/manual/es/gearmanclient.addservers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/addservers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 24900
---

GearmanClient::addServers

Añade una lista de servidores de tareas al cliente

## Descripción

```php
public GearmanClient::addServers([string $servers], [bool $setupExceptionHandler]): bool
```php

Añade una lista de servidores de tareas que pueden ser utilizados para realizar una tarea. No se realiza ninguna entrada/salida en un socket aquí; los servidores son simplemente añadidos a la lista completa de servidores.

## Parámetros

`servers`  
Una lista de servidores, separados por comas, cada uno especificado según el formato '`host:port`'.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Añadir dos servidores

```
<?php

## Crea nuestro objeto cliente.
$gmclient= new GearmanClient();

## Añade varios servidores de tareas, el primero escuchando en el puerto por defecto, 4730
$gmclient->addServers("10.0.0.1,10.0.0.2:7003");

?>

   
```php

## Véase también

GearmanClient::addServer
