---
title: GearmanClient::jobStatus
description: Recupera el estado de un trabajo en segundo plano
source_url: https://www.php.net/manual/es/gearmanclient.jobstatus.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/jobstatus.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 25150
---

GearmanClient::jobStatus

gearman_job_status

Recupera el estado de un trabajo en segundo plano

## Descripción

Estilo orientado a objetos (método) :

```php
public GearmanClient::jobStatus(string $job_handle): array
```php

Recupera el estado de un trabajo en segundo plano para el gestor de trabajos proporcionado. Las informaciones de estado especifican si el trabajo es conocido, si el trabajo está actualmente en ejecución, así como el porcentaje de realización.

## Parámetros

`job_handle`  
El manejador de trabajos asignado por el servidor Gearman

## Valores devueltos

Un array que contiene las informaciones de estado para el trabajo correspondiente al gestor de trabajos proporcionado. El primer elemento es un bool indicando si el trabajo es conocido, el segundo es un bool indicando si el trabajo está en ejecución, el tercero y el cuarto corresponden al numerador y denominador del porcentaje de realización.

## Ejemplos

Supervisa el estado de un trabajo en segundo plano que tarda en ejecutarse

```
<?php

/* Crea un cliente */
$gmclient= new GearmanClient();

/* Añade un servidor por defecto */
$gmclient->addServer();

/* Ejecuta el cliente */
$job_handle = $gmclient->doBackground("reverse", "this is a test");

if ($gmclient->returnCode() != GEARMAN_SUCCESS)
{
  echo "Código de retorno incorrecto\n";
  exit;
}

$done = false;
do
{
   sleep(3);
   $stat = $gmclient->jobStatus($job_handle);
   if (!$stat[0]) // el trabajo es conocido, significando que no ha terminado
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

GearmanClient::doStatus
