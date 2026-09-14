---
title: SolrUtils::digestXmlResponse
description: Convierte una cadena de respuesta XML a un objeto SolrObject
source_url: https://www.php.net/manual/es/solrutils.digestxmlresponse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrutils/digestxmlresponse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 80950
---

SolrUtils::digestXmlResponse

Convierte una cadena de respuesta XML a un objeto SolrObject

## Descripción

```php
public static SolrUtils::digestXmlResponse(string $xmlresponse, [int $parse_mode]): SolrObject
```php

Este método convierte una cadena de respuesta XML del servidor Apache Solr a un objeto SolrObject. Lanza una excepción SolrException si hubo un error.

## Parámetros

`xmlresponse`  
La cadena de respuesta XML del servidor Solr.

`parse_mode`  
Use SolrResponse::PARSE_SOLR_OBJ o SolrResponse::PARSE_SOLR_DOC

## Valores devueltos

Devuelve el objeto SolrObject que representa la respuesta XML.

Si el parámetro parse_mode setá establecido a SolrResponse::PARSE_SOLR_OBJ Solr los documentos serán analizados como instancias de SolrObject.

si está establecido a SolrResponse::PARSE_SOLR_DOC, serán analizados como instancias de SolrDocument.
