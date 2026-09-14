---
title: fann_merge_train_data
description: Funde los datos de entrenamiento
source_url: https://www.php.net/manual/es/function.fann-merge-train-data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-merge-train-data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21600
---

fann_merge_train_data

Funde los datos de entrenamiento

## Descripción

```php
fann_merge_train_data(resource $data1, resource $data2): resource
```php

Funde los datos de data1 y data2 en un nuevo `resource` de datos de entrenamiento.

## Parámetros

`data1`  
Un `resource` de datos de entrenamiento de red neuronal.

`data2`  
Un `resource` de datos de entrenamiento de red neuronal.

## Valores devueltos

El nuevo `resource` de datos de entrenamiento fundido, o `false` en caso de error.
