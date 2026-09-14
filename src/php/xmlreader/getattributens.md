---
title: XMLReader::getAttributeNs
description: Recupera el valor de un atributo por nombre local y URI
source_url: https://www.php.net/manual/es/xmlreader.getattributens.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader/getattributens.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: false
translation_revision: 4a742792d
order: 103150
---

XMLReader::getAttributeNs

Recupera el valor de un atributo por nombre local y URI

## Descripción

```php
public XMLReader::getAttributeNs(string $name, string $namespace): string
```php

Devuelve el valor de un atributo por nombre y URI del espacio de nombres o una cadena de caracteres vacía si el atributo no existe o no está establecido en el nodo.

## Parámetros

`name`  
El nombre local.

`namespace`  
El URI del espacio de nombres.

## Valores devueltos

El valor del atributo, o `null` si no se encuentra ningún atributo con el `name` y `namespace` dados o no está establecido en el elemento.

## Historial de cambios

| Versión | Descripción                                |
|---------|--------------------------------------------|
| 8.0.0   | Esta función ya no puede devolver `false`. |

## Véase también

XMLReader::getAttribute, XMLReader::getAttributeNo
