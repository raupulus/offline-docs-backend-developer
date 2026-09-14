---
title: XMLReader::moveToAttributeNs
description: Mover el cursor a un atributo dado
source_url: https://www.php.net/manual/es/xmlreader.movetoattributens.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/movetoattributens.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103210
---

XMLReader::moveToAttributeNs

Mover el cursor a un atributo dado

## Descripción

```php
public XMLReader::moveToAttributeNs(string $name, string $namespace): bool
```php

Posiciona el cursor en el atributo dado en el espacio de nombres especificado.

## Parámetros

`name`  
El nombre local.

`namespace`  
El URI namespace.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

XMLReader::moveToElement, XMLReader::moveToAttribute, XMLReader::moveToAttributeNo, XMLReader::moveToFirstAttribute
