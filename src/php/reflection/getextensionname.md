---
title: ReflectionClass::getExtensionName
description: Obtiene el nombre de la extensión que define la clase
source_url: https://www.php.net/manual/es/reflectionclass.getextensionname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getextensionname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69150
---

ReflectionClass::getExtensionName

Obtiene el nombre de la extensión que define la clase

## Descripción

```php
public ReflectionClass::getExtensionName(): string
```php

Obtiene el nombre de la extensión que define la clase.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nombre de la extensión que define la clase, o `false` para las clases definidas por el usuario.

## Ejemplos

Uso simple de ReflectionClass::getExtensionName

```
<?php
$class = new ReflectionClass('ReflectionClass');
$extension = $class->getExtensionName();
var_dump($extension);
?>

    
```php

El ejemplo anterior mostrará:

    string(10) "Reflection"

## Véase también

ReflectionClass::getExtension
