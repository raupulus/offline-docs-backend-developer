---
title: SolrClient::query
description: Envía una consulta al servidor
source_url: https://www.php.net/manual/es/solrclient.query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: 3b3be96b7
order: 77270
---

SolrClient::query

Envía una consulta al servidor

## Descripción

```php
public SolrClient::query(SolrParams $query): SolrQueryResponse
```php

Envía una consulta al servidor.

## Parámetros

`query`  
Un objeto `SolrParam`. Se recomienda usar `SolrQuery` para consultas avanzadas.

## Valores devueltos

Devuelve un objeto `SolrUpdateResponse` en caso de éxito o lanza una excepción en caso de error.

## Errores/Excepciones

Lanza una `SolrClientException` si el cliente falló o hubo un problema de conexión.

Lanza una `SolrServerException` si el Servidor de Solr falló al satisfacer la consulta.

## Ejemplos

Ejemplo de SolrClient::query

```
<?php

$opciones = array
(
    'hostname' => 'localhost',
    'login'    => 'username',
    'password' => 'password',
    'port'     => '8983',
);

$cliente = new SolrClient($opciones);

$consulta = new SolrQuery();

$consulta->setQuery('lucene');

$consulta->setStart(0);

$consulta->setRows(50);

$consulta->addField('cat')->addField('features')->addField('id')->addField('timestamp');

$respuesta_consulta = $cliente->query($consulta);

$response = $respuesta_consulta->getResponse();

print_r($response);

?>

    
```php

Resultado del ejemplo anterior es similar a:

    SolrObject Object
    (
        [responseHeader] => SolrObject Object
            (
                [status] => 0
                [QTime] => 3
                [params] => SolrObject Object
                    (
                        [fl] => cat,features,id,timestamp
                        [indent] => on
                        [start] => 0
                        [q] => lucene
                        [wt] => xml
                        [version] => 2.2
                        [rows] => 50
                    )

            )

        [response] => SolrObject Object
            (
                [numFound] => 1
                [start] => 0
                [docs] => Array
                    (
                        [0] => SolrObject Object
                            (
                                [id] => SOLR1000
                                [cat] => Array
                                    (
                                        [0] => software
                                        [1] => search
                                    )

                                [features] => Array
                                    (
                                        [0] => Advanced Full-Text Search Capabilities using Lucene
                                        [1] => Optimized for High Volume Web Traffic
                                        [2] => Standards Based Open Interfaces - XML and HTTP
                                        [3] => Comprehensive HTML Administration Interfaces
                                        [4] => Scalability - Efficient Replication to other Solr Search Servers
                                        [5] => Flexible and Adaptable with XML configuration and Schema
                                        [6] => Good unicode support: héllo (hello with an accent over the e)
                                    )

                            )

                    )

            )

    )
