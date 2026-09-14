---
title: ReflectionExtension::getVersion
description: Obtiene la versión de la extensión
source_url: https://www.php.net/manual/es/reflectionextension.getversion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionextension/getversion.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70250
---

ReflectionExtension::getVersion

Obtiene la versión de la extensión

## Descripción

```php
public ReflectionExtension::getVersion(): string
```php

Obtiene la versión de la extensión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La versión de la extensión, o `null` si la extensión no tiene versión.

## Ejemplos

Ejemplo con ReflectionExtension::getVersion

```
<?php
$ext = new ReflectionExtension('mysqli');
var_dump($ext->getVersion());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(3) "0.1"

## Véase también

ReflectionExtension::info
