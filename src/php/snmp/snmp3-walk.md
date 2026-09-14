---
title: snmp3_walk
description: Recupera todos los objetos SNMP desde un agente
source_url: https://www.php.net/manual/es/function.snmp3-walk.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmp3-walk.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74850
---

snmp3_walk

Recupera todos los objetos

SNMP

desde un agente

## Descripción

```php
snmp3_walk(string $hostname, string $security_name, string $security_level, string $auth_protocol, string $auth_passphrase, string $privacy_protocol, string $privacy_passphrase, array $object_id, [int $timeout], [int $retries]): array
```php

La función `snmp3_walk` se utiliza para leer todos los valores desde un agente SNMP especificado por el parámetro `host`.

Aunque el nivel de seguridad no utilice un protocolo de autenticación, se deben especificar valores válidos.

## Parámetros

`hostname`  
El nombre del host del agente SNMP (servidor).

`security_name`  
El nombre de la seguridad, habitualmente, el nombre del usuario.

`security_level`  
El nivel de seguridad (noAuthNoPriv\|authNoPriv\|authPriv).

`auth_protocol`  
El protocolo de autenticación (`"MD5"`, `"SHA"`, `"SHA256"` o `"SHA512"`).

`auth_passphrase`  
La frase secreta de autenticación.

`privacy_protocol`  
El protocolo privado (DES o AES).

`privacy_passphrase`  
La frase secreta privada.

`object_id`  
Si vale `null`, `object_id` será la raíz del árbol de objetos SNMP y todos los objetos subyacentes se devuelven en forma de array.

Si `object_id` está especificado, todos los objetos SNMP bajo el objeto `object_id` serán devueltos.

`timeout`  
El número de microsegundos antes del primer tiempo límite.

`retries`  
El número de intentos en caso de que ocurra el tiempo límite.

## Valores devueltos

Devuelve un array de valores de objetos SNMP comenzando desde el objeto `object_id` como raíz, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `auth_protocol` acepta ahora `"SHA256"` y `"SHA512"` cuando es soportado por libnetsnmp. |

## Ejemplos

Ejemplo con `snmp3_walk`

```
<?php
$ret = snmp3_walk('localhost', 'james', 'authPriv', 'SHA', 'secret007', 'AES', 'secret007', 'IF-MIB::ifName');
var_export($ret);
?>

   
```php

La llamada a la función anterior devolverá todos los objetos SNMP desde el agente SNMP ejecutándose en localhost: array ( 0 =\> 'STRING: lo', 1 =\> 'STRING: eth0', 2 =\> 'STRING: eth2', 3 =\> 'STRING: sit0', 4 =\> 'STRING: sixxs', )

## Véase también

snmp3_real_walk
