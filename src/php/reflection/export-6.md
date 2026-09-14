---
title: ReflectionMethod::export
description: Exportación de un método de reflexión
source_url: https://www.php.net/manual/es/reflectionmethod.export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionmethod/export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: d8c71db13
order: 70940
---

ReflectionMethod::export

Exportación de un método de reflexión

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.4.0, y ha sido *ELIMINADA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
public static ReflectionMethod::export(string $class, string $name, [bool $return]): string
```php

Exporta un objeto ReflectionMethod.

## Parámetros

`class`  
El nombre de la clase.

`name`  
El nombre del método.

`return`  
Definirlo a `true` retornará la exportación en lugar de emitirla. Definirlo a `false` (por defecto) hará lo contrario.

## Valores devueltos

Si el parámetro `return` se establece a `true`, entonces la exportación se devuelve como un `string`, de lo contrario se devuelve `null`.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | Esta función ha sido eliminada. |
| 7.4.0   | Esta función está obsoleta.     |

## Véase también

ReflectionMethod::\_\_construct, ReflectionMethod::\_\_toString
