---
title: fann_set_weight
description: Establecer una conexión de la red
source_url: https://www.php.net/manual/es/function.fann-set-weight.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-weight.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 22220
---

fann_set_weight

Establecer una conexión de la red

## Descripción

```php
fann_set_weight(resource $ann, int $from_neuron, int $to_neuron, float $weight): bool
```php

Establecer una conexión de la red.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`from_neuron`  
La neurona donde empiza la conexión.

`to_neuron`  
La neurona donde finaliza la conexión.

`weight`  
El peso de la conexión.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.
