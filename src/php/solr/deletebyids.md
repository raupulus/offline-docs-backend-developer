---
title: SolrClient::deleteByIds
description: Elimina mediante Ids
source_url: https://www.php.net/manual/es/solrclient.deletebyids.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/deletebyids.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: 3b3be96b7
order: 77170
---

SolrClient::deleteByIds

Elimina mediante Ids

## Descripción

```php
public SolrClient::deleteByIds(array $ids): SolrUpdateResponse
```php

Elimina una colección de documentos con el conjunto de ids especificado.

## Parámetros

`ids`  
Una matriz de IDs que representa el campo uniqueKey declarado en el esquema para cada documento a ser eliminado. Debe ser una variable de PHP real.

## Valores devueltos

Devuelve un objeto `SolrUpdateResponse` en caso de éxito y lanza una excepción en caso de error.

## Errores/Excepciones

Lanza una `SolrClientException` si el cliente falló o hubo un problema de conexión.

Lanza una `SolrServerException` si el Servidor de Solr falló al procesar la petición.

## Véase también

SolrClient::deleteById, SolrClient::deleteByQuery, SolrClient::deleteByQueries
