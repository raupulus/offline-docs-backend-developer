---
title: GearmanClient::do
description: Ejecuta una sola tarea y retorna el resultado [obsoleto]
source_url: https://www.php.net/manual/es/gearmanclient.do.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/do.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_revision: cf0a919c1
order: 25030
---

GearmanClient::do

Ejecuta una sola tarea y retorna el resultado \[obsoleto\]

## Descripción

```php
public GearmanClient::do(string $function_name, string $workload, [string $unique]): string
```php

El método GearmanClient::do es obsoleto desde pecl/gearman 1.0.0. Use GearmanClient::doNormal.

## Parámetros

`function_name`  
Una función registrada que el trabajador va a ejecutar

`workload`  
Datos serializados a analizar

`unique`  
Un identificador único utilizado para identificar una tarea particular

## Valores devueltos

Un string representando el resultado de la tarea ejecutada.

## Ejemplos

Envío de un trabajo con retorno inmediato

```
<?php

## Código del cliente

echo "Starting\n";

## Creación del objeto cliente
$gmclient= new GearmanClient();

## Adición del servidor por defecto (localhost).
$gmclient->addServer();

echo "Sending job\n";

$result = $gmclient->doNormal("reverse", "Hello!");

echo "Success: $result\n";

?>

    
```php

```
<?php

echo "Starting\n";

## Creación del objeto trabajador
$gmworker= new GearmanWorker();

## Adición del servidor por defecto (localhost).
$gmworker->addServer();

## Registra la función "reverse" en el servidor. Cambiar la función del trabajador
## a "reverse_fn_fast" para usar un trabajar más rápido que no genera salida.
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
  return strrev($job->workload());
}

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Starting
    Sending job
    Success: !olleH

Envío de un trabajo y obtención del estado incremental

Se envía un trabajo y el script comprueba constantemente mediante un bucle la información de estado. El trabajador tiene un retardo artificial que provoca un trabajo de larga duración y envía el estado y datos según se van procesando. Cada llamada a GearmanClient::do produce información de estado del trabajo en ejecución.

```
<?php

## Código del cliente

## Creamos el objeto cliente
$gmclient= new GearmanClient();

## Añadimos el servidor por defecto (localhost).
$gmclient->addServer();

echo "Sending job\n";

## Enviamos trabajo "reverse"
do
{
  $result = $gmclient->doNormal("reverse", "Hello!");
  # Comprobamos llegada de posibles paquetes y errores

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
      echo "Error: " . $gmclient->error() . "\n";
      echo "Errno: " . $gmclient->getErrno() . "\n";
      exit;
  }
}
while($gmclient->returnCode() != GEARMAN_SUCCESS);

echo "Success: $result\n";

?>

    
```php

```
<?php

## Código del trabajador

echo "Starting\n";

## Creamos el objeto trabajador
$gmworker= new GearmanWorker();

## Añadimos servidor por defecto (localhost).
$gmworker->addServer();

## Registramos la función "reverse" en el servidor
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

  # Este bucle para comprobar el estado no es necesario, tan sólo muestra como funciona
  for ($x= 0; $x < $workload_size; $x++)
  {
    echo "Sending status: " + $x + 1 . "/$workload_size complete\n";
    $job->sendStatus($x+1, $workload_size);
    $job->sendData(substr($workload, $x, 1));
    sleep(1);
  }

  $result= strrev($workload);
  echo "Result: $result\n";

  # Retornamos lo que queremos enviar al cliente
  return $result;
}

?>

    
```php

Resultado del ejemplo anterior es similar a:

Worker output:

    Starting
    Waiting for job...
    Received job: H:foo.local:106
    Workload: Hello! (6)
    1/6 complete
    2/6 complete
    3/6 complete
    4/6 complete
    5/6 complete
    6/6 complete
    Result: !olleH

        

Client output:

    Starting
    Sending job
    Status: 1/6 complete
    Data: H
    Status: 2/6 complete
    Data: e
    Status: 3/6 complete
    Data: l
    Status: 4/6 complete
    Data: l
    Status: 5/6 complete
    Data: o
    Status: 6/6 complete
    Data: !
    Success: !olleH

## Véase también

GearmanClient::doHigh

GearmanClient::doLow

GearmanClient::doBackground

GearmanClient::doHighBackground

GearmanClient::doLowBackground
