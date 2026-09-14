---
title: ReflectionClass::newInstanceWithoutConstructor
description: Crea una nueva instancia de la clase sin invocar el constructor
source_url: https://www.php.net/manual/es/reflectionclass.newinstancewithoutconstructor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/newinstancewithoutconstructor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 69620
---

ReflectionClass::newInstanceWithoutConstructor

Crea una nueva instancia de la clase sin invocar el constructor

## Descripción

```php
public ReflectionClass::newInstanceWithoutConstructor(): object
```php

Crea una nueva instancia de la clase sin invocar su constructor.

## Parámetros

## Valores devueltos

## Errores/Excepciones

Una `ReflectionException` si la clase es una clase interna que no puede ser instanciada sin invocar su constructor. Esta excepción está limitada únicamente a las clases internas que son [finales](#language.oop5.final).

## Véase también

ReflectionClass::newInstance, ReflectionClass::newInstanceArgs
