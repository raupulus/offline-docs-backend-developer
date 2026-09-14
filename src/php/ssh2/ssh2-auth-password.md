---
title: ssh2_auth_password
description: Autenticación vía SSH utilizando una contraseña en texto claro
source_url: https://www.php.net/manual/es/function.ssh2-auth-password.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-auth-password.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86440
---

ssh2_auth_password

Autenticación vía SSH utilizando una contraseña en texto claro

## Descripción

```php
ssh2_auth_password(resource $session, string $username, string $password): bool
```php

Autenticación vía SSH utilizando una contraseña en texto claro. Desde la versión 0.12, esta función también soporta el método keyboard_interactive.

## Parámetros

`session`  
Un identificador de conexión SSH, obtenido desde la función `ssh2_connect`.

`username`  
Nombre de usuario remoto.

`password`  
Contraseña para el usuario `username`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Autenticación con una contraseña

```
<?php
$connection = ssh2_connect('shell.example.com', 22);

if (ssh2_auth_password($connection, 'username', 'secret')) {
  echo "Autenticación exitosa!\n";
} else {
  die('Fallo en la autenticación...');
}
?>

   
```php
