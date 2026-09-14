---
title: ReflectionProperty::isPublic
description: Verifica si la propiedad es pública
source_url: https://www.php.net/manual/es/reflectionproperty.ispublic.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/ispublic.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: e0e74c05c
order: 71730
---

ReflectionProperty::isPublic

Verifica si la propiedad es pública

## Descripción

```php
public ReflectionProperty::isPublic(): bool
```php

Verifica si la propiedad es pública.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si la propiedad está marcada como pública, `false` en caso contrario.

> [!NOTE]
> Tenga en cuenta que esto solo se refiere a la visibilidad principal, y no a una [visibilidad de definición](#language.oop5.visibility-members-aviz), si está especificada.

## Notas

> [!NOTE]
> Debe tenerse en cuenta que el hecho de que una propiedad sea `pública` no significa siempre que sea accesible en escritura. Una propiedad puede ser virtual sin gancho `set`, o podría ser `readonly` y haber sido ya escrita, o podría tener una [visibilidad `set` definida](#language.oop5.visibility-members-aviz) como no pública. En todos estos casos, este método devolverá `true`, pero la propiedad no será modificable.

## Véase también

ReflectionProperty::isProtected, ReflectionProperty::isProtectedSet, ReflectionProperty::isPrivate, ReflectionProperty::isPrivateSet, ReflectionProperty::isReadOnly, ReflectionProperty::isStatic
