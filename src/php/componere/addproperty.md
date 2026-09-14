---
title: Componere\Definition::addProperty
description: Añade propiedad
source_url: https://www.php.net/manual/es/componere-definition.addproperty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/componere/componere/definition/addproperty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: componere
translation_status: ready
translation_revision: 6dcc757d9
order: 8090
---

Componere\Definition::addProperty

Añade propiedad

## Descripción

```php
public Componere\Definition::addProperty(string $name, Componere\Value $value): Definition
```php

Declarará una propiedad de clase sobre la definición actual

## Parámetros

`name`  
El nombre de la propiedad distingue mayúsculas y minúsculas

`value`  
El valor por omisión de la propiedad

## Valores devueltos

La definición actual

## Excepciones

> [!WARNING]
> Lanzará `RuntimeException` si `Definition` se registró

> [!WARNING]
> Lanzará `RuntimeException` si `name` ya está declarada como una propiedad
