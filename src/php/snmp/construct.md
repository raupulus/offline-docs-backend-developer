---
title: SNMP::__construct
description: Crea una instancia SNMP que representa la sesión con el agente remoto
  SNMP
source_url: https://www.php.net/manual/es/snmp.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/snmp/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74940
---

SNMP::\_\_construct

Crea una instancia SNMP que representa la sesión con el agente remoto

SNMP

## Descripción

```php
public SNMP::__construct(int $version, string $hostname, string $community, [int $timeout], [int $retries])
```php

Crea una instancia SNMP que representa una sesión con un agente SNMP remoto.

## Parámetros

`version`  
Versión del protocolo SNMP: `SNMP::VERSION_1`, `SNMP::VERSION_2C`, `SNMP::VERSION_3`.

`hostname`  
El agente SNMP. El parámetro `hostname` puede ser prefijado con el puerto del agente opcional SNMP después de una coma. Las direcciones IPV6 deben estar rodeadas de corchetes (\[\]) si se utilizan puertos adicionales. Si FQDN se utiliza para el parámetro `hostname`, será resuelto por la extensión PHP SNMP, y no por el motor Net-SNMP. El uso de direcciones IPV6 al utilizar FQDN puede ser forzado rodeando FQDN con corchetes. A continuación se muestran algunos ejemplos:

|  |  |
|----|----|
| IPv4 con puerto por defecto | 127.0.0.1 |
| IPv6 con puerto por defecto | ::1 o \[::1\] |
| IPv4 con puerto específico | 127.0.0.1:1161 |
| IPv6 con puerto específico | \[::1\]:1161 |
| FQDN con puerto por defecto | host.domain |
| FQDN con puerto específico | host.domain:1161 |
| FQDN con puerto por defecto, forzando el uso de direcciones IPV6 | \[host.domain\] |
| FQDN con puerto específico, forzando el uso de direcciones IPV6 | \[host.domain\]:1161 |

`community`  
Especifica el nivel de seguridad para la `version` dada. El objetivo de la cadena de acceso `community` es específico a la versión de SNMP:

|  |  |
|----|----|
| `SNMP::VERSION_1` | `public` para permiso de solo lectura o `private` para lectura-escritura |
| `SNMP::VERSION_2C` | `public` para permiso de solo lectura o `private` para lectura-escritura |
| `SNMP::VERSION_3` | Nombre de seguridad SNMPv3, puede ser uno de los siguientes: `noAuthNoPriv`, `authNoPriv` (se requiere una contraseña de autenticación y un protocolo de autenticación), o `authPriv` (se requiere una contraseña y un protocolo de autenticación, así como una contraseña y un protocolo de confidencialidad) |

SNMPv3 requiere la configuración de los parámetros de sesión relacionados con la seguridad con el método SNMP::setSecurity.

`timeout`  
El número de microsegundos antes del primer tiempo límite.

`retries`  
El número de intentos cuando ocurre un tiempo límite.

## Errores/Excepciones

SNMP::\_\_construct lanza una excepción cuando los parámetros son incorrectos o la versión del protocolo SNMP es desconocida.

## Ejemplos

Recuperación de la ubicación física del host

```
<?php

$session = new SNMP(SNMP_VERSION_1, "127.0.0.1", "public");
$sysdescr = $session->get("sysDescr.0");
echo "$sysdescr\n";

?>

   
```php

Resultado del ejemplo anterior es similar a:

    STRING: Test server

## Véase también

SNMP::close
