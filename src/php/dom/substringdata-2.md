---
title: DOMCharacterData::substringData
description: Extrae un rango de datos de los datos de carácter
source_url: https://www.php.net/manual/es/domcharacterdata.substringdata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domcharacterdata/substringdata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 7d5c74c9a
order: 12880
---

DOMCharacterData::substringData

Extrae un rango de datos de los datos de carácter

## Descripción

```php
public DOMCharacterData::substringData(int $offset, int $count): string
```php

Devuelve la sub-cadena especificada.

## Parámetros

`offset`  
La posición del inicio de la cadena a extraer.

`count`  
El número de caracteres a extraer.

## Valores devueltos

La sub-cadena especificada. Si la suma de `offset` y `count` excede la longitud total de la cadena, entonces todas las unidades de puntos de código UTF-8 hasta el final de los datos serán devueltas.

## Errores/Excepciones

Puede lanzar una DOMException con los siguientes códigos de error:

`DOM_INDEX_SIZE_ERR`  
Lanzado si `offset` es negativo o mayor que el número de unidades de puntos de código UTF-8 en los datos o si `count` es negativo.

## Véase también

DOMCharacterData::appendData, DOMCharacterData::deleteData, DOMCharacterData::insertData, DOMCharacterData::replaceData
