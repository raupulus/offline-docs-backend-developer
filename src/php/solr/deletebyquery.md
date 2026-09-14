---
title: SolrClient::deleteByQuery
description: Elimina todos los documentos que coincidan con la consulta dada
source_url: https://www.php.net/manual/es/solrclient.deletebyquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/deletebyquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: 3b3be96b7
order: 77190
---

SolrClient::deleteByQuery

Elimina todos los documentos que coincidan con la consulta dada

## Descripción

```php
public SolrClient::deleteByQuery(string $query): SolrUpdateResponse
```php

Elimina todos los documentos que coincidan con la consulta dada.

## Parámetros

`query`  
La consulta

## Valores devueltos

Devuelve un objeto `SolrUpdateResponse` en caso de éxito y lanza una excepción en caso de error.

## Errores/Excepciones

Lanza una `SolrClientException` si el cliente falló o hubo un problema de conexión.

Lanza una `SolrServerException` si el Servidor de Solr falló al procesar la petición.

## Ejemplos

Ejemplo de SolrQuery::deleteByQuery

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

//Esto borrará el índice por completo
$cliente->deleteByQuery("*:*");
$cliente->commit();

?>

    
```php

## Véase también

SolrClient::deleteById, SolrClient::deleteByIds, SolrClient::deleteByQueries
