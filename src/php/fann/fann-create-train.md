---
title: fann_create_train
description: Crea una estructura de datos de entrenamiento vacía
source_url: https://www.php.net/manual/es/function.fann-create-train.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-create-train.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 21020
---

fann_create_train

Crea una estructura de datos de entrenamiento vacía

## Descripción

```php
fann_create_train(int $num_data, int $num_input, int $num_output): resource
```php

Crea una estructura de datos de entrenamiento vacía.

## Parámetros

`num_data`  
El número de datos de entrenamiento

`num_input`  
El número de entradas por datos de entrenamiento

`num_output`  
El número de salidas por datos de entrenamiento

## Valores devueltos

Devuelve un `resource` de datos de entrenamiento en caso de éxito, o `false` en caso de error.

## Notas

> [!NOTE]
> Esta función ahora está disponible si la extensión fann ha sido compilada con libfann \>= 2.2.

## Véase también

`fann_read_train_from_file`, `fann_train_on_data`, `fann_destroy_train`, `fann_save_train`
