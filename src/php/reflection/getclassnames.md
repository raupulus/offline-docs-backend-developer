---
title: ReflectionExtension::getClassNames
description: Obtiene los nombres de las clases
source_url: https://www.php.net/manual/es/reflectionextension.getclassnames.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionextension/getclassnames.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70190
---

ReflectionExtension::getClassNames

Obtiene los nombres de las clases

## Descripción

```php
public ReflectionExtension::getClassNames(): array
```php

Obtiene una lista de los nombres de clases definidas en la extensión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` de nombres de clases, como se definen en la extensión. Si no se define ninguna clase, se devuelve un array vacío.

## Ejemplos

Ejemplo con ReflectionExtension::getClassNames

```
<?php
$ext = new ReflectionExtension('XMLWriter');
var_dump($ext->getClassNames());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      [0]=>
      string(9) "XMLWriter"
    }

## Véase también

ReflectionExtension::getClasses, ReflectionExtension::getName
