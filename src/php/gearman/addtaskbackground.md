---
title: GearmanClient::addTaskBackground
description: Añade una tarea de fondo para su ejecución en paralelo
source_url: https://www.php.net/manual/es/gearmanclient.addtaskbackground.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/addtaskbackground.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 24920
---

GearmanClient::addTaskBackground

Añade una tarea de fondo para su ejecución en paralelo

## Descripción

```php
public GearmanClient::addTaskBackground(string $function_name, string $workload, [mixed $context], [string $unique_key]): GearmanTask
```php

Añade una tarea de fondo para su ejecución en paralelo con otras tareas. Llámese a este método para todas las tareas que deban ejecutarse en paralelo, y luego, llámese al método GearmanClient::runTasks para realizar las tareas.

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

2 tareas, una de ellas en segundo plano

Este ejemplo muestra la diferencia entre la ejecución en segundo plano y una ejecución normal. El cliente añade 2 tareas que deben ejecutar la misma función, pero una ha sido añadida con el método addTaskBackground. Se define una función de retorno para monitorear el progreso del trabajo. Un agente simple con un retraso artificial reporta el progreso y el cliente lo procesa mediante la función de retorno. Se ejecutan 2 agentes en este ejemplo. Obsérvese que la tarea en segundo plano no es mostrada por el cliente.

```
<?php

## El script del cliente

## Crea un cliente Gearman
$gmc= new GearmanClient();

## Añade un servidor de trabajos por omisión
$gmc->addServer();

## Define 2 funciones de retorno para monitorear el progreso
$gmc->setCompleteCallback("reverse_complete");
$gmc->setStatusCallback("reverse_status");

## Añade una tarea para la función "reverse"
$task= $gmc->addTask("reverse", "Hello World!", null, "1");

## Añade otra tarea, pero esta vez, en segundo plano
$task= $gmc->addTaskBackground("reverse", "!dlroW olleH", null, "2");

if (! $gmc->runTasks())
{
    echo "ERROR " . $gmc->error() . "\n";
    exit;
}

echo "HECHO\n";

function reverse_status($task)
{
    echo "ESTADO : " . $task->unique() . ", " . $task->jobHandle() . " - " . $task->taskNumerator() .
         "/" . $task->taskDenominator() . "\n";
}

function reverse_complete($task)
{
    echo "TERMINADO : " . $task->unique() . ", " . $task->data() . "\n";
}

?>

   
```php

```
<?php

## El script del agente

echo "Inicio\n";

## Crea un agente.
$gmworker= new GearmanWorker();

## Añade un servidor por omisión (localhost).
$gmworker->addServer();

## Registra la función "reverse" en este servidor.
$gmworker->addFunction("reverse", "reverse_fn");

print "Esperando trabajo...\n";
while($gmworker->work())
{
  if ($gmworker->returnCode() != GEARMAN_SUCCESS)
  {
    echo "return_code: " . $gmworker->returnCode() . "\n";
    break;
  }
}

function reverse_fn($job)
{
  echo "Trabajo recibido : " . $job->handle() . "\n";

  $workload = $job->workload();
  $workload_size = $job->workloadSize();

  echo "Carga del agente : $workload ($workload_size)\n";

  # Este ciclo no es necesario, pero ayuda a entender el funcionamiento
  for ($x= 0; $x < $workload_size; $x++)
  {
    echo "Enviando estado : " . ($x + 1) . "/$workload_size complete\n";
    $job->sendStatus($x+1, $workload_size);
    $job->sendData(substr($workload, $x, 1));
    sleep(1);
  }

  $result= strrev($workload);
  echo "Resultado : $result\n";

  # Se devuelve al cliente lo que se desee.
  return $result;
}

?>

   
```php

El agente muestra, para los 2 trabajos :

    Trabajo recibido : H:foo.local:65
    Carga del agente : !dlroW olleH (12)
    1/12 complete
    Trabajo recibido : H:foo.local:66
    Carga del agente : Hello World! (12)
    Enviando estado : 1/12 complete
    Enviando estado : 2/12 complete
    Enviando estado : 2/12 complete
    Enviando estado : 3/12 complete
    Enviando estado : 3/12 complete
    Enviando estado : 4/12 complete
    Enviando estado : 4/12 complete
    Enviando estado : 5/12 complete
    Enviando estado : 5/12 complete
    Enviando estado : 6/12 complete
    Enviando estado : 6/12 complete
    Enviando estado : 7/12 complete
    Enviando estado : 7/12 complete
    Enviando estado : 8/12 complete
    Enviando estado : 8/12 complete
    Enviando estado : 9/12 complete
    Enviando estado : 9/12 complete
    Enviando estado : 10/12 complete
    Enviando estado : 10/12 complete
    Enviando estado : 11/12 complete
    Enviando estado : 11/12 complete
    Enviando estado : 12/12 complete
    Enviando estado : 12/12 complete
    Resultado : !dlroW olleH
    Resultado : Hello World!

       

Salida del cliente :

    ESTADO : 1, H:foo.local:66 - 1/12
    ESTADO : 1, H:foo.local:66 - 2/12
    ESTADO : 1, H:foo.local:66 - 3/12
    ESTADO : 1, H:foo.local:66 - 4/12
    ESTADO : 1, H:foo.local:66 - 5/12
    ESTADO : 1, H:foo.local:66 - 6/12
    ESTADO : 1, H:foo.local:66 - 7/12
    ESTADO : 1, H:foo.local:66 - 8/12
    ESTADO : 1, H:foo.local:66 - 9/12
    ESTADO : 1, H:foo.local:66 - 10/12
    ESTADO : 1, H:foo.local:66 - 11/12
    ESTADO : 1, H:foo.local:66 - 12/12
    TERMINADO : 1, !dlroW olleH
    HECHO

## Véase también

GearmanClient::addTask

GearmanClient::addTaskHigh

GearmanClient::addTaskLow

GearmanClient::addTaskHighBackground

GearmanClient::addTaskLowBackground

GearmanClient::runTasks
