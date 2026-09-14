---
title: SolrInputDocument::sort
description: Ordena los campos dentro de un documento
source_url: https://www.php.net/manual/es/solrinputdocument.sort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrinputdocument/sort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 78480
---

SolrInputDocument::sort

Ordena los campos dentro de un documento

## Descripción

```php
public SolrInputDocument::sort(int $sortOrderBy, [int $sortDirection]): bool
```php

Los campos se cambian de lugar según el criterio y la dirección de ordenación especificados Los campos pueden ser ordenados por valor boost, nombre de campo y número de valores. El parámetro \$order_by debe ser: \* SolrInputDocument::SORT_FIELD_NAME \* SolrInputDocument::SORT_FIELD_BOOST_VALUE \* SolrInputDocument::SORT_FIELD_VALUE_COUNT La dirección de ordenación puede ser: \* SolrInputDocument::SORT_DEFAULT \* SolrInputDocument::SORT_ASC \* SolrInputDocument::SORT_DESC

## Parámetros

`sortOrderBy`  
El criterio de ordenación

`sortDirection`  
La dirección de ordenación

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
