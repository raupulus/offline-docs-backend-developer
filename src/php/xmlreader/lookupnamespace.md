---
title: XMLReader::lookupNamespace
description: Consulta el espacio de nombres para un prefijo
source_url: https://www.php.net/manual/es/xmlreader.lookupnamespace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/lookupnamespace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_revision: 4a742792d
order: 103180
---

XMLReader::lookupNamespace

Consulta el espacio de nombres para un prefijo

## Descripción

```php
public XMLReader::lookupNamespace(string $prefix): string
```php

Consulta en el ámbito del espacio de nombres para un prefijo dado.

## Parámetros

`prefix`  
String que contienen el prefijo.

## Valores devueltos

El valor del espacio de nombres, o `null` si no existe ningún espacio de nombres.

## Historial de cambios

| Versión | Descripción                                |
|---------|--------------------------------------------|
| 8.0.0   | Esta función ya no puede devolver `false`. |
