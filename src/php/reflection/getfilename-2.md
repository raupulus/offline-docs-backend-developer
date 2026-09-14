---
title: ReflectionConstant::getFileName
description: Devuelve el nombre del fichero que define
source_url: https://www.php.net/manual/es/reflectionconstant.getfilename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionconstant/getfilename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c477749c8
order: 69920
---

ReflectionConstant::getFileName

Devuelve el nombre del fichero que define

## Descripción

```php
public ReflectionConstant::getFileName(): string
```php

Devuelve el nombre del fichero en el que se ha definido la constante.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre del fichero en el que se ha definido la constante. Si la constante está definida en el núcleo PHP o en una extensión PHP, `false` es devuelto.
