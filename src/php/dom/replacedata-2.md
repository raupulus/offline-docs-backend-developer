---
title: DOMCharacterData::replaceData
description: Reemplaza una subcadena en los datos de carácter
source_url: https://www.php.net/manual/es/domcharacterdata.replacedata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domcharacterdata/replacedata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 7d5c74c9a
order: 12860
---

DOMCharacterData::replaceData

Reemplaza una subcadena en los datos de carácter

## Descripción

```php
public DOMCharacterData::replaceData(int $offset, int $count, string $data): bool
```php

Reemplaza `count` caracteres a partir de la posición `offset` con los datos `data`.

## Parámetros

`offset`  
La posición a partir de la cual se inicia el reemplazo.

`count`  
El número de caracteres a reemplazar. Si la suma de `offset` y `count` excede la longitud total de la cadena, entonces todos los caracteres hasta el final de los datos serán reemplazados.

`data`  
La cadena utilizada para reemplazar los caracteres seleccionados.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_INDEX_SIZE_ERR`  
Lanzado si `offset` es negativo o mayor que el número de unidades de puntos de código UTF-8 en los datos o si `count` es negativo.

## Véase también

DOMCharacterData::appendData, DOMCharacterData::deleteData, DOMCharacterData::insertData, DOMCharacterData::substringData
