---
title: Transliterator::createFromRules
description: Crea un transliterador desde reglas
source_url: https://www.php.net/manual/es/transliterator.createfromrules.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/transliterator/createfromrules.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: c142be811
order: 42550
---

Transliterator::createFromRules

transliterator_create_from_rules

Crea un transliterador desde reglas

## Descripción

Estilo orientado a objetos

```php
public static Transliterator::createFromRules(string $rules, [int $direction]): Transliterator
```php

Estilo procedimental

```php
transliterator_create_from_rules(string $rules, [int $direction]): Transliterator
```

Crea un transliterador desde reglas.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`rules`  
Las reglas como se definen en Transform Rules Syntax de UTS \#35 : Unicode LDML.

`direction`  
La dirección, por omisión [Transliterator::FORWARD](#transliterator.constants.forward). Puede ser también definido como [Transliterator::REVERSE](#transliterator.constants.reverse).

## Valores devueltos

Devuelve un objeto `Transliterator` en caso de éxito, o `null` si ocurre un error.

## Véase también

Transliterator::getErrorMessage, Transliterator::create
