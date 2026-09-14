---
title: SVMModel::load
description: Cargar un modelo SVM guardado
source_url: https://www.php.net/manual/es/svmmodel.load.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svm/svmmodel/load.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svm
translation_status: ready
translation_revision: 1ca2d4af9
order: 89810
---

SVMModel::load

Cargar un modelo SVM guardado

## Descripción

```php
public SVMModel::load(string $filename): bool
```php

Cargar un archivo de un modelo listo para la clasificación o regresión.

## Parámetros

`filename`  
El nombre del modelo.

## Valores devueltos

Lanza SVMException en caso de error. Devuelve true en caso de éxito.

## Véase también

SVMModel::save
