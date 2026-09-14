---
title: SolrDisMaxQuery::setQueryPhraseSlop
description: Especifica la cantidad de tolerancia permitida en las consultas de frase
  explícitamente incluidas en la cadena de consulta del usuario (parámetro qf)
source_url: https://www.php.net/manual/es/solrdismaxquery.setqueryphraseslop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/setqueryphraseslop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 7418592d8
order: 77730
---

SolrDisMaxQuery::setQueryPhraseSlop

Especifica la cantidad de tolerancia permitida en las consultas de frase explícitamente incluidas en la cadena de consulta del usuario (parámetro qf)

## Descripción

```php
public SolrDisMaxQuery::setQueryPhraseSlop(string $slop): SolrDisMaxQuery
```php

La cantidad de tolerancia en las consultas de frase explícitamente incluidas en la cadena de consulta del usuario con el parámetro *qf*.

La tolerancia se refiere al número de posiciones que debe moverse un token respecto a otro token para coincidir con una frase especificada en una consulta.

## Parámetros

`slop`  
La cantidad de tolerancia

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::setQueryPhraseSlop`

```
<?php

$dismaxQuery = new SolrDisMaxQuery();
$dismaxQuery->setQueryPhraseSlop(3);
echo $dismaxQuery;
?>

   
```php

Resultado del ejemplo anterior es similar a:

    defType=edismax&qs=3
