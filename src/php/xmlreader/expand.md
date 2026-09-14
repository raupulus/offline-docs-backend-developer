---
title: XMLReader::expand
description: Devuelve una copia del nodo actual como un nodo de objeto DOM
source_url: https://www.php.net/manual/es/xmlreader.expand.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/expand.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103090
---

XMLReader::expand

Devuelve una copia del nodo actual como un nodo de objeto DOM

## Descripción

```php
public XMLReader::expand([DOMNode $baseNode]): DOMNode
```php

Este método copia el nodo actual y devuelve el objeto DOM apropiado.

## Parámetros

`baseNode`  
Un `DOMNode` que define el objetivo `DOMDocument` para el objeto DOM creado.

## Valores devueltos

El objeto `DOMNode` resultante o `false` en caso de error.
