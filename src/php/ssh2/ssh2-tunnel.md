---
title: ssh2_tunnel
description: Abre un túnel a través de un servidor remoto
source_url: https://www.php.net/manual/es/function.ssh2-tunnel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-tunnel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86750
---

ssh2_tunnel

Abre un túnel a través de un servidor remoto

## Descripción

```php
ssh2_tunnel(resource $session, string $host, int $port): resource
```php

Abre un socket hacia un host/puerto arbitrario a través de un servidor SSH conectado.

## Parámetros

`session`  
Un identificador de conexión SSH, obtenido desde la función `ssh2_connect`.

`host`  

`port`  

## Valores devueltos

## Ejemplos

Apertura de un túnel en un host arbitrario

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_pubkey_file($connection, 'username', 'id_dsa.pub', 'id_dsa');

$tunnel = ssh2_tunnel($connection, '10.0.0.101', 12345);
?>

   
```php

## Véase también

ssh2_connect

fsockopen
