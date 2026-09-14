---
title: Dom\TokenList::supports
description: Indica si el token dado es admitido
source_url: https://www.php.net/manual/es/dom-tokenlist.supports.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/tokenlist/supports.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: ffd2ef754
order: 12730
---

Dom\TokenList::supports

Indica si el token dado es admitido

## Descripción

```php
public Dom\TokenList::supports(string $token): bool
```php

Indica si `token` está en la lista de tokens admitidos del atributo asociado.

## Parámetros

`token`  
El token.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Genera una TypeError cuando el atributo no define una lista de tokens admitidos.
