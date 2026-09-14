---
title: XMLReader::readString
description: Lee el contenido del nodo actual como string
source_url: https://www.php.net/manual/es/xmlreader.readstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/readstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103300
---

XMLReader::readString

Lee el contenido del nodo actual como string

## Descripción

```php
public XMLReader::readString(): string
```php

Lee el contenido del nodo actual como string.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el contenido del nodo actual como cadena. En caso de error devuelve una cadena vacía.

## Notas

> [!CAUTION]
> Esta función solo está disponible si PHP es compilado utilizando la biblioteca libxml 20620 o posterior.

## Véase también

`XMLReader::readOuterXml`, `XMLReader::readInnerXml`, `XMLReader::expand`
