---
title: GearmanClient::addTaskHigh
description: Añade una tarea de alta prioridad para ser ejecutada en paralelo
source_url: https://www.php.net/manual/es/gearmanclient.addtaskhigh.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/addtaskhigh.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 24930
---

GearmanClient::addTaskHigh

Añade una tarea de alta prioridad para ser ejecutada en paralelo

## Descripción

```php
public GearmanClient::addTaskHigh(string $function_name, string $workload, [mixed $context], [string $unique_key]): GearmanTask
```php

Añade una tarea de alta prioridad para ser ejecutada en paralelo con otras tareas. Esta método debe ser llamado para que todas las tareas se ejecuten simultáneamente, luego GearmanClient::runTasks debe ser llamado para realizar el trabajo. Las tareas con alta prioridad serán seleccionadas de la cola antes que las de prioridad más baja.

## Parámetros

`function_name`  
Una función registrada que el trabajador va a ejecutar

`workload`  
Datos serializados a analizar

`context`  
Contexto de la aplicación a asociar con una tarea

`unique_key`  
Un identificador único utilizado para identificar una tarea particular

## Valores devueltos

Un objeto `GearmanTask` o `false` si la tarea no puede ser añadida.

## Ejemplos

Una tarea de alta prioridad junto con dos tareas normales

Se añade una tarea de alta prioridad junto con otras dos tareas. Un solo agente está disponible, de forma que las tareas se ejecutan una a una, con la de alta prioridad en primer lugar.

```
<?php

## crea el cliente Gearman
$gmc= new GearmanClient();

## añade el servidor por defecto
$gmc->addServer();

## establece el retorno cuando la tarea está completada
$gmc->setCompleteCallback("inverse_complete");

## añade tareas, una de ellas con alta prioridad
$task= $gmc->addTask("inverse", "Bonjour le monde!", null, "1");
$task= $gmc->addTaskHigh("inverse", "!ednom el ruojnoB", null, "2");
$task= $gmc->addTask("inverse", "Bonjour le monde!", null, "3");

if (! $gmc->runTasks())
{
    echo "ERROR " . $gmc->error() . "\n";
    exit;
}
echo "Hecho\n";

function inverse_complete($task)
{
    echo "Completada : " . $task->unique() . ", " . $task->data() . "\n";
}

?>

   
```php

Resultado del ejemplo anterior es similar a:

    Completada : 2, Bonjour le monde!
    Completada : 3, !ednom el ruojnoB
    Completada : 1, !ednom el ruojnoB
    Hecho

## Véase también

GearmanClient::addTask

GearmanClient::addTaskLow

GearmanClient::addTaskBackground

GearmanClient::addTaskHighBackground

GearmanClient::addTaskLowBackground

GearmanClient::runTasks
