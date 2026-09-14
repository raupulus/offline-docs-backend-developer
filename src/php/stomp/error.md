---
title: Stomp::error
description: Obtiene el último error stomp
source_url: https://www.php.net/manual/es/stomp.error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stomp/stomp/error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stomp
translation_status: ready
translation_revision: 9c7e8795c
order: 87590
---

Stomp::error

stomp_error

Obtiene el último error stomp

## Descripción

Estilo orientado a objetos (método):

```php
public Stomp::error(): string
```php

Estilo procedimental:

```php
stomp_error(resource $link): string
```

Obtiene el último error stomp.

## Parámetros

`link`  
Estilo procedimental únicamente: El identificador stomp devuelto por la función`stomp_connect`.

## Valores devueltos

Devuelve una cadena de error o `false` si no hay errores.

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

var_dump($stomp->error());

if (!$stomp->abort('unknown-transaction', array('receipt' => 'foo'))) {
    var_dump($stomp->error());
}

/* cerrar la conexión */
unset($stomp);

?>

    
```

Resultado del ejemplo anterior es similar a:

    bool(false)
    string(43) "Invalid transaction id: unknown-transaction"

Estilo procedimental

```php
<?php

/* conexión */
$link = stomp_connect('ssl://localhost:61612');

/* comprobar la conexión */
if (!$link) {
    die('Connection failed: ' . stomp_connect_error());
}

var_dump(stomp_error($link));

if (!stomp_abort($link, 'unknown-transaction', array('receipt' => 'foo'))) {
    var_dump(stomp_error($link));
}

/* cerrar la conexión */
stomp_close($link);

?>

    
```

Resultado del ejemplo anterior es similar a:

    bool(false)
    string(43) "Invalid transaction id: unknown-transaction"
