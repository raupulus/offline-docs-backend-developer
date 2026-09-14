---
title: DOMElement::hasAttribute
description: Comprueba si existe un atributo
source_url: https://www.php.net/manual/es/domelement.hasattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/hasattribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 13510
---

DOMElement::hasAttribute

Comprueba si existe un atributo

## Descripción

```php
public DOMElement::hasAttribute(string $qualifiedName): bool
```php

Indica si un atributo llamado `qualifiedName` existe como miembro del elemento.

## Parámetros

`qualifiedName`  
El nombre del atributo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

DOMElement::hasAttributeNS, DOMElement::getAttribute, DOMElement::setAttribute, DOMElement::removeAttribute
