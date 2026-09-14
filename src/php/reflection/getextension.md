---
title: ReflectionClass::getExtension
description: Obtiene un objeto ReflectionExtension para la extensión que define la
  clase
source_url: https://www.php.net/manual/es/reflectionclass.getextension.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getextension.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69140
---

ReflectionClass::getExtension

Obtiene un objeto

ReflectionExtension

para la extensión que define la clase

## Descripción

```php
public ReflectionClass::getExtension(): ReflectionExtension
```php

Obtiene un objeto `ReflectionExtension` para la extensión que define la clase.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto `ReflectionExtension` que representa la extensión que define la clase, o `null` para las clases definidas por el usuario.

## Ejemplos

Uso simple de ReflectionClass::getExtension

```
<?php
$class = new ReflectionClass('ReflectionClass');
$extension = $class->getExtension();
var_dump($extension);
?>

    
```php

El ejemplo anterior mostrará:

    object(ReflectionExtension)#2 (1) {
      ["name"]=>
      string(10) "Reflection"
    }

## Véase también

ReflectionClass::getExtensionName
