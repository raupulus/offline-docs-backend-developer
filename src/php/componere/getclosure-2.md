---
title: Componere\Patch::getClosure
description: Obtener Cierre
source_url: https://www.php.net/manual/es/componere-patch.getclosure.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/componere/componere/patch/getclosure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: componere
translation_status: ready
translation_revision: 6dcc757d9
order: 8230
---

Componere\Patch::getClosure

Obtener Cierre

## Descripción

```php
public Componere\Patch::getClosure(string $name): Closure
```php

Devolverá un cierre para el método especificado por el nombre

## Parámetros

`name`  
El nombre del método insensible a las mayúsculas y minúsculas

## Valores devueltos

Un cierre vinculado al ámbito y objeto correctos

## Excepciones

> [!WARNING]
> Lanzará `RuntimeException` si `name` no se pudo encontrar
