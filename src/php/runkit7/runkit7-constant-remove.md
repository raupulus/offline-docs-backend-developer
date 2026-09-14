---
title: runkit7_constant_remove
description: Elimina una constante ya definida
source_url: https://www.php.net/manual/es/function.runkit7-constant-remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/functions/runkit7-constant-remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_reviewed: true
translation_revision: c4625323f
order: 72860
---

runkit7_constant_remove

Elimina una constante ya definida

## Descripción

```php
runkit7_constant_remove(string $constant_name): bool
```php

## Parámetros

`constant_name`  
El nombre de la constante a eliminar. Puede ser el nombre de una constante global, o `classname::constname` indicando una constante de clase.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

define

runkit7_constant_add

runkit7_constant_redefine
