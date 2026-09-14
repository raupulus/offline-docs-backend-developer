---
title: DOMText::isWhitespaceInElementContent
description: Indica si este nodo de texto contiene espacios en blanco
source_url: https://www.php.net/manual/es/domtext.iswhitespaceinelementcontent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domtext/iswhitespaceinelementcontent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 14260
---

DOMText::isWhitespaceInElementContent

Indica si este nodo de texto contiene espacios en blanco

## Descripción

```php
public DOMText::isWhitespaceInElementContent(): bool
```php

Indica si este nodo de texto contiene únicamente espacios en blanco o si está vacío. El nodo de texto está determinado a contener espacios en blanco en el contenido del elemento durante la carga del documento.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el nodo contiene cero o más carecteres espacio en blanco y nada más. De lo contrario deveulve `false`.
