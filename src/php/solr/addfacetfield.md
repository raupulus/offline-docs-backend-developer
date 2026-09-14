---
title: SolrQuery::addFacetField
description: Añade otro campo a la faceta
source_url: https://www.php.net/manual/es/solrquery.addfacetfield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/addfacetfield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: 04beb0011
order: 78830
---

SolrQuery::addFacetField

Añade otro campo a la faceta

## Descripción

```php
public SolrQuery::addFacetField(string $field): SolrQuery
```php

Añade otro campo a la faceta

## Parámetros

`field`  
El nombre del campo

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

$consulta = new SolrQuery();

$consulta->setQuery($consulta);

$consulta->addField('price')->addField('color');

$consulta->setFacet(true);

$consulta->addFacetField('price')->addFacetField('color');

$respuesta_consulta = $cliente->query($consulta);

$respuesta = $respuesta_consulta->getResponse();

print_r($respuesta['facet_counts']['facet_fields']);

?>

    
```php

Resultado del ejemplo anterior es similar a:

    SolrObject Object
    (
        [color] => SolrObject Object
            (
                [blue] => 20
                [green] => 100
            )

    )
