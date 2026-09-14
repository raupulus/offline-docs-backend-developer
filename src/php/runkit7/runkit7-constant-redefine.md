---
title: runkit7_constant_redefine
description: Redefine una constante ya definida
source_url: https://www.php.net/manual/es/function.runkit7-constant-redefine.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/functions/runkit7-constant-redefine.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_reviewed: true
translation_revision: c4625323f
order: 72850
---

runkit7_constant_redefine

Redefine una constante ya definida

## Descripción

```php
runkit7_constant_redefine(string $constant_name, mixed $value, [int $new_visibility]): bool
```php

## Parámetros

`constant_name`  
La constante a redefinir. Puede ser el nombre de una constante global, o `classname::constname` indicando una constante de clase.

`value`  
El valor a asignar a la constante.

`new_visibility`  
La nueva visibilidad de la constante, para constantes de clase. Por omisión, permanece sin cambios. Una de las constantes `RUNKIT7_ACC_*`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

runkit7_constant_add

runkit7_constant_remove
