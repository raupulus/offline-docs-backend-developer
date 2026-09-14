---
title: SolrClient::commit
description: Finaliza todas las añadiduras/eliminaciones hechas al índice
source_url: https://www.php.net/manual/es/solrclient.commit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/commit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 0545e305c
order: 77140
---

SolrClient::commit

Finaliza todas las añadiduras/eliminaciones hechas al índice

## Descripción

```php
public SolrClient::commit([bool $softCommit], [bool $waitSearcher], [bool $expungeDeletes]): SolrUpdateResponse
```php

Este método finaliza todas las añadiduras/eliminaciones hechas al índice.

## Parámetros

`softCommit`  
Refresca la 'vista' del índice para un mayor rendimiento, pero si sin garantizar "on-disk". (Solr4.0+)

Una consignación suave es mucho más rápida ya que solamente hace visibles los cabios de índices y usa fsync con los ficheros de índices o escribe un nuevo descriptor de índice. Si la JVM falla o hay una bajada de tensión, los cambios acaecidos después de la úlitma consignación dura se perderán. Las búsquedas que tengan requisitos cercanos al tiempo real (que requieren que los cambios de índices estén rápidamente visibles para búsquedas) necesitarán más a menudo consignas suaves, y menos frecuentemente duras.

`waitSearcher`  
Bloqueo hasta que un nuevo buscador sea abierto y registrado como el buscador de consultas principal, haciendo los cambios visibles.

`expungeDeletes`  
Mezcla segmentos con eliminaciones para desechar. (Solr1.4+)

## Valores devueltos

Devuelve un objeto `SolrUpdateResponse` en caso de éxito o lanza una excepción en caso de error.

## Errores/Excepciones

Lanza una `SolrClientException` si el cliente falló o hubo un problema de conexión.

Lanza una `SolrServerException` si el Servidor de Solr falló al procesar la petición.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL solr 1.1.0, PECL solr 2.0.0 | Se eliminó el parámetro \$maxSegments. |
| PECL solr 2.0.0b | Cambio en la API: SolrClient::commit (\[ int \$maxSegments = 0 \[, bool \$softCommit = false \[, bool \$waitSearcher = true\[, bool \$expungeDeletes = false \]\]\] ) |
| PECL solr 0.9.2 | Firma: SolrClient::commit (\[ int \$maxSegments = 1 \[, bool \$waitFlush = true \[, bool \$waitSearcher = true \]\]\] ). \$waitFlush: Bloquea hasta que los cambios de índices sean volcados a disco. |

## Notas

> [!WARNING]
> Solr \>= 2.0 de PECL solamente soporta Solr Server \>= 4.0

## Véase también

SolrClient::optimize, SolrClient::rollback
