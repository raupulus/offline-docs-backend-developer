---
title: Pdo\Pgsql::setNoticeCallback
description: Establece una función de retrollamada para gestionar los mensajes de
  aviso y advertencia generados por el servidor
source_url: https://www.php.net/manual/es/pdo-pgsql.setnoticecallback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_pgsql/pdo/pgsql/setnoticecallback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_pgsql
translation_status: ready
translation_reviewed: true
translation_revision: 9ec2c28f9
order: 62590
---

Pdo\Pgsql::setNoticeCallback

Establece una función de retrollamada para gestionar los mensajes de aviso y advertencia generados por el servidor

## Descripción

```php
public Pdo\Pgsql::setNoticeCallback(callable $callback): void
```php

Establece una función de retrollamada para gestionar los mensajes de aviso y advertencia generados por el servidor. Esto incluye los mensajes emitidos por PostgreSQL, así como aquellos generados por las funciones SQL definidas por el usuario utilizando `RAISE`. Tenga en cuenta que la recepción efectiva de estos mensajes depende del parámetro del servidor `client_min_messages`.

## Parámetros

`callback`  
Si se pasa `null`, la función de retrollamada se reinicializa a su estado por omisión.

De lo contrario, la función de retrollamada es una retrollamada con la siguiente firma:

```php
handler(string $message): void
```

`message`  
Un mensaje generado por el servidor.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de Pdo\Pgsql::setNoticeCallback

```php
<?php
$pdo = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);

$pdo->exec('CREATE TABLE parent(id int primary key)');
$pdo->exec('CREATE TABLE child(id int references parent)');

$pdo->setNoticeCallback(function ($message) {
    echo $message;
});

$pdo->exec('TRUNCATE parent CASCADE');
?>

   
```

Resultado del ejemplo anterior es similar a:

    NOTICE:  truncate cascades to table "child"
