---
title: Stomp::__construct
description: Abre una conexión
source_url: https://www.php.net/manual/es/stomp.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stomp/stomp/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stomp
translation_status: ready
translation_revision: 9c7e8795c
order: 87570
---

Stomp::\_\_construct

stomp_connect

Abre una conexión

## Descripción

Estilo orientado a objetos (constructor):

```php
public Stomp::__construct([string $broker], [string $username], [string $password], [array $headers])
```php

Estilo procedimental:

```php
stomp_connect([string $broker], [string $username], [string $password], [array $headers]): resource
```

Abre una conexión con un Message Broker compatible con el protocolo STOMP.

## Parámetros

`broker`  
La URI broker

`username`  
El nombre de usuario.

`password`  
La contraseña.

`headers`  
Array asociativo que contiene los encabezados adicionales (ejemplo: receipt).

## Valores devueltos

> [!NOTE]
> Un encabezado de transacción puede ser especificado, indicando que la confirmación de los mensajes debe ser parte de la transacción.

## Historial de cambios

| Versión          | Descripción                        |
|------------------|------------------------------------|
| PECL stomp 1.0.1 | El paramétro `headers` fue añadido |

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

/* cerrar la conexión */
stomp_close($link);

?>

    
```
