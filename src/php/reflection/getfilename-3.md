---
title: ReflectionFunctionAbstract::getFileName
description: Obtiene el nombre del fichero
source_url: https://www.php.net/manual/es/reflectionfunctionabstract.getfilename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunctionabstract/getfilename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 70570
---

ReflectionFunctionAbstract::getFileName

Obtiene el nombre del fichero

## Descripción

```php
public ReflectionFunctionAbstract::getFileName(): string
```php

Obtiene el nombre del fichero desde una función definida en el espacio de usuario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre del fichero en el que la función ha sido definida. Si la función es definida en el núcleo de PHP o una extensión PHP, `false` es devuelto.

## Véase también

ReflectionFunctionAbstract::getNamespaceName
