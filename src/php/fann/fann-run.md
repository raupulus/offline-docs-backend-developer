---
title: fann_run
description: Ejecutará la entrada a través de la red neuronal
source_url: https://www.php.net/manual/es/function.fann-run.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-run.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21690
---

fann_run

Ejecutará la entrada a través de la red neuronal

## Descripción

```php
fann_run(resource $ann, array $input): array
```php

Ejecutará la entrada a través de la red neuronal, devolviendo un array de salidas, el número de las que son iguales al número de neuronas de la capa de salida.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`input`  
Un array de valores de entrada.

## Valores devueltos

Un array de valores de salida, o `false` en caso de error.
