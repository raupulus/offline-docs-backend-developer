---
title: SNMP::setSecurity
description: Configura los parámetros de seguridad de las sesiones SNMPv3
source_url: https://www.php.net/manual/es/snmp.setsecurity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/snmp/setsecurity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 75000
---

SNMP::setSecurity

Configura los parámetros de seguridad de las sesiones

SNMP

v3

## Descripción

```php
public SNMP::setSecurity(string $securityLevel, [string $authProtocol], [string $authPassphrase], [string $privacyProtocol], [string $privacyPassphrase], [string $contextName], [string $contextEngineId]): bool
```php

Configura los parámetros de seguridad de las sesiones del protocolo SNMPv3.

## Parámetros

`securityLevel`  
el nivel de seguridad (noAuthNoPriv\|authNoPriv\|authPriv)

`authProtocol`  
el protocolo de autenticación (MD5 o SHA)

`authPassphrase`  
la frase de paso para la autenticación

`privacyProtocol`  
el protocolo privado (DES o AES)

`privacyPassphrase`  
la frase de paso para el protocolo privado

`contextName`  
el nombre del contexto

`contextEngineId`  
el contexto EngineID

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con SNMP::setSecurity

```
<?php
  $session = new SNMP(SNMP_VERSION_3, $hostname, $rwuser, $timeout, $retries);
  $session->setSecurity('authPriv', 'MD5', $auth_pass, 'AES', $priv_pass, '', 'aeeeff');
?>

   
```php

## Véase también

SNMP::\_\_construct
