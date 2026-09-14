---
title: Pool::collect
description: Recopila las referencias de las tareas completadas
source_url: https://www.php.net/manual/es/pool.collect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/pool/collect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66610
---

Pool::collect

Recopila las referencias de las tareas completadas

## Descripción

```php
public Pool::collect([Callable $collector]): int
```php

Permite al pool recopilar referencias determinadas para ser colectadas por el colector dado opcionalmente.

## Parámetros

`collector`  
Un colector que puede ser llamado y que devuelve un valor booleano para determinar si la tarea puede ser colectada o no. Solo en casos raros debe utilizarse un colector personalizado.

## Valores devueltos

Número de tareas restantes en el pool para ser colectadas.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL pthreads 3.0.0 | Ahora se devuelve un entero, y el argumento `collector` es ahora opcional. |

## Ejemplos

Un ejemplo básico de Pool::collect

```
<?php
$pool = new Pool(4);

for ($i = 0; $i < 15; ++$i) {
    $pool->submit(new class extends Threaded {});
}

while ($pool->collect()); // bloquea hasta que todas las tareas hayan finalizado

$pool->shutdown();

   
```php
