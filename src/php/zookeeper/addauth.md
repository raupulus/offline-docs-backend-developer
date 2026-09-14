---
title: Zookeeper::addAuth
description: Especifica la información de autenticación de la aplicación
source_url: https://www.php.net/manual/es/zookeeper.addauth.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/addauth.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109550
---

Zookeeper::addAuth

Especifica la información de autenticación de la aplicación

## Descripción

```php
public Zookeeper::addAuth(string $scheme, string $cert, [callable $completion_cb]): bool
```php

La aplicación llama a esta función para especificar su información de autenticación. El servidor usará el proveedor de seguridad especificado por el parámetro scheme para autenticar la conexión del cliente. Si la solicitud de autenticación falla: - la conexión del servidor se abandona. - el observador es llamado con el valor ZOO_AUTH_FAILED_STATE como parámetro de estado.

## Parámetros

`scheme`  
El id del esquema de autenticación. Soportado nativamente: "digest" autenticación basada en contraseña.

`cert`  
La información de autenticación de la aplicación. El valor real depende del esquema.

`completion_cb`  
La rutina a invocar cuando la solicitud ha terminado. Uno de los siguientes códigos de resultado puede ser pasado a la función de devolución de llamada de finalización: - ZOK la operación se completó con éxito - ZAUTHFAILED la autenticación falló

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Este método emite un error/advertencia PHP cuando el número de parámetros o los tipos son incorrectos o cuando la operación falla.

> [!CAUTION]
> Desde la versión 0.3.0, este método emite `ZookeeperException` y sus derivados.

## Ejemplos

Ejemplo de Zookeeper::addAuth

Añade la autenticación antes de solicitar el valor del nodo.

```
<?php
$zookeeper = new Zookeeper('localhost:2181');
$path = '/path/to/node';
$value = 'nodevalue';
$zookeeper->set($path, $value);

$zookeeper->addAuth('digest', 'user0:passwd0');
$r = $zookeeper->get($path);
if ($r)
  echo $r;
else
  echo 'ERR';
?>

   
```php

El ejemplo anterior mostrará:

    nodevalue

## Véase también

Zookeeper::create

Zookeeper::setAcl

Zookeeper::getAcl

Estado de ZooKeeper

ZookeeperException
