---
title: Spoofchecker::setChecks
description: Especifica las verificaciones a realizar
source_url: https://www.php.net/manual/es/spoofchecker.setchecks.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/spoofchecker/setchecks.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42500
---

Spoofchecker::setChecks

Especifica las verificaciones a realizar

## Descripción

```php
public Spoofchecker::setChecks(int $checks): void
```php

Define los controles que serán realizados por SpoofChecker::isSuspicious.

## Parámetros

`checks`  
Los controles que serán realizados por SpoofChecker::isSuspicious. Una máscara de bits de `Spoofchecker::SINGLE_SCRIPT_CONFUSABLE`, `Spoofchecker::MIXED_SCRIPT_CONFUSABLE`, `Spoofchecker::WHOLE_SCRIPT_CONFUSABLE`, `Spoofchecker::ANY_CASE`, `Spoofchecker::SINGLE_SCRIPT`, `Spoofchecker::INVISIBLE` o `Spoofchecker::CHAR_LIMIT`. Por omisión, todas las verificaciones a partir de ICU 58; antes de esta versión, `Spoofchecker::SINGLE_SCRIPT` estaba excluido.

## Valores devueltos

No se retorna ningún valor.
