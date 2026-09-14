---
title: GearmanWorker::setTimeout
description: Define el tiempo de espera máximo de actividad del socket I/O
source_url: https://www.php.net/manual/es/gearmanworker.settimeout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanworker/settimeout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25910
---

GearmanWorker::setTimeout

Define el tiempo de espera máximo de actividad del socket I/O

## Descripción

```php
public GearmanWorker::setTimeout(int $timeout): true
```php

Define el intervalo de tiempo para esperar actividad del socket I/O.

## Parámetros

`timeout`  
Un intervalo de tiempo, en milisegundos. Un valor negativo indica que el tiempo de espera será infinito.

## Valores devueltos

Retorna siempre `true`.

## Ejemplos

Un agente simple que espera 5 segundos

```
<?php

echo "Inicio\n";

## Crea un nuevo agente.
$gmworker= new GearmanWorker();

## Añade un servidor por omisión (localhost).
$gmworker->addServer();

## Registra una función "reverse" con el servidor.
$gmworker->addFunction("reverse", "reverse_fn");

## Define el tiempo de espera a 5 segundos
$gmworker->setTimeout(5000);

echo "Esperando trabajo...\n";
while(@$gmworker->work() || $gmworker->returnCode() == GEARMAN_TIMEOUT)
{
  if ($gmworker->returnCode() == GEARMAN_TIMEOUT)
  {
    # Normalmente, debería realizarse alguna tarea útil aquí...
    echo "Tiempo de espera expirado. Esperando el próximo trabajo...\n";
    continue;
  }

  if ($gmworker->returnCode() != GEARMAN_SUCCESS)
  {
    echo "return_code: " . $gmworker->returnCode() . "\n";
    break;
  }
}

echo "Hecho\n";

function reverse_fn($job)
{
  return strrev($job->workload());
}

?>

   
```php

La ejecución de un agente sin ningún trabajo enviado generará una salida que se asemejará a algo como:

    Inicio
    Esperando trabajo...
    Tiempo de espera expirado. Esperando el próximo trabajo...
    Tiempo de espera expirado. Esperando el próximo trabajo...
    Tiempo de espera expirado. Esperando el próximo trabajo...

## Véase también

GearmanWorker::timeout
