---
title: Zookeeper::exists
description: Comprueba la existencia de un nodo de forma sincrónica
source_url: https://www.php.net/manual/es/zookeeper.exists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/exists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109610
---

Zookeeper::exists

Comprueba la existencia de un nodo de forma sincrónica

## Descripción

```php
public Zookeeper::exists(string $path, [callable $watcher_cb]): array
```php

## Parámetros

`path`  
El nombre del nodo. Expresado como un nombre de archivo con barras separando los ancestros del nodo.

`watcher_cb`  
Si es distinto de cero, se establecerá un observador en el servidor para notificar al cliente si el nodo cambia. El observador se activará incluso si el nodo no existe.

## Valores devueltos

Devuelve el valor stat de la ruta si el nodo dado existe, en caso contrario false.

## Errores/Excepciones

Este método emite un error/advertencia de PHP cuando el número de parámetros o los tipos son incorrectos o la comprobación de existencia del nodo ha fallado.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Ejemplos

Ejemplo de Zookeeper::exists

Comprueba la existencia de un nodo.

```
<?php
$zookeeper = new Zookeeper('localhost:2181');
$path = '/path/to/node';
$r = $zookeeper->exists($path);
if ($r)
  echo 'EXISTS';
else
  echo 'N/A or ERR';
?>

   
```php

El ejemplo anterior mostrará:

    EXISTS

## Véase también

Zookeeper::get

ZookeeperException
