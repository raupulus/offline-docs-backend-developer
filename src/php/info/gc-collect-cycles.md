---
title: gc_collect_cycles
description: Fuerza la recolección de los ciclos de basura existentes
source_url: https://www.php.net/manual/es/function.gc-collect-cycles.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/gc-collect-cycles.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_revision: eec7af839
order: 38780
---

gc_collect_cycles

Fuerza la recolección de los ciclos de basura existentes

## Descripción

```php
gc_collect_cycles(): int
```php

Recogida de las fuerzas de los ciclos de basura existentes.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de ciclos de recogida.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | El valor de retorno ya no incluye las cadenas y los recursos que fueron recolectados indirectamente a través de los ciclos. |

## Véase también

[Recolección de Basura](#features.gc)
