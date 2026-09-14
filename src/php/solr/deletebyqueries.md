---
title: SolrClient::deleteByQueries
description: Elimina todos los documentos que coincidan con cualquiera de las consultas
source_url: https://www.php.net/manual/es/solrclient.deletebyqueries.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/deletebyqueries.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: 3b3be96b7
order: 77180
---

SolrClient::deleteByQueries

Elimina todos los documentos que coincidan con cualquiera de las consultas

## Descripción

```php
public SolrClient::deleteByQueries(array $queries): SolrUpdateResponse
```php

Elimina todos los documentos que coincidan con cualquiera de las consultas

## Parámetros

`queries`  
La matriz de consultas. Debe ser una variable de php real.

## Valores devueltos

Devuelve un objeto SolrUpdateResponse en caso de éxito y lanza una SolrClientException en caso de error.

## Errores/Excepciones

Lanza una `SolrClientException` si el cliente falló o hubo un problema de conexión.

Lanza una `SolrServerException` si el Servidor de Solr falló al procesar la petición.

## Véase también

SolrClient::deleteById, SolrClient::deleteByIds, SolrClient::deleteByQuery
