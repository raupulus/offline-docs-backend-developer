---
title: ReflectionConstant::isDeprecated
description: Verifica la deprecación
source_url: https://www.php.net/manual/es/reflectionconstant.isdeprecated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionconstant/isdeprecated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c477749c8
order: 69970
---

ReflectionConstant::isDeprecated

Verifica la deprecación

## Descripción

```php
public ReflectionConstant::isDeprecated(): bool
```php

Verifica si la constante está deprecada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si está deprecada, de lo contrario `false`.

## Ejemplos

Ejemplo de ReflectionConstant::isDeprecated

```
<?php
// E_STRICT está deprecado a partir de PHP 8.4
var_dump((new ReflectionConstant('E_STRICT'))->isDeprecated());
?>

   
```php

Salida del ejemplo anterior en PHP 8.4:

    bool(true)
