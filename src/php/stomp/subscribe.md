---
title: Stomp::subscribe
description: Registrarse para escuchar a un destino dado
source_url: https://www.php.net/manual/es/stomp.subscribe.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stomp/stomp/subscribe.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stomp
translation_status: ready
translation_revision: 9c7e8795c
order: 87660
---

Stomp::subscribe

stomp_subscribe

Registrarse para escuchar a un destino dado

## Descripción

Estilo orientado a objetos (método):

```php
public Stomp::subscribe(string $destination, [array $headers]): bool
```php

Estilo procedimental:

```php
stomp_subscribe(resource $link, string $destination, [array $headers]): bool
```

Registrarse para escuchar a un destino dado.

## Parámetros

`link`  
Estilo procedimental únicamente: El identificador stomp devuelto por la función`stomp_connect`.

`destination`  
Destino al que suscribirse.

`headers`  
Array asociativo que contiene los encabezados adicionales (ejemplo: receipt).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Vea `stomp_ack`.

## Notas

> [!TIP]
> Stomp es, por naturaleza, asíncrono. Una comunicación síncrona puede ser implementada añadiendo un encabezado receipt. Esto hará que los métodos no devuelvan nada hasta que el mensaje de confirmación no haya sido recibido o hasta que el tiempo de espera no sea alcanzado.
