---
title: ssh2_publickey_init
description: Inicializa un Publickey Subsystem (subsistema de clave pública)
source_url: https://www.php.net/manual/es/function.ssh2-publickey-init.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-publickey-init.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86570
---

ssh2_publickey_init

Inicializa un Publickey Subsystem (subsistema de clave pública)

## Descripción

```php
ssh2_publickey_init(resource $session): resource
```php

Solicita el subsistema de clave pública desde un servidor SSH2 ya conectado.

El subsistema de clave pública permite a un cliente ya conectado e identificado gestionar la lista de claves públicas autorizadas registradas en el servidor objetivo de manera agnóstica a la implementación. Si el servidor no soporta el subsistema de clave pública, la función `ssh2_publickey_init` devolverá `false`.

## Parámetros

`session`  

## Valores devueltos

Devuelve un recurso `SSH2 Publickey Subsystem` para usar con todos los otros métodos ssh2_publickey\_\*() o `false` si ocurre un error.

## Notas

> [!NOTE]
> El publickey subsystem es utilizado para gestionar las claves públicas en un servidor en el cual el cliente ya está *identificado*. Para identificarse a un sistema remoto utilizando la identificación por clave pública, utilice la función `ssh2_auth_pubkey_file` en su lugar.

## Véase también

ssh2_publickey_add

ssh2_publickey_remove

ssh2_publickey_list
