---
title: SVMModel::save
description: Guardar un modelo en un archivo
source_url: https://www.php.net/manual/es/svmmodel.save.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svm/svmmodel/save.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svm
translation_status: ready
translation_revision: 1ca2d4af9
order: 89840
---

SVMModel::save

Guardar un modelo en un archivo

## Descripción

```php
public SVMModel::save(string $filename): bool
```php

Guardar los datos del modelo en un archivo, para su uso posterior.

## Parámetros

`filename`  
El archivo para guardar el modelo.

## Valores devueltos

Lanza SVMException en caso de error. Devuelve true en caso de éxito.

## Véase también

SVMModel::load
