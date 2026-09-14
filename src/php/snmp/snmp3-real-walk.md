---
title: snmp3_real_walk
description: Devuelve todos los objetos incluyendo los identificadores de sus respectivos
  objetos
source_url: https://www.php.net/manual/es/function.snmp3-real-walk.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmp3-real-walk.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74830
---

snmp3_real_walk

Devuelve todos los objetos incluyendo los identificadores de sus respectivos objetos

## Descripción

```php
snmp3_real_walk(string $hostname, string $security_name, string $security_level, string $auth_protocol, string $auth_passphrase, string $privacy_protocol, string $privacy_passphrase, array $object_id, [int $timeout], [int $retries]): array
```php

La función `snmp3_real_walk` se utiliza para recorrer un número de objetos SNMP comenzando por el objeto cuyo identificador es `object_id` y devuelve no solo sus valores, sino también los identificadores de los objetos asociados.

## Parámetros

`hostname`  
El nombre del host del agente SNMP (servidor).

`security_name`  
El nombre de seguridad, generalmente el nombre de usuario.

`security_level`  
El nivel de seguridad (noAuthNoPriv\|authNoPriv\|authPriv).

`auth_protocol`  
El protocolo de autenticación (MD5 o SHA).

`auth_passphrase`  
La frase secreta de autenticación.

`privacy_protocol`  
El protocolo de privacidad (`"MD5"`, `"SHA"`, `"SHA256"` o `"SHA512"`).

`privacy_passphrase`  
La frase secreta privada.

`object_id`  
El identificador del objeto SNMP.

`timeout`  
El número de microsegundos antes del primer tiempo límite.

`retries`  
El número de intentos en caso de que ocurra un tiempo límite.

## Valores devueltos

Devuelve un array asociativo de identificadores de objetos SNMP junto con sus valores en caso de éxito, o `false` si ocurre un error. En caso de error, se emite una alerta de nivel E_WARNING.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `auth_protocol` acepta ahora `"SHA256"` y `"SHA512"` cuando es soportado por libnetsnmp. |

## Ejemplos

Ejemplo con `snmp3_real_walk`

```
<?php
 var_export(snmp3_real_walk('localhost', 'james', 'authPriv', 'SHA', 'secret007', 'AES', 'secret007', 'IF-MIB::ifName'));
?>

   
```php

El ejemplo anterior mostrará algo como: array ( 'IF-MIB::ifName.1' =\> 'STRING: lo', 'IF-MIB::ifName.2' =\> 'STRING: eth0', 'IF-MIB::ifName.3' =\> 'STRING: eth2', 'IF-MIB::ifName.4' =\> 'STRING: sit0', 'IF-MIB::ifName.5' =\> 'STRING: sixxs', )

## Véase también

snmpwalk
