---
title: Parle\RLexer::pushState
description: Empuja un nuevo estado de inicio
source_url: https://www.php.net/manual/es/parle-rlexer.pushstate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/parle/rlexer/pushstate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 60750
---

Parle\RLexer::pushState

Empuja un nuevo estado de inicio

## Descripción

```php
public Parle\RLexer::pushState(string $state): int
```php

Este analizador léxico puede tener más de una máquina de estados. Esto permite analizar diferentes tokens según el contexto, permitiendo así realizar un análisis sintáctico simple. Una vez empujado un estado, puede ser utilizado con una variante de firma Parle\RLexer::push adecuada.

## Parámetros

`state`  
El nombre del estado.

## Valores devueltos
