---
title: Fiber::getCurrent
description: Obtiene la instancia de Fibra en ejecución
source_url: https://www.php.net/manual/es/fiber.getcurrent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/fiber/getcurrent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 8fee3ae97
order: 3420
---

Fiber::getCurrent

Obtiene la instancia de Fibra en ejecución

## Descripción

```php
public static Fiber::getCurrent(): Fiber
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la instancia `Fiber` en ejecución o `null` si este método es llamado desde fuera de una fibra.
