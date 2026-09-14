---
title: DOMImplementation::createDocument
description: Crea un objeto DOM Document del tipo especificado con sus elementos
source_url: https://www.php.net/manual/es/domimplementation.createdocument.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domimplementation/createdocument.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 7d5c74c9a
order: 13760
---

DOMImplementation::createDocument

Crea un objeto DOM Document del tipo especificado con sus elementos

## Descripción

```php
public DOMImplementation::createDocument([string $namespace], [string $qualifiedName], [DOMDocumentType $doctype]): DOMDocument
```php

Crea un objeto `DOMDocument` del tipo especificado con estos elementos del documento.

## Parámetros

`namespace`  
La URI del espacio de nombres de los elementos del documento a crear.

`qualifiedName`  
El nombre cualificado de los elementos del documento a crear.

`doctype`  
El tipo de documento a crear o `null`.

## Valores devueltos

Un nuevo objeto `DOMDocument`. Si `namespace`, `qualifiedName`, y `doctype` son nulos, el `DOMDocument` devuelto está vacío sin ningún elemento de documento.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_WRONG_DOCUMENT_ERR`  
Lanzado si `doctype` ya ha sido utilizado con un documento diferente o ha sido creado desde una implementación diferente.

`DOM_NAMESPACE_ERR`  
Lanzado si hay un error en el espacio de nombres, determinado por `namespace` y `qualifiedName`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | La función ahora tiene un tipo de retorno tentativo `DOMDocument`. |
| 8.0.3 | `namespace` ahora es nullable. |
| 8.0.0 | `doctype` ahora es nullable. |
| 8.0.0 | Llamar a esta función de manera estática ahora lanzará una `Error`. Anteriormente, se generaba un error `E_DEPRECATED`. |

## Véase también

DOMDocument::\_\_construct, DOMImplementation::createDocumentType
