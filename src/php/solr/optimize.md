---
title: SolrClient::optimize
description: Defragmenta el índice
source_url: https://www.php.net/manual/es/solrclient.optimize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/optimize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b8758b060
order: 77250
---

SolrClient::optimize

Defragmenta el índice

## Descripción

```php
public SolrClient::optimize([int $maxSegments], [bool $softCommit], [bool $waitSearcher]): SolrUpdateResponse
```php

Defragmenta el índice para un rendimiento de búsquda más rápido.

## Parámetros

`maxSegments`  
Optimiza como máximo este número de segmentos. Desde Solr 1.3

`softCommit`  
Refresca la 'vista' del índice para un mayor rendimiento, pero si sin garantizar "on-disk". (Solr4.0+)

`waitSearcher`  
Bloqueo hasta que un nuevo buscador sea abierto y registrado como el buscador de consultas principal, haciendo los cambios visibles.

## Valores devueltos

Devuelve un objeto SolrUpdateResponse en caso de éxito y lanza una excepción en caso de error.

## Errores/Excepciones

Lanza una `SolrClientException` si el cliente falló o hubo un problema de conexión.

Lanza una `SolrServerException` si el Servidor de Solr falló al procesar la petición.

## Notas

> [!WARNING]
> Solr \>= 2.0 de PECL solamente soporta Solr Server \>= 4.0
>
> Antes de Solr 2.0 de PECL, este método solía aceptar estos argumentos: "int \$maxSegments, bool \$waitFlush, bool \$waitSearcher".

## Véase también

SolrClient::commit, SolrClient::rollback
