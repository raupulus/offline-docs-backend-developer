---
title: DOMElement::removeAttributeNS
description: Elimina un atributo
source_url: https://www.php.net/manual/es/domelement.removeattributens.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/removeattributens.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 7d5c74c9a
order: 13590
---

DOMElement::removeAttributeNS

Elimina un atributo

## Descripción

```php
public DOMElement::removeAttributeNS(string $namespace, string $localName): void
```php

Elimina el atributo `localName` en el espacio de nombre `namespace` de el elemento.

## Parámetros

`namespace`  
La URI del espacio de nombres.

`localName`  
El nombre local.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_NO_MODIFICATION_ALLOWED_ERR`  
Lanzado si el nodo es de sólo lectura.

## Véase también

DOMElement::hasAttributeNS, DOMElement::getAttributeNS, DOMElement::setAttributeNS
