---
title: ssh2_publickey_remove
description: Elimina una clave pública autorizada
source_url: https://www.php.net/manual/es/function.ssh2-publickey-remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-publickey-remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86590
---

ssh2_publickey_remove

Elimina una clave pública autorizada

## Descripción

```php
ssh2_publickey_remove(resource $pkey, string $algoname, string $blob): bool
```php

Elimina una clave pública autorizada.

## Parámetros

`pkey`  
Recurso Publickey Subsystem

`algoname`  
Algoritmo de clave pública (ejemplo): ssh-dss, ssh-rsa

`blob`  
Blob de clave pública como datos binarios sin tratar

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Notas

> [!NOTE]
> El publickey subsystem es utilizado para gestionar las claves públicas en un servidor en el cual el cliente ya está *identificado*. Para identificarse a un sistema remoto utilizando la identificación por clave pública, utilice la función `ssh2_auth_pubkey_file` en su lugar.

## Véase también

ssh2_publickey_init

ssh2_publickey_add

ssh2_publickey_list
