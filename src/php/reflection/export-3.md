---
title: ReflectionClassConstant::export
description: Exporta
source_url: https://www.php.net/manual/es/reflectionclassconstant.export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclassconstant/export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69710
---

ReflectionClassConstant::export

Exporta

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.4.0, y ha sido *ELIMINADA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
public static ReflectionClassConstant::export(mixed $class, string $name, [bool $return]): string
```php

Exporta una reflexión.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`class`  
La reflexión a exportar.

`name`  
El nombre de la constante de clase.

`return`  
Definirlo a `true` retornará la exportación en lugar de emitirla. Definirlo a `false` (por defecto) hará lo contrario.

## Valores devueltos

## Véase también

ReflectionClassConstant::\_\_toString
