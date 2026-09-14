---
title: fann_get_train_error_function
description: Devuelve la función de error empleada durante un entrenamiento
source_url: https://www.php.net/manual/es/function.fann-get-train-error-function.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-train-error-function.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21550
---

fann_get_train_error_function

Devuelve la función de error empleada durante un entrenamiento

## Descripción

```php
fann_get_train_error_function(resource $ann): int
```php

Devuelve la función de error empleada durante un entrenamiento.

Las funciones de error están descritas en las constantes de [funciones de error](#constants.fann-errorfunc).

La función de error predeteminada es `FANN_ERRORFUNC_TANH`.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

La constante de [función de error](#constants.fann-errorfunc), o `false` en caso de error.

## Véase también

`fann_set_train_error_function`
