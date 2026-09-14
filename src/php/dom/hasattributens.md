---
title: DOMElement::hasAttributeNS
description: Comprueba si un atributo existe
source_url: https://www.php.net/manual/es/domelement.hasattributens.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/hasattributens.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 13520
---

DOMElement::hasAttributeNS

Comprueba si un atributo existe

## Descripción

```php
public DOMElement::hasAttributeNS(string $namespace, string $localName): bool
```php

Indica si un atributo en el espacio de nombres `namespace` llamado `localName` existe como miembro del elemento.

## Parámetros

`namespace`  
La URI del espacio de nombres.

`localName`  
El nombre local.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

DOMElement::hasAttribute, DOMElement::getAttributeNS, DOMElement::setAttributeNS, DOMElement::removeAttributeNS
