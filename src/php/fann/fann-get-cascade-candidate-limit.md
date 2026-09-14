---
title: fann_get_cascade_candidate_limit
description: Devuelve el límite de candidatas
source_url: https://www.php.net/manual/es/function.fann-get-cascade-candidate-limit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-cascade-candidate-limit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21190
---

fann_get_cascade_candidate_limit

Devuelve el límite de candidatas

## Descripción

```php
fann_get_cascade_candidate_limit(resource $ann): float
```php

El límite de candidatas es un límite de cuánto podrían ser entrenadas las neuronas candidatas. El límite es un límite de la proporción entre el ECM y la puntuación de la candidata.

Establecezca este valor a uno más bajo para evitar el sobreajuste, y a uno más alto si el sobreajuste no es un problema.

El límite de candidatas predetermiado es 1000.0.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El límite de candidatas, o `false` en caso de error.

## Véase también

`fann_set_cascade_candidate_limit`
