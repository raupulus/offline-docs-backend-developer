---
title: fann_train
description: Entrenar una iteración con un conjunto de entradas y un conjunto de salidas
  deseadas
source_url: https://www.php.net/manual/es/function.fann-train.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-train.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22300
---

fann_train

Entrenar una iteración con un conjunto de entradas y un conjunto de salidas deseadas

## Descripción

```php
fann_train(resource $ann, array $input, array $desired_output): bool
```php

Entrenar una iteración con un conjunto de entradas y un conjunto de salidas deseadas. Este entrenamiento siempre es incremental, ya que solamente está presente un patrón.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`input`  
Un array de entradas. Este array debe ser exactamente de `fann_get_num_input` de longitud.

`desired_output`  
Un array de salidas deseadas. Este array debe ser exactamente de `fann_get_num_output` de longitud.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_train_on_data`, `fann_train_epoch`, `fann_get_num_input`, `fann_get_num_output`
