---
title: ssh2_auth_agent
description: Autenticación SSH utilizando el agente ssh
source_url: https://www.php.net/manual/es/function.ssh2-auth-agent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-auth-agent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86410
---

ssh2_auth_agent

Autenticación SSH utilizando el agente ssh

## Descripción

```php
ssh2_auth_agent(resource $session, string $username): bool
```php

Autenticación SSH utilizando el agente ssh.

> [!NOTE]
> La función `ssh2_auth_agent` solo está disponible cuando la extensión ssh2 ha sido compilada con libssh \>= 1.2.3.

## Parámetros

`session`  
Un identificador de conexión SSH, obtenido desde una llamada a la función `ssh2_connect`.

`username`  
Nombre de usuario remoto.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Autenticación utilizando un agente ssh

```
<?php
$connection = ssh2_connect('shell.example.com', 22);

if (ssh2_auth_agent($connection, 'username')) {
  echo "¡Autenticación exitosa!\n";
} else {
  die('Autenticación fallida...');
}
?>

   
```php
