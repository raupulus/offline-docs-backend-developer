---
title: GearmanClient::doNormal
description: Ejecuta una tarea y devuelve el resultado
source_url: https://www.php.net/manual/es/gearmanclient.donormal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/donormal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25100
---

GearmanClient::doNormal

Ejecuta una tarea y devuelve el resultado

## Descripción

```php
public GearmanClient::doNormal(string $function, string $workload, [string $unique]): string
```php

Ejecuta una tarea y devuelve una `string` que representa el resultado. Corresponde a las clases `GearmanClient` y `GearmanWorker` aceptar el formato del resultado.

## Parámetros

`function`  
Una función registrada que el trabajador va a ejecutar

`workload`  
Datos serializados a analizar

`unique`  
Un identificador único utilizado para identificar una tarea particular

## Valores devueltos

Una `string` que representa el resultado de la tarea ejecutada.

## Ejemplos

Envío de una tarea con retorno inmediato

```
<?php

?>

    
```php

```
<?php

## Código del cliente

echo "Inicio\n";

## Creación del objeto cliente.
$gmclient= new GearmanClient();

## Adición del servidor por omisión (localhost).
$gmclient->addServer();

echo "Envío de la tarea\n";

$result = $gmclient->doNormal("reverse", "Hello!");

echo "Éxito: $result\n";

?>

    
```php

```
<?php

echo "Inicio\n";

## Creación del objeto worker.
$gmworker= new GearmanWorker();

## Adición del servidor por omisión (localhost).
$gmworker->addServer();

## Registro de la función "reverse" con el servidor. Modifica la función worker
## a "reverse_fn_fast" para un worker más rápido sin salida.
$gmworker->addFunction("reverse", "reverse_fn");

print "Esperando una tarea...\n";
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

    Inicio
    Envío de la tarea
    Éxito: !olleH

Envío de una tarea y recuperación incremental del estado

Una tarea es enviada y el script se ejecuta en bucle para recuperar las informaciones de estado. El worker tiene un retraso artificial que lo convierte en una tarea larga y envía el estado y los datos cuando la ejecución ocurre. Cada subllamada a la función GearmanClient::doNormal produce informaciones de estado sobre la tarea en curso.

```
<?php

## Código del cliente

## Creación del objeto cliente.
$gmclient= new GearmanClient();

## Adición del servidor por omisión (localhost).
$gmclient->addServer();

echo "Envío de la tarea\n";

## Envío de la tarea reverse
do
{
  $result = $gmclient->doNormal("reverse", "Hello!");
  # Verifica los paquetes devueltos así como los errores.

  switch($gmclient->returnCode())
  {
    case GEARMAN_WORK_DATA:
      echo "Datos: $result\n";
      break;
    case GEARMAN_WORK_STATUS:
      list($numerator, $denominator)= $gmclient->doStatus();
      echo "Estado: $numerator/$denominator completado\n";
      break;
    case GEARMAN_WORK_FAIL:
      echo "Fallo\n";
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

echo "Éxito: $result\n";

?>

    
```php

```
<?php

## Código del worker

echo "Inicio\n";

## Creación del objeto worker.
$gmworker= new GearmanWorker();

## Adición del servidor por omisión (localhost).
$gmworker->addServer();

## Registro de la función "reverse" con el servidor.
$gmworker->addFunction("reverse", "reverse_fn");

print "Esperando una tarea...\n";
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
  echo "Tarea recibida: " . $job->handle() . "\n";

  $workload = $job->workload();
  $workload_size = $job->workloadSize();

  echo "Workload: $workload ($workload_size)\n";

  # Este bucle de estado no es necesario, solo muestra cómo funciona
  for ($x= 0; $x < $workload_size; $x++)
  {
    echo "Envío del estado: " . $x + 1 . "/$workload_size completado\n";
    $job->sendStatus($x+1, $workload_size);
    $job->sendData(substr($workload, $x, 1));
    sleep(1);
  }

  $result= strrev($workload);
  echo "Resultado: $result\n";

  # Devuelve lo que se desea devolver al cliente.
  return $result;
}

?>

    
```php

Resultado del ejemplo anterior es similar a:

Salida del worker:

    Inicio
    Esperando una tarea...
    Tarea recibida: H:foo.local:106
    Workload: Hello! (6)
    1/6 completado
    2/6 completado
    3/6 completado
    4/6 completado
    5/6 completado
    6/6 completado
    Resultado: !olleH

        

Salida del cliente:

    Inicio
    Envío de la tarea
    Estado: 1/6 completado
    Datos: H
    Estado: 2/6 completado
    Datos: e
    Estado: 3/6 completado
    Datos: l
    Estado: 4/6 completado
    Datos: l
    Estado: 5/6 completado
    Datos: o
    Estado: 6/6 completado
    Datos: !
    Éxito: !olleH

## Véase también

GearmanClient::doHigh

GearmanClient::doLow

GearmanClient::doBackground

GearmanClient::doHighBackground

GearmanClient::doLowBackground
