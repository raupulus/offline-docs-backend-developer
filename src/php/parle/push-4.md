---
title: Parle\RParser::push
description: Añade una regla de gramática
source_url: https://www.php.net/manual/es/parle-rparser.push.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/parle/rparser/push.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: 0dad2268d
order: 60850
---

Parle\RParser::push

Añade una regla de gramática

## Descripción

```php
public Parle\RParser::push(string $name, string $rule): int
```php

Añade una regla de gramática. El identificador de producción devuelto puede ser utilizado más tarde en el proceso de análisis para identificar la regla correspondiente.

## Parámetros

`name`  
El nombre de la regla.

`rule`  
La regla a añadir. La sintaxis es compatible con Bison.

## Valores devueltos

Devuelve un `int` representando el índice de la regla.
