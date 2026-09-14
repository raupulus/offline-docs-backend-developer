---
title: ReflectionExtension::getClasses
description: Obtiene las clases
source_url: https://www.php.net/manual/es/reflectionextension.getclasses.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionextension/getclasses.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70180
---

ReflectionExtension::getClasses

Obtiene las clases

## Descripción

```php
public ReflectionExtension::getClasses(): array
```php

Obtiene una lista de las clases de una extensión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de objetos `ReflectionClass`, uno por cada clase definida en la extensión. Si no se define ninguna clase, se devolverá un array vacío.

## Ejemplos

Ejemplo con ReflectionExtension::getClasses

```
<?php
$ext = new ReflectionExtension('XMLWriter');
var_dump($ext->getClasses());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      ["XMLWriter"]=>
      object(ReflectionClass)#2 (1) {
        ["name"]=>
        string(9) "XMLWriter"
      }
    }

## Véase también

ReflectionExtension::getClassNames
