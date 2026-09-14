---
title: ReflectionProperty::isPrivate
description: Verifica si la propiedad es privada
source_url: https://www.php.net/manual/es/reflectionproperty.isprivate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/isprivate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 16f66c05a
order: 71680
---

ReflectionProperty::isPrivate

Verifica si la propiedad es privada

## Descripción

```php
public ReflectionProperty::isPrivate(): bool
```php

Verifica si la propiedad es privada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si la propiedad es privada, `false` en caso contrario.

> [!NOTE]
> Se debe tener en cuenta que esto se refiere únicamente a la visibilidad principal, y no a una [visibilidad de definición](#language.oop5.visibility-members-aviz), si está especificada.

## Véase también

ReflectionProperty::isPublic, ReflectionProperty::isProtected, ReflectionProperty::isReadOnly, ReflectionProperty::isStatic
