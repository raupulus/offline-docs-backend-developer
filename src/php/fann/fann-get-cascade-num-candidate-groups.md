---
title: fann_get_cascade_num_candidate_groups
description: Devuelve el número de grupos de candidatas
source_url: https://www.php.net/manual/es/function.fann-get-cascade-num-candidate-groups.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-cascade-num-candidate-groups.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21250
---

fann_get_cascade_num_candidate_groups

Devuelve el número de grupos de candidatas

## Descripción

```php
fann_get_cascade_num_candidate_groups(resource $ann): int
```php

El número de grupos de candidatas es el número de grupos de candidatas idénticos que se emplearán durante un entrenamiento.

Este número se puede usar para tener más candidatas sin tener que definir nuevos parámetros para las candidatas.

Véase `fann_get_cascade_num_candidates` para una descripción de las neuronas candidatas generadas por este parámetro.

El número de grupos de candidatas predeterminado es 2.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El número de grupos de candidatas, o `false` en caso de error.

## Véase también

`fann_set_cascade_num_candidate_groups`
