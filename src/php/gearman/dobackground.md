---
title: GearmanClient::doBackground
description: Ejecuta una tarea en segundo plano
source_url: https://www.php.net/manual/es/gearmanclient.dobackground.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/dobackground.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25040
---

GearmanClient::doBackground

Ejecuta una tarea en segundo plano

## Descripción

```php
public GearmanClient::doBackground(string $function, string $workload, [string $unique]): string
```php

Ejecuta una tarea en segundo plano, devuelve el gestor de trabajos que podrá ser utilizado para recuperar el estado de la tarea en curso.

## Parámetros

`function`  
Una función registrada que el trabajador va a ejecutar

`workload`  
Datos serializados a analizar

`unique`  
Un identificador único utilizado para identificar una tarea particular

## Valores devueltos

El gestor de trabajos para la tarea enviada.

## Ejemplos

Envía y supervisa un trabajo en segundo plano

El agente de este ejemplo tiene un retraso artificial introducido para simular un trabajo cuya ejecución tarda mucho tiempo. El script del cliente verifica periódicamente el estado del trabajo en curso.

```
<?php

/* Crea un cliente */
$gmclient= new GearmanClient();

/* Añade un servidor por omisión */
$gmclient->addServer();

/* Ejecuta el cliente */
$job_handle = $gmclient->doBackground("reverse", "this is a test");

if ($gmclient->returnCode() != GEARMAN_SUCCESS)
{
  echo "Código de retorno erróneo\n";
  exit;
}

$done = false;
do
{
   sleep(3);
   $stat = $gmclient->jobStatus($job_handle);
   if (!$stat[0]) // la tarea es conocida por lo que no está terminada
      $done = true;
   echo "Ejecución : " . ($stat[1] ? "true" : "false") . ", numerador : " . $stat[2] . ", denominador : " . $stat[3] . "\n";
}
while(!$done);

echo "hecho !\n";

?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ejecución : true, numerador : 3, denominador : 14
    Ejecución : true, numerador : 6, denominador : 14
    Ejecución : true, numerador : 9, denominador : 14
    Ejecución : true, numerador : 12, denominador : 14
    Ejecución : false, numerador : 0, denominador : 0
    hecho !

## Véase también

GearmanClient::doNormal

GearmanClient::doHigh

GearmanClient::doLow

GearmanClient::doHighBackground

GearmanClient::doLowBackground
