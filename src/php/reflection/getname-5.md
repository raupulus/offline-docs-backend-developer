---
title: ReflectionExtension::getName
description: Obtiene el nombre de la extensión
source_url: https://www.php.net/manual/es/reflectionextension.getname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionextension/getname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70240
---

ReflectionExtension::getName

Obtiene el nombre de la extensión

## Descripción

```php
public ReflectionExtension::getName(): string
```php

Obtiene el nombre de la extensión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nombre de la extensión.

## Ejemplos

Ejemplo con ReflectionExtension::getName

```
<?php
$ext = new ReflectionExtension('mysqli');
var_dump($ext->getName());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(6) "mysqli"

## Véase también

ReflectionExtension::getClassNames
