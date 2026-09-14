---
title: fann_set_rprop_increase_factor
description: Establece el factor de aumento empleado durante un entrenamiento RPROP
source_url: https://www.php.net/manual/es/function.fann-set-rprop-increase-factor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-rprop-increase-factor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22120
---

fann_set_rprop_increase_factor

Establece el factor de aumento empleado durante un entrenamiento RPROP

## Descripción

```php
fann_set_rprop_increase_factor(resource $ann, float $rprop_increase_factor): bool
```php

Establece el factor de aumento empleado durante un entrenamiento RPROP.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`rprop_increase_factor`  
El aumento de disminución.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_rprop_increase_factor`
