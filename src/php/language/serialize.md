---
title: Serializable::serialize
description: Representación en formato cadena de un objeto
source_url: https://www.php.net/manual/es/serializable.serialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/serializable/serialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 460f49a93
order: 3900
---

Serializable::serialize

Representación en formato cadena de un objeto

## Descripción

```php
public Serializable::serialize(): string
```php

Devuelve la representación de un objeto en formato string.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la representación de un objeto o `null`

## Errores/Excepciones

Lanza una `Exception` cuando de devuelen otros tipos aparte de string y `null`

## Véase también

[\_\_sleep()](#object.sleep), [\_\_serialize()](#object.serialize)
