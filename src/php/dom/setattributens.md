---
title: DOMElement::setAttributeNS
description: Añade un nuevo atributo
source_url: https://www.php.net/manual/es/domelement.setattributens.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domelement/setattributens.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 7d5c74c9a
order: 13650
---

DOMElement::setAttributeNS

Añade un nuevo atributo

## Descripción

```php
public DOMElement::setAttributeNS(string $namespace, string $qualifiedName, string $value): void
```php

Establece un atributo con el espacio de nombres `namespace` y el nombre `qualifiedName` al valor dado. Si el atributo no existe, se creará.

## Parámetros

`namespace`  
La URI del espacio de nombres.

`qualifiedName`  
El nombre cualificado del atributo, como `prefijo:nombre_etiqueta`.

`value`  
El valor del atributo.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_NO_MODIFICATION_ALLOWED_ERR`  
Lanzado si el nodo es de sólo lectura.

`DOM_NAMESPACE_ERR`  
Lanzado si `qualifiedName` es un nombre cualificado malformado, o si `qualifiedName` tienen un prefijo y `namespace` es `null`.

## Véase también

DOMElement::hasAttributeNS, DOMElement::getAttributeNS, DOMElement::removeAttributeNS
