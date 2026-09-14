---
title: GearmanWorker::addFunction
description: Registra y añade una función de retrollamada
source_url: https://www.php.net/manual/es/gearmanworker.addfunction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanworker/addfunction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25760
---

GearmanWorker::addFunction

Registra y añade una función de retrollamada

## Descripción

```php
public GearmanWorker::addFunction(string $function_name, callable $function, [mixed $context], [int $timeout]): bool
```php

Registra una función de retrollamada con el servidor de trabajos y especifica una retrollamada correspondiente a esta función. Opcionalmente, fija datos de contexto de la aplicación a utilizar cuando la función de retrollamada es llamada, así como un tiempo límite de ejecución.

## Parámetros

`function_name`  
El nombre de la función a registrar con el servidor de trabajos

`function`  
Una función de retrollamada a llamar cuando un trabajo es enviado

`context`  
Una referencia a datos de contexto de la aplicación que pueden ser modificados por la función del agente.

`timeout`  
Un intervalo de tiempo, en segundos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Agente simple que utiliza datos de contexto de la aplicación

```
<?php

## Crea un agente Gearman
$worker= new GearmanWorker();

## Añade el servidor por omisión (localhost)
$worker->addServer();

## Define una variable que contiene los datos de la aplicación
$count= 0;

## Añade la función "reverse"
$worker->addFunction("reverse", "reverse_cb", $count);

## Inicia el agente
while ($worker->work());

function reverse_cb($job, &$count)
{
  $count++;
  return "$count: " . strrev($job->workload());
}

?>

   
```php

La ejecución de un cliente que envía 2 trabajos para la función reverse mostrará algo como:

    1: olleh
    2: dlrow

## Véase también

GearmanClient::do
