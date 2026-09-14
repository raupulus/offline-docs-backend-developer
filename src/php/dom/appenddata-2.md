---
title: DOMCharacterData::appendData
description: Añade la cadena al final de los datos en el nodo
source_url: https://www.php.net/manual/es/domcharacterdata.appenddata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domcharacterdata/appenddata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: ccc76b5d8
order: 12810
---

DOMCharacterData::appendData

Añade la cadena al final de los datos en el nodo

## Descripción

```php
public DOMCharacterData::appendData(string $data): true
```php

Añade la cadena `data` al final de los datos en el nodo.

## Parámetros

`data`  
La cadena a añadir.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                      |
|---------|------------------------------------------------------------------|
| 8.3.0   | Esta función ahora tiene un tipo de retorno tentativo de `true`. |

## Véase también

DOMCharacterData::deleteData, DOMCharacterData::insertData, DOMCharacterData::replaceData, DOMCharacterData::substringData
