---
title: ssh2_auth_pubkey_file
description: Identificación utilizando una clave pública
source_url: https://www.php.net/manual/es/function.ssh2-auth-pubkey-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-auth-pubkey-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 74ef2355c
order: 86450
---

ssh2_auth_pubkey_file

Identificación utilizando una clave pública

## Descripción

```php
ssh2_auth_pubkey_file(resource $session, string $username, string $pubkeyfile, string $privkeyfile, [string $passphrase]): bool
```php

Identificación utilizando una clave pública, leída desde un fichero.

## Parámetros

`session`  
Un identificador de conexión SSH, obtenido desde la función `ssh2_connect`.

`username`  
Nombre del usuario para autenticarse en el servidor remoto.

`pubkeyfile`  
El fichero que contiene la clave pública debe estar en formato OpenSSH. Debe parecerse a esto:

ssh-rsa AAAAB3NzaC1yc2EAAA....NX6sqSnHA8= rsa-key-20121110

`privkeyfile`  

`passphrase`  
Si `privkeyfile` está cifrado (y debe estarlo), la frase de paso debe ser proporcionada.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Identificación utilizando una clave pública

```
<?php
$connection = ssh2_connect('shell.example.com', 22, array('hostkey'=>'ssh-rsa'));

if (ssh2_auth_pubkey_file($connection, 'username',
                          '/home/username/.ssh/id_rsa.pub',
                          '/home/username/.ssh/id_rsa', 'secret')) {
  echo "Identificación exitosa utilizando una clave pública\n";
} else {
  die('Fallo en la identificación utilizando una clave pública');
}
?>

   
```php

## Notas

> [!NOTE]
> La biblioteca libssh subyacente no soporta muy limpiamente las autenticaciones parciales. Es decir, que si debe proporcionar a la vez una clave pública y una contraseña, entonces parecerá como si la función estuviera en error. En este caso particular, un error en esta llamada puede simplemente significar que la autenticación no está aún terminada. Debe ignorar este error y continuar con la llamada `ssh2_auth_password` para terminar la autenticación.

## Véase también

ssh2_auth_pubkey
