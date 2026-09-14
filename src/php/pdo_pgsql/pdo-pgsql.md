---
title: La clase Pdo\Pgsql
source_url: https://www.php.net/manual/es/class.pdo-pgsql.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_pgsql/pdo-pgsql.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_pgsql
translation_status: ready
translation_reviewed: true
translation_revision: 205c3b8ad
order: 62600
---

## Introducción

Una subclase de `PDO` que representa una conexión utilizando el controlador PDO PostgreSQL.

Este controlador admite un analizador de consultas SQL dedicado para el dialecto PostgreSQL. Puede gestionar los siguientes elementos:

- Los literales de string simples y dobles, con el duplicado como mecanismo de escape

- Los literales de string "escapados" de estilo C

- Los literales de string en dólares

- Dos guiones y los comentarios de estilo C (no anidados)

- El soporte de `??` como secuencia de escape para el operador `?`.

## Sinopsis de la clase

Pdo

Pgsql

extends

PDO

Constantes heredadas

Constantes

public

const

int

Pdo\Pgsql::ATTR_DISABLE_PREPARES

public

const

int

Pdo\Pgsql::ATTR_RESULT_MEMORY_SIZE

public

const

int

Pdo\Pgsql::TRANSACTION_IDLE

public

const

int

Pdo\Pgsql::TRANSACTION_ACTIVE

public

const

int

Pdo\Pgsql::TRANSACTION_INTRANS

public

const

int

Pdo\Pgsql::TRANSACTION_INERROR

public

const

int

Pdo\Pgsql::TRANSACTION_UNKNOWN

Métodos

Métodos heredados

## Constantes predefinidas

`Pdo\Pgsql::ATTR_DISABLE_PREPARES`  
Envía la consulta y los argumentos al servidor en una sola vez, evitando la necesidad de crear una sentencia preparada nombrada por separado. Si la consulta va a ser ejecutada una sola vez, esto puede reducir la latencia evitando un viaje de ida y vuelta innecesario al servidor.

`Pdo\Pgsql::ATTR_RESULT_MEMORY_SIZE`  
Devuelve la cantidad de memoria, en bytes, asignada a la instancia de `PDOStatement` del resultado de la consulta especificada, o `null` si no existe ningún resultado antes de la ejecución de la consulta.

`PDO::ATTR_PREFETCH`  
A partir de PHP 8.5.0, asignar el valor `0` a este atributo activa la obtención perezosa (fila a fila): las filas se recuperan del servidor de una en una a medida que se obtienen, en lugar de almacenar en memoria todo el conjunto de resultados antes de la primera llamada a PDOStatement::fetch. Esto reduce el uso de memoria para conjuntos de resultados grandes. Cualquier otro valor mantiene el comportamiento almacenado en búfer por omisión.

Puede establecerse por conexión con PDO::setAttribute, o por sentencia mediante las opciones de controlador de PDO::prepare o PDO::query.

> [!CAUTION]
> En modo perezoso, una conexión sólo puede tener una sentencia activa a la vez. Ejecutar otra sentencia descarta de forma silenciosa las filas no leídas de la anterior; no se genera ningún error.

`Pdo\Pgsql::TRANSACTION_IDLE`  
> [!WARNING]
> Esta constante no tiene efecto y está obsoleta a partir de PHP 8.5.0.

`Pdo\Pgsql::TRANSACTION_ACTIVE`  
> [!WARNING]
> Esta constante no tiene efecto y está obsoleta a partir de PHP 8.5.0.

`Pdo\Pgsql::TRANSACTION_INTRANS`  
> [!WARNING]
> Esta constante no tiene efecto y está obsoleta a partir de PHP 8.5.0.

`Pdo\Pgsql::TRANSACTION_INERROR`  
> [!WARNING]
> Esta constante no tiene efecto y está obsoleta a partir de PHP 8.5.0.

`Pdo\Pgsql::TRANSACTION_UNKNOWN`  
> [!WARNING]
> Esta constante no tiene efecto y está obsoleta a partir de PHP 8.5.0.
