---
title: fann_set_cascade_weight_multiplier
description: Establece el multiplicador de peso
source_url: https://www.php.net/manual/es/function.fann-set-cascade-weight-multiplier.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-cascade-weight-multiplier.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22000
---

fann_set_cascade_weight_multiplier

Establece el multiplicador de peso

## Descripción

```php
fann_set_cascade_weight_multiplier(resource $ann, float $cascade_weight_multiplier): bool
```php

Establece el multiplicador de peso.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`cascade_weight_multiplier`  
El multiplicador de peso.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_cascade_weight_multiplier`
