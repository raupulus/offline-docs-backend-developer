---
title: IntlDatePatternGenerator::create
description: Crear una nueva instancia de IntlDatePatternGenerator
source_url: https://www.php.net/manual/es/intldatepatterngenerator.create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intldatepatterngenerator/create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41300
---

IntlDatePatternGenerator::create

IntlDatePatternGenerator::\_\_construct

Crear una nueva instancia de IntlDatePatternGenerator

## Descripción

```php
public static IntlDatePatternGenerator::create([string $locale]): IntlDatePatternGenerator
```php

```php
public IntlDatePatternGenerator::__construct([string $locale])
```

Crea una nueva instancia de `IntlDatePatternGenerator`.

## Parámetros

`locale`  
La configuración local/regional. Si se pasa `null`, se utiliza el parámetro ini [intl.default_locale](#ini.intl.default-locale).

## Valores devueltos

Devuelve una instancia de `IntlDatePatternGenerator` en caso de éxito, o `null` en caso de error.
