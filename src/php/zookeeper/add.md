---
title: ZookeeperConfig::add
description: Agregar servidores al conjunto
source_url: https://www.php.net/manual/es/zookeeperconfig.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeperconfig/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109780
---

ZookeeperConfig::add

Agregar servidores al conjunto

## Descripción

```php
public ZookeeperConfig::add(string $members, [int $version], [array $stat]): void
```php

## Parámetros

`members`  
La lista separada por comas de los servidores que se añadirán al conjunto. Cada uno tiene una línea de configuración para un servidor a añadir (como aparecería en un en un fichero de configuración), sólo para quórums mayoritarios.

`version`  
La versión esperada del nodo. La función fallará si la versión actual del nodo no coincide con la versión esperada. Si se utiliza -1, no se realizará la comprobación de la versión.

`stat`  
Si no es NULL, contendrá el valor de stat para la ruta de retorno.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Este método lanza `ZookeeperException` y sus derivados cuando el número o tipo de parámetros es incorrecto o el valor no se puede guardar en el nodo.

## Ejemplos

Ejemplo de ZookeeperConfig::add

Agrega miembros.

```
<?php
$client = new Zookeeper();
$client->connect('localhost:2181');
$client->addAuth('digest', 'timandes:timandes');
$zkConfig = $client->getConfig();
$zkConfig->set("server.1=localhost:2888:3888:participant;0.0.0.0:2181");
$zkConfig->add("server.2=localhost:2889:3889:participant;0.0.0.0:2182");
$r = $zkConfig->get();
if ($r)
  echo $r;
else
  echo 'ERR';
?>

   
```php

El ejemplo anterior mostrará:

    server.1=localhost:2888:3888:participant;0.0.0.0:2181
    server.2=localhost:2889:3889:participant;0.0.0.0:2182
    version=0xca01e881a2

## Véase también

ZookeeperConfig::get

ZookeeperConfig::set

ZookeeperConfig::remove

ZookeeperException
