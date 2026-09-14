---
title: fann_create_shortcut
description: Crea una red neuronal de retropropagación estándar que no está completamente
  conectada y que posee conexiones de atajo
source_url: https://www.php.net/manual/es/function.fann-create-shortcut.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-create-shortcut.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 20960
---

fann_create_shortcut

Crea una red neuronal de retropropagación estándar que no está completamente conectada y que posee conexiones de atajo

## Descripción

```php
fann_create_shortcut(int $num_layers, int $num_neurons1, int $num_neurons2, int ...$num_neuronsN): resource
```php

Crea una red neuronal de retropropagación estándar que no está completamente conectada y que también posee conexiones de atajo.

Las conexiones de atajo son conexiones que saltan capas. Una red completamente conectada con conexiones de atajo es una red donde todas las neuronas están conectadas a todas las neuronas de capas posteriores, incluyendo conexiones directas entre la capa de entrada y la de salida.

## Parámetros

`num_layers`  
El número total de capas incluyendo la capa de entrada y de salida.

`num_neurons1`  
El número de neuronas de la primera capa.

`num_neurons2`  
El número de neuronas de la segunda capa.

`num_neuronsN`  
El número de neuronas de la otras capas.

## Valores devueltos

Devuelve un recurso de red neuronal en caso de éxito, o `false` en caso de error.

## Véase también

`fann_create_shortcut_array`, `fann_create_sparse`, `fann_create_standard`
