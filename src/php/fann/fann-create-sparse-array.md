---
title: fann_create_sparse_array
description: Crea una red neuronal de retropropagación estándar que no está completamente
  conectada empleando un array con tamaños de capas
source_url: https://www.php.net/manual/es/function.fann-create-sparse-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-create-sparse-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 20970
---

fann_create_sparse_array

Crea una red neuronal de retropropagación estándar que no está completamente conectada empleando un array con tamaños de capas

## Descripción

```php
fann_create_sparse_array(float $connection_rate, int $num_layers, array $layers): resource
```php

Crea una red neuronal de retropropagación estándar que no está completamente conectada empleando un array con tamaños de capas

## Parámetros

`connection_rate`  
El índice de conexión controla cuántas conexiones habrá en la red. Si el índice de conexión está establecido a 1, la red estará completamente conectada, aunque si está establecida a 0.5, solamente se establecerán la mitad de las conexiones. Un índice de conexión de 1 generará el mismo resultado que `fann_create_standard`.

`num_layers`  
El número total de capas incluyendo la capa de entrada y de salida.

`layers`  
Un array con los tamaños de las capas.

## Valores devueltos

Devuelve un recurso de red neuronal en caso de éxito, o `false` en caso de error.

## Véase también

`fann_create_sparse`, `fann_create_standard`, `fann_create_shortcut`
