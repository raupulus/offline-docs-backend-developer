---
title: imap_sort
description: Ordena mensajes
source_url: https://www.php.net/manual/es/function.imap-sort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-sort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38560
---

imap_sort

Ordena mensajes

## Descripción

```php
imap_sort(IMAP\Connection $imap, int $criteria, bool $reverse, [int $flags], [string $search_criteria], [string $charset]): array
```php

Recupera y ordena los números de mensajes en función de los parámetros dados.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`criteria`  
Los criterios `criteria` pueden ser uno (y solo uno) de los siguientes:

- `SORTDATE` : fecha del mensaje

- `SORTARRIVAL` : fecha de llegada

- `SORTFROM` : nombre del primer buzón de la dirección de origen (From address)

- `SORTSUBJECT` : asunto del mensaje

- `SORTTO` : nombre del primer buzón de destino (To address)

- `SORTCC` : nombre del buzón de copia oculta (cc address)

- `SORTSIZE` : tamaño del mensaje en bytes

`reverse`  
Si se debe ordenar en orden inverso.

`flags`  
Los `flags` son máscaras de bits, de uno o más de los siguientes elementos:

- `SE_UID` : devuelve UID en lugar de números

- `SE_NOPREFETCH` : no predescargar los mensajes encontrados

`search_criteria`  
Criterios de búsqueda en formato IMAP2. Para más detalles ver `imap_search`.

`charset`  
Conjunto de caracteres MIME a utilizar durante la búsqueda de `string`.

## Valores devueltos

Devuelve un array de números de mensajes ordenados en función de los parámetros proporcionados, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |
| 8.0.0 | `reverse` es un `bool` en lugar de `int`. |
| 8.0.0 | `search_criteria` y `charset` son ahora `nullable`. |
