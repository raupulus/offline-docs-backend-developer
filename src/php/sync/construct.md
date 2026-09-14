---
title: SyncEvent::__construct
description: Construye un nuevo objeto SyncEvent
source_url: https://www.php.net/manual/es/syncevent.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sync/syncevent/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sync
translation_status: ready
translation_revision: f0edac300
order: 93520
---

SyncEvent::\_\_construct

Construye un nuevo objeto SyncEvent

## Descripción

```php
public SyncEvent::__construct([string $name], [bool $manual], [bool $prefire])
```php

Construye un objeto de evento nombrado o no.

## Parámetros

`name`  
El nombre del evento si es un objeto de evento nombrado.

> [!NOTE]
> Si el nombre ya existe, debe ser posible abrirlo con el usuario actual que ejecuta el proceso, o se lanzará una excepción con el contenido del mensaje de error.

`manual`  
Especifica si el objeto de evento debe ser reinicializado manualmente o no.

> [!NOTE]
> La reinicialización manual de los objetos de eventos permite la puesta en espera de los procesos hasta que el objeto sea reinicializado.

`prefire`  
Especifica si se debe o no pre-enviar (la señal) al objeto de evento.

> [!NOTE]
> Solo tiene impacto si la llamada al proceso/hilo es el primero en crear el objeto.

## Valores devueltos

El nuevo objeto `SyncEvent`.

## Errores/Excepciones

Se lanza una excepción si el objeto de evento no puede ser creado o abierto.

## Ejemplos

Ejemplo con `SyncEvent::__construct`

```
<?php
// En una aplicación web:
$event = new SyncEvent("GetAppReport");
$event->fire();

// En un cron:
$event = new SyncEvent("GetAppReport");
$event->wait();
?>

   
```php

## Historial de cambios

| Versión         | Descripción                      |
|-----------------|----------------------------------|
| PECL sync 1.1.0 | Adición del parámetro `prefire`. |

## Véase también

SyncEvent::fire

SyncEvent::reset

SyncEvent::wait
