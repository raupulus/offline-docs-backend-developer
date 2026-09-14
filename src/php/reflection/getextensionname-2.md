---
title: ReflectionConstant::getExtensionName
description: Devuelve el nombre de la extensión definitoria
source_url: https://www.php.net/manual/es/reflectionconstant.getextensionname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionconstant/getextensionname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c477749c8
order: 69910
---

ReflectionConstant::getExtensionName

Devuelve el nombre de la extensión definitoria

## Descripción

```php
public ReflectionConstant::getExtensionName(): string
```php

Devuelve el nombre de la extensión que ha definido la constante.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nombre de la extensión que ha definido la constante, o `false` para las constantes definidas por el usuario.

## Ejemplos

Uso básico de ReflectionConstant::getExtensionName

```
<?php
var_dump((new ReflectionConstant('SQLITE3_TEXT'))->getExtensionName());
?>

   
```php

El ejemplo anterior mostrará:

    string(7) "sqlite3"

## Véase también

ReflectionConstant::getExtension
