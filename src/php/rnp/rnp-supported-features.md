---
title: rnp_supported_features
description: Devuelve las funcionalidades soportadas en formato JSON
source_url: https://www.php.net/manual/es/function.rnp-supported-features.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-supported-features.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72370
---

rnp_supported_features

Devuelve las funcionalidades soportadas en formato JSON

## Descripción

```php
rnp_supported_features(string $type): string
```php

Devuelve el formato JSON que contiene un array de los valores de funcionalidades rnp soportadas (algoritmos, curvas, etc.) por tipo.

## Parámetros

`type`  
Ver las constantes RNP_FEATURE\_\* para los valores soportados.

## Valores devueltos

Un string que contiene un array formateado en JSON de los algoritmos, curvas, etc. soportados o `false` si ocurre un error.
