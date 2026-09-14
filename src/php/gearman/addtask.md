---
title: GearmanClient::addTask
description: Añade una tarea para ser ejecutada en paralelo
source_url: https://www.php.net/manual/es/gearmanclient.addtask.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/addtask.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 24910
---

GearmanClient::addTask

Añade una tarea para ser ejecutada en paralelo

## Descripción

```php
public GearmanClient::addTask(string $function_name, string $workload, [mixed $context], [string $unique_key]): GearmanTask
```php

Añade una tarea para ser ejecutada en paralelo con otras tareas. Esta método debe ser llamado para todas las tareas a ejecutar en paralelo, y posteriormente, debe llamarse al método GearmanClient::runTasks para ejecutar las tareas. Tenga en cuenta que es necesario contar con suficientes agentes disponibles para ejecutar en paralelo todas las tareas.

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

Un objeto `GearmanTask` o `false` si la tarea no pudo ser añadida.

## Ejemplos

Añadir 2 tareas

```
<?php

## Crea un cliente gearman
$gmclient= new GearmanClient();

## Añade el servidor de trabajos por defecto
$gmclient->addServer();

## Define una función a llamar cuando el trabajo está completo
$gmclient->setCompleteCallback("complete");

## Añade una tarea que ejecuta la función "reverse" sobre la cadena "Hello World!"
$gmclient->addTask("reverse", "Hello World!", null, "1");

## Añade otra tarea que ejecuta la función "reverse" sobre la cadena "!dlroW olleH"
$gmclient->addTask("reverse", "!dlroW olleH", null, "2");

## Ejecuta las tareas
$gmclient->runTasks();

function complete($task)
{
  print "Completado : " . $task->unique() . ", " . $task->data() . "\n";
}

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Completado : 2, Hello World!
    Completado : 1, !dlroW olleH

Añadir 2 tareas pasando el contexto de la aplicación

```
<?php

$client = new GearmanClient();
$client->addServer();

## Define una función a llamar cuando el trabajo está completo
$client->setCompleteCallback("reverse_complete");

## Añade algunas tareas que contienen un marcador en el lugar donde debe colocarse el resultado
$results = array();
$client->addTask("reverse", "Hello World!", $results, "t1");
$client->addTask("reverse", "!dlroW olleH", $results, "t2");

$client->runTasks();

## El resultado debe estar ahora contenido en las funciones de devolución de llamada
foreach ($results as $id => $result)
   echo $id . ": " . $result['handle'] . ", " . $result['data'] . "\n";

function reverse_complete($task, $results)
{
   $results[$task->unique()] = array("handle"=>$task->jobHandle(), "data"=>$task->data());
}

?>

    
```php

Resultado del ejemplo anterior es similar a:

    t2: H.foo:21, Hello World!
    t1: H:foo:22, !dlroW olleH

## Véase también

GearmanClient::addTaskHigh

GearmanClient::addTaskLow

GearmanClient::addTaskBackground

GearmanClient::addTaskHighBackground

GearmanClient::addTaskLowBackground

GearmanClient::runTasks
