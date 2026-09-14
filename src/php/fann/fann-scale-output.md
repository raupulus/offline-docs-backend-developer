---
title: fann_scale_output
description: Escalar datos en un vector de entrada antes de alimentarlo a una RNA
  basada en parámetros previamente calculados
source_url: https://www.php.net/manual/es/function.fann-scale-output.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-scale-output.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: ea7caabb1
order: 21750
---

fann_scale_output

Escalar datos en un vector de entrada antes de alimentarlo a una RNA basada en parámetros previamente calculados

## Descripción

```php
fann_scale_output(resource $ann, array $output_vector): bool
```php

Escalar datos en un vector de entrada antes de alimentarlo a una RNA basada en parámetros previamente calculados.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`output_vector`  
El vector de salida a escalar

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Véase también

`fann_descale_output`, `fann_scale_input`
