---
title: ssh2_auth_none
description: Identificación como "none"
source_url: https://www.php.net/manual/es/function.ssh2-auth-none.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-auth-none.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86430
---

ssh2_auth_none

Identificación como "none"

## Descripción

```php
ssh2_auth_none(resource $session, string $username): mixed
```php

Intenta una identificación como "none", que, habitualmente, falla (y debe fallar). Aparte del fallo, esta función debe devolver un array que contiene los métodos de identificación aceptables.

## Parámetros

`session`  
Un identificador de conexión SSH, obtenido con la función `ssh2_connect`.

`username`  
Nombre de usuario remoto.

## Valores devueltos

Devuelve `true` si el servidor acepta "none" como método de identificación, o un array de métodos de identificación aceptables en caso de fallo.

## Ejemplos

Recuperación de la lista de métodos de identificación

```
<?php
$connection = ssh2_connect('shell.example.com', 22);

$auth_methods = ssh2_auth_none($connection, 'user');

if (in_array('password', $auth_methods)) {
  echo "El servidor soporta la identificación por contraseña\n";
}
?>

   
```php
