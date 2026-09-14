---
title: runkit7_object_id
description: Devuelve el identificador de objeto para un objeto dado
source_url: https://www.php.net/manual/es/function.runkit7-object-id.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/functions/runkit7-object-id.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_reviewed: true
translation_revision: c4625323f
order: 72980
---

runkit7_object_id

Devuelve el identificador de objeto para un objeto dado

## Descripción

```php
runkit7_object_id(object $obj): int
```php

Esta función es equivalente a `spl_object_id`.

Esta función devuelve un identificador único para el objeto. El identificador de objeto es único durante la vida del objeto. Una vez destruido el objeto, su identificador puede ser reutilizado para otros objetos. Este comportamiento es similar a `spl_object_hash`.

## Parámetros

`obj`  
Un objeto cualquiera.

## Valores devueltos

Un identificador entero que es único para cada objeto actualmente existente y siempre es el mismo para cada objeto.

## Notas

> [!NOTE]
> Cuando un objeto es destruido, su identificador puede ser reutilizado para otros objetos.

## Véase también

spl_object_id
