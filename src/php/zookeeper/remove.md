---
title: ZookeeperConfig::remove
description: Eliminar servidores del conjunto
source_url: https://www.php.net/manual/es/zookeeperconfig.remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeperconfig/remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109800
---

ZookeeperConfig::remove

Eliminar servidores del conjunto

## Descripción

```php
public ZookeeperConfig::remove(string $id_list, [int $version], [array $stat]): void
```php

## Parámetros

`id_list`  
La lista separada por comas de IDs de servidores a eliminar del conjunto. Cada uno tiene un identificador de un servidor a eliminar, sólo para quórums mayoritarios.

`version`  
La versión esperada del nodo. La función fallará si la versión actual del nodo no coincide con la versión esperada. Si se utiliza -1, no se realizará la comprobación de la versión.

`stat`  
Si no es NULL, contendrá el valor de stat para la ruta de retorno.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Este método lanza `ZookeeperException` y sus derivados cuando el número o el tipo de los parámetros es incorrecto o si la eliminación del valor del nodo falla.

## Ejemplos

Ejemplo de ZookeeperConfig::remove

Quita miembros.

```
<?php
$client = new Zookeeper();
$client->connect('localhost:2181');
$client->addAuth('digest', 'timandes:timandes');
$zkConfig = $client->getConfig();
$zkConfig->set("server.1=localhost:2888:3888:participant;0.0.0.0:2181,server.2=localhost:2889:3889:participant;0.0.0.0:2182");
$zkConfig->remove("2");
echo $zkConfig->get();
if ($r)
  echo $r;
else
  echo 'ERR';
?>

   
```php

El ejemplo anterior mostrará:

    server.1=localhost:2888:3888:participant;0.0.0.0:2181
    version=0xca01e881a2

## Véase también

ZookeeperConfig::get

ZookeeperConfig::add

ZookeeperConfig::set

ZookeeperException
