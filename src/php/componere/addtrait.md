---
title: Componere\Abstract\Definition::addTrait
description: Añadir rasgo
source_url: https://www.php.net/manual/es/componere-abstract-definition.addtrait.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/componere/componere/abstract/definition/addtrait.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: componere
translation_status: ready
translation_revision: 6dcc757d9
order: 8060
---

Componere\Abstract\Definition::addTrait

Añadir rasgo

## Descripción

```php
public Componere\Abstract\Definition::addTrait(string $trait): Definition
```php

Usará el rasgo dado para la definición actual

## Parámetros

`trait`  
El nombre del rasgo insensible a las mayúsculas y minúsculas

## Valores devueltos

La definición actual

## Excepciones

> [!WARNING]
> Lanzará `RuntimeException` si `Definition` se registró
