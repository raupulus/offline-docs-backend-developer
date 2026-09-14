---
title: XMLReader::getAttributeNo
description: Obtiene el valor de un atributo por el indice
source_url: https://www.php.net/manual/es/xmlreader.getattributeno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/getattributeno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103140
---

XMLReader::getAttributeNo

Obtiene el valor de un atributo por el indice

## Descripción

```php
public XMLReader::getAttributeNo(int $index): string
```php

Devuelve el valor de un atributo basado en su posición o una cadena vacia si el atributo no existe o no está posicionado en un eleménto del nodo.

## Parámetros

`index`  
La posición del atributo.

## Valores devueltos

El valor del atributo, o `null` si el atributo no existe en el `index` o no está posicionado en el eleménto.

## Véase también

XMLReader::getAttribute, XMLReader::getAttributeNs
