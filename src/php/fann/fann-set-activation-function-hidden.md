---
title: fann_set_activation_function_hidden
description: Establece la función de activación para todas las capas ocultas
source_url: https://www.php.net/manual/es/function.fann-set-activation-function-hidden.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-activation-function-hidden.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21780
---

fann_set_activation_function_hidden

Establece la función de activación para todas las capas ocultas

## Descripción

```php
fann_set_activation_function_hidden(resource $ann, int $activation_function): bool
```php

Establece la función de activación para todas las capas ocultas.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`activation_function`  
La constante de [funciones de activación](#constants.fann-activation-funcs).

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_set_activation_function`, `fann_set_activation_function_layer`, `fann_set_activation_function_output`, `fann_set_activation_steepness`
