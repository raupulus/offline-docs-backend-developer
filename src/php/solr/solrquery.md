---
title: La clase SolrQuery
source_url: https://www.php.net/manual/es/class.solrquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 80740
---

## Introducción

Representa una colección de pares nombre-valor enviados al servidor Solr durante una petición.

## Sinopsis de la clase

SolrQuery

SolrQuery

extends

SolrModifiableParams

Serializable

Constantes

const

int

SolrQuery::ORDER_ASC

0

const

int

SolrQuery::ORDER_DESC

1

const

int

SolrQuery::FACET_SORT_INDEX

0

const

int

SolrQuery::FACET_SORT_COUNT

1

const

int

SolrQuery::TERMS_SORT_INDEX

0

const

int

SolrQuery::TERMS_SORT_COUNT

1

Propiedades

Métodos

Métodos heredados

## Constantes predefinidas

`SolrQuery::ORDER_ASC`  
Se usa para especificar la forma de ordenación debería se ascendente

`SolrQuery::ORDER_DESC`  
Se usa para especificar la forma de ordenación debería se descendente

`SolrQuery::FACET_SORT_INDEX`  
Se usa para especificar que la faceta debería ordenarse según el índice

`SolrQuery::FACET_SORT_COUNT`  
Se usa para especificar que la faceta debería ordenarse según la cuenta

`SolrQuery::TERMS_SORT_INDEX`  
Usado en TermsComponent

`SolrQuery::TERMS_SORT_COUNT`  
Usado en TermsComponent
