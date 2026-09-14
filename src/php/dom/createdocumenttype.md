---
title: DOMImplementation::createDocumentType
description: Crea un objeto DOMDocumentType vacío
source_url: https://www.php.net/manual/es/domimplementation.createdocumenttype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domimplementation/createdocumenttype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 7d5c74c9a
order: 13770
---

DOMImplementation::createDocumentType

Crea un objeto DOMDocumentType vacío

## Descripción

```php
public DOMImplementation::createDocumentType(string $qualifiedName, [string $publicId], [string $systemId]): DOMDocumentType
```php

Crea un objeto `DOMDocumentType` vacío. Las declaraciones y notaciones de entidades no están disponibles. Las expansiones de referencias de entidades y los añadidos de atributos por omisión no se efectúan tampoco.

## Parámetros

`qualifiedName`  
El nombre cualificado del tipo de documento a crear.

`publicId`  
El identificador público externo del subconjunto.

`systemId`  
El identificador de sistema externo del subconjunto.

## Valores devueltos

Un nuevo nodo `DOMDocumentType` con su `ownerDocument` definido a `null` o `false` en caso de error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_NAMESPACE_ERR`  
Se lanza si hay un error con el espacio de nombres, determinado por `qualifiedName`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Llamar a esta función de manera estática lanzará ahora una `Error`. Anteriormente, se generaba un error `E_DEPRECATED`. |

## Ejemplos

Creación de un documento con una DTD adjunta

```
 
<?php

// Creación de una instancia de la clase DOMImplementation
$imp = new DOMImplementation;

// Creación de una instancia DOMDocumentType
$dtd = $imp->createDocumentType('graph', '', 'graph.dtd');

// Creación de una instancia DOMDocument
$dom = $imp->createDocument("", "", $dtd);

// Definición de otras propiedades
$dom->encoding = 'UTF-8';
$dom->standalone = false;

// Creación de un elemento vacío
$element = $dom->createElement('graph');

// Adición del elemento
$dom->appendChild($element);

// Recupera y muestra el documento
echo $dom->saveXML();

?>

    
```php

El ejemplo anterior mostrará:

```
<!DOCTYPE graph SYSTEM "graph.dtd">
<graph/>

    
```php

## Véase también

DOMImplementation::createDocument
