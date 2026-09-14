---
title: spl_object_id
description: Devuelve el gestor de objeto entero para un objeto dado
source_url: https://www.php.net/manual/es/function.spl-object-id.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/functions/spl-object-id.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 60809ebcf
order: 82330
---

spl_object_id

Devuelve el gestor de objeto entero para un objeto dado

## Descripción

```php
spl_object_id(object $object): int
```php

Esta función devuelve un identificador único para el objeto. El id del objeto es único durante la vida del objeto. Una vez que el objeto es destruido, su id puede ser reutilizado para otros objetos. Este comportamiento es similar a `spl_object_hash`.

## Parámetros

`object`  
Cualquier objeto.

## Valores devueltos

Un identificador entero que es único para cada objeto actualmente existente y siempre el mismo para cada objeto.

## Ejemplos

Un ejemplo de `spl_object_id`

```
<?php
$id = spl_object_id($object);
$storage[$id] = $object;
?>

    
```php

## Notas

> [!NOTE]
> Cuando un objeto es destruido, su id puede ser reutilizado para otros objetos.
