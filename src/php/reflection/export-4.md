---
title: ReflectionExtension::export
description: Exportación
source_url: https://www.php.net/manual/es/reflectionextension.export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionextension/export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70170
---

ReflectionExtension::export

Exportación

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.4.0, y ha sido *ELIMINADA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
public static ReflectionExtension::export(string $name, [string $return]): string
```php

Exporte una extensión reflejada. El formato de retorno de esta función es idéntico al argumento CLI `--re [extension]`.

## Parámetros

`name`  
La reflexión a exportar.

`return`  
Definirlo a `true` retornará la exportación en lugar de emitirla. Definirlo a `false` (por defecto) hará lo contrario.

## Valores devueltos

Si el parámetro `return` se establece a `true`, entonces la exportación se devuelve como un `string`, de lo contrario se devuelve `null`.

## Véase también

ReflectionExtension::info, ReflectionExtension::\_\_toString
