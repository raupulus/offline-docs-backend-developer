---
title: GearmanWorker::addServers
description: Añade múltiples servidores de trabajos
source_url: https://www.php.net/manual/es/gearmanworker.addservers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanworker/addservers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25790
---

GearmanWorker::addServers

Añade múltiples servidores de trabajos

## Descripción

```php
public GearmanWorker::addServers([string $servers], [bool $setupExceptionHandler]): bool
```php

Añade uno o múltiples servidores de trabajos al agente. Serán añadidos a una lista de servidores que podrán ser utilizados para ejecutar trabajos. No se realiza ninguna operación de I/O de socket aquí.

## Parámetros

`servers`  
Una lista de servidores de trabajos separados por comas, en formato host:port. Si el puerto no se especifica, se utilizará el valor por omisión 4730.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Añadir 2 servidores de trabajos

```
<?php

$worker= new GearmanWorker();
$worker->addServers("10.0.0.1,10.0.0.2:7003");

?>

   
```php

## Véase también

GearmanWorker::addServer
