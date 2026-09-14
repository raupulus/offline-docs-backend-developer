---
title: fann_set_cascade_candidate_limit
description: Establece el límite de candidatas
source_url: https://www.php.net/manual/es/function.fann-set-cascade-candidate-limit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-cascade-candidate-limit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21910
---

fann_set_cascade_candidate_limit

Establece el límite de candidatas

## Descripción

```php
fann_set_cascade_candidate_limit(resource $ann, float $cascade_candidate_limit): bool
```php

Establece el límite de candidatas.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`cascade_candidate_limit`  
El límite de candidatas.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_cascade_candidate_limit`
