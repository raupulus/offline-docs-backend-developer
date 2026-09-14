---
title: Spoofchecker::setRestrictionLevel
description: Establece el nivel de restricción
source_url: https://www.php.net/manual/es/spoofchecker.setrestrictionlevel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/spoofchecker/setrestrictionlevel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 99a4fb21d
order: 42510
---

Spoofchecker::setRestrictionLevel

Establece el nivel de restricción

## Descripción

```php
public Spoofchecker::setRestrictionLevel(int $level): void
```php

Establece el nivel de restricción de SpoofChecker::isSuspicious.

## Parámetros

`level`  
El nivel de restricción de SpoofChecker::isSuspicious. Uno de los siguientes: `Spoofchecker::ASCII`, `Spoofchecker::SINGLE_SCRIPT_RESTRICTIVE`, `Spoofchecker::HIGHLY_RESTRICTIVE`, `Spoofchecker::MODERATELY_RESTRICTIVE`, `Spoofchecker::MINIMALLY_RESTRICTIVE`, o `Spoofchecker::UNRESTRICTIVE`. Por omisión `Spoofchecker::HIGHLY_RESTRICTIVE`.

## Valores devueltos

No se retorna ningún valor.
