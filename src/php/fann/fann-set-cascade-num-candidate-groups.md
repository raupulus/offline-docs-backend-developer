---
title: fann_set_cascade_num_candidate_groups
description: Establece el número de grupos de candidatas
source_url: https://www.php.net/manual/es/function.fann-set-cascade-num-candidate-groups.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-cascade-num-candidate-groups.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21970
---

fann_set_cascade_num_candidate_groups

Establece el número de grupos de candidatas

## Descripción

```php
fann_set_cascade_num_candidate_groups(resource $ann, int $cascade_num_candidate_groups): bool
```php

Establece el número de grupos de candidatas.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`cascade_num_candidate_groups`  
El número de grupos de candidatas.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_cascade_num_candidate_groups`
