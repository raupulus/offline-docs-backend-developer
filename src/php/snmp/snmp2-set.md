---
title: snmp2_set
description: Define el valor de un objeto SNMP
source_url: https://www.php.net/manual/es/function.snmp2-set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmp2-set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: dd22c7821
order: 74790
---

snmp2_set

Define el valor de un objeto

SNMP

## Descripción

```php
snmp2_set(string $hostname, string $community, array $object_id, array $type, array $value, [int $timeout], [int $retries]): bool
```php

La función `snmp2_set` se utiliza para definir el valor de un objeto SNMP especificado por su identificador `object_id`.

## Parámetros

`hostname`  
El nombre del host del agente SNMP (servidor).

`community`  
La comunidad de escritura.

`object_id`  
El identificador del objeto SNMP.

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

`timeout`  
El número de microsegundos antes del primer tiempo límite.

`retries`  
El número de intentos en caso de que ocurra el tiempo límite.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

Si el host SNMP rechaza el tipo de datos, se emitirá una alerta de tipo E_WARNING, como "Warning: Error in packet. Reason: (badValue) The value given has the wrong type or length.". Si se especifica un OID desconocido o inválido, la alerta emitida contendrá probablemente esto: "Could not add variable".

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Ahora lanza un ValueError cuando la longitud del nombre de host es igual o mayor a 128 bytes, cuando el puerto es negativo o mayor que 65535, o cuando los valores de timeout o reintentos son menores a -1 o demasiado grandes. |

## Ejemplos

Ejemplo con `snmp2_set`

```
<?php
  snmp2_set("localhost", "public", "IF-MIB::ifAlias.3", "s", "foo");
?>
 
   
```php

Ejemplo con `snmp2_set` para configurar el identificador del objeto SNMP BITS

```
<?php
  snmp2_set("localhost", "public", 'FOO-MIB::bar.42', 'b', '0 1 2 3 4');
// or
  snmp2_set("localhost", "public", 'FOO-MIB::bar.42', 'x', 'F0');
?>
 
    
```php

## Véase también

snmp2_get
