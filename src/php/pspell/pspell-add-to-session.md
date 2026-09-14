---
title: pspell_add_to_session
description: Añade la palabra al diccionario personal de la sesión actual
source_url: https://www.php.net/manual/es/function.pspell-add-to-session.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-add-to-session.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66360
---

pspell_add_to_session

Añade la palabra al diccionario personal de la sesión actual

## Descripción

```php
pspell_add_to_session(PSpell\Dictionary $dictionary, string $word): bool
```php

`pspell_add_to_session` añade una palabra al diccionario personal asociado a la versión actual. Es una función similar a `pspell_add_to_personal`.

## Parámetros

`dictionary`  
Una instancia de `PSpell\Dictionary`.

`word`  
La palabra añadida.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `dictionary` ahora espera una instancia de `PSpell\Dictionary` ; anteriormente, se esperaba un `resource`. |
