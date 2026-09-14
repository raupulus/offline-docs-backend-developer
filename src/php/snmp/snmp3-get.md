---
title: snmp3_get
description: Recupera un objeto SNMP
source_url: https://www.php.net/manual/es/function.snmp3-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmp3-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: dd22c7821
order: 74810
---

snmp3_get

Recupera un objeto

SNMP

## Descripción

```php
snmp3_get(string $hostname, string $security_name, string $security_level, string $auth_protocol, string $auth_passphrase, string $privacy_protocol, string $privacy_passphrase, array $object_id, [int $timeout], [int $retries]): mixed
```php

La función `snmp3_get` se utiliza para leer el valor de un objeto SNMP especificado por el identificador `object_id`.

## Parámetros

`hostname`  
El nombre del host del agente SNMP (servidor).

`security_name`  
El nombre de la seguridad, habitualmente, el nombre de usuario.

`security_level`  
El nivel de seguridad (noAuthNoPriv\|authNoPriv\|authPriv).

`auth_protocol`  
El protocolo de autenticación (MD5 o SHA)

`auth_passphrase`  
La frase secreta de autenticación.

`privacy_protocol`  
El protocolo de autenticación (`"MD5"`, `"SHA"`, `"SHA256"` o `"SHA512"`).

`privacy_passphrase`  
La frase secreta privada.

`object_id`  
El identificador del objeto SNMP.

`timeout`  
El número de microsegundos antes del primer tiempo límite.

`retries`  
El número de intentos en caso de tiempo límite.

## Valores devueltos

Devuelve el valor del objeto SNMP en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Ahora lanza un ValueError cuando la longitud del nombre de host es igual o mayor a 128 bytes, cuando el puerto es negativo o mayor que 65535, o cuando los valores de timeout o reintentos son menores a -1 o demasiado grandes. |
| 8.1.0 | El parámetro `auth_protocol` acepta ahora `"SHA256"` y `"SHA512"` cuando es soportado por libnetsnmp. |

## Ejemplos

Ejemplo con `snmp3_get`

```
<?php
$nameOfSecondInterface = snmp3_get('localhost', 'james', 'authPriv', 'SHA', 'secret007', 'AES', 'secret007', 'IF-MIB::ifName.2');
?>

   
```php

## Véase también

snmp3_set
