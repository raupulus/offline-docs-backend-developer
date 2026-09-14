---
title: MongoDB\Driver\Server::executeQuery
description: Ejecuta una consulta de base de datos en este servidor
source_url: https://www.php.net/manual/es/mongodb-driver-server.executequery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/executequery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 6047c10c1
order: 50980
---

MongoDB\Driver\Server::executeQuery

Ejecuta una consulta de base de datos en este servidor

## Descripción

```php
final public MongoDB\Driver\Server::executeQuery(string $namespace, MongoDB\Driver\Query $query, [array $options]): MongoDB\Driver\Cursor
```php

Ejecuta la consulta en este servidor.

Los valores por omisión para la opción `"readPreference"` y la opción `"readConcern"` de la consulta se deducirán de una transacción activa (indicada por la opción `"session"`), luego por la [URI de conexión](#mongodb-driver-manager.construct-uri).

> [!NOTE]
> La opción `"readPreference"` no controla el servidor hacia el cual el controlador emite la operación; siempre se ejecutará en este objeto servidor. En su lugar, puede ser utilizado al emitir la operación a un secundario (desde una conexión de conjunto de réplicas, no autónoma) o el nodo Mongos para asegurarse de que el controlador defina el protocolo de fila en consecuencia o añada la preferencia de lectura a la operación, respectivamente.

## Parámetros

`namespace` (`string`)  
Un espacio de nombres completamente calificado (ej. `"databaseName.collectionName"`)

`query` (`MongoDB\Driver\Query`)  
La consulta a ejecutar.

`options`  
| Opción | Tipo | Descripción |
|----|----|----|
| readPreference | `MongoDB\Driver\ReadPreference` | Una preferencia de lectura a utilizar para seleccionar un servidor para la operación. |
| session | `MongoDB\Driver\Session` | Una sesión a asociar a la operación. |

options

## Valores devueltos

Retorna un `MongoDB\Driver\Cursor` en caso de éxito.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una excepción

MongoDB\Driver\Exception\ConnectionException

si la conexión al servidor falla por una razón distinta a un problema de identificación

Lanza una excepción

MongoDB\Driver\Exception\AuthenticationException

si se requiere una identificación pero falla

Lanza una excepción

MongoDB\Driver\Exception\RuntimeException

si ocurre un error (i.e. operadores de consulta inválidos).

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | El parámetro `options` ya no acepta una instancia `MongoDB\Driver\WriteConcern`. |
| PECL mongodb 1.21.0 | Pasar un objeto `MongoDB\Driver\ReadPreference` como `options` está obsoleto y será eliminado en la 2.0. |
| PECL mongodb 1.4.0 | El tercer parámetro es ahora un array de `options`. Para la compatibilidad ascendente, este parámetro siempre aceptará un objeto `MongoDB\Driver\ReadPreference`. |

## Véase también

MongoDB\Driver\Cursor

MongoDB\Driver\Query

MongoDB\Driver\ReadPreference

MongoDB\Driver\Manager::executeQuery
