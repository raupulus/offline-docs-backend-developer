---
title: fann_set_rprop_decrease_factor
description: Establece el factor de disminución empleado durante un entrenamiento
  RPROP
source_url: https://www.php.net/manual/es/function.fann-set-rprop-decrease-factor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-rprop-decrease-factor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22080
---

fann_set_rprop_decrease_factor

Establece el factor de disminución empleado durante un entrenamiento RPROP

## Descripción

```php
fann_set_rprop_decrease_factor(resource $ann, float $rprop_decrease_factor): bool
```php

Establece el factor de disminución empleado durante un entrenamiento RPROP.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`rprop_decrease_factor`  
El factor de disminución.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_rprop_decrease_factor`
