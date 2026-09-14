---
title: SolrQuery::addFilterQuery
description: Especifica una consulta de filtro
source_url: https://www.php.net/manual/es/solrquery.addfilterquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/addfilterquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: c1194eea5
order: 78860
---

SolrQuery::addFilterQuery

Especifica una consulta de filtro

## Descripción

```php
public SolrQuery::addFilterQuery(string $fq): SolrQuery
```php

Especifica una consulta de filtro

## Parámetros

`fq`  
La consulta de filtro

## Valores devueltos

Devuelve el objeto SolrQuery actual.

## Ejemplos

Ejemplo de SolrQuery::addFilterQuery

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

$consulta = new SolrQuery();

$consulta->setQuery('*:*');

$consulta->addFilterQuery('color:blue,green');

$respuesta_consulta = $cliente->query($consulta);

$respuesta = $respuesta_consulta->getResponse();

print_r($respuesta['facet_counts']['facet_fields']);

?>

    
```php

Resultado del ejemplo anterior es similar a:

     &fq=color:blue,green
