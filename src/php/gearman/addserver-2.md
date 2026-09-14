---
title: GearmanWorker::addServer
description: Añade un servidor de trabajos
source_url: https://www.php.net/manual/es/gearmanworker.addserver.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanworker/addserver.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25780
---

GearmanWorker::addServer

Añade un servidor de trabajos

## Descripción

```php
public GearmanWorker::addServer([string $host], [int $port], [bool $setupExceptionHandler]): bool
```php

Añade un servidor de trabajos a este agente. Será añadido a una lista de servidores a utilizar para ejecutar los trabajos. No se realiza ninguna operación de I/O de socket aquí.

## Parámetros

`host`  
El nombre de host del servidor de trabajos.

`port`  
El puerto del servidor de trabajos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Añadir servidores Gearman

```
<?php
$worker= new GearmanWorker();
$worker->addServer("10.0.0.1");
$worker->addServer("10.0.0.2", 7003);
?>

   
```php

## Véase también

GearmanWorker::addServers
