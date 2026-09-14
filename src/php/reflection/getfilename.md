---
title: ReflectionClass::getFileName
description: Obtiene el nombre del fichero donde la clase ha sido declarada
source_url: https://www.php.net/manual/es/reflectionclass.getfilename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getfilename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69160
---

ReflectionClass::getFileName

Obtiene el nombre del fichero donde la clase ha sido declarada

## Descripción

```php
public ReflectionClass::getFileName(): string
```php

Obtiene el nombre del fichero donde la clase ha sido declarada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Obtiene el nombre del fichero donde la clase ha sido declarada. Si la clase es declarada en el núcleo de PHP o en una extensión PHP, `false` es devuelto.

## Véase también

ReflectionClass::getExtensionName
