---
title: SQLite3Result::fetchArray
description: Recupera un conjunto de resultados en forma de array
source_url: https://www.php.net/manual/es/sqlite3result.fetcharray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3result/fetcharray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: true
translation_revision: 61374bbe2
order: 85890
---

SQLite3Result::fetchArray

Recupera un conjunto de resultados en forma de array

## Descripción

```php
public SQLite3Result::fetchArray([int $mode]): array
```php

Recupera un conjunto de resultados en forma de array asociativo o indexado numéricamente, o ambos. Por omisión, se obtienen ambos.

## Parámetros

`mode`  
Controla la forma en que la siguiente línea debe ser devuelta a la función llamante. Este valor puede ser `SQLITE3_ASSOC`, `SQLITE3_NUM`, o `SQLITE3_BOTH`.

- `SQLITE3_ASSOC` : Devuelve un array indexado por el nombre de la columna, tal como se devuelve en el conjunto de resultados correspondiente.

- `SQLITE3_NUM` : Devuelve un array indexado por el número de la columna, tal como se devuelve en el conjunto de resultados, comenzando por la columna 0.

- `SQLITE3_BOTH` : Devuelve un array indexado por el nombre y el número de la columna, tal como se devuelve por el conjunto de resultados, comenzando por la columna 0.

## Valores devueltos

Devuelve una línea del conjunto de resultados, en forma de array asociativo, o en forma de array indexado, o ambos. Devuelve `false` si no hay más líneas.

Los tipos de los valores del array devuelto son mapeados desde tipos SQLite3 de la siguiente manera: los enteros son mapeados a `int` si se ajustan al rango `PHP_INT_MIN`.. `PHP_INT_MAX`, y a `string` en caso contrario. Los números de punto flotante son mapeados a `float`, los valores `null` son mapeados a `null`, y las cadenas y los objetos BLOB son mapeados a `string`.
