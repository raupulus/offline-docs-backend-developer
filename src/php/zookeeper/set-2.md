---
title: ZookeeperConfig::set
description: Cambia la pertenencia al conjunto de clústeres ZK y los roles de los
  pares en el conjunto.
source_url: https://www.php.net/manual/es/zookeeperconfig.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeperconfig/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109810
---

ZookeeperConfig::set

Cambia la pertenencia al conjunto de clústeres ZK y los roles de los pares en el conjunto.

## Descripción

```php
public ZookeeperConfig::set(string $members, [int $version], [array $stat]): void
```php

## Parámetros

`members`  
La lista separada por comas de los nuevos miembros (por ejemplo, el contenido de un archivo de configuración de miembros) - para ser utilizado sólo con la reconfiguración no incremental.

`version`  
La versión esperada del nodo. La función fallará si la versión actual del nodo no coincide con la versión esperada. Si se utiliza -1, no se realizará la comprobación de la versión.

`stat`  
Si no es NULL, contendrá el valor de stat para la ruta de retorno.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Este método lanza `ZookeeperException` y sus derivados cuando el número o tipo de parámetros es incorrecto o si guardar el valor en el nodo falla.

## Ejemplos

Ejemplo de ZookeeperConfig::set

Reconfiguración.

```
<?php
$client = new Zookeeper();
$client->connect('localhost:2181');
$client->addAuth('digest', 'timandes:timandes');
$zkConfig = $client->getConfig();
$zkConfig->set("server.1=localhost:2888:3888:participant;0.0.0.0:2181");
?>

   
```php

## Véase también

ZookeeperConfig::get

ZookeeperConfig::add

ZookeeperConfig::remove

ZookeeperException
