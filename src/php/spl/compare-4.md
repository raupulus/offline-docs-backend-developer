---
title: SplPriorityQueue::compare
description: Comparar las prioridades con el fin de colocar los elementos correctamente
  en el montón, mientras que tamizar arriba
source_url: https://www.php.net/manual/es/splpriorityqueue.compare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splpriorityqueue/compare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 85290
---

SplPriorityQueue::compare

Comparar las prioridades con el fin de colocar los elementos correctamente en el montón, mientras que tamizar arriba

## Descripción

```php
public SplPriorityQueue::compare(mixed $priority1, mixed $priority2): int
```php

Compare `priority1` con `priority2`.

## Parámetros

`priority1`  
La prioridad del primer nodo que se compara.

`priority2`  
La prioridad del segundo nodo que se compara.

## Valores devueltos

Resultados de la comparación, entero positivo si `priority1`es mayor que `priority2` , O si son iguales, entero negativo lo contrario.

> [!NOTE]
> Varios elementos con la misma prioridad que se quita de la cola sin ningún orden en particular.
