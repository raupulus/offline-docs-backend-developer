---
title: fann_get_layer_array
description: Obtener el número de neuronas de cada capa de la red
source_url: https://www.php.net/manual/es/function.fann-get-layer-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-layer-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 21340
---

fann_get_layer_array

Obtener el número de neuronas de cada capa de la red

## Descripción

```php
fann_get_layer_array(resource $ann): array
```php

Obtener el número de neuronas de cada capa de la red neuronal.

Las tendencias no se incluyen, coincidiendo así las capas con las funciones fann_create.

## Parámetros

`ann`  
Un `resource` de red neuronal.

## Valores devueltos

Un array de números de neuronas en cada capa.
