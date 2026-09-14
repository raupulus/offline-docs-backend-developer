---
title: SolrDisMaxQuery::__construct
description: Constructor de clase
source_url: https://www.php.net/manual/es/solrdismaxquery.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: ecaa21464
order: 77580
---

SolrDisMaxQuery::\_\_construct

Constructor de clase

## Descripción

```php
public SolrDisMaxQuery::__construct([string $q])
```php

Constructor de clase que inicializa el objeto y define el parámetro q si se proporciona

## Parámetros

`q`  
El parámetro de búsqueda (parámetro q)

## Valores devueltos

## Errores/Excepciones

Genera una excepción `SolrIllegalArgumentException` si se ha pasado un parámetro inválido.

## Ejemplos

Ejemplo de `SolrDisMaxQuery::__construct`

```
<?php

$dismaxQuery = new SolrDisMaxQuery('lucene');
echo $dismaxQuery;

?>

   
```php

El ejemplo anterior mostrará:

    q=lucene&defType=edismax
