---
title: La clase SolrClient
source_url: https://www.php.net/manual/es/class.solrclient.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 4d17b7b49
order: 77340
---

## Introducción

Usada para enviar solicitudes al servidor Solr. Actualmente no está soportado clonar y serializar instancias de SolrClient.

## Sinopsis de la clase

SolrClient

final

SolrClient

Constantes

const

int

SolrClient::SEARCH_SERVLET_TYPE

1

const

int

SolrClient::UPDATE_SERVLET_TYPE

2

const

int

SolrClient::THREADS_SERVLET_TYPE

4

const

int

SolrClient::PING_SERVLET_TYPE

8

const

int

SolrClient::TERMS_SERVLET_TYPE

16

const

int

SolrClient::SYSTEM_SERVLET_TYPE

32

const

string

SolrClient::DEFAULT_SEARCH_SERVLET

select

const

string

SolrClient::DEFAULT_UPDATE_SERVLET

update

const

string

SolrClient::DEFAULT_THREADS_SERVLET

admin/threads

const

string

SolrClient::DEFAULT_PING_SERVLET

admin/ping

const

string

SolrClient::DEFAULT_TERMS_SERVLET

terms

const

string

SolrClient::DEFAULT_SYSTEM_SERVLET

admin/system

Métodos

## Constantes predefinidas

`SolrClient::SEARCH_SERVLET_TYPE`  
Usado cuando se actualiza servlet de búsqueda.

`SolrClient::UPDATE_SERVLET_TYPE`  
Usado cuando se actualiza el servlet de actualización.

`SolrClient::THREADS_SERVLET_TYPE`  
Usado cuando se actualiza el servlet de hilos.

`SolrClient::PING_SERVLET_TYPE`  
Usado cuando se actualiza el servlet de ping.

`SolrClient::TERMS_SERVLET_TYPE`  
Usado cuando se actualiza el servlet de términos.

`SolrClient::SYSTEM_SERVLET_TYPE`  
Usado cuando se obtiene información del sistema desde el servlet de sistema.

`SolrClient::DEFAULT_SEARCH_SERVLET`  
Este es el valor inicial del servlet de búsqueda.

`SolrClient::DEFAULT_UPDATE_SERVLET`  
Este es el valor inicial del servlet de actualizacion.

`SolrClient::DEFAULT_THREADS_SERVLET`  
Este es el valor inicial del servlet de hilos.

`SolrClient::DEFAULT_PING_SERVLET`  
Este es el valor inicial del servlet de ping.

`SolrClient::DEFAULT_TERMS_SERVLET`  
Este es el valor inicial del servlet de términos usados por TermsComponent

`SolrClient::DEFAULT_SYSTEM_SERVLET`  
Este es el valor inicial del servlet del sistema usado para obtener información de Solr Server
