---
title: fann_set_train_stop_function
description: Establece la función de parada empleada durante el entrenamiento
source_url: https://www.php.net/manual/es/function.fann-set-train-stop-function.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-train-stop-function.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22190
---

fann_set_train_stop_function

Establece la función de parada empleada durante el entrenamiento

## Descripción

```php
fann_set_train_stop_function(resource $ann, int $stop_function): bool
```php

Establece la función de parada empleada durante el entrenamiento.

Las funciones de parada están descritas en las constantes de [funciones de parada](#constants.fann-stopfunc).

## Parámetros

`ann`  
Un `resource` de red neuronal.

`stop_function`  
La constante de [función de parada](#constants.fann-stopfunc).

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_train_stop_function`
