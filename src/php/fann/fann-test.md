---
title: fann_test
description: Realiza una prueba con un conjunto de entradas y un conjunto de salidas
  deseadas
source_url: https://www.php.net/manual/es/function.fann-test.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-test.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 22260
---

fann_test

Realiza una prueba con un conjunto de entradas y un conjunto de salidas deseadas

## Descripción

```php
fann_test(resource $ann, array $input, array $desired_output): array
```php

Realiza una prueba con un conjunto de entradas y un conjunto de salidas deseadas. Esta operación actualiza el error cuadrático medio, pero no modifica de ninguna manera la red.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`input`  
Un array de entradas. Este array debe tener una longitud exacta de `fann_get_num_input`.

`desired_output`  
Un array de salidas deseadas. Este array debe tener una longitud exacta de `fann_get_num_output`.

## Valores devueltos

Devuelve las salidas de prueba en caso de éxito, o `false` en caso de error.

## Véase también

`fann_test_data`, `fann_train`, `fann_get_num_input`, `fann_get_num_output`
