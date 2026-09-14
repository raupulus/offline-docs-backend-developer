---
title: Stomp::readFrame
description: Leer la siguiente trama
source_url: https://www.php.net/manual/es/stomp.readframe.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stomp/stomp/readframe.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stomp
translation_status: ready
translation_reviewed: false
translation_revision: 9c7e8795c
order: 87630
---

Stomp::readFrame

stomp_read_frame

Leer la siguiente trama

## Descripción

Estilo orientado a objetos (método):

```php
public Stomp::readFrame([string $class_name]): stompframe
```php

Estilo procedimental:

```php
stomp_read_frame(resource $link): array
```

Lee la siguiente trama. Es posible crear una instancia de un objeto de una clase específica, y pasar parámetros al constructor de esa clase.

## Parámetros

`link`  
Estilo procedimental únicamente: El identificador stomp devuelto por la función`stomp_connect`.

`class_name`  
El nombre de la clase a instanciar. Si no se especifica, un objeto stompFrame es devuelto.

## Valores devueltos

> [!NOTE]
> Un encabezado de transacción puede ser especificado, indicando que la confirmación de los mensajes debe ser parte de la transacción.

## Historial de cambios

| Versión          | Descripción                             |
|------------------|-----------------------------------------|
| PECL stomp 0.4.0 | El parámentro `class_name` fue añadido. |

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

/* suscribirse a mensajes de la cola 'foo' */
$stomp->subscribe('/queue/foo');

/* leer una trama */
var_dump($stomp->readFrame());

/* cerrar la conexión */
unset($stomp);

?>

    
```

Resultado del ejemplo anterior es similar a:

    object(StompFrame)#2 (3) {
      ["command"]=>
      string(7) "MESSAGE"
      ["headers"]=>
      array(5) {
        ["message-id"]=>
        string(41) "ID:php.net-55293-1257226743606-4:2:-1:1:1"
        ["destination"]=>
        string(10) "/queue/foo"
        ["timestamp"]=>
        string(13) "1257226805828"
        ["expires"]=>
        string(1) "0"
        ["priority"]=>
        string(1) "0"
      }
      ["body"]=>
      string(3) "bar"
    }

Estilo procedimental

```php
<?php

/* conexión */
$link = stomp_connect('ssl://localhost:61612');

/* comprobar la conexión */
if (!$link) {
    die('Connection failed: ' . stomp_connect_error());
}

/* suscribirse a mensajes de la cola 'foo' */
stomp_subscribe($link, '/queue/foo');

/* leer una trama */
$frame = stomp_read_frame($link);

/* cerrar la conexión */
stomp_close($link);

?>

    
```

Resultado del ejemplo anterior es similar a:

    array(3) {
      ["command"]=>
      string(7) "MESSAGE"
      ["body"]=>
      string(3) "bar"
      ["headers"]=>
      array(6) {
        ["transaction"]=>
        string(2) "t1"
        ["message-id"]=>
        string(41) "ID:php.net-55293-1257226743606-4:3:-1:1:1"
        ["destination"]=>
        string(10) "/queue/foo"
        ["timestamp"]=>
        string(13) "1257227037059"
        ["expires"]=>
        string(1) "0"
        ["priority"]=>
        string(1) "0"
      }
    }
