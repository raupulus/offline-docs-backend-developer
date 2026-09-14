---
title: fann_set_sarprop_temperature
description: Establece la temperatura de sarprop
source_url: https://www.php.net/manual/es/function.fann-set-sarprop-temperature.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/functions/fann-set-sarprop-temperature.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: false
translation_revision: 242efce0d
order: 22150
---

fann_set_sarprop_temperature

Establece la temperatura de sarprop

## Descripción

```php
fann_set_sarprop_temperature(resource $ann, float $sarprop_temperature): bool
```php

Establece la temperatura de sarprop.

## Parámetros

`ann`  
Un `resource` de red neuronal.

`sarprop_temperature`  
La temperatura de sarprop.

## Valores devueltos

Devuelve `true` en caso de éxito, `false` de lo contrario.

## Notas

> [!NOTE]
> Esta función ahora está disponible si la extensión fann ha sido compilada con libfann \>= 2.2.

## Véase también

`fann_get_sarprop_temperature`
