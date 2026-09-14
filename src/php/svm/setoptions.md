---
title: SVM::setOptions
description: Define argumentos de entrenamiento
source_url: https://www.php.net/manual/es/svm.setoptions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svm/svm/setoptions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svm
translation_status: ready
translation_reviewed: false
translation_revision: 1ca2d4af9
order: 89710
---

SVM::setOptions

Define argumentos de entrenamiento

## Descripción

```php
public SVM::setOptions(array $params): bool
```php

Define uno o más argumentos de entrenamiento.

## Parámetros

`params`  
Un array de argumentos de entrenamiento, cuyos claves son las constantes SVM.

## Valores devueltos

Devuelve `true` en caso de éxito, y lanza una excepción SVMException si ocurre un error.
