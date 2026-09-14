---
title: SolrClient::__construct
description: Constructor para el objeto SolrClient
source_url: https://www.php.net/manual/es/solrclient.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: ecaa21464
order: 77150
---

SolrClient::\_\_construct

Constructor para el objeto SolrClient

## Descripción

```php
public SolrClient::__construct(array $clientOptions)
```php

Constructor para el objeto SolrClient

## Parámetros

`clientOptions`  
Esto es una matriz que contiene una de las siguientes claves:

\- secure (Valor booleano que indica si conectarse o no en modo seguro) - hostname (El nombre del host para el servidor Solr) - port (El número de puerto) - path (La ruta del servidor solr) - wt (El nombre del autor de la respuesta p.ej. xml, json) - login (EL nombre de usuario para la Autenticación HTTP, si la hubiera) - password (La contraseña de la Autenticación HTTP) - proxy_host (El nombre del host para el servidor proxy, si lo hubiera) - proxy_port (El puerto del servidor proxy) - proxy_login (El nombre de usuario del proxy) - proxy_password (La contraseña del proxy) - timeout (El tiempo máximo en segundos permitido para la operación de transferencia de datos http. Por defecto es 30 segundos) - ssl_cert (Nombre de fichero a un archvio con formato PEM que contiene la clave + certificado privados (concatenado en ese orden) ) - ssl_key (Nombre de fichero a un fichero de clave privada con formato PEM) - ssl_keypassword (Contraseña para la clave privada) - ssl_cainfo (Nombre del fichero que mantiene uno o más certificados CA para ser verificados con su par) - ssl_capath (Nombre del directorio que mantiene múltiples certificados CA para ser verificados con su par) Por favor, observe que si el fichero ssl_cert solamente contiene el certificado privado, se tiene que especificar un fichero ssl_key distinto La opción ssl_keypassword es necesaria si las opciones ssl_cert o ssl_key están establecidas.

## Errores/Excepciones

Lanza una `SolrIllegalArgumentException` en caso de error.

## Ejemplos

Ejemplo de SolrClient::\_\_construct

```
<?php

$opciones = array
(
    'hostname' => SOLR_SERVER_HOSTNAME,
    'login'    => SOLR_SERVER_USERNAME,
    'password' => SOLR_SERVER_PASSWORD,
    'port'     => SOLR_SERVER_PORT,
    'path'     => SOLR_PATH_TO_SOLR,
    'wt'       => 'xml',
);

$cliente = new SolrClient($opciones);

$doc = new SolrInputDocument();

$doc->addField('id', 334455);
$doc->addField('cat', 'Software');
$doc->addField('cat', 'Lucene');

$respuestaActualización = $cliente->addDocument($doc);

?>

    
```php

Resultado del ejemplo anterior es similar a:

## Véase también

SolrClient::getOptions
