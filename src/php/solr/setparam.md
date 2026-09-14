---
title: SolrParams::setParam
description: Establece el parámetro al valor especificado
source_url: https://www.php.net/manual/es/solrparams.setparam.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrparams/setparam.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: '475439775'
order: 78710
---

SolrParams::setParam

Establece el parámetro al valor especificado

## Descripción

```php
public SolrParams::setParam(string $name, string $value): SolrParams
```php

Establece el parámetro de consulta al valor especificado. Es usado para parámetros que sólo pueden ser especificados una vez. Subsiguientes llamadas con el mismo parámetro sobrescribirá el valor existente.

## Parámetros

`name`  
Nomvre del parámetro

`value`  
Valor del parámetro

## Valores devueltos

Devuelve un objeto SolrParam en caso de éxito y `false` sobre el valor.

## Ejemplos

Ejemplo de SolrParams::setParam

```
<?php

$parámetro = new SolrParams();

$parámetro->setParam('q', 'solr')->setParam('rows', 2);

?>

    
```php

Resultado del ejemplo anterior es similar a:
