---
title: DOMCharacterData::insertData
description: Inserta una cadena en el desplazamiento de punto de código UTF-8 especificado
source_url: https://www.php.net/manual/es/domcharacterdata.insertdata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domcharacterdata/insertdata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 7d5c74c9a
order: 12840
---

DOMCharacterData::insertData

Inserta una cadena en el desplazamiento de punto de código UTF-8 especificado

## Descripción

```php
public DOMCharacterData::insertData(int $offset, string $data): bool
```php

Inserta la cadena `data` en la posición `offset`.

## Parámetros

`offset`  
La posición de la inserción.

`data`  
La cadena a insertar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_INDEX_SIZE_ERR`  
Se lanza si `offset` es negativo o mayor que el número de puntos de código UTF-8 en los datos.

## Véase también

DOMCharacterData::appendData, DOMCharacterData::deleteData, DOMCharacterData::replaceData, DOMCharacterData::substringData
