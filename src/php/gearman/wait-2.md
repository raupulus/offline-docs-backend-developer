---
title: GearmanWorker::wait
description: Espera una actividad de uno o varios servidores de trabajos
source_url: https://www.php.net/manual/es/gearmanworker.wait.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanworker/wait.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25950
---

GearmanWorker::wait

Espera una actividad de uno o varios servidores de trabajos

## Descripción

```php
public GearmanWorker::wait(): bool
```php

Pone a espera al agente de una actividad de uno o varios servidores de trabajos durante un funcionamiento en modo I/O no bloqueante. En caso de fallo, se emitirá una advertencia de nivel `E_WARNING` con el contenido del último error Gearman ocurrido.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejecutar un agente en modo no bloqueante

```
<?php

echo "Inicio\n";

## Crea un nuevo agente
$worker= new GearmanWorker();

## Hace al agente no bloqueante
$worker->addOptions(GEARMAN_WORKER_NON_BLOCKING);

## Añade un servidor por defecto (localhost, puerto 4730)
$worker->addServer();

## Añade una función "reverse"
$worker->addFunction('reverse', 'reverse_fn');

## Intenta obtener un trabajo
while (@$worker->work() ||
       $worker->returnCode() == GEARMAN_IO_WAIT ||
       $worker->returnCode() == GEARMAN_NO_JOBS)
{
  if ($worker->returnCode() == GEARMAN_SUCCESS)
    continue;

  echo "Esperando el primer trabajo...\n";
  if (!@$worker->wait())
  {
    if ($worker->returnCode() == GEARMAN_NO_ACTIVE_FDS)
    {
      # No estamos conectados a ningún servidor; por lo tanto, esperamos un poco
      # antes de intentar una reconexión.
      sleep(5);
      continue;
    }
    break;
  }
}

echo "Error del agente: " . $worker->error() . "\n";

function reverse_fn($job)
{
  return strrev($job->workload());
}

?>

   
```php

## Véase también

GearmanWorker::work
