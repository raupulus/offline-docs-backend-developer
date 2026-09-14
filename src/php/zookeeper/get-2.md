---
title: ZookeeperConfig::get
description: Devuelve la última configuración validada del clúster ZooKeeper conocida
  por el servidor al que está conectado el cliente, de forma sincrónica
source_url: https://www.php.net/manual/es/zookeeperconfig.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeperconfig/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109790
---

ZookeeperConfig::get

Devuelve la última configuración validada del clúster ZooKeeper conocida por el servidor al que está conectado el cliente, de forma sincrónica

## Descripción

```php
public ZookeeperConfig::get([callable $watcher_cb], [array $stat]): string
```php

## Parámetros

`watcher_cb`  
Si es distinto de cero, se colocará un observador en el servidor para notificar al cliente si cambia el nodo.

`stat`  
Si no es NULL, contendrá el valor de stat para la ruta de retorno.

## Valores devueltos

Devuelve la cadena de configuración en caso de éxito, y false en caso de fallo.

## Errores/Excepciones

Este método lanza `ZookeeperException` y sus derivados cuando el número o tipo de parámetros es incorrecto o si falla la recuperación de la configuración.

## Ejemplos

Ejemplo de ZookeeperConfig::get

Obtener la configuración.

```
<?php
$zk = new Zookeeper();
$zk->connect('localhost:2181');
$zk->addAuth('digest', 'timandes:timandes');
$zkConfig = $zk->getConfig();
$r = $zkConfig->get();
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

ZookeeperConfig::set

ZookeeperConfig::add

ZookeeperConfig::remove

ZookeeperException
