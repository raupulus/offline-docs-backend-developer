---
title: solr_get_version
description: Devuelve la versión actual de la extensión Apache Solr
source_url: https://www.php.net/manual/es/function.solr-get-version.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/functions/solr-get-version.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 77100
---

solr_get_version

Devuelve la versión actual de la extensión Apache Solr

## Descripción

```php
solr_get_version(): string
```php

Esta función devuelve la versión actual de la extensión como una cadena.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una cadena en caso de éxito y `false` en caso de fallo.

## Errores/Excepciones

Esta función no lanza errores o excepciones.

## Ejemplos

Ejemplo de `solr_get_version`

```
<?php

$versión_solr = solr_get_version();

print $versión_solr;

?>

    
```php

Resultado del ejemplo anterior es similar a:

    0.9.6

## Véase también

`SolrUtils::getSolrVersion`
