---
title: SolrDocument::sort
description: Ordena los campos del documento
source_url: https://www.php.net/manual/es/solrdocument.sort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdocument/sort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 78090
---

SolrDocument::sort

Ordena los campos del documento

## Descripción

```php
public SolrDocument::sort(int $sortOrderBy, [int $sortDirection]): bool
```php

Los campos se cambian de lugar según el criterio y la dirección de ordenación especificados Los campos pueden ser ordenados por valor boost, nombre de campo y número de valores. El parámetro sortOrderBy debe ser: \* SolrDocument::SORT_FIELD_NAME \* SolrDocument::SORT_FIELD_BOOST_VALUE \* SolrDocument::SORT_FIELD_VALUE_COUNT El parámetro sortDirection puede ser: \* SolrDocument::SORT_DEFAULT \* SolrDocument::SORT_ASC \* SolrDocument::SORT_DESC La ordenación predeterminada es de manera ascendente.

## Parámetros

`sortOrderBy`  
El criterio de ordenación.

`sortDirection`  
La dirección de ordenación.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
