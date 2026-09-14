---
title: Componere\Abstract\Definition::addMethod
description: Añadir método
source_url: https://www.php.net/manual/es/componere-abstract-definition.addmethod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/componere/componere/abstract/definition/addmethod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: componere
translation_status: ready
translation_revision: 6dcc757d9
order: 8050
---

Componere\Abstract\Definition::addMethod

Añadir método

## Descripción

```php
public Componere\Abstract\Definition::addMethod(string $name, Componere\Method $method): Definition
```php

Creará o anulará un método en la definición actual.

## Parámetros

`name`  
El nombre del método insensible a las mayúsculas y minúsculas

`method`  
`Componere\Method` que no se haya añadido previamente a otra `Definition`

## Valores devueltos

La Definition actual

## Excepciones

> [!WARNING]
> Lanzará `RuntimeException` si `Definition` se registró

> [!WARNING]
> Lanzará `RuntimeException` si el método se añadió a otra definición
