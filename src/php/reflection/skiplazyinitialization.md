---
title: ReflectionProperty::skipLazyInitialization
description: Marca una propiedad como no perezosa
source_url: https://www.php.net/manual/es/reflectionproperty.skiplazyinitialization.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/skiplazyinitialization.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c0fa5077c
order: 71810
---

ReflectionProperty::skipLazyInitialization

Marca una propiedad como no perezosa

## Descripción

```php
public ReflectionProperty::skipLazyInitialization(object $object): void
```php

Marca una propiedad como no perezosa de modo que pueda ser accedida directamente sin desencadenar la inicialización perezosa. La propiedad es inicializada a su valor por defecto, si lo tiene. La propiedad no debe ser dinámica, estática o virtual, y el objeto debe ser una instancia de una clase definida por el usuario o `stdClass`.

Si era la última propiedad perezosa, el objeto es marcado como no perezoso y el inicializador o la función de fábrica es desvinculado.

## Parámetros

`object`  
El objeto sobre el cual marcar la propiedad.

## Valores devueltos

No se retorna ningún valor.

## Véase también

objetos perezosos

ReflectionProperty::setRawValueWithoutLazyInitialization

ReflectionClass::newLazyGhost
