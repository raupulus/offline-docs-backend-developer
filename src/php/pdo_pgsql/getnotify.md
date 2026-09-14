---
title: Pdo\Pgsql::getNotify
description: Devuelve una notificación asíncrona
source_url: https://www.php.net/manual/es/pdo-pgsql.getnotify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_pgsql/pdo/pgsql/getnotify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_pgsql
translation_status: ready
translation_revision: 858400b07
order: 62540
---

Pdo\Pgsql::getNotify

Devuelve una notificación asíncrona

## Descripción

```php
public Pdo\Pgsql::getNotify([int $fetchMode], [int $timeoutMilliseconds]): array
```php

Devuelve un conjunto de resultados que representa una notificación asíncrona pendiente.

## Parámetros

`fetchMode`  
El formato en el que debe estar el conjunto de resultados, una de las constantes siguientes: `PDO::FETCH_DEFAULT`, `PDO::FETCH_BOTH`, `PDO::FETCH_ASSOC`, `PDO::FETCH_NUM`

`timeoutMilliseconds`  
El tiempo de espera para una respuesta, en milisegundos.

## Valores devueltos

Si una notificación está pendiente, devuelve una sola fila, en caso contrario devuelve `false`. La fila tiene un campo `message` (el nombre del canal) y un campo `pid` (el identificador de proceso (PID) del backend notificador). Si la notificación lleva una carga útil (payload) no vacía, la fila tiene además un campo `payload`. Con `PDO::FETCH_NUM`, estos campos están en los índices `0`, `1` y `2`.

## Errores/Excepciones

Se lanza una ValueError si `fetchMode` no es una de las constantes `PDO::FETCH_*` válidas.

Se lanza una ValueError si `timeoutMilliseconds` es inferior a `0`.

Se lanza una `E_WARNING` cuando `timeoutMilliseconds` es superior al valor que puede contener un entero firmado de 32 bits, en cuyo caso será el valor máximo de un entero firmado de 32 bits.

## Ejemplos

Ejemplo de Pdo\Pgsql::getNotify

Suscribirse a un canal con `LISTEN`, luego leer la siguiente notificación pendiente con un tiempo de espera de un segundo.

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$db->exec('LISTEN messages');
$db->exec("NOTIFY messages, 'hello'");

$notification = $db->getNotify(PDO::FETCH_ASSOC, 1000);
var_export($notification);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array (
      'message' => 'messages',
      'pid' => 1928,
      'payload' => 'hello',
    )

## Véase también

PDO::query

PDOStatement::fetch

PDOStatement::fetchAll
