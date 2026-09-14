---
title: ldap_set_option
description: Modifica el valor de una opción LDAP
source_url: https://www.php.net/manual/es/function.ldap-set-option.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-set-option.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: 5b3a84935
order: 43520
---

ldap_set_option

Modifica el valor de una opción LDAP

## Descripción

```php
ldap_set_option(LDAP\Connection $ldap, int $option, array $value): bool
```php

Modifica el valor de la opción `option` reemplazando el valor actual por `value`.

## Parámetros

`ldap`  
Puede ser una instancia `LDAP\Connection`, devuelta por `ldap_connect`, para definir la opción para esta conexión, o `null` para definir la opción globalmente.

`option`  
El parámetro `option` puede tomar uno de los siguientes valores:

| Opción                          | Tipo     | Disponible a partir de |
|---------------------------------|----------|------------------------|
| `LDAP_OPT_DEREF`                | `int`    |                        |
| `LDAP_OPT_SIZELIMIT`            | `int`    |                        |
| `LDAP_OPT_TIMELIMIT`            | `int`    |                        |
| `LDAP_OPT_NETWORK_TIMEOUT`      | `int`    |                        |
| `LDAP_OPT_PROTOCOL_VERSION`     | `int`    |                        |
| `LDAP_OPT_ERROR_NUMBER`         | `int`    |                        |
| `LDAP_OPT_REFERRALS`            | `bool`   |                        |
| `LDAP_OPT_RESTART`              | `bool`   |                        |
| `LDAP_OPT_HOST_NAME`            | `string` |                        |
| `LDAP_OPT_ERROR_STRING`         | `string` |                        |
| `LDAP_OPT_DIAGNOSTIC_MESSAGE`   | `string` |                        |
| `LDAP_OPT_MATCHED_DN`           | `string` |                        |
| `LDAP_OPT_SERVER_CONTROLS`      | `array`  |                        |
| `LDAP_OPT_CLIENT_CONTROLS`      | `array`  |                        |
| `LDAP_OPT_X_KEEPALIVE_IDLE`     | `int`    | PHP 7.1.0              |
| `LDAP_OPT_X_KEEPALIVE_PROBES`   | `int`    | PHP 7.1.0              |
| `LDAP_OPT_X_KEEPALIVE_INTERVAL` | `int`    | PHP 7.1.0              |
| `LDAP_OPT_X_TLS_CACERTDIR`      | `string` | PHP 7.1.0              |
| `LDAP_OPT_X_TLS_CACERTFILE`     | `string` | PHP 7.1.0              |
| `LDAP_OPT_X_TLS_CERTFILE`       | `string` | PHP 7.1.0              |
| `LDAP_OPT_X_TLS_CIPHER_SUITE`   | `string` | PHP 7.1.0              |
| `LDAP_OPT_X_TLS_CRLCHECK`       | `int`    | PHP 7.1.0              |
| `LDAP_OPT_X_TLS_CRLFILE`        | `string` | PHP 7.1.0              |
| `LDAP_OPT_X_TLS_DHFILE`         | `string` | PHP 7.1.0              |
| `LDAP_OPT_X_TLS_KEYILE`         | `string` | PHP 7.1.0              |
| `LDAP_OPT_X_TLS_PROTOCOL_MIN`   | `int`    | PHP 7.1.0              |
| `LDAP_OPT_X_TLS_PROTOCOL_MAX`   | `int`    | PHP 8.4.0              |
| `LDAP_OPT_X_TLS_RANDOM_FILE`    | `string` | PHP 7.1.0              |
| `LDAP_OPT_X_TLS_REQUIRE_CERT`   | `int`    | PHP 7.0.5              |

Las opciones `LDAP_OPT_SERVER_CONTROLS` y `LDAP_OPT_CLIENT_CONTROLS` requieren una lista de controles, lo que significa que el valor debe ser un array de controles. Un control está compuesto por un *oid* como identificador, un valor opcional *value*, y un flag opcional de "criticalidad" (*criticality*). En PHP, un control se define como un array, por lo que las claves son *oid* con una cadena como valor, y dos claves opcionales. Estas claves son *value* con una cadena como valor, y *iscritical* con un valor booleano. Por omisión, *iscritical* vale *`false`*. Ver el archivo [draft-ietf-ldapext-ldap-c-api-xx.txt](https://www.ietf.org/proceedings/50/I-D/ldapext-ldap-c-api-05.txt) para más detalles. Consulte el segundo ejemplo para una ilustración.

> [!NOTE]
> Todas las opciones TLS deben ser definidas globalmente antes de `ldap_connect` para una conexión ldaps, o para la conexión antes de `ldap_start_tls`.

`value`  
El nuevo valor para la opción `option` especificada.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |

## Ejemplos

Modificación de la versión del protocolo

```
<?php
// $ds debe ser una instancia de conexión LDAP\Connection válida
if (ldap_set_option($ds, LDAP_OPT_PROTOCOL_VERSION, 3)) {
    echo "Versión LDAPv3";
} else {
    echo "No es posible modificar la versión del protocolo a 3";
}
?>

    
```php

Modificación de los controles del servidor

```
<?php
// $ds debe ser una instancia de conexión LDAP\Connection válida
$ctrl1 = array("oid" => "1.2.752.58.10.1", "iscritical" => true);
// iscritical vale por omisión FALSE
$ctrl2 = array("oid" => "1.2.752.58.1.10", "value" => "magic");
// intenta usar los dos controles
if (!ldap_set_option($ds, LDAP_OPT_SERVER_CONTROLS, array($ctrl1, $ctrl2))) {
    echo "No es posible modificar los controles del servidor";
}
?>

    
```php

## Notas

> [!NOTE]
> Esta función solo está disponible cuando se utiliza OpenLDAP 2.x.x o Netscape Directory SDK x.x.

## Véase también

`ldap_get_option`
