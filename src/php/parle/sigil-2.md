---
title: Parle\RParser::sigil
description: Recupera una parte correspondiente de una regla
source_url: https://www.php.net/manual/es/parle-rparser.sigil.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/parle/rparser/sigil.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: 0dad2268d
order: 60880
---

Parle\RParser::sigil

Recupera una parte correspondiente de una regla

## Descripción

```php
public Parle\RParser::sigil([int $idx]): string
```php

Recupera una parte correspondiente de una regla. Este método es equivalente a la funcionalidad de pseudo-variable en Bison.

## Parámetros

`idx`  
El identificador de correspondencia, basado en cero.

## Valores devueltos

Devuelve una `string` con la parte correspondiente.
