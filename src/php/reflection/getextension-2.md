---
title: ReflectionConstant::getExtension
description: Devuelve la ReflectionExtension de la extensión definitoria
source_url: https://www.php.net/manual/es/reflectionconstant.getextension.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionconstant/getextension.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c477749c8
order: 69900
---

ReflectionConstant::getExtension

Devuelve la

ReflectionExtension

de la extensión definitoria

## Descripción

```php
public ReflectionConstant::getExtension(): ReflectionExtension
```php

Devuelve un objeto `ReflectionExtension` para la extensión que ha definido la constante.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto `ReflectionExtension` que representa la extensión que ha definido la constante, o `null` para las constantes definidas por el usuario.

## Ejemplos

Uso básico de ReflectionConstant::getExtension

```
<?php
var_dump((new ReflectionConstant('SQLITE3_TEXT'))->getExtension());
?>

   
```php

El ejemplo anterior mostrará:

    object(ReflectionExtension)#2 (1) {
      ["name"]=>
      string(7) "sqlite3"
    }

## Véase también

ReflectionConstant::getExtensionName
