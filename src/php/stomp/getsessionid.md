---
title: Stomp::getSessionId
description: Obtiene el identificador de sesión actual stomp
source_url: https://www.php.net/manual/es/stomp.getsessionid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stomp/stomp/getsessionid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stomp
translation_status: ready
translation_revision: 9c7e8795c
order: 87610
---

Stomp::getSessionId

stomp_get_session_id

Obtiene el identificador de sesión actual stomp

## Descripción

Estilo orientado a objetos (método):

```php
public Stomp::getSessionId(): string
```php

Estilo procedimental:

```php
stomp_get_session_id(resource $link): string
```

Obtiene el identificador de sesión actual stomp.

## Parámetros

`link`  
Estilo procedimental únicamente: El identificador stomp devuelto por la función`stomp_connect`.

## Valores devueltos

El identificador de sesión como `string` en caso de éxito o `false` si ocurre un error.

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

var_dump($stomp->getSessionId());

/* cerrar la conexión */
unset($stomp);

?>

    
```

Resultado del ejemplo anterior es similar a:

    string(35) "ID:php.net-52873-1257291895530-4:14"

Estilo procedural

```php
<?php

/* conexión */
$link = stomp_connect('ssl://localhost:61612');

/* comprobar la conexión */
if (!$link) {
    die('Connection failed: ' . stomp_connect_error());
}

var_dump(stomp_get_session_id($link));

/* cerrar la conexión */
stomp_close($link);

?>

    
```

Resultado del ejemplo anterior es similar a:

    string(35) "ID:php.net-52873-1257291895530-4:14"
