---
title: XMLReader::moveToAttributeNo
description: Mueve el cursor a un atributo por su índice
source_url: https://www.php.net/manual/es/xmlreader.movetoattributeno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/movetoattributeno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_revision: 4a742792d
order: 103200
---

XMLReader::moveToAttributeNo

Mueve el cursor a un atributo por su índice

## Descripción

```php
public XMLReader::moveToAttributeNo(int $index): bool
```php

Coloca el cursor en el atributo en función de su posición.

## Parámetros

`index`  
La posición de el atributo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

XMLReader::moveToElement, XMLReader::moveToAttribute, XMLReader::moveToAttributeNs, XMLReader::moveToFirstAttribute
