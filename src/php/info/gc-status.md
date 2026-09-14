---
title: gc_status
description: Obtiene información sobre el recolector de basura
source_url: https://www.php.net/manual/es/function.gc-status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/gc-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 29e86aa41
order: 38830
---

gc_status

Obtiene información sobre el recolector de basura

## Descripción

```php
gc_status(): array
```php

Obtiene información sobre el estado actual del recolector de basura.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `array` asociativo con los siguientes elementos:

- `"runs"`

- `"collected"`

- `"threshold"`

- `"roots"`

- `"running"`

- `"protected"`

- `"full"`

- `"buffer_size"`

- `"application_time"`

- `"collector_time"`

- `"destructor_time"`

- `"free_time"`

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | `gc_status` devuelve ahora los campos adicionales siguientes: `"running"`, `"protected"`, `"full"`, `"buffer_size"`, `"application_time"`, `"collector_time"`, `"destructor_time"`, y `"free_time"`. |

## Ejemplos

Uso de `gc_status`

```
<?php

// crear el árbol de objetos que requiere la recolección de basura
$a = new stdClass();
$a->b = [];
for ($i = 0; $i < 100000; $i++) {
    $b = new stdClass();
    $b->a = $a;
    $a->b[] = $b;
}
unset($a);
unset($b);
gc_collect_cycles();

var_dump(gc_status());

    
```php

Resultado del ejemplo anterior es similar a:

    array(4) {
      ["runs"]=>
      int(5)
      ["collected"]=>
      int(100002)
      ["threshold"]=>
      int(50001)
      ["roots"]=>
      int(0)
    }

        

Resultado del ejemplo anterior en PHP 8.3 es similar a:

    array(12) {
      ["running"]=>
      bool(false)
      ["protected"]=>
      bool(false)
      ["full"]=>
      bool(false)
      ["runs"]=>
      int(5)
      ["collected"]=>
      int(100002)
      ["threshold"]=>
      int(50001)
      ["buffer_size"]=>
      int(131072)
      ["roots"]=>
      int(0)
      ["application_time"]=>
      float(0.031182458)
      ["collector_time"]=>
      float(0.020106291)
      ["destructor_time"]=>
      float(0)
      ["free_time"]=>
      float(0.003707167)
    }

## Véase también

[Recolector de basura (Garbage Collection)](#features.gc)
