---
title: Zookeeper::setLogStream
description: Define el flujo que utilizará la biblioteca para el registro
source_url: https://www.php.net/manual/es/zookeeper.setlogstream.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/setlogstream.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109740
---

Zookeeper::setLogStream

Define el flujo que utilizará la biblioteca para el registro

## Descripción

```php
public Zookeeper::setLogStream(resource $stream): bool
```php

La librería zookeeper utiliza stderr como flujo de registro por defecto. La aplicación debe asegurarse de que el flujo es escribible. Pasar NULL restablece el flujo a su valor por defecto (stderr).

## Parámetros

`stream`  
El flujo que utilizará la biblioteca para el registro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Este método emite un error/advertencia de PHP cuando el número de parámetros o tipos es incorrecto o la operación falla.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Véase también

Zookeeper::setDebugLevel

ZookeeperException
