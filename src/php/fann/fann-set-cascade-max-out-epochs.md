---
title: fann_set_cascade_max_out_epochs
description: Establece el máximo de épocas de salida
source_url: https://www.php.net/manual/es/function.fann-set-cascade-max-out-epochs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-cascade-max-out-epochs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21940
---

fann_set_cascade_max_out_epochs

Establece el máximo de épocas de salida

## Descripción

```php
fann_set_cascade_max_out_epochs(resource $ann, int $cascade_max_out_epochs): bool
```php

Establece el máximo de épocas de salida.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`cascade_max_out_epochs`  
El máximo de épocas de salida.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_cascade_max_out_epochs`
