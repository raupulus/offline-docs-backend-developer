---
title: ReflectionFiber::getTrace
description: Devuelve la traza de llamadas del punto de ejecución actual
source_url: https://www.php.net/manual/es/reflectionfiber.gettrace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfiber/gettrace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70360
---

ReflectionFiber::getTrace

Devuelve la traza de llamadas del punto de ejecución actual

## Descripción

```php
public ReflectionFiber::getTrace([int $options]): array
```php

Devuelve la traza de llamadas del punto de ejecución actual de la `Fiber` reflejada.

## Parámetros

`options`  
El valor de `options` puede ser uno de los flags siguientes.

| Opción | Descripción |
|----|----|
| `DEBUG_BACKTRACE_PROVIDE_OBJECT` | Valor por defecto. |
| `DEBUG_BACKTRACE_IGNORE_ARGS` | No incluir la información de argumentos para las funciones en la traza de llamadas. |

Opciones disponibles

## Valores devueltos

La traza de llamadas del punto de ejecución actual de la fibra.
