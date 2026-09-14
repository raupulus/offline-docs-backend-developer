---
title: Stomp::commit
description: Validar una transacción en curso
source_url: https://www.php.net/manual/es/stomp.commit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stomp/stomp/commit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stomp
translation_status: ready
translation_reviewed: false
translation_revision: 9c7e8795c
order: 87560
---

Stomp::commit

stomp_commit

Validar una transacción en curso

## Descripción

Estilo orientado a objetos (método):

```php
public Stomp::commit(string $transaction_id, [array $headers]): bool
```php

Estilo procedimental:

```php
stomp_commit(resource $link, string $transaction_id, [array $headers]): bool
```

Valida una transacción en curso.

## Parámetros

`link`  
Estilo procedimental únicamente: El identificador stomp devuelto por la función`stomp_connect`.

`transaction_id`  
La identificación de la transacción.

`headers`  
Array asociativo que contiene los encabezados adicionales (ejemplo: receipt).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Estilo orientado a objetos

```php
<?php

/* conexión */
try {
    $stomp = new Stomp('tcp://localhost:61613');
} catch(StompException $e) {
    die('Connection failed: ' . $e->getMessage());
}

/* iniciar una transacción */
$stomp->begin('t1');

/* enviar un mensaje a la cola */
$stomp->send('/queue/foo', 'bar', array('transaction' => 't1'));

/* validar */
$stomp->commit('t1');

/* cerrar la conexión */
unset($stomp);

?>

    
```

Estilo procedimental

```php
<?php

/* conexión */
$link = stomp_connect('tcp://localhost:61613');

/* comprobar la conexión */
if (!$link) {
    die('Connection failed: ' . stomp_connect_error());
}

/* iniciar una transacción */
stomp_begin($link, 't1');

/* enviar un mensaje a la cola 'foo' */
stomp_send($link, '/queue/foo', 'bar', array('transaction' => 't1'));

/* validar */
stomp_commit($link, 't1');

/* cerrar la conexión */
stomp_close($link);

?>

    
```

## Notas

> [!TIP]
> Stomp es, por naturaleza, asíncrono. Una comunicación síncrona puede ser implementada añadiendo un encabezado receipt. Esto hará que los métodos no devuelvan nada hasta que el mensaje de confirmación no haya sido recibido o hasta que el tiempo de espera no sea alcanzado.
