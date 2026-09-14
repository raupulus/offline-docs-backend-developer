---
title: ReflectionExtension::__clone
description: Clonación
source_url: https://www.php.net/manual/es/reflectionextension.clone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionextension/clone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70150
---

ReflectionExtension::\_\_clone

Clonación

## Descripción

```php
private ReflectionExtension::__clone(): void
```php

El método clone impide que un objeto sea clonado. Los objetos de reflexión no pueden ser clonados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se devuelve ningún valor. Si se llama, se producirá un error fatal.

## Historial de cambios

| Versión | Descripción                 |
|---------|-----------------------------|
| 8.1.0   | Este método ya no es final. |

## Véase también

ReflectionExtension::\_\_construct, [Clonación de objetos](#language.oop5.cloning)
