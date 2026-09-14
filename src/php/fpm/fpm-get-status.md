---
title: fpm_get_status
description: Devuelve el estado actual del pool FPM
source_url: https://www.php.net/manual/es/function.fpm-get-status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fpm/functions/fpm-get-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fpm
translation_status: ready
translation_reviewed: false
translation_revision: 0ba9e74eb
order: 24270
---

fpm_get_status

Devuelve el estado actual del pool FPM

## Descripción

```php
fpm_get_status(): array
```php

Esta función devuelve el estado completo del pool de FPM en forma de un array asociativo. Siempre devuelve el estado completo, incluyendo las informaciones de estado por proceso. Ver el manual de la [página de estado FPM](#fpm.status) para más detalles.

Tenga en cuenta que esta función solo estará definida si FPM se utiliza para servir el script.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Array asociativo que contiene el estado completo del pool FPM, o `false` si ocurre un error.
