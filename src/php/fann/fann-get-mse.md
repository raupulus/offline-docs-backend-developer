---
title: fann_get_MSE
description: Lee el error cuadrático medio de la red
source_url: https://www.php.net/manual/es/function.fann-get-mse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-mse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21370
---

fann_get_MSE

Lee el error cuadrático medio de la red

## Descripción

```php
fann_get_MSE(resource $ann): float
```php

Lee el error cuadrático medio de la red.

Este valor se calcula durante un entrenamiento o una prueba, por lo que a veces puede estar un poco alejados si los pesos han cambiado desde el último cálculo de este valor.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

El error cuadrático medio, o `false` en caso de error.

## Véase también

`fann_test_data`
