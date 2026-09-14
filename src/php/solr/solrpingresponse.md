---
title: La clase SolrPingResponse
source_url: https://www.php.net/manual/es/class.solrpingresponse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrpingresponse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 4d17b7b49
order: 78780
---

## Introducción

Representa una respuesta a una petición ping al servidor

## Sinopsis de la clase

SolrPingResponse

final

SolrPingResponse

extends

SolrResponse

Constantes

const

int

SolrPingResponse::PARSE_SOLR_OBJ

0

const

int

SolrPingResponse::PARSE_SOLR_DOC

1

Propiedades

Métodos

Métodos heredados

## Propiedades

`http_status`  
El estado http de la resupuesta.

`parser_mode`  
Modo de analizar los documentos, si como instancias de SolrObject o de SolrDocument.

`success`  
¿Ocurrió un error durante la solicitud?

`http_status_message`  
Messaje detallado del estado http

`http_request_url`  
La URL solicitada

`http_raw_request_headers`  
Una cadena de cabeceras en bruto enviada durante la solicitud

`http_raw_request`  
La solicitud en bruto enviada al servidor

`http_raw_response_headers`  
Las cabeceras de resupuesta del servidor Solr

`http_raw_response`  
El mensaje de respuesta del servidor

`http_digested_response`  
La respuesta en formato serializado de PHP.

## Constantes predefinidas

## Constantes de la Clase SolrPingResponse

`SolrPingResponse::PARSE_SOLR_OBJ`  
Los documentos deberían ser analizados como instancias de SolrObject

`SolrPingResponse::PARSE_SOLR_DOC`  
Los documentos deberían ser analizados como instancias de SolrDocument.
