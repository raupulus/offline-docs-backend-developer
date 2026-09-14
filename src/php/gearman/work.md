---
title: GearmanWorker::work
description: Atender y ejecutar un trabajo
source_url: https://www.php.net/manual/es/gearmanworker.work.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanworker/work.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25960
---

GearmanWorker::work

Atender y ejecutar un trabajo

## Descripción

```php
public GearmanWorker::work(): bool
```php

Espera un trabajo y llama a la función de devolución de llamada correspondiente. Emite una advertencia de tipo `E_WARNING` que contiene el último error de Gearman si el código devuelto no es una de las siguientes constantes: `GEARMAN_SUCCESS`, `GEARMAN_IO_WAIT`, o `GEARMAN_WORK_FAIL`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con GearmanWorker::work

```
<?php

## Crea un agente
$worker = new GearmanWorker();

## Añade un servidor de trabajos por omisión (localhost)
$worker->addServer();

## Añade la función "reverse"
$worker->addFunction("reverse", "my_reverse_function");

## Inicia la escucha del agente para obtener un trabajo
while ($worker->work());

function my_reverse_function($job)
{
  return strrev($job->workload());
}

?>

   
```php

## Véase también

GearmanWorker::addFunction
