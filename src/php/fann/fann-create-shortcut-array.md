---
title: fann_create_shortcut_array
description: Crea una red neuronal de retropropagación estándar que no está completamente
  conectada y que posee conexiones de atajo
source_url: https://www.php.net/manual/es/function.fann-create-shortcut-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-create-shortcut-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 20950
---

fann_create_shortcut_array

Crea una red neuronal de retropropagación estándar que no está completamente conectada y que posee conexiones de atajo

## Descripción

```php
fann_create_shortcut_array(int $num_layers, array $layers): resource
```php

Crea una red neuronal de retropropagación estándar que no está completamente conectada y que tiene conexiones de atajo, empleando un array con tamaños de capas.

## Parámetros

`num_layers`  
El número total de capas incluyendo la capa de entrada y de salida.

`layers`  
Un array con los tamaños de las capas.

## Valores devueltos

Devuelve un recurso de red neuronal en caso de éxito, o `false` en caso de error.

## Véase también

`fann_create_shortcut`, `fann_create_sparse`, `fann_create_standard`
