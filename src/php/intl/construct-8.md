---
title: Transliterator::__construct
description: Constructor privado para prohibir la instanciación
source_url: https://www.php.net/manual/es/transliterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/transliterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42530
---

Transliterator::\_\_construct

Constructor privado para prohibir la instanciación

## Descripción

```php
final private Transliterator::__construct()
```php

Este método no debe ser llamado. Su único propósito es prohibir la instanciación con el operador [new](#language.oop5.basic.new).

Utilícense los métodos factorizados Transliterator::create y Transliterator::createFromRules en su lugar.

## Parámetros

Esta función no contiene ningún parámetro.

## Véase también

Transliterator::create, Transliterator::createFromRules
