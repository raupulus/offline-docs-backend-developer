---
title: ReflectionClass::getTraitAliases
description: Devuelve un array de alias del trait
source_url: https://www.php.net/manual/es/reflectionclass.gettraitaliases.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/gettraitaliases.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ca840c9a6
order: 69340
---

ReflectionClass::getTraitAliases

Devuelve un array de alias del trait

## Descripción

```php
public ReflectionClass::getTraitAliases(): array
```php

Obtiene un array de alias de métodos definidos en la clase actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array con los nuevos nombres de métodos como claves y los nombres originales como valores (en formato `"TraitName::original"`).
