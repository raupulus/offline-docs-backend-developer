---
title: DOMCharacterData::deleteData
description: Elimina un rango de caracteres de los datos de carácter
source_url: https://www.php.net/manual/es/domcharacterdata.deletedata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domcharacterdata/deletedata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 7d5c74c9a
order: 12830
---

DOMCharacterData::deleteData

Elimina un rango de caracteres de los datos de carácter

## Descripción

```php
public DOMCharacterData::deleteData(int $offset, int $count): bool
```php

Borra `count` caracteres a partir de la posición `offset`.

## Parámetros

`offset`  
La posición a partir de la cual se debe comenzar a borrar.

`count`  
El número de caracteres a borrar. Si la suma de `offset` y `count` excede la longitud total de la cadena, entonces todos los caracteres hasta el final de la cadena serán borrados.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_INDEX_SIZE_ERR`  
Se lanza si `offset` es negativo o mayor que el número de puntos de código UTF-8 en los datos o si `count` es negativo.

## Véase también

DOMCharacterData::appendData, DOMCharacterData::insertData, DOMCharacterData::replaceData, DOMCharacterData::substringData
