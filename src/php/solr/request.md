---
title: SolrClient::request
description: Envía una petición de actualización sin formato
source_url: https://www.php.net/manual/es/solrclient.request.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/request.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: dcf567d21
order: 77280
---

SolrClient::request

Envía una petición de actualización sin formato

## Descripción

```php
public SolrClient::request(string $raw_request): SolrUpdateResponse
```php

Envía una petición de actualización XML sin formato al servidor

## Parámetros

`raw_request`  
Una cadena XML con la solicitud sin formato al servidor.

## Valores devueltos

Devuelve un objeto `SolrUpdateResponse` en caso de éxito. Lanza una excepción en caso de error.

## Errores/Excepciones

Lanza una `SolrIllegalArgumentException` si `raw_request` es un string vacío.

Lanza una `SolrClientException` si el cliente falló o hubo un problema de conexión.

Lanza una `SolrServerException` si el Servidor de Solr falló al satisfacer la consulta.

## Ejemplos

Ejemplo de SolrClient::request

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

$respuesta_actualización = $cliente->request("<commit/>");

$respuesta = $respuesta_actualización->getResponse();

print_r($respuesta);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    ...
