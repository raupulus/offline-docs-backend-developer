---
title: Serializable::unserialize
description: Construye el objeto
source_url: https://www.php.net/manual/es/serializable.unserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/serializable/unserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 460f49a93
order: 3910
---

Serializable::unserialize

Construye el objeto

## Descripción

```php
public Serializable::unserialize(string $data): void
```php

Es llamado durante la unserialización del objeto.

> [!NOTE]
> Este método actua como el [constructor](#language.oop5.decon.constructor) del objeto. El método [\_\_construct()](#object.construct) *no* será llamado después de este método.

## Parámetros

`data`  
La representación en formato string de un objeto.

## Valores devueltos

El valor devuelto por este método es ignorado.

## Véase también

[\_\_wakeup()](#object.wakeup), [\_\_unserialize()](#object.unserialize)
