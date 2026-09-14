---
title: fann_set_cascade_max_cand_epochs
description: Establece el máximo de épocas de candidatas
source_url: https://www.php.net/manual/es/function.fann-set-cascade-max-cand-epochs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-cascade-max-cand-epochs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21930
---

fann_set_cascade_max_cand_epochs

Establece el máximo de épocas de candidatas

## Descripción

```php
fann_set_cascade_max_cand_epochs(resource $ann, int $cascade_max_cand_epochs): bool
```php

Establece el máximo de épocas de candidatas.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`cascade_max_cand_epochs`  
El máximo de épocas de candidatas.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_cascade_max_cand_epochs`
