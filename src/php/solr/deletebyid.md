---
title: SolrClient::deleteById
description: Eliminar por Id
source_url: https://www.php.net/manual/es/solrclient.deletebyid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/deletebyid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: 3b3be96b7
order: 77160
---

SolrClient::deleteById

Eliminar por Id

## Descripción

```php
public SolrClient::deleteById(string $id): SolrUpdateResponse
```php

Elimina el documento con el ID especificado, donde ID es el valor del campo uniqueKey declarado en el esquema.

## Parámetros

`id`  
El valor del campo uniqueKey declarado en el esquema

## Valores devueltos

Devuelve un objeto `SolrUpdateResponse` en caso de éxito y lanza una excepción en caso de error.

## Errores/Excepciones

Lanza una `SolrClientException` si el cliente falló o hubo un problema de conexión.

Lanza una `SolrServerException` si el Servidor de Solr falló al procesar la petición.

## Véase también

SolrClient::deleteByIds, SolrClient::deleteByQuery, SolrClient::deleteByQueries
