---
title: SolrClient::getById
description: Devuelve un documento por su identificador. Utiliza la funcionalidad
  de búsqueda en tiempo real de Solr (Solr Realtime Get - RTG)
source_url: https://www.php.net/manual/es/solrclient.getbyid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/getbyid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: dd07341fa
order: 77210
---

SolrClient::getById

Devuelve un documento por su identificador. Utiliza la funcionalidad de búsqueda en tiempo real de Solr (Solr Realtime Get - RTG)

## Descripción

```php
public SolrClient::getById(string $id): SolrQueryResponse
```php

Devuelve un documento por su identificador. Utiliza la búsqueda en tiempo real de Solr.

## Parámetros

`id`  
El identificador del documento.

## Valores devueltos

`SolrQueryResponse`

## Ejemplos

Ejemplo de `SolrClient::getById`

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
$response = $client->getById('GB18030TEST');
print_r($response->getResponse());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    SolrObject Object
    (
        [doc] => SolrObject Object
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

    )

## Véase también

SolrClient::getByIds
