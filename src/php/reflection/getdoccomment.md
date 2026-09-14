---
title: ReflectionClass::getDocComment
description: Recupera los comentarios de documentación
source_url: https://www.php.net/manual/es/reflectionclass.getdoccomment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getdoccomment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69120
---

ReflectionClass::getDocComment

Recupera los comentarios de documentación

## Descripción

```php
public ReflectionClass::getDocComment(): string
```php

Recupera los comentarios de documentación desde una clase. Los comentarios de documentación comienzan con `/**`. Si existen varios comentarios de documentación por encima de la definición de la clase, se tomará el más cercano a la clase.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El comentario de documentación, si existe, `false` en caso contrario.

## Ejemplos

Ejemplo con ReflectionClass::getDocComment

```
<?php
/**
 * Una clase de prueba
 *
 * @param  foo bar
 * @return baz
 */
class TestClass { }

$rc = new ReflectionClass('TestClass');
var_dump($rc->getDocComment());
?>

    
```php

El ejemplo anterior mostrará:

    string(61) "/**
     * Una clase de prueba
     *
     * @param  foo bar
     * @return baz
     */"

## Véase también

ReflectionClass::getName
