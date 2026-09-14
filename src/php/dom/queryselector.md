---
title: Dom\ParentNode::querySelector
description: Devuelve el primer elemento que coincide con los selectores CSS
source_url: https://www.php.net/manual/es/dom-parentnode.queryselector.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/parentnode/queryselector.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: e64de8bee
order: 12620
---

Dom\ParentNode::querySelector

Devuelve el primer elemento que coincide con los selectores CSS

## Descripción

```php
public Dom\ParentNode::querySelector(string $selectors): Dom\Element
```php

Devuelve el primer elemento que coincide con los selectores CSS especificados en `selectors`.

## Parámetros

`selectors`  
Un string que contiene uno o varios selectores CSS.

## Valores devueltos

Devuelve el primer `Dom\Element` que coincide con `selectors`. Devuelve `null` si ningún elemento coincide.

## Errores/Excepciones

Lanza una DOMException con el código `Dom\SYNTAX_ERR` cuando `selectors` no es un string de selector CSS válido.

## Véase también

Dom\ParentNode::querySelectorAll
