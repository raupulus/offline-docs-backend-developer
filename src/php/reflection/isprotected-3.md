---
title: ReflectionProperty::isProtected
description: Verifica si la propiedad es protegida
source_url: https://www.php.net/manual/es/reflectionproperty.isprotected.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/isprotected.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 16f66c05a
order: 71710
---

ReflectionProperty::isProtected

Verifica si la propiedad es protegida

## Descripción

```php
public ReflectionProperty::isProtected(): bool
```php

Verifica si la propiedad es protegida.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si la propiedad es protegida, `false` en caso contrario.

> [!NOTE]
> Tenga en cuenta que esto se refiere únicamente a la visibilidad principal, y no a una [visibilidad de definición](#language.oop5.visibility-members-aviz), si está especificada.

## Véase también

ReflectionProperty::isPublic, ReflectionProperty::isPrivate, ReflectionProperty::isReadOnly, ReflectionProperty::isStatic
