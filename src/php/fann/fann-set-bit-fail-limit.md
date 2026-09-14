---
title: fann_set_bit_fail_limit
description: Establece el límite de fallo de bit empleado durante un entrenamiento
source_url: https://www.php.net/manual/es/function.fann-set-bit-fail-limit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-bit-fail-limit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21860
---

fann_set_bit_fail_limit

Establece el límite de fallo de bit empleado durante un entrenamiento

## Descripción

```php
fann_set_bit_fail_limit(resource $ann, float $bit_fail_limit): bool
```php

Establece el límite de fallo de bit empleado durante un entrenamiento.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`bit_fail_limit`  
El límite de fallo de bit.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_get_bit_fail_limit`
