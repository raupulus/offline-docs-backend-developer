---
title: spl_object_hash
description: Devuelve el identificador de hash para un objeto dado
source_url: https://www.php.net/manual/es/function.spl-object-hash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/functions/spl-object-hash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: f7e42edba
order: 82320
---

spl_object_hash

Devuelve el identificador de hash para un objeto dado

## Descripción

```php
spl_object_hash(object $object): string
```php

Esta función devuelve un identificador único para el objeto. Este identificador puede ser utilizado como clave de hash para almacenar los objetos o para identificarlos, mientras el objeto no sea destruido. Una vez destruido el objeto, el identificador puede ser reutilizado para otros objetos. Este comportamiento es similar al de la `spl_object_id`.

## Parámetros

`object`  
Cualquier objeto.

## Valores devueltos

Un `string` único para cada objeto existente y que será siempre idéntico para cada objeto.

## Ejemplos

Ejemplo con `spl_object_hash`

```
<?php
$id = spl_object_hash($object);
$storage[$id] = $object;
?>

    
```php

## Notas

> [!NOTE]
> Cuando un objeto es destruido, su identificador de hash podrá ser reutilizado para otros objetos.

> [!NOTE]
> Los hash de objeto deben ser comparados por su identidad con `===` y `!==`, ya que el hash devuelto podría ser una [cadena numérica](#language.types.numeric-strings). Por ejemplo: `0000000000000e600000000000000000`.

## Véase también

`spl_object_id`
