---
title: SolrQuery::addFacetQuery
description: Añade una consulta de faceta
source_url: https://www.php.net/manual/es/solrquery.addfacetquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/addfacetquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: c05bc653c
order: 78840
---

SolrQuery::addFacetQuery

Añade una consulta de faceta

## Descripción

```php
public SolrQuery::addFacetQuery(string $facetQuery): SolrQuery
```php

Añade una consulta de faceta

## Parámetros

`facetQuery`  
La consulta de faceta

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usa el valor de retorno.

## Ejemplos

Ejemplo de SolrQuery::addFacetField

```
<?php

$opciones = array
(
        'hostname' => SOLR_SERVER_HOSTNAME,
        'login'    => SOLR_SERVER_USERNAME,
        'password' => SOLR_SERVER_PASSWORD,
        'port'     => SOLR_SERVER_PORT,
);

$cliente = new SolrClient($opciones);

$consulta = new SolrQuery('*:*');

$consulta->setFacet(true);

$consulta->addFacetQuery('price:[* TO 500]')->addFacetQuery('price:[500 TO *]');

$respuesta_consulta = $cliente->query($consulta);

$respuesta = $respuesta_consulta->getResponse();

print_r($respuesta->facet_counts->facet_queries);

?>

    
```php

Resultado del ejemplo anterior es similar a:

    SolrObject Object
    (
        [price:[* TO 500]] => 14
        [price:[500 TO *]] => 2
    )
