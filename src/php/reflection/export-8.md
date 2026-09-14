---
title: ReflectionParameter::export
description: Exportación
source_url: https://www.php.net/manual/es/reflectionparameter.export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionparameter/export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 71220
---

ReflectionParameter::export

Exportación

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.4.0, y ha sido *ELIMINADA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
public static ReflectionParameter::export(string $function, string $parameter, [bool $return]): string
```php

Exportación.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`function`  
El nombre de la función.

`parameter`  
El nombre del parámetro.

`return`  
Definirlo a `true` retornará la exportación en lugar de emitirla. Definirlo a `false` (por defecto) hará lo contrario.

## Valores devueltos

La reflexión exportada.

## Véase también

ReflectionParameter::\_\_toString
