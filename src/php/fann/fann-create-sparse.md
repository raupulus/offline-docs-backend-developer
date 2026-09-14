---
title: fann_create_sparse
description: Crea una red neuronal de retropropagación estándar que no está conectada
  completamente
source_url: https://www.php.net/manual/es/function.fann-create-sparse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-create-sparse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 20980
---

fann_create_sparse

Crea una red neuronal de retropropagación estándar que no está conectada completamente

## Descripción

```php
fann_create_sparse(float $connection_rate, int $num_layers, int $num_neurons1, int $num_neurons2, int ...$num_neuronsN): resource
```php

Crea una red neuronal de retropropagación estándar que no está conectada completamente.

## Parámetros

`connection_rate`  
El índice de conexión controla cuántas conexiones habrá en la red. Si el índice de conexión está establecido a 1, la red estará completamente conectada, aunque si está establecida a 0.5, solamente se establecerán la mitad de las conexiones. Un índice de conexión de 1 generará el mismo resultado que `fann_create_standard`.

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

`fann_create_sparse_array`, `fann_create_standard`, `fann_create_shortcut`
