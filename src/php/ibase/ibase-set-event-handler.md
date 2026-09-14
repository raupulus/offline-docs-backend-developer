---
title: ibase_set_event_handler
description: Registra una función de retrollamada para un evento interBase
source_url: https://www.php.net/manual/es/function.ibase-set-event-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-set-event-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30550
---

ibase_set_event_handler

Registra una función de retrollamada para un evento interBase

## Descripción

```php
ibase_set_event_handler(callable $event_handler, string $event_name, string ...$event_names): resource
```php

```php
ibase_set_event_handler(resource $connection, callable $event_handler, string $event_name, string ...$event_names): resource
```

`ibase_set_event_handler` registra la función PHP `event_handler` como gestor de eventos para los eventos especificados.

## Parámetros

`event_handler`  
Función de retrollamada llamada con el nombre del evento y la conexión de recurso como argumentos cuando un evento especificado es publicado en la base de datos.

La función de retrollamada `event_handler` debe devolver `false` si el gestor debe ser cancelado. Cualquier otro valor de retorno es ignorado. Esta función acepta hasta 15 argumentos de evento.

`event_name`  
El nombre del evento.

`event_names`  
15 eventos como máximo están permitidos.

## Valores devueltos

El valor devuelto es un recurso de evento. Puede ser utilizado para liberar el gestor de eventos utilizando `ibase_free_event_handler`.

## Ejemplos

Ejemplo con `ibase_set_event_handler`

```php
<?php

function event_handler($event_name, $link)
{
    if ($event_name == "NEW ORDER") {
        // Procesamiento del nuevo pedido
        ibase_query($link, "UPDATE orders SET status='handled'");
    } else if ($event_name == "DB_SHUTDOWN") {
        // Liberación del gestor
        return false;
    }
}

ibase_set_event_handler($link, "event_handler", "NEW_ORDER", "DB_SHUTDOWN");
?>

   
```

## Véase también

ibase_free_event_handler

ibase_wait_event
