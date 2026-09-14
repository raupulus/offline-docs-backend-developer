---
title: Stomp::setReadTimeout
description: Establecer el tiempo de espera de lectura
source_url: https://www.php.net/manual/es/stomp.setreadtimeout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stomp/stomp/setreadtimeout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stomp
translation_status: ready
translation_reviewed: false
translation_revision: 9c7e8795c
order: 87650
---

Stomp::setReadTimeout

stomp_set_read_timeout

Establecer el tiempo de espera de lectura

## Descripción

Estilo orientado a objetos (método):

```php
public Stomp::setReadTimeout(int $seconds, [int $microseconds]): void
```php

Estilo procedimental:

```php
stomp_set_read_timeout(resource $link, int $seconds, [int $microseconds]): void
```

Establece el tiempo de espera de lectura.

## Parámetros

`link`  
Estilo procedimental únicamente: El identificador stomp devuelto por la función`stomp_connect`.

`seconds`  
Los segundos parte de el tiempo de espera a ser establecido.

`microseconds`  
Los microsegundos parte de el tiempo de espera a ser establecido.

## Valores devueltos

No se retorna ningún valor.

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

$stomp->setReadTimeout(10);

/* cerrar la conexión */
unset($stomp);

?>

    
```

Estilo procedimental

```php
<?php

/* conexión */
$link = stomp_connect('ssl://localhost:61612');

/* comprobar la conexión */
if (!$link) {
    die('Connection failed: ' . stomp_connect_error());
}

stomp_set_read_timeout($link, 10);

/* cerrar la conexión */
stomp_close($link);

?>

    
```
