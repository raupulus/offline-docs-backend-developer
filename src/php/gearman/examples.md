---
title: Ejemplos
source_url: https://www.php.net/manual/es/gearman.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 24870
---

## Ejemplos

## Uso básico

Cliente y trabajador básicos en Gearman

Este ejemplo muestra un cliente y un trabajador muy sencillo. El cliente envía un string al servidor de trabajos, y el trabajador da la vuelta al string y lo envía de vuelta. El trabajo se realiza de forma síncrona.

```php
<?php

## Se crea el objeto cliente
$gmclient= new GearmanClient();

## Se añade el servidor por defecto (localhost).
$gmclient->addServer();

echo "Sending job\n";

## Enviamos trabajo "reverse"
do
{
  $result = $gmclient->do("reverse", "Hello!");

  # Comprobación de varios paquetes de retorno y errores
  switch($gmclient->returnCode())
  {
    case GEARMAN_WORK_DATA:
      echo "Data: $result\n";
      break;
    case GEARMAN_WORK_STATUS:
      list($numerator, $denominator)= $gmclient->doStatus();
      echo "Status: $numerator/$denominator complete\n";
      break;
    case GEARMAN_WORK_FAIL:
      echo "Failed\n";
      exit;
    case GEARMAN_SUCCESS:
      break;
    default:
      echo "RET: " . $gmclient->returnCode() . "\n";
      exit;
  }
}
while($gmclient->returnCode() != GEARMAN_SUCCESS);

?>

   
```

```php
<?php

echo "Starting\n";

## Se crea el objeto del trabajador
$gmworker= new GearmanWorker();

## Se añade el servidor por defecto (localhost).
$gmworker->addServer();

## Registro de la función "reverse" en el servidor. Cambiar la función del
## trabajador a "reverse_fn_fast" para un trabajo más rápido sin mensajes de
## estado.
$gmworker->addFunction("reverse", "reverse_fn");

print "Waiting for job...\n";
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
  echo "Received job: " . $job->handle() . "\n";

  $workload = $job->workload();
  $workload_size = $job->workloadSize();

  echo "Workload: $workload ($workload_size)\n";

  # Este bucle de estado no es necesario, sólo es para mostrar cómo funciona
  for ($x= 0; $x < $workload_size; $x++)
  {
    echo "Sending status: " . ($x + 1) . "/$workload_size complete\n";
    $job->sendStatus($x, $workload_size);
    sleep(1);
  }

  $result= strrev($workload);
  echo "Result: $result\n";

  # Retornamos lo que hay que enviar de vuelta al cliente
  return $result;
}

## Una forma mucho más sencilla y que da menos información sería:
function reverse_fn_fast($job)
{
  return strrev($job->workload());
}

?>

   
```

Resultado del ejemplo anterior es similar a:

    % php reverse_worker.php
    Starting
    Waiting for job...
    Received job: H:foo.local:36
    Workload: Hello! (6)
    Sending status: 1/6 complete
    Sending status: 2/6 complete
    Sending status: 3/6 complete
    Sending status: 4/6 complete
    Sending status: 5/6 complete
    Sending status: 6/6 complete
    Result: !olleH

       

    % php reverse_client.php
    Starting
    Sending job
    Status: 1/6 complete
    Status: 2/6 complete
    Status: 3/6 complete
    Status: 4/6 complete
    Status: 5/6 complete
    Status: 6/6 complete
    Success: !olleH

## Cliente y trabajador básicos en Gearman, trabajo en segundo plano

Cliente y trabajador básicos en Gearman, trabajo en segundo plano

Este ejemplo muestra un trabajador y un cliente muy sencillos. El cliente envía un string al servidor de trabajos como trabajo en segundo plano, y el trabajador da la vuelta al string. Notar que como el trabajo se realiza de forma asíncrona, el cliente no espera a que se complete el trabajo y termina (y, por tanto, el cliente nunca recibe los resultados).

```php
<?php

## Creación del objeto cliente
$gmclient= new GearmanClient();

## Se añade el servidor por defecto (localhost)
$gmclient->addServer();

## Ejecutar el cliente "reverse" en segundo plano
$job_handle = $gmclient->doBackground("reverse", "this is a test");

if ($gmclient->returnCode() != GEARMAN_SUCCESS)
{
  echo "bad return code\n";
  exit;
}

echo "done!\n";

?>

   
```

```php
<?php

echo "Starting\n";

## Creación del objeto trabajador
$gmworker= new GearmanWorker();

## Se añade el servidor por defecto (localhost).
$gmworker->addServer();

## Registro de la función "reverse" en el servidor. Cambiar la funcion del
## trabajador a "reverse_fn_fast" para usar un trabajador más rápido sin
## mostrar mensajes de estado
$gmworker->addFunction("reverse", "reverse_fn");

print "Waiting for job...\n";
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
  echo "Received job: " . $job->handle() . "\n";

  $workload = $job->workload();
  $workload_size = $job->workloadSize();

  echo "Workload: $workload ($workload_size)\n";

  # Este bucle de estado no es necesario, únicamente muestra cómo funciona
  for ($x= 0; $x < $workload_size; $x++)
  {
    echo "Sending status: " . ($x + 1) . "/$workload_size complete\n";
    $job->sendStatus($x, $workload_size);
    sleep(1);
  }

  $result= strrev($workload);
  echo "Result: $result\n";

  # Retorna lo que se quiere enviar de vuelta al cliente
  return $result;
}

## Una versión mucho más sencilla y que muestra menos información del proceso sería:
function reverse_fn_fast($job)
{
  return strrev($job->workload());
}

?>

   
```

Resultado del ejemplo anterior es similar a:

    % php reverse_worker.php
    Starting
    Waiting for job...
    Received job: H:foo.local:41
    Workload: this is a test (14)
    1/14 complete
    2/14 complete
    3/14 complete
    4/14 complete
    5/14 complete
    6/14 complete
    7/14 complete
    8/14 complete
    9/14 complete
    10/14 complete
    11/14 complete
    12/14 complete
    13/14 complete
    14/14 complete
    Result: tset a si siht

       

    % php reverse_client_bg.php
    done!

## Cliente y trabajador básicos, enviando tareas

Cliente y trabajador básicos, enviando tareas

En este ejemplo, se extiende el cliente básico que da la vuelta al texto para ejecutar dos tareas en paralelo. El trabajador "reverse" es idéntico excepto la parte del envío del datos durante el proceso.

```php
<?php

## Creación del cliente Gearman
$gmc= new GearmanClient();

## Añade el servidor por defecto (localhost)
$gmc->addServer();

## Registra alguna llamadas de retorno
$gmc->setCreatedCallback("reverse_created");
$gmc->setDataCallback("reverse_data");
$gmc->setStatusCallback("reverse_status");
$gmc->setCompleteCallback("reverse_complete");
$gmc->setFailCallback("reverse_fail");

## Asignación de datos arbitrarios para la aplicación
$data['foo'] = 'bar';

## Añade dos tareas
$task= $gmc->addTask("reverse", "foo", $data);
$task2= $gmc->addTaskLow("reverse", "bar", NULL);

##  Ejecuta las tareas en paralelo (se asumen múltiples trabajadores)
if (! $gmc->runTasks())
{
    echo "ERROR " . $gmc->error() . "\n";
    exit;
}

echo "DONE\n";

function reverse_created($task)
{
    echo "CREATED: " . $task->jobHandle() . "\n";
}

function reverse_status($task)
{
    echo "STATUS: " . $task->jobHandle() . " - " . $task->taskNumerator() .
         "/" . $task->taskDenominator() . "\n";
}

function reverse_complete($task)
{
    echo "COMPLETE: " . $task->jobHandle() . ", " . $task->data() . "\n";
}

function reverse_fail($task)
{
    echo "FAILED: " . $task->jobHandle() . "\n";
}

function reverse_data($task)
{
    echo "DATA: " . $task->data() . "\n";
}

?>

   
```

```php
<?php

echo "Starting\n";

## Creación del objeto trabajador
$gmworker= new GearmanWorker();

## Añade el servidor por defecto (localhost).
$gmworker->addServer();

## Registra la función "reverse" en el servidor. Cambiar la función a
## "reverse_fn_fast" para obtener un worker más rápido que no genera
## informacion del proceso
$gmworker->addFunction("reverse", "reverse_fn");

print "Waiting for job...\n";
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
  echo "Received job: " . $job->handle() . "\n";

  $workload = $job->workload();
  $workload_size = $job->workloadSize();

  echo "Workload: $workload ($workload_size)\n";

  # Este bucle de estado no es necesario, sólo es para mostrar cómo funciona
  for ($x= 0; $x < $workload_size; $x++)
  {
    echo "Sending status: " . ($x + 1) . "/$workload_size complete\n";
    $job->sendStatus($x+1, $workload_size);
    $job->sendData(substr($workload, $x, 1));
    sleep(1);
  }

  $result= strrev($workload);
  echo "Result: $result\n";

  # Retornamos lo que queremos enviar de vuelta al cliente
  return $result;
}

## Una versión mucho más sencilla y que muestra menos información del proceso sería:
function reverse_fn_fast($job)
{
  return strrev($job->workload());
}

?>

   
```

Resultado del ejemplo anterior es similar a:

    % php reverse_worker.php
    Starting
    Waiting for job...
    Received job: H:foo.local:45
    Workload: foo (3)
    1/3 complete
    2/3 complete
    3/3 complete
    Result: oof
    Received job: H:foo.local:44
    Workload: bar (3)
    1/3 complete
    2/3 complete
    3/3 complete
    Result: rab

       

    % php reverse_client_task.php
    CREATED: H:foo.local:44
    CREATED: H:foo.local:45
    STATUS: H:foo.local:45 - 1/3
    DATA: f
    STATUS: H:foo.local:45 - 2/3
    DATA: o
    STATUS: H:foo.local:45 - 3/3
    DATA: o
    COMPLETE: H:foo.local:45, oof
    STATUS: H:foo.local:44 - 1/3
    DATA: b
    STATUS: H:foo.local:44 - 2/3
    DATA: a
    STATUS: H:foo.local:44 - 3/3
    DATA: r
    COMPLETE: H:foo.local:44, rab
    DONE
