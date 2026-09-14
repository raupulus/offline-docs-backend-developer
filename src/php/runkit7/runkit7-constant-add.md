---
title: runkit7_constant_add
description: Similar a define(), pero permite definir constantes en las definiciones
  de clase también
source_url: https://www.php.net/manual/es/function.runkit7-constant-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/functions/runkit7-constant-add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_reviewed: true
translation_revision: c4625323f
order: 72840
---

runkit7_constant_add

Similar a define(), pero permite definir constantes en las definiciones de clase también

## Descripción

```php
runkit7_constant_add(string $constant_name, mixed $value, [int $newVisibility]): bool
```php

## Parámetros

`constant_name`  
El nombre de la constante a declarar. Puede ser un string para indicar una constante global, o `classname::constname` para indicar una constante de clase.

`value`  
NULL, Bool, Long, Double, String, Array, o Resource a almacenar en la nueva constante.

`newVisibility`  
La visibilidad de la constante, para las constantes de clase. Público por omisión. Una de las constantes `RUNKIT7_ACC_*`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

define

runkit7_constant_redefine

runkit7_constant_remove
