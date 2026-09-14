---
title: ReflectionClass::getEndLine
description: Obtiene el final de una línea
source_url: https://www.php.net/manual/es/reflectionclass.getendline.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getendline.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69130
---

ReflectionClass::getEndLine

Obtiene el final de una línea

## Descripción

```php
public ReflectionClass::getEndLine(): int
```php

Obtiene el número de la última línea desde una definición de clase, definida por el usuario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El número de la última línea desde una definición de clase, definida por el usuario, o `false` si es desconocido.

## Ejemplos

Ejemplo con ReflectionClass::getEndLine

```
<?php
// Clase de prueba
class TestClass { }

$rc = new ReflectionClass('TestClass');

echo $rc->getEndLine();
?>

    
```php

El ejemplo anterior mostrará:

    3

## Véase también

ReflectionClass::getStartLine
