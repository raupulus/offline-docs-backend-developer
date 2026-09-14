---
title: Ev::depth
description: Retorna la profundidad de recursión
source_url: https://www.php.net/manual/es/ev.depth.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/ev/depth.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 17770
---

Ev::depth

Retorna la profundidad de recursión

## Descripción

```php
final public static Ev::depth(): int
```php

El número de veces que el método Ev::run ha sido invocado, menos el número de veces que el método Ev::run ha finalizado normalmente, en otras palabras, la profundidad de recursión. Fuera de Ev::run, este número vale `0`. En una función de retrollamada, este número vale `1`, mientras que el método Ev::run sea invocado recursivamente (o desde otro hilo), en cuyo caso, será superior.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`ev_depth` retorna la profundidad de recursión del bucle por omisión.

## Véase también

Ev::iteration
