---
title: SolrInputDocument::addChildDocuments
description: Añade un array de documentos hijos
source_url: https://www.php.net/manual/es/solrinputdocument.addchilddocuments.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrinputdocument/addchilddocuments.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: d00128a85
order: 78280
---

SolrInputDocument::addChildDocuments

Añade un array de documentos hijos

## Descripción

```php
public SolrInputDocument::addChildDocuments(array $docs): void
```php

Añade un array de documentos hijos al documento de entrada actual.

## Parámetros

`docs`  
Un `array` de objetos `SolrInputDocument`.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una `SolrIllegalArgumentException` en caso de error.

Lanza una `SolrException` en caso de error interno.

## Ejemplos

Ejemplo de `SolrInputDocument::addChildDocuments`

```
<?php

include "bootstrap.php";

$options = array
(
    'hostname' => SOLR_SERVER_HOSTNAME,
    'login'    => SOLR_SERVER_USERNAME,
    'password' => SOLR_SERVER_PASSWORD,
    'port'     => SOLR_SERVER_PORT,
    'path'     => SOLR_SERVER_STORE_PATH,
);

$client = new SolrClient($options);

$product = new SolrInputDocument();

$product->addField('id', 'P-BLACK');
$product->addField('cat', 'tshirt');
$product->addField('cat', 'polo');
$product->addField('content_type', 'product');

$small = new SolrInputDocument();
$small->addField('id', 'TS-BLK-S');
$small->addField('content_type', 'sku');
$small->addField('size', 'S');
$small->addField('inventory', 100);

$medium = new SolrInputDocument();
$medium->addField('id', 'TS-BLK-M');
$medium->addField('content_type', 'sku');
$medium->addField('size', 'M');
$medium->addField('inventory', 200);

$large = new SolrInputDocument();
$large->addField('id', 'TS-BLK-L');
$large->addField('content_type', 'sku');
$large->addField('size', 'L');
$large->addField('inventory', 300);

// añade los documentos hijos
$skus = [$small, $medium, $large];
$product->addChildDocuments($skus);

// añade el bloque de documento producto al índice
$updateResponse = $client->addDocument(
        $product,
        true, // sobrescribe si el documento existe
        10000 // valida el commit en 10 segundos
);

print_r($updateResponse->getResponse());

   
```php

Resultado del ejemplo anterior es similar a:

    SolrObject Object
    (
        [responseHeader] => SolrObject Object
            (
                [status] => 0
                [QTime] => 5
            )
    )

## Véase también

SolrInputDocument::addChildDocument

SolrInputDocument::hasChildDocuments

SolrInputDocument::getChildDocuments

SolrInputDocument::getChildDocumentsCount
