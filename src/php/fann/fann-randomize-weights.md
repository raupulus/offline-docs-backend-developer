---
title: fann_randomize_weights
description: Dar a cada conexión un peso aleatorio entre min_weight y max_weight
source_url: https://www.php.net/manual/es/function.fann-randomize-weights.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-randomize-weights.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21640
---

fann_randomize_weights

Dar a cada conexión un peso aleatorio entre min_weight y max_weight

## Descripción

```php
fann_randomize_weights(resource $ann, float $min_weight, float $max_weight): bool
```php

Dar a cada conexión un peso aleatorio entre `min_weight` y `max_weight`.

Desde el comienzo, los pesos son aleatorios, entre -0.1 y 0.1.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`min_weight`  
El valor del peso máximo.

`max_weight`  
El valor del peso mínimo.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_init_weights`
