---
title: SolrClient::addDocuments
description: Añade una colección de instancias de SolrInputDocument al índice
source_url: https://www.php.net/manual/es/solrclient.adddocuments.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/adddocuments.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b8758b060
order: 77130
---

SolrClient::addDocuments

Añade una colección de instancias de SolrInputDocument al índice

## Descripción

```php
public SolrClient::addDocuments(array $docs, [bool $overwrite], [int $commitWithin]): void
```php

Añade una colección de documentos al índice.

## Parámetros

`docs`  
Una array que contiene la colección de instancias de SolrInputDocument. Este array debe ser una variable real.

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

Lanza una `SolrServerException` si el Servidor de Solr falló al procesar la petición.

## Ejemplos

Ejemplo de SolrClient::addDocuments

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

$doc2 = clone $doc;

$doc2->deleteField('id');
$doc2->addField('id', 334456);

$docs = array($doc, $doc2);

$respuestaActualización = $cliente->addDocuments($docs);

// no se escribirán los cambios en disco hasta que se proporcione $commitWithin o se llame a SolrClient::commit

print_r($respuestaActualización->getResponse());

?>

    
```php

Resultado del ejemplo anterior es similar a:

    SolrObject Object
    (
        [responseHeader] => SolrObject Object
            (
                [status] => 0
                [QTime] => 2
            )

    )

## Véase también

SolrClient::addDocument, SolrClient::commit
