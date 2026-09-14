---
title: XMLReader::readInnerXml
description: Recupera el XML del actual nodo
source_url: https://www.php.net/manual/es/xmlreader.readinnerxml.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/readinnerxml.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103280
---

XMLReader::readInnerXml

Recupera el XML del actual nodo

## Descripción

```php
public XMLReader::readInnerXml(): string
```php

Lee el contenido del actual nodo, incluyendo notas pequeñas y marcado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el contenido del nodo actual como una cadena de caracteres. Devuelve una cadena vacía en caso de error.

## Notas

> [!CAUTION]
> Esta función solo está disponible si PHP es compilado utilizando la biblioteca libxml 20620 o posterior.

## Véase también

`XMLReader::readString`, `XMLReader::readOuterXml`, `XMLReader::expand`
