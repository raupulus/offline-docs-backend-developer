---
title: SolrClient::getByIds
description: Devuelve documentos por sus identificadores. Utiliza la funcionalidad
  de búsqueda en tiempo real de Solr (Solr Realtime Get - RTG)
source_url: https://www.php.net/manual/es/solrclient.getbyids.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/getbyids.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: dd07341fa
order: 77220
---

SolrClient::getByIds

Devuelve documentos por sus identificadores. Utiliza la funcionalidad de búsqueda en tiempo real de Solr (Solr Realtime Get - RTG)

## Descripción

```php
public SolrClient::getByIds(array $ids): SolrQueryResponse
```php

Devuelve los documentos por sus identificadores. Utiliza la búsqueda en tiempo real de Solr.

## Parámetros

`ids`  
Los identificadores de los documentos.

## Valores devueltos

`SolrQueryResponse`

## Ejemplos

Ejemplo de `SolrClient::getByIds`

```
<?php

include "bootstrap.php";

$options = array
(
    'hostname' => SOLR_SERVER_HOSTNAME,
    'login'    => SOLR_SERVER_USERNAME,
    'password' => SOLR_SERVER_PASSWORD,
    'port'     => SOLR_SERVER_PORT,
    'path'     => SOLR_SERVER_PATH
);

$client = new SolrClient($options);
$response = $client->getByIds(['GB18030TEST', '6H500F0']);

print_r($response->getResponse());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    SolrObject Object
    (
        [response] => SolrObject Object
            (
                [numFound] => 2
                [start] => 0
                [docs] => Array
                    (
                        [0] => SolrObject Object
                            (
                                [id] => GB18030TEST
                                [name] => Array
                                    (
                                        [0] => Test with some GB18030 encoded characters
                                    )

                                [features] => Array
                                    (
                                        [0] => No accents here
                                        [1] => 这是一个功能
                                        [2] => This is a feature (translated)
                                        [3] => 这份文件是很有光泽
                                        [4] => This document is very shiny (translated)
                                    )

                                [price] => Array
                                    (
                                        [0] => 0
                                    )

                                [inStock] => Array
                                    (
                                        [0] => 1
                                    )

                                [_version_] => 1510294336239042560
                            )

                        [1] => SolrObject Object
                            (
                                [id] => 6H500F0
                                [name] => Array
                                    (
                                        [0] => Maxtor DiamondMax 11 - hard drive - 500 GB - SATA-300
                                    )

                                [manu] => Array
                                    (
                                        [0] => Maxtor Corp.
                                    )

                                [manu_id_s] => maxtor
                                [cat] => Array
                                    (
                                        [0] => electronics
                                        [1] => hard drive
                                    )

                                [features] => Array
                                    (
                                        [0] => SATA 3.0Gb/s, NCQ
                                        [1] => 8.5ms seek
                                        [2] => 16MB cache
                                    )

                                [price] => Array
                                    (
                                        [0] => 350
                                    )

                                [popularity] => Array
                                    (
                                        [0] => 6
                                    )

                                [inStock] => Array
                                    (
                                        [0] => 1
                                    )

                                [store] => Array
                                    (
                                        [0] => 45.17614,-93.87341
                                    )

                                [manufacturedate_dt] => 2006-02-13T15:26:37Z
                                [_version_] => 1510294336449806336
                            )

                    )

            )

    )

## Véase también

SolrClient::getById
