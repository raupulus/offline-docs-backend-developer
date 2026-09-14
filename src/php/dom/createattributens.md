---
title: DOMDocument::createAttributeNS
description: Crea un nuevo atributo con un espacio de nombres asociado
source_url: https://www.php.net/manual/es/domdocument.createattributens.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/createattributens.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 7d5c74c9a
order: 13010
---

DOMDocument::createAttributeNS

Crea un nuevo atributo con un espacio de nombres asociado

## Descripción

```php
public DOMDocument::createAttributeNS(string $namespace, string $qualifiedName): DOMAttr
```php

Esta función crea una nueva instancia de la clase `DOMAttr`. Este nodo no será mostrado en el documento, a menos que sea insertado con `DOMNode::appendChild`.

## Parámetros

`namespace`  
El URI del espacio de nombres.

`qualifiedName`  
El nombre de la etiqueta y el prefijo del atributo, en este formato: `prefijo:nombreEtiqueta`.

## Valores devueltos

El nuevo `DOMAttr` o `false` si ocurre un error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_INVALID_CHARACTER_ERR`  
Lanzado si `qualifiedName` contiene un carácter inválido.

`DOM_NAMESPACE_ERR`  
Lanzado si `qualifiedName` es un nombre cualificado mal formado o si `qualifiedName` tiene un sufijo y `namespace` es `null`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Llamar a este método sin especificar un prefijo elegirá ahora un prefijo en lugar de asumir el espacio de nombres por defecto. Anteriormente, esto creaba un atributo sin prefijo y aplicaba incorrectamente el espacio de nombres al elemento propietario ya que los espacios de nombres por defecto no se aplican a los atributos. |
| 8.3.0 | Llamar a este método utilizando un prefijo ya declarado en el elemento propietario con un URI de espacio de nombres diferente cambiará ahora el nuevo prefijo para evitar conflictos de espacio de nombres. Esto alinea el comportamiento con la especificación del DOM. Anteriormente, esto lanzaba una `DOMException` con el código `DOM_NAMESPACE_ERR`. |

## Véase también

DOMNode::appendChild, DOMDocument::createAttribute, DOMDocument::createCDATASection, DOMDocument::createComment, DOMDocument::createDocumentFragment, DOMDocument::createElement, DOMDocument::createElementNS, DOMDocument::createEntityReference, DOMDocument::createProcessingInstruction, DOMDocument::createTextNode
