---
title: SolrClient::addDocument
description: Añade un documento al índice
source_url: https://www.php.net/manual/es/solrclient.adddocument.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/adddocument.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b8758b060
order: 77120
---

SolrClient::addDocument

Añade un documento al índice

## Descripción

```php
public SolrClient::addDocument(SolrInputDocument $doc, [bool $overwrite], [int $commitWithin]): SolrUpdateResponse
```php

Este método añade un documento al índice.

## Parámetros

`doc`  
La instancia de SolrInputDocument.

`overwrite`  
Si sobrescribir el documento existente o no. Si es `false` existirán duplicados (varios documento con el mismo ID).

> [!WARNING]
> En Solr \< 2.0 de PECL se usó \$allowDups en lugar de \$overwrite, que tiene la misma funcionalidad con la bandera booleana opuesta.
>
> \$allowDups = false es lo mismo que \$overwrite = true

`commitWithin`  
Número de milisegundos dentro de los que autoconsignar este documento. Disponible desde Solr 1.4. El valor predeterminado (0) significa deshabilitado.

Cuando se especifica este valor, deja el control de cúando realizar la consignación al mismo Solr, optimizando el número de consignaciones a un mínimo mientras aún se cumple con los requisitos de latencia de actualizaciones, por lo que Solr realizará automáticamente una consignación cuando la agregación más antigua en el búfer venza.

## Valores devueltos

Devuelve un objeto `SolrUpdateResponse` o lanza una excepción en caso de error.

## Errores/Excepciones

Lanza una `SolrClientException` si el cliente falló o hubo un problema de conexión.

Lanza una `SolrServerException` si el servidor de Solr falló al procesar la petición.

## Ejemplos

Ejemplo de SolrClient::addDocument

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

$doc = new SolrInputDocument();

$doc->addField('id', 334455);
$doc->addField('cat', 'Software');
$doc->addField('cat', 'Lucene');

$respuestaActualización = $cliente->addDocument($doc);

// se ha de consignar los cambios a escribir is no se usó $commitWithin
$client->commit();

print_r($respuestaActualización->getResponse());

?>

    
```php

Resultado del ejemplo anterior es similar a:

    SolrObject Object
    (
        [responseHeader] => SolrObject Object
            (
                [status] => 0
                [QTime] => 1
            )

    )

Ejemplo 2 de SolrClient::addDocument

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

$doc = new SolrInputDocument();

$doc->addField('id', 334455);
$doc->addField('cat', 'Software');
$doc->addField('cat', 'Lucene');

// No es necesario llamar a commit() ya que se proporciona $commitWithin, por lo que Solr Server autoconsignará en 10 segundos
$respuestaActualización = $cliente->addDocument($doc, false, 10000);

print_r($updateResponse->getResponse());

?>

    
```php

Resultado del ejemplo anterior es similar a:

    SolrObject Object
    (
        [responseHeader] => SolrObject Object
            (
                [status] => 0
                [QTime] => 1
            )

    )

## Véase también

SolrClient::addDocuments, SolrClient::commit
