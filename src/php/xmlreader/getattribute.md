---
title: XMLReader::getAttribute
description: Obtiener el valor del atributo nombrado
source_url: https://www.php.net/manual/es/xmlreader.getattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/getattribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103130
---

XMLReader::getAttribute

Obtiener el valor del atributo nombrado

## Descripción

```php
public XMLReader::getAttribute(string $name): string
```php

Devuelve el valor del atributo nombrado o `null` si el atributo no existe o no está posicionado en un eleménto del nodo.

## Parámetros

`name`  
El nombre del atributo.

## Valores devueltos

El valor del atributo, o `null` si no se encuetra un atributo con el nombre dado por `name` o no está posicionado en un nodo de elemento.

## Historial de cambios

| Versión | Descripción                                |
|---------|--------------------------------------------|
| 8.0.0   | Esta función ya no puede devolver `false`. |

## Véase también

XMLReader::getAttributeNo, XMLReader::getAttributeNs
