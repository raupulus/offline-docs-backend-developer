---
title: fann_get_train_stop_function
description: Devuelve la función de parada empleada durante el entrenamiento
source_url: https://www.php.net/manual/es/function.fann-get-train-stop-function.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-train-stop-function.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21560
---

fann_get_train_stop_function

Devuelve la función de parada empleada durante el entrenamiento

## Descripción

```php
fann_get_train_stop_function(resource $ann): int
```php

Devuelve la función de parada empleada durante el entrenamiento.

Las funciones de parada están descritas en las constantes de [funciones de parada](#constants.fann-stopfunc).

La función de parada predeterminada es `FANN_STOPFUNC_MSE`.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

La constante de [función de parada](#constants.fann-stopfunc), o `false` en caso de error.

## Véase también

`fann_set_train_stop_function`
