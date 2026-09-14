---
title: SVMModel::__construct
description: Construye un nuevo objeto SVMModel
source_url: https://www.php.net/manual/es/svmmodel.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svm/svmmodel/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svm
translation_status: ready
translation_reviewed: false
translation_revision: 1ca2d4af9
order: 89760
---

SVMModel::\_\_construct

Construye un nuevo objeto SVMModel

## Descripción

```php
public SVMModel::__construct([string $filename])
```php

Construye un nuevo objeto SVMModel. Los modelos se construyen generalmente desde la función SVM::train, mientras que los modelos guardados pueden ser restaurados directamente.

## Parámetros

`filename`  
El nombre del archivo para el modelo guardado a cargar.

## Errores/Excepciones

Lanza una excepción `SVMException` si ocurre un error.

## Véase también

SVMModel::load
