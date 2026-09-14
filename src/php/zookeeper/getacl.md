---
title: Zookeeper::getAcl
description: Devuelve las ACL asociadas a un nodo de forma sincrónica
source_url: https://www.php.net/manual/es/zookeeper.getacl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/getacl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109630
---

Zookeeper::getAcl

Devuelve las ACL asociadas a un nodo de forma sincrónica

## Descripción

```php
public Zookeeper::getAcl(string $path): array
```php

## Parámetros

`path`  
El nombre del nodo. Expresado como un nombre de archivo con barras separando los ancestros del nodo.

## Valores devueltos

Devuelve un array de ACLs en caso de éxito y false en caso de fallo.

## Errores/Excepciones

Este método emite un error/advertencia de PHP si el número de parámetros o los tipos son incorrectos o si no se han podido recuperar las ACL del nodo.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Ejemplos

Ejemplo de Zookeeper::getAcl

Devuelve las ACL de un nodo.

```
<?php
$zookeeper = new Zookeeper('localhost:2181');
$aclArray = array(
  array(
    'perms'  => Zookeeper::PERM_ALL,
    'scheme' => 'world',
    'id'     => 'anyone',
  )
);
$path = '/path/to/newnode';
$zookeeper->setAcl($path, $aclArray);

$r = $zookeeper->getAcl($path);
if ($r)
  var_dump($r);
else
  echo 'ERR';
?>

   
```php

El ejemplo anterior mostrará:

    array(1) {
      [0]=>
      array(3) {
        ["perms"]=>
        int(31)
        ["scheme"]=>
        string(5) "world"
        ["id"]=>
        string(6) "anyone"
      }
    }

## Véase también

Zookeeper::create

Zookeeper::setAcl

Permisos de ZooKeeper

ZookeeperException
