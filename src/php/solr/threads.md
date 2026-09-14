---
title: SolrClient::threads
description: Verifica el estado de los hilos
source_url: https://www.php.net/manual/es/solrclient.threads.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/threads.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: 3b3be96b7
order: 77330
---

SolrClient::threads

Verifica el estado de los hilos

## Descripción

```php
public SolrClient::threads(): void
```php

Verifica el estado de los hilos

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto SolrGenericResponse.

## Errores/Excepciones

Lanza una `SolrClientException` si el cliente falló o hubo un problema de conexión.

Lanza una `SolrServerException` si el Servidor de Solr falló al procesar la petición.
