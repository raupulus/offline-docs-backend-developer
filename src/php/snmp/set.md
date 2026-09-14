---
title: SNMP::set
description: Define el valor de un objeto SNMP
source_url: https://www.php.net/manual/es/snmp.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/snmp/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74990
---

SNMP::set

Define el valor de un objeto SNMP

## Descripción

```php
public SNMP::set(array $objectId, array $type, array $value): bool
```php

Solicita al agente remoto SNMP que defina el valor de uno o varios objetos SNMP especificados por su identificador `objectId`.

## Parámetros

`objectId`  
El identificador del objeto SNMP.

Cuando el número de OIDs en el array object_id es superior a la propiedad max_oids del objeto, el método deberá utilizar varias solicitudes para realizar las actualizaciones solicitadas. En este caso, la verificación del tipo y del valor se realiza por partes, por lo que la segunda solicitud (y otras sub-solicitudes) fallará debido a un tipo o valor incorrecto para el OID solicitado. Para detectar este comportamiento, se emite una alerta cuando el número de OIDs en el array object_id es superior a la propiedad max_oids.

`type`  
El MIB define el tipo de cada identificador de objeto. Debe ser especificado como un carácter simple de la lista siguiente.

|     |                                    |
|-----|------------------------------------|
| =   | El tipo es recuperado desde el MIB |
| i   | INTEGER                            |
| u   | INTEGER                            |
| s   | STRING                             |
| x   | HEX STRING                         |
| d   | DECIMAL STRING                     |
| n   | NULLOBJ                            |
| o   | OBJID                              |
| t   | TIMETICKS                          |
| a   | IPADDRESS                          |
| b   | BITS                               |

tipos

Si la constante `OPAQUE_SPECIAL_TYPES` ha sido definida durante la compilación de la biblioteca SNMP, los caracteres siguientes también estarán disponibles:

|     |                 |
|-----|-----------------|
| U   | int64 sin signo |
| I   | int64 con signo |
| F   | float           |
| D   | double          |

tipos

La mayoría de estos valores utilizan el tipo ASN.1 correspondiente. 's', 'x', 'd' y 'b' son todas formas diferentes de especificar el valor OCTET STRING y el tipo sin signo 'u' también es utilizado para manejar los valores Gauge32.

Si los ficheros MIB se cargan en el árbol MIB con "snmp_read_mib" o especificándolos en la configuración de libsnmp, se puede usar '=' como el parámetro `type` para todos los identificadores de objeto, ya que entonces el tipo se puede leer automáticamente desde el MIB.

Nota que hay 2 formas de definir una variable de tipo BITS como i.e. "SYNTAX BITS {telnet(0), ftp(1), http(2), icmp(3), snmp(4), ssh(5), https(6)}":

- Utilizando el tipo "b" y una lista de octetos. Este método no es recomendado ya que la petición GET para un mismo OID retornará i.e. 0xF8.

- Utilizando el tipo "x" y un número hexadecimal pero sin(!) el prefijo usual "0x".

Consúltese la sección sobre ejemplos para más detalles.

`value`  
El nuevo valor.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Este método no lanza excepciones por defecto. Para activar el lanzamiento de excepciones SNMPException cuando ocurren errores de la biblioteca, el parámetro de la clase SNMP `exceptions_enabled` ebe ser definido al valor correspondiente. Ver las [ explicaciones sobre `SNMP::$exceptions_enabled`](#snmp.props.exceptions-enabled) para más detalles.

## Ejemplos

Define un solo identificador de objeto SNMP

```
<?php
  $session = new SNMP(SNMP_VERSION_2C, "127.0.0.1", "private");
  $session->set('SNMPv2-MIB::sysContact.0', 's', "Nobody");
?>

   
```php

Define varios valores utilizando una sola llamada al método SNMP::set

```
<?php
  $session = new SNMP(SNMP_VERSION_2C, "127.0.0.1", "private");
  $session->set(array('SNMPv2-MIB::sysContact.0', 'SNMPv2-MIB::sysLocation.0'), array('s', 's'), array("Nobody", "Nowhere"));
// o
  $session->set(array('SNMPv2-MIB::sysContact.0', 'SNMPv2-MIB::sysLocation.0'), 's', array("Nobody", "Nowhere"));
?>

   
```php

Ejemplo con SNMP::set para configurar el identificador de objeto SNMP BITS

```
<?php
  $session = new SNMP(SNMP_VERSION_2C, "127.0.0.1", "private");
  $session->set('FOO-MIB::bar.42', 'b', '0 1 2 3 4');
// o
  $session->set('FOO-MIB::bar.42', 'x', 'F0');
?>
 
   
```php

## Véase también

SNMP::get
