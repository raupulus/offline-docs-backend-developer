---
title: fann_init_weights
description: Inicializar los pesos empleando el algoritmo de Widrow + Nguyen
source_url: https://www.php.net/manual/es/function.fann-init-weights.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-init-weights.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21580
---

fann_init_weights

Inicializar los pesos empleando el algoritmo de Widrow + Nguyen

## Descripción

```php
fann_init_weights(resource $ann, resource $train_data): bool
```php

Inicializar los pesos empleando el algoritmo de Widrow + Nguyen.

Esta función tiene un comportamiento similar a `fann_randomize_weights`. Empleará el algoritmo desarrollado por Derrick Nguyen y Bernard Widrow para establecer los pesos de tal forma que aceleren el entrenamiento. Esta técnica no siempre funciona, por lo que en algunos casos puede ser menoes eficiente que una simple inicialización aleatoria.

El algoritmo requiere el acceso al rango de datos de entrada (por ejemplo, entradas mayores y menores), por lo que acepta un segundo parámetro, data, que son los datos de entrenamiento que se emplearán para entrenar la red.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`train_data`  
Un `resource` de datos de entrenamiento de red neuronal.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_randomize_weights`, `fann_read_train_from_file`
