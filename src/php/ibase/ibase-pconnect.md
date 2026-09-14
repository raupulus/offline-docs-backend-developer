---
title: ibase_pconnect
description: Abre una conexión persistente a una base de datos InterBase
source_url: https://www.php.net/manual/es/function.ibase-pconnect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-pconnect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30460
---

ibase_pconnect

Abre una conexión persistente a una base de datos InterBase

## Descripción

```php
ibase_pconnect([string $database], [string $username], [string $password], [string $charset], [int $buffers], [int $dialect], [string $role], [int $sync]): resource
```php

Abre una conexión persistente a una base de datos InterBase.

`ibase_pconnect` se comporta de manera similar a `ibase_connect`, con dos diferencias principales.

La primera es que, al conectar, la función intentará encontrar una conexión (persistente) ya abierta. Si la encuentra, esta última será devuelta, en lugar de una nueva conexión. De lo contrario, se abrirá una nueva conexión.

La segunda es que la conexión no se cerrará al final del script, sino que permanecerá abierta para su uso posterior. (`ibase_close` no cerrará una conexión abierta con `ibase_pconnect`). Este tipo de enlace se denomina 'persistente'.

## Parámetros

`database`  
El argumento `database` debe ser una ruta de acceso válida al fichero de la base de datos en el servidor donde reside. Si el servidor no es local, debe estar precedido por 'hostname:' (TCP/IP), '//hostname/' (NetBEUI) o 'hostname@' (IPX/SPX), según el protocolo utilizado.

`username`  
El nombre de usuario. Puede ser definido con la directiva `ibase.default_user` del `php.ini`.

`password`  
La contraseña para el usuario `username`. Puede ser definida con la directiva `ibase.default_password` del `php.ini`.

`charset`  
`charset` es el conjunto de caracteres por omisión para la base de datos.

`buffers`  
`buffers` es el número de buffers de la base de datos que se asignarán para la caché del lado del servidor. Si este parámetro vale 0 o si se omite, el servidor elegirá este número por sí mismo.

`dialect`  
`dialect` selecciona el dialecto SQL por omisión para todas las consultas ejecutadas en la conexión, y valdrá por omisión, el más alto soportado por la biblioteca cliente. Solo funciona con InterBase 6 y superiores.

`role`  
Solo funciona con InterBase 5 y superiores.

`sync`  

## Valores devueltos

Devuelve un identificador de conexión InterBase en caso de éxito, o `false` si ocurre un error.

## Véase también

ibase_close

ibase_connect
