---
title: XMLReader::moveToAttribute
description: Mueve el cursor a un atributo nombrado
source_url: https://www.php.net/manual/es/xmlreader.movetoattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/movetoattribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103190
---

XMLReader::moveToAttribute

Mueve el cursor a un atributo nombrado

## Descripción

```php
public XMLReader::moveToAttribute(string $name): bool
```php

Posciciona el cursor a un atributo nombrado.

## Parámetros

`name`  
El nombre del atributo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

XMLReader::moveToElement, XMLReader::moveToAttributeNo, XMLReader::moveToAttributeNs, XMLReader::moveToFirstAttribute
