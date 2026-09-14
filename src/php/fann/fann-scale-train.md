---
title: fann_scale_train
description: Escalar datos de entrada y salida basados en parámetros previamente calculados
source_url: https://www.php.net/manual/es/function.fann-scale-train.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-scale-train.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21770
---

fann_scale_train

Escalar datos de entrada y salida basados en parámetros previamente calculados

## Descripción

```php
fann_scale_train(resource $ann, resource $train_data): bool
```php

Escalar datos de entrada y salida basados en parámetros previamente calculados.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`train_data`  
Un `resource` de datos de entrenamiento de red neuronal.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_descale_train`, `fann_set_scaling_params`
