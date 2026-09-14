---
title: SolrClient::setResponseWriter
description: Establece el autor de la respuesta usado para preparar la respuesta de
  Solr
source_url: https://www.php.net/manual/es/solrclient.setresponsewriter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/setresponsewriter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: 8494712d3
order: 77300
---

SolrClient::setResponseWriter

Establece el autor de la respuesta usado para preparar la respuesta de Solr

## Descripción

```php
public SolrClient::setResponseWriter(string $responseWriter): void
```php

Establece el autor de la respuesta usado para preparar la respuesta de Solr

## Parámetros

`responseWriter`  
Uno de los siguientes autores:

json

phps

xml

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de SolrClient::setResponseWriter

```
<?php

// Esta es mi clase personalizada para los objetos
class SolrClass
{
   public $_propiedades = array();

   public function __get($nombre_propiedad) {

      if (property_exists($this, $nombre_propiedad)) {

          return $this->$nombre_propiedad;

      } else if (isset($_propiedades[$nombre_propiedad])) {

          return $_propiedades[$nombre_propiedad];
      }

      return null;
   }
}

$opciones = array
(
  'hostname' => 'localhost',
  'port' => 8983,
  'path' => '/solr/core1'
);

$cliente = new SolrClient($opciones);

$cliente->setResponseWriter("json");

//$respuesta = $cliente->ping();

$consulta = new SolrQuery();

$consulta->setQuery("*:*");

$consulta->set("objectClassName", "SolrClass");

$consulta->set("objectPropertiesStorageMode", 1); // 0 para propiedades independientes, 1 para combinadas

try
{

$respuesta = $cliente->query($consulta);

$resp = $respuesta->getResponse();

print_r($respuesta);

print_r($resp);

} catch (Exception $e) {

print_r($e);

}

?>

    
```php
