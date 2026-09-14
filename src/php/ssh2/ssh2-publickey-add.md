---
title: ssh2_publickey_add
description: Añade una clave pública autorizada
source_url: https://www.php.net/manual/es/function.ssh2-publickey-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-publickey-add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86560
---

ssh2_publickey_add

Añade una clave pública autorizada

## Descripción

```php
ssh2_publickey_add(resource $pkey, string $algoname, string $blob, [bool $overwrite], [array $attributes]): bool
```php

> [!NOTE]
> El publickey subsystem es utilizado para gestionar las claves públicas en un servidor en el cual el cliente ya está *identificado*. Para identificarse a un sistema remoto utilizando la identificación por clave pública, utilice la función `ssh2_auth_pubkey_file` en su lugar.

## Parámetros

`pkey`  
Recurso Publickey Subsystem creado por `ssh2_publickey_init`.

`algoname`  
Algoritmo de clave pública (ejemplo): ssh-dss, ssh-rsa

`blob`  
Blob de clave pública como datos binarios sin tratar

`overwrite`  
Si la clave especificada ya existe, ¿debería ser sobrescrita?

`attributes`  
Array asociativo de atributos para asignar a esta clave pública. Consulte ietf-secsh-publickey-subsystem para una lista de los atributos soportados. Para marcar un atributo como obligatorio, anteponga un asterisco a su nombre. Si el servidor no es capaz de soportar un atributo marcado como obligatorio, abandonará el proceso de adición.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Adición de una clave pública con `ssh2_publickey_add`

```
<?php
$ssh2 = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($ssh2, 'jdoe', 'password');
$pkey = ssh2_publickey_init($ssh2);

$keyblob = base64_decode('
AAAAB3NzaC1yc2EAAAABIwAAAIEA5HVt6VqSGd5PTrLRdjNONxXH1tVFGn0
Bd26BF0aCP9qyJRlvdJ3j4WBeX4ZmrveGrjMgkseSYc4xZ26sDHwfL351xj
zaLpipu\BGRrw17mWVBhuCExo476ri5tQFzbTc54VEHYckxQ16CjSTibI5X
69GmnYC9PNqEYq/1TP+HF10=');

ssh2_publickey_add($pkey, 'ssh-rsa', $keyblob, false, array('comment'=>"John's Key"));
?>

   
```php

## Véase también

ssh2_publickey_init

ssh2_publickey_remove

ssh2_publickey_list
