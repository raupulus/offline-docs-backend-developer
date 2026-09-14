---
title: Componere\Definition::addConstant
description: Añade constante
source_url: https://www.php.net/manual/es/componere-definition.addconstant.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/componere/componere/definition/addconstant.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: componere
translation_status: ready
translation_revision: 6dcc757d9
order: 8080
---

Componere\Definition::addConstant

Añade constante

## Descripción

```php
public Componere\Definition::addConstant(string $name, Componere\Value $value): Definition
```php

Declarará una constante de clase en la definición actual

## Parámetros

`name`  
El nombre de la constante que distingue entre mayúsculas y minúsculas

`value`  
El valor de la constante, no debe ser indefinido o estático

## Valores devueltos

La definición actual

## Excepciones

> [!WARNING]
> Lanzará `RuntimeException` si `Definition` fué registrado

> [!WARNING]
> Lanzará `RuntimeException` si `name` ya está declarada como una constante

> [!WARNING]
> Lanzará `RuntimeException` si `value` es estática

> [!WARNING]
> Lanzará `RuntimeException` si `value` no está definida
