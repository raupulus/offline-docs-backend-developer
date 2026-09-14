---
title: ssh2_publickey_list
description: Lista las claves públicas actualmente autorizadas
source_url: https://www.php.net/manual/es/function.ssh2-publickey-list.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-publickey-list.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86580
---

ssh2_publickey_list

Lista las claves públicas actualmente autorizadas

## Descripción

```php
ssh2_publickey_list(resource $pkey): array
```php

Lista las claves públicas actualmente autorizadas.

## Parámetros

`pkey`  
Recurso Publickey Subsystem.

## Valores devueltos

Devuelve un array de claves indexadas numéricamente, cada una de ellas es un array asociativo que contiene: nombre, blob y elementos attrs.

| Clave Array | Significado |
|----|----|
| name | Nombre del algoritmo utilizado por esta clave pública, por ejemplo: `ssh-dss` o `ssh-rsa`. |
| blob | Blob de clave pública como datos binarios sin tratar. |
| attrs | Atributos asignados a esta clave pública. El atributo más común y el único soportado por la clave pública versión 1 de los servidores es `comment`, que puede ser cualquier forma de string. |

Elemento de clave pública

## Ejemplos

Lista de claves autorizadas con `ssh2_publickey_list`

```
<?php
$ssh2 = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($ssh2, 'jdoe', 'secret');
$pkey = ssh2_publickey_init($ssh2);

$list = ssh2_publickey_list($pkey);

foreach($list as $key) {
  echo "Clave : {$key['name']}\n";
  echo "Blob : " . chunk_split(base64_encode($key['blob']), 40, "\n") . "\n";
  echo "Comentario : {$key['attrs']['comment']}\n\n";
}
?>

   
```php

El ejemplo anterior mostrará:

    Clave : ssh-rsa
    Blob : AAAAB3NzaC1yc2EAAAABIwAAAIEA5HVt6VqSGd5P
    TrLRdjNONxXH1tVFGn0Bd26BF0aCP9qyJRlvdJ3j
    4WBeX4ZmrveGrjMgkseSYc4xZ26sDHwfL351xjza
    Lpipu\BGRrw17mWVBhuCExo476ri5tQFzbTc54VE
    HYckxQ16CjSTibI5X69GmnYC9PNqEYq/1TP+HF10
    Comentario : Clave de John

    Clave : ssh-rsa
    Blob : AAAAB3NzaHVt6VqSGd5C1yc2EAAAABIwA232dnJA
    AIEA5HVt6VqSGd5PTrLRdjNONxX/1TP+HF1HVt6V
    qSGd50H1tVFGn0BB3NzaC1yc2EAd26BF0aCP9qyJ
    RlvdJ3j4WBeX4ZmrveGrjMgkseSYc4xZ26HVt6Vq
    SGd5sDHwfL351xjzaLpipu\BGB3NzaC1yc2EA/1T
    Comentario : Clave de Alice

## Notas

> [!NOTE]
> El publickey subsystem es utilizado para gestionar las claves públicas en un servidor en el cual el cliente ya está *identificado*. Para identificarse a un sistema remoto utilizando la identificación por clave pública, utilice la función `ssh2_auth_pubkey_file` en su lugar.

## Véase también

ssh2_publickey_init

ssh2_publickey_add

ssh2_publickey_remove
