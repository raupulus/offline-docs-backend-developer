---
title: fann_reset_errno
description: Reinicia el número del último error
source_url: https://www.php.net/manual/es/function.fann-reset-errno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-reset-errno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21660
---

fann_reset_errno

Reinicia el número del último error

## Descripción

```php
fann_reset_errno(resource $errdat): void
```php

Reinicia el número del último error.

## Parámetros

`errdat`  
O bien un `resource` de red neuronal, o un `resource` de datos de entrenamiento de red neuronal.

## Valores devueltos

No devuelve ningún valor.

## Véase también

`fann_get_errno`, `fann_reset_errstr`
