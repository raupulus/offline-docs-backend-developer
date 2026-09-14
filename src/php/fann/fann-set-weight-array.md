---
title: fann_set_weight_array
description: Establecer las conexiones de la red
source_url: https://www.php.net/manual/es/function.fann-set-weight-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-weight-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22210
---

fann_set_weight_array

Establecer las conexiones de la red

## Descripción

```php
fann_set_weight_array(resource $ann, array $connections): bool
```php

Establecer las conexiones de la red.

Solamente se pueden cambiar los pesos. Las conexiones y los pesos se ignoran si no existen en la red.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`connections`  
Un array de objetos `FANNConnection`

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.
