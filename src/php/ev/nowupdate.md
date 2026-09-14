---
title: Ev::nowUpdate
description: Establece el tiempo actual solicitándolo al kernel; actualiza el tiempo
  devuelto por Ev::now durante la ejecución
source_url: https://www.php.net/manual/es/ev.nowupdate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/ev/nowupdate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 17830
---

Ev::nowUpdate

Establece el tiempo actual solicitándolo al kernel; actualiza el tiempo devuelto por Ev::now durante la ejecución

## Descripción

```php
final public static Ev::nowUpdate(): void
```php

Establece el tiempo actual solicitándolo al kernel; actualiza el tiempo devuelto por el método Ev::now durante la ejecución. Esta es una operación costosa, y se realiza habitualmente automáticamente en el método Ev::run.

Este método es raramente útil, pero cuando las funciones de retrollamada de evento se ejecutan durante mucho tiempo sin entrar en un bucle de evento, actualizar *libev* con el tiempo actual es una buena idea.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Véase también

Ev::now
