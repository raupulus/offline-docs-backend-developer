---
title: fann_set_cascade_candidate_change_fraction
description: Establece la fracción de cambio de candidatas en cascada
source_url: https://www.php.net/manual/es/function.fann-set-cascade-candidate-change-fraction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-cascade-candidate-change-fraction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21900
---

fann_set_cascade_candidate_change_fraction

Establece la fracción de cambio de candidatas en cascada

## Descripción

```php
fann_set_cascade_candidate_change_fraction(resource $ann, float $cascade_candidate_change_fraction): bool
```php

Establece la fracción de cambio de candidatas en cascada.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`cascade_candidate_change_fraction`  
La fracción de cambio de candidatas en cascada.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_cascade_candidate_change_fraction`
