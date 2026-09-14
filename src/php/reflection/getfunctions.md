---
title: ReflectionExtension::getFunctions
description: Obtiene las funciones de una extensión
source_url: https://www.php.net/manual/es/reflectionextension.getfunctions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionextension/getfunctions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70220
---

ReflectionExtension::getFunctions

Obtiene las funciones de una extensión

## Descripción

```php
public ReflectionExtension::getFunctions(): array
```php

Obtiene las funciones de una extensión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array asociativo de objetos `ReflectionFunction`, para cada función definida en la extensión, cuyas claves son los nombres de las funciones. Si no hay funciones definidas, se devuelve un array vacío.

## Ejemplos

Ejemplo con ReflectionExtension::getFunctions

```
<?php
$dom = new ReflectionExtension('SimpleXML');

print_r($dom->getFunctions());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [simplexml_load_file] => ReflectionFunction Object
            (
                [name] => simplexml_load_file
            )

        [simplexml_load_string] => ReflectionFunction Object
            (
                [name] => simplexml_load_string
            )

        [simplexml_import_dom] => ReflectionFunction Object
            (
                [name] => simplexml_import_dom
            )

    )

## Véase también

ReflectionExtension::getClasses, `get_extension_funcs`
