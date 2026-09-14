---
title: SVMModel::getSvrProbability
description: Recupera el valor sigma para los tipos de regresión
source_url: https://www.php.net/manual/es/svmmodel.getsvrprobability.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svm/svmmodel/getsvrprobability.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svm
translation_status: ready
translation_reviewed: false
translation_revision: 1ca2d4af9
order: 89800
---

SVMModel::getSvrProbability

Recupera el valor sigma para los tipos de regresión

## Descripción

```php
public SVMModel::getSvrProbability(): float
```php

Para los modelos de regresión, devuelve un valor sigma; Si no hay información de probabilidad o el modelo no es SVR, 0 será devuelto.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un valor sigma.
