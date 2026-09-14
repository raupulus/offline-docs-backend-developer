---
title: SolrClient::ping
description: Comprueba si el servidor Solr está todavía activo
source_url: https://www.php.net/manual/es/solrclient.ping.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/ping.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: 3b3be96b7
order: 77260
---

SolrClient::ping

Comprueba si el servidor Solr está todavía activo

## Descripción

```php
public SolrClient::ping(): SolrPingResponse
```php

Comprueba si el servidor Solr está todavía activo. Envía una petición HEAD al servidor Apache Solr.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto `SolrPingResponse` en caso de éxito y lanza una excepción en caso de error.

## Errores/Excepciones

Lanza una `SolrClientException` si el cliente falló o hubo un problema de conexión.

Lanza una `SolrServerException` si el Servidor de Solr falló al satisfacer la petición.

## Ejemplos

Ejemplo de SolrClient::ping

```
<?php
$options = array
(
    'hostname' => SOLR_SERVER_HOSTNAME,
    'login'    => SOLR_SERVER_USERNAME,
    'password' => SOLR_SERVER_PASSWORD,
    'port'     => SOLR_SERVER_PORT,
);

$client = new SolrClient($options);

$pingresponse = $client->ping();

?>

    
```php

Resultado del ejemplo anterior es similar a:
