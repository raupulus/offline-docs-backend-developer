---
title: Ev::suspend
description: Suspende el bucle de eventos predeterminado
source_url: https://www.php.net/manual/es/ev.suspend.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/ev/suspend.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 17900
---

Ev::suspend

Suspende el bucle de eventos predeterminado

## Descripción

```php
final public static Ev::suspend(): void
```php

Los métodos Ev::suspend y Ev::resume suspenden y reanudan el bucle predeterminado.

Todos los temporizadores de los observadores serán suspendidos entre una *suspensión* y una *reanudación*, y todos los observadores *periódicos* serán actualizados (asimismo, todos los eventos ocurridos durante esta suspensión se perderán).

Tras una llamada al método Ev::suspend, no está permitido llamar a una función en el bucle proporcionado distinta del método Ev::resume. Asimismo, no está permitido llamar al método Ev::resume sin una llamada previa al método Ev::suspend.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Véase también

Ev::resume
