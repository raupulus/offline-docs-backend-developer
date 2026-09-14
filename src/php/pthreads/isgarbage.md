---
title: Collectable::isGarbage
description: Determina si un objeto ha sido marcado como obsoleto
source_url: https://www.php.net/manual/es/collectable.isgarbage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/collectable/isgarbage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66570
---

Collectable::isGarbage

Determina si un objeto ha sido marcado como obsoleto

## Descripción

```php
public Collectable::isGarbage(): true
```php

Puede ser llamado en Pool::collect para determinar si este objeto está obsoleto.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Véase también

Pool::collect
