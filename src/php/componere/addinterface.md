---
title: Componere\Abstract\Definition::addInterface
description: Añadir Interface
source_url: https://www.php.net/manual/es/componere-abstract-definition.addinterface.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/componere/componere/abstract/definition/addinterface.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: componere
translation_status: ready
translation_revision: 6dcc757d9
order: 8040
---

Componere\Abstract\Definition::addInterface

Añadir Interface

## Descripción

```php
public Componere\Abstract\Definition::addInterface(string $interface): Definition
```php

Implementará la interface dada en la definición actual

## Parámetros

`interface`  
El nombre de una interface insensible a las mayúsculas y minúsculas

## Valores devueltos

La definición actual

## Excepciones

> [!WARNING]
> Lanzará `RuntimeException` si `Definition` se registró
