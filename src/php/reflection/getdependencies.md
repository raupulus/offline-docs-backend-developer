---
title: ReflectionExtension::getDependencies
description: Obtiene las dependencias
source_url: https://www.php.net/manual/es/reflectionextension.getdependencies.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionextension/getdependencies.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70210
---

ReflectionExtension::getDependencies

Obtiene las dependencias

## Descripción

```php
public ReflectionExtension::getDependencies(): array
```php

Obtiene las dependencias, listando tanto las dependencias requeridas como las dependencias en conflicto.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` asociativo cuyas claves son las dependencias y como valores, `Required`, `Optional` o `Conflicts`.

## Ejemplos

Ejemplo con ReflectionExtension::getDependencies

```
<?php
$dom = new ReflectionExtension('dom');

print_r($dom->getDependencies());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [libxml] => Required
        [domxml] => Conflicts
    )

## Véase también

ReflectionClass::getVersion
