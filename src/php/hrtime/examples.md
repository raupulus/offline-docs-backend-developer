---
title: Ejemplos
source_url: https://www.php.net/manual/es/hrtime.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hrtime/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hrtime
translation_status: ready
translation_reviewed: false
translation_revision: 3e7e14916
order: 29450
---

## Ejemplos

## Uso básico

El ejemplo muestra el uso básico de la clase StopWatch

Medir la ejecución de varios bloques de código y obtener el total

```php
<?php

$c = new HRTime\StopWatch;

$c->start();
/* medir la ejecución de este bloque de código */
for ($i = 0; $i < 1024*1024; $i++);
$c->stop();
$transcurrido0 = $c->getLastElapsedTime(HRTime\Unit::NANOSECOND);

/* la medición no se ejecuta aquí */
for ($i = 0; $i < 1024*1024; $i++);

$c->start();
/* medir la ejecución de este bloque de código */
for ($i = 0; $i < 1024*1024; $i++);
$c->stop();
$transcurrido1 = $c->getLastElapsedTime(HRTime\Unit::NANOSECOND);

$total_transcurrido = $c->getElapsedTime(HRTime\Unit::NANOSECOND);

?>

   
```
