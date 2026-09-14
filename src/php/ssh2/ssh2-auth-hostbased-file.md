---
title: ssh2_auth_hostbased_file
description: Identificación utilizando una clave de host pública
source_url: https://www.php.net/manual/es/function.ssh2-auth-hostbased-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-auth-hostbased-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86420
---

ssh2_auth_hostbased_file

Identificación utilizando una clave de host pública

## Descripción

```php
ssh2_auth_hostbased_file(resource $session, string $username, string $hostname, string $pubkeyfile, string $privkeyfile, [string $passphrase], [string $local_username]): bool
```php

Identificación utilizando una clave de host pública leída desde un fichero.

## Parámetros

`session`  
Un identificador de conexión SSH, obtenido a través de la función `ssh2_connect`.

`username`  

`hostname`  

`pubkeyfile`  

`privkeyfile`  

`passphrase`  
Si `privkeyfile` está cifrado (y debe estarlo), la frase secreta debe ser proporcionada.

`local_username`  
Si `local_username` es omitido, entonces el valor de `username` será utilizado para ello.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Identificación utilizando una clave de host pública

```
<?php
$connection = ssh2_connect('shell.example.com', 22, array('hostkey'=>'ssh-rsa'));

if (ssh2_auth_hostbased_file($connection, 'remoteusername', 'myhost.example.com',
                             '/usr/local/etc/hostkey_rsa.pub',
                             '/usr/local/etc/hostkey_rsa', 'secret',
                             'localusername')) {
  echo "Identificación utilizando una clave de host pública con éxito\n";
} else {
  die('Fallo en la identificación utilizando una clave de host pública con éxito');
}
?>

   
```php

## Notas

> [!NOTE]
> `ssh2_auth_hostbased_file` requiere libssh2 \>= 0.7 y PHP/SSH2 \>= 0.7.
