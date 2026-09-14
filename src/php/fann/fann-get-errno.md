---
title: fann_get_errno
description: Devuelve el número del último error
source_url: https://www.php.net/manual/es/function.fann-get-errno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-get-errno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 21320
---

fann_get_errno

Devuelve el número del último error

## Descripción

```php
fann_get_errno(resource $errdat): int
```php

Devuelve el número del último error.

## Parámetros

`errdat`  
O bien un `resource` de red neuronal, o un `resource` de datos de entrenamiento de red neuronal.

## Valores devueltos

El número de error, o `false` en caso de error.

## Véase también

`fann_reset_errno`, `fann_get_errstr`
