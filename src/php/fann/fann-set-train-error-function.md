---
title: fann_set_train_error_function
description: Establecer la función de error empleada durante un entrenamiento
source_url: https://www.php.net/manual/es/function.fann-set-train-error-function.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-train-error-function.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22180
---

fann_set_train_error_function

Establecer la función de error empleada durante un entrenamiento

## Descripción

```php
fann_set_train_error_function(resource $ann, int $error_function): bool
```php

Establecer la función de error empleada durante un entrenamiento.

Las funciones de error están descritas en las constantes de [funciones de error](#constants.fann-errorfunc).

## Parámetros

`ann`  
Un `resource` de red neuronal.

`error_function`  
La constante de [función de error](#constants.fann-errorfunc) .

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_train_error_function`
