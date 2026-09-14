---
title: La clase SolrDocument
source_url: https://www.php.net/manual/es/class.solrdocument.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdocument.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 78140
---

## Introducción

Representa un documento Solr recuperado de una respuesta a una consulta.

## Sinopsis de la clase

SolrDocument

final

SolrDocument

ArrayAccess

Iterator

Serializable

Constantes

const

int

SolrDocument::SORT_DEFAULT

1

const

int

SolrDocument::SORT_ASC

1

const

int

SolrDocument::SORT_DESC

2

const

int

SolrDocument::SORT_FIELD_NAME

1

const

int

SolrDocument::SORT_FIELD_VALUE_COUNT

2

const

int

SolrDocument::SORT_FIELD_BOOST_VALUE

4

Métodos

## Constantes predefinidas

`SolrDocument::SORT_DEFAULT`  
Modo predeterminado para ordenar los campos dentro de un documento.

`SolrDocument::SORT_ASC`  
Ordena los campos de forma ascendente

`SolrDocument::SORT_DESC`  
Ordena los campos de forma descendente

`SolrDocument::SORT_FIELD_NAME`  
Ordena los campos por nombre de campo.

`SolrDocument::SORT_FIELD_VALUE_COUNT`  
Ordena los campos según el número de valores de cada campo.

`SolrDocument::SORT_FIELD_BOOST_VALUE`  
Ordena los campos según sus valores boost.
