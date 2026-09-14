---
title: SolrDocument::toArray
description: Devuelve una matriz como representación de un documento
source_url: https://www.php.net/manual/es/solrdocument.toarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdocument/toarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 78100
---

SolrDocument::toArray

Devuelve una matriz como representación de un documento

## Descripción

```php
public SolrDocument::toArray(): array
```php

Devuelve una matriz como representación de un documento.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una matriz como representación de un documento.

## Ejemplos

Ejemplo de SolrDocument::toArray

```
<?php

$doc = new SolrDocument();

$doc->addField('id', 1123);

$doc->features = "PHP Client Side";
$doc->features = "Fast development cycles";

$doc['cat'] = 'Software';
$doc['cat'] = 'Custom Search';
$doc->cat   = 'Information Technology';

print_r($doc->toArray());

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [document_boost] => 0
        [field_count] => 3
        [fields] => Array
            (
                [0] => SolrDocumentField Object
                    (
                        [name] => id
                        [boost] => 0
                        [values] => Array
                            (
                                [0] => 1123
                            )

                    )

                [1] => SolrDocumentField Object
                    (
                        [name] => features
                        [boost] => 0
                        [values] => Array
                            (
                                [0] => PHP Client Side
                                [1] => Fast development cycles
                            )

                    )

                [2] => SolrDocumentField Object
                    (
                        [name] => cat
                        [boost] => 0
                        [values] => Array
                            (
                                [0] => Software
                                [1] => Custom Search
                                [2] => Information Technology
                            )

                    )

            )

    )
