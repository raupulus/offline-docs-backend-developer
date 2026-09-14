---
title: Stomp::getReadTimeout
description: Obtener la lectura del tiempo de espera de la solicitud
source_url: https://www.php.net/manual/es/stomp.getreadtimeout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stomp/stomp/getreadtimeout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stomp
translation_status: ready
translation_reviewed: false
translation_revision: 9c7e8795c
order: 87600
---

Stomp::getReadTimeout

stomp_get_read_timeout

Obtener la lectura del tiempo de espera de la solicitud

## Descripción

Estilo orientado a objetos (método):

```php
public Stomp::getReadTimeout(): array
```php

Estilo procedimental:

```php
stomp_get_read_timeout(resource $link): array
```

Obtiene la lectura del tiempo de espera de la solicitud

## Parámetros

`link`  
Estilo procedimental únicamente: El identificador stomp devuelto por la función`stomp_connect`.

## Valores devueltos

Devuelve un array con dos elementos: sec y usec.

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

var_dump($stomp->getReadTimeout());

/* cerrar la conexión */
unset($stomp);

?>

    
```

Resultado del ejemplo anterior es similar a:

    array(2) {
      ["sec"]=>
      int(2)
      ["usec"]=>
      int(0)
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

var_dump(stomp_get_read_timeout($link));

/* cerrar la conexión */
stomp_close($link);

?>

    
```

Resultado del ejemplo anterior es similar a:

    array(2) {
      ["sec"]=>
      int(2)
      ["usec"]=>
      int(0)
    }
