---
title: fann_set_cascade_min_cand_epochs
description: Establece el mínimo de épocas de candidatas
source_url: https://www.php.net/manual/es/function.fann-set-cascade-min-cand-epochs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-cascade-min-cand-epochs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: 242efce0d
order: 21950
---

fann_set_cascade_min_cand_epochs

Establece el mínimo de épocas de candidatas

## Descripción

```php
fann_set_cascade_min_cand_epochs(resource $ann, int $cascade_min_cand_epochs): bool
```php

Establece el mínimo de épocas de candidatas.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`cascade_min_cand_epochs`  
El máximo de mínimo de candidatas.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Notas

> [!NOTE]
> Esta función ahora está disponible si la extensión fann ha sido compilada con libfann \>= 2.2.

## Véase también

`fann_get_cascade_min_cand_epochs`
