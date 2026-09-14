---
title: XMLReader::readOuterXml
description: Recupera el XML del actual nodo, incluyendo él mismo
source_url: https://www.php.net/manual/es/xmlreader.readouterxml.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/readouterxml.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103290
---

XMLReader::readOuterXml

Recupera el XML del actual nodo, incluyendo él mismo

## Descripción

```php
public XMLReader::readOuterXml(): string
```php

Lee el contenido del actual nodo, incluyendo el nodo mismo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el contenido del actual nodo, incluyendo el de él mismo, como una cadena. Cadena vacía en fallo.

## Notas

> [!CAUTION]
> Esta función solo está disponible si PHP es compilado utilizando la biblioteca libxml 20620 o posterior.

## Véase también

`XMLReader::readString`, `XMLReader::readInnerXml`, `XMLReader::expand`
