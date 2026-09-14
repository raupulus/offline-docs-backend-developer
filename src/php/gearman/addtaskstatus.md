---
title: GearmanClient::addTaskStatus
description: Añade una tarea para obtener el estado
source_url: https://www.php.net/manual/es/gearmanclient.addtaskstatus.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/addtaskstatus.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 24970
---

GearmanClient::addTaskStatus

Añade una tarea para obtener el estado

## Descripción

```php
public GearmanClient::addTaskStatus(string $job_handle, [mixed $context]): GearmanTask
```php

Utilizado para solicitar el estado al servidor Gearman, que llamará al retorno de estado especificado (mediante GearmanClient::setStatusCallback).

## Parámetros

`job_handle`  
El descriptor para la tarea cuyo estado se desea obtener

`context`  
Los datos a pasar al retorno de estado, generalmente una referencia a un array o a un objeto

## Valores devueltos

Un objeto `GearmanTask` o `false` en caso de error.

## Ejemplos

Supervisar la finalización de múltiples tareas en segundo plano

Un retraso artificial se introduce en el agente de este ejemplo para simular un proceso largo. Solo se lanza un agente en este ejemplo.

```
<?php

/* crea nuestro objeto */
$gmclient= new GearmanClient();

/* añade el servidor por omisión */
$gmclient->addServer();

/* lanza una tarea en segundo plano y guarda los descriptores */
$handles = array();
$handles[0] = $gmclient->doBackground("inverse", "¡Hola mundo!");
$handles[1] = $gmclient->doBackground("inverse", "!ednom el ruojnoB");

$gmclient->setStatusCallback("inverse_estado");

/* Consulta al servidor para ver cuándo las tareas en segundo plano terminan; */
/* un método mejor consiste en llamar a los retornos de evento */
do
{
   /* Utiliza la variable de contexto para saber cuántas tareas se han completado */
   $done = 0;
   $gmclient->addTaskStatus($handles[0], $done);
   $gmclient->addTaskStatus($handles[1], $done);
   $gmclient->runTasks();
   echo "Completado: $done\n";
   sleep(1);
}
while ($done != 2);

function inverse_estado($task, $done)
{
   if (!$task->isKnown())
      $done++;
}

?>

   
```php

Resultado del ejemplo anterior es similar a:

    Completado: 0
    Completado: 0
    Completado: 0
    Completado: 0
    Completado: 0
    Completado: 0
    Completado: 0
    Completado: 0
    Completado: 0
    Completado: 0
    Completado: 0
    Completado: 0
    Completado: 1
    Completado: 1
    Completado: 1
    Completado: 1
    Completado: 1
    Completado: 1
    Completado: 1
    Completado: 1
    Completado: 1
    Completado: 1
    Completado: 1
    Completado: 1
    Completado: 2

## Véase también

GearmanClient::setStatusCallback
