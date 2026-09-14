---
title: Componere\cast_by_ref
description: Moldeado
source_url: https://www.php.net/manual/es/componere.cast_by_ref.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/componere/functions/componere.cast_by_ref.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: componere
translation_status: ready
translation_revision: 6dcc757d9
order: 8420
---

Componere\cast_by_ref

Moldeado

## Descripción

```php
Componere\cast_by_ref(string $type, object $object): object
```php

## Parámetros

type  
Un tipo definido por el usuario

`object`  
Un objeto con un tipo definido por el usuario compatible con Type

## Valores devueltos

Un `object` de tipo Type, moldeado de `object`, donde los miembros son referencias a miembros de `object`

## Errores/Excepciones

> [!WARNING]
> Lanzará `InvalidArgumentException` si el tipo de `object` es o se deriva de una clase interna

> [!WARNING]
> Lanzará `InvalidArgumentException` si Type es una interface

> [!WARNING]
> Lanzará `InvalidArgumentException` si Type es un rasgo

> [!WARNING]
> Lanzará `InvalidArgumentException` si Type es una abstracta

> [!WARNING]
> Lanzará `InvalidArgumentException` si Type no es compatible con el tipo de `object`

## Véase también
