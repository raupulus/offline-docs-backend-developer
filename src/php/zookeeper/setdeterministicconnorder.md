---
title: Zookeeper::setDeterministicConnOrder
description: Activa/desactiva la aleatorización del orden de los puntos finales de
  quórum.
source_url: https://www.php.net/manual/es/zookeeper.setdeterministicconnorder.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/setdeterministicconnorder.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109730
---

Zookeeper::setDeterministicConnOrder

Activa/desactiva la aleatorización del orden de los puntos finales de quórum.

## Descripción

```php
public static Zookeeper::setDeterministicConnOrder(bool $yesOrNo): bool
```php

Si se establece en true, hará que el cliente se conecte a los nodos del quórum en el orden especificado en la llamada a zookeeper_init(). Un valor falso causará que zookeeper_init() intercambie los puntos finales de los nodos del quórum, lo que es bueno para una distribución más uniforme de las conexiones de los clientes entre los nodos del quórum. El cliente ZooKeeper C utiliza false por defecto.

## Parámetros

`yesOrNo`  
Activa/desactiva la aleatorización del orden de los puntos finales de quórum.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Este método emite un error/advertencia de PHP cuando el número de parámetros o tipos es incorrecto o la operación falla.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Véase también

Zookeeper::\_\_construct

Zookeeper::connect

ZookeeperException
