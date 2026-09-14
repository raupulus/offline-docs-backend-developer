---
title: Componere\Definition::getClosure
description: Obtener Cierre
source_url: https://www.php.net/manual/es/componere-definition.getclosure.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/componere/componere/definition/getclosure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: componere
translation_status: ready
translation_revision: 6dcc757d9
order: 8110
---

Componere\Definition::getClosure

Obtener Cierre

## Descripción

```php
public Componere\Definition::getClosure(string $name): Closure
```php

Devolverá un cierre para el método especificado por el nombre

## Parámetros

`name`  
El nombre del método insensible a las mayúsculas y minúsculas

## Valores devueltos

Un cierre vinculado al alcance correcto

## Excepciones

> [!WARNING]
> Lanzará `RuntimeException` si `Definition` se registró

> [!WARNING]
> Lanzará `RuntimeException` si `name` no se pudo encontrar
