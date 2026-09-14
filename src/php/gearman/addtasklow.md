---
title: GearmanClient::addTaskLow
description: Añade una tarea de baja prioridad para ser ejecutada en paralelo
source_url: https://www.php.net/manual/es/gearmanclient.addtasklow.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/addtasklow.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 24950
---

GearmanClient::addTaskLow

Añade una tarea de baja prioridad para ser ejecutada en paralelo

## Descripción

```php
public GearmanClient::addTaskLow(string $function_name, string $workload, [mixed $context], [string $unique_key]): GearmanTask
```php

Añade una tarea de baja prioridad para ser ejecutada en paralelo con otras tareas. Esta método debe ser llamado para que todas las tareas se ejecuten simultáneamente, luego debe llamarse a GearmanClient::runTasks para realizar el trabajo. Las tareas con baja prioridad serán seleccionadas de la cola después de las de mayor prioridad.

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

Una tarea de baja prioridad junto con dos tareas normales

Se añade una tarea de baja prioridad junto con otras dos tareas. Solo hay un agente disponible, por lo que las tareas se ejecutan una tras otra, con la de baja prioridad al final.

```
<?php

## crea el cliente Gearman
$gmc= new GearmanClient();

## añade el servidor por defecto
$gmc->addServer();

## establece la devolución de llamada cuando la tarea está completada
$gmc->setCompleteCallback("inverse_complete");

## añade tareas, una de ellas con baja prioridad
$task= $gmc->addTask("inverse", "¡Hola mundo!", null, "1");
$task= $gmc->addTaskLow("inverse", "!ednom el ruojnoB", null, "2");
$task= $gmc->addTask("inverse", "¡Hola mundo!", null, "3");

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

    Completada : 3, !ednom el ruojnoB
    Completada : 1, !ednom el ruojnoB
    Completada : 2, ¡Hola mundo!
    Hecho

## Véase también

GearmanClient::addTask

GearmanClient::addTaskHigh

GearmanClient::addTaskBackground

GearmanClient::addTaskHighBackground

GearmanClient::addTaskLowBackground

GearmanClient::runTasks
