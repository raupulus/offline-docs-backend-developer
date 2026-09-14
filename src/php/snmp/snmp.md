---
title: La clase SNMP
source_url: https://www.php.net/manual/es/class.snmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/snmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 75020
---

## Introducción

Representa una sesión SNMP.

## Sinopsis de la clase

SNMP

Constantes

public

const

int

SNMP::VERSION_1

public

const

int

SNMP::VERSION_2c

public

const

int

SNMP::VERSION_2C

public

const

int

SNMP::VERSION_3

public

const

int

SNMP::ERRNO_NOERROR

public

const

int

SNMP::ERRNO_ANY

public

const

int

SNMP::ERRNO_GENERIC

public

const

int

SNMP::ERRNO_TIMEOUT

public

const

int

SNMP::ERRNO_ERROR_IN_REPLY

public

const

int

SNMP::ERRNO_OID_NOT_INCREASING

public

const

int

SNMP::ERRNO_OID_PARSING_ERROR

public

const

int

SNMP::ERRNO_MULTIPLE_SET_QUERIES

Propiedades

public

readonly

array

info

public

int

null

max_oids

public

int

valueretrieval

public

bool

quick_print

public

bool

enum_print

public

int

oid_output_format

public

bool

oid_increasing_check

public

int

exceptions_enabled

Métodos

## Propiedades

`max_oids`  
Número máximo de OID por solicitud GET/SET/GETBULK

`valueretrieval`  
Controla la forma en que se devolverán los valores SNMP

|  |  |
|----|----|
| `SNMP_VALUE_LIBRARY` | Los valores se devolverán de la misma forma que la biblioteca Net-SNMP. |
| `SNMP_VALUE_PLAIN` | Los valores se devolverán en valor pleno, sin la información de tipo SNMP. |
| `SNMP_VALUE_OBJECT` | Los valores se devolverán en forma de objetos con las propiedades "value" y "type", donde el tipo podrá ser una constante SNMP_OCTET_STR, SNMP_COUNTER etc... La forma en que se devuelve la "value" se basa en la constante definida: `SNMP_VALUE_LIBRARY` o `SNMP_VALUE_PLAIN`. |

`quick_print`  
Valor del parámetro `quick_print` en la biblioteca NET-SNMP

Define el valor del parámetro `quick_print` en la biblioteca NET-SNMP. Cuando está definido (1), la biblioteca SNMP devolverá valores rápidamente imprimibles. Esto significa únicamente que los valores serán impresos. Cuando el parámetro `quick_print` no está definido (por defecto), la biblioteca NET-SNMP imprimirá información adicional incluyendo el tipo de la valor (i.e. IpAddress o OID). Además, si quick_print no está activado, la biblioteca imprimirá los valores hexadecimales para todas las cadenas que contengan hasta 3 caracteres.

`enum_print`  
Controla la forma en que se imprimen los valores enum.

Permite indicar a walk/get etc. si deben buscar automáticamente los valores enum en el MIIB y devolverlos además de sus cadenas legibles por humanos.

`oid_output_format`  
Controla el formato de salida OID

|  |  |
|----|----|
| `SNMP_OID_OUTPUT_FULL` | La forma completa, como "iso.org.dod...." |
| `SNMP_OID_OUTPUT_NUMERIC` | La forma numérica, como ".1.3.6.1.4.1.8072.3.2.10" |
| `SNMP_OID_OUTPUT_MODULE` | La forma corta, como "NET-SNMP-TC::linux" |
| `SNMP_OID_OUTPUT_SUFFIX` | TBD |
| `SNMP_OID_OUTPUT_UCD` | TBD |
| `SNMP_OID_OUTPUT_NONE` | TBD |

Representación OID .1.3.6.1.2.1.1.3.0 para diversos valores de `oid_output_format`

`oid_increasing_check`  
Controla la verificación de la desactivación para el aumento de la OID durante el recorrido del árbol OID

Algunos agentes SNMP son conocidos por devolver OIDs en el orden incorrecto, pero pueden continuar el recorrido. Otros agentes devuelven OIDs en el orden incorrecto y pueden conducir al método SNMP::walk en un bucle infinito hasta que se alcance el límite de memoria. La biblioteca PHP SNMP, por defecto, realiza la verificación del aumento de la OID y detiene el recorrido del árbol OID cuando detecta una posible bucle emitiendo una alerta. Defina la variable `oid_increasing_check` a `false` para desactivar esta verificación.

`exceptions_enabled`  
Controla qué excepción SNMPException será emitida en lugar de las alertas. Utilizar el operador OR de las constantes `SNMP::ERRNO_*`. Por defecto, todas las excepciones SNMP están desactivadas.

`info`  
Propiedad de solo lectura que contiene la configuración del agente remoto: nombre de host, puerto, tiempo de espera por defecto, número de recuperación por defecto

## Constantes predefinidas

## Tipos de errores SNMP

`SNMP::ERRNO_NOERROR`  
No ha ocurrido ningún error específico SNMP.

`SNMP::ERRNO_GENERIC`  
Ha ocurrido un error SNMP genérico.

`SNMP::ERRNO_TIMEOUT`  
Solicitud al agente SNMP alcanza el tiempo de espera.

`SNMP::ERRNO_ERROR_IN_REPLY`  
El agente SNMP devuelve un error en la respuesta.

`SNMP::ERRNO_OID_NOT_INCREASING`  
El agente SNMP no incrementa más el OID durante la ejecución del comando WALK (BULK). Esto indica que hay un problema con el agente SNMP.

`SNMP::ERRNO_OID_PARSING_ERROR`  
La biblioteca falla al analizar el OID (y/o el tipo para el comando SET). No se realiza ninguna solicitud.

`SNMP::ERRNO_MULTIPLE_SET_QUERIES`  
La biblioteca utilizará varias solicitudes para la operación SET solicitada. Esto significa que la operación se realizará de forma no transaccional y que los fragmentos siguientes podrán fallar si se proporciona un tipo o valor incorrecto.

`SNMP::ERRNO_ANY`  
Todos los códigos operador OR de las constantes SNMP::ERRNO\_\*.

## Versiones del protocolo SNMP

`SNMP::VERSION_1`  

`SNMP::VERSION_2C`, `SNMP::VERSION_2c`  

`SNMP::VERSION_3`
