---
title: fann_create_standard_array
description: Crea una red neuronal de retropropagación estándar completamente conectada
  empleando un array con tamaños de capas
source_url: https://www.php.net/manual/es/function.fann-create-standard-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-create-standard-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 20990
---

fann_create_standard_array

Crea una red neuronal de retropropagación estándar completamente conectada empleando un array con tamaños de capas

## Descripción

```php
fann_create_standard_array(int $num_layers, array $layers): resource
```php

Crea una red neuronal de retropropagación estándar completamente conectada.

Habrá una neurona de tendencia en cada capa (excepto en la de salida), y dicha neurona estará conectada a todas las neuronas de la siguiente capa. Al ejecutar la red, los nodos de tendencia siempre emiten 1.

Para destruir una red neuronal, utilice la función `fann_destroy`.

## Parámetros

`num_layers`  
El número total de capas incluyendo la capa de entrada y de salida.

`layers`  
Un array con los tamaños de las capas.

## Valores devueltos

Devuelve un recurso de red neuronal en caso de éxito, o `false` en caso de error.

## Véase también

`fann_create_standard`, `fann_create_sparse`, `fann_create_shortcut`
