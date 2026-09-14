---
title: Stomp::begin
description: Iniciar una transacción
source_url: https://www.php.net/manual/es/stomp.begin.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stomp/stomp/begin.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stomp
translation_status: ready
translation_revision: 9c7e8795c
order: 87550
---

Stomp::begin

stomp_begin

Iniciar una transacción

## Descripción

Estilo orientado a objetos (método):

```php
public Stomp::begin(string $transaction_id, [array $headers]): bool
```php

Estilo procedimental:

```php
stomp_begin(resource $link, string $transaction_id, [array $headers]): bool
```

Inicia una transacción.

## Parámetros

`link`  
Estilo procedimental únicamente: El identificador stomp devuelto por la función`stomp_connect`.

`transaction_id`  
La identificación de la transacción.

`headers`  
Array asociativo que contiene los encabezados adicionales (ejemplo: receipt).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Vea `stomp_commit` o `stomp_abort`.

## Notas

> [!TIP]
> Stomp es, por naturaleza, asíncrono. Una comunicación síncrona puede ser implementada añadiendo un encabezado receipt. Esto hará que los métodos no devuelvan nada hasta que el mensaje de confirmación no haya sido recibido o hasta que el tiempo de espera no sea alcanzado.
