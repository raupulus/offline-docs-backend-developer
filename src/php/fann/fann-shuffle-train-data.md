---
title: fann_shuffle_train_data
description: Mezcla los datos de entrenamiento, aleatorizando el orden
source_url: https://www.php.net/manual/es/function.fann-shuffle-train-data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-shuffle-train-data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22230
---

fann_shuffle_train_data

Mezcla los datos de entrenamiento, aleatorizando el orden

## Descripción

```php
fann_shuffle_train_data(resource $train_data): bool
```php

Mezcla los datos de entrenamiento, aleatorizando el orden. Es lo recomendado para entrenamientos incrementales, mientras que no tiene influencia durante entrenamientos por lotes.

## Parámetros

`train_data`  
Un `resource` de datos de entrenamiento de red neuronal.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.
