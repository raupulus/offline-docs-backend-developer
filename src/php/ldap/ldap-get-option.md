---
title: ldap_get_option
description: Lee/escrit el valor actual de una opción
source_url: https://www.php.net/manual/es/function.ldap-get-option.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-get-option.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: 5b3a84935
order: 43290
---

ldap_get_option

Lee/escrit el valor actual de una opción

## Descripción

```php
ldap_get_option(LDAP\Connection $ldap, int $option, [array $value]): bool
```php

Establece el valor `value` a la opción especificada.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`, para obtener la opción de esa conexión, o `null` para obtener la opción global.

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
| `LDAP_OPT_DIAGNOSTIC_MESSAGE`   | `string` |                        |
| `LDAP_OPT_REFERRALS`            | `int`    |                        |
| `LDAP_OPT_RESTART`              | `int`    |                        |
| `LDAP_OPT_HOST_NAME`            | `string` |                        |
| `LDAP_OPT_ERROR_STRING`         | `string` |                        |
| `LDAP_OPT_MATCHED_DN`           | `string` |                        |
| `LDAP_OPT_SERVER_CONTROLS`      | `array`  |                        |
| `LDAP_OPT_CLIENT_CONTROLS`      | `array`  |                        |
| `LDAP_OPT_X_KEEPALIVE_IDLE`     | `int`    | 7.1                    |
| `LDAP_OPT_X_KEEPALIVE_PROBES`   | `int`    | 7.1                    |
| `LDAP_OPT_X_KEEPALIVE_INTERVAL` | `int`    | 7.1                    |
| `LDAP_OPT_X_TLS_CACERTDIR`      | string   | 7.1                    |
| `LDAP_OPT_X_TLS_CACERTFILE`     | `string` | 7.1                    |
| `LDAP_OPT_X_TLS_CERTFILE`       | `string` | 7.1                    |
| `LDAP_OPT_X_TLS_CIPHER_SUITE`   | `string` | 7.1                    |
| `LDAP_OPT_X_TLS_CRLCHECK`       | `int`    | 7.1                    |
| `LDAP_OPT_X_TLS_CRL_NONE`       | `int`    | 7.1                    |
| `LDAP_OPT_X_TLS_CRL_PEER`       | `int`    | 7.1                    |
| `LDAP_OPT_X_TLS_CRL_ALL`        | `int`    | 7.1                    |
| `LDAP_OPT_X_TLS_CRLFILE`        | `string` | 7.1                    |
| `LDAP_OPT_X_TLS_DHFILE`         | `string` | 7.1                    |
| `LDAP_OPT_X_TLS_KEYFILE`        | `string` | 7.1                    |
| `LDAP_OPT_X_TLS_PACKAGE`        | `string` | 7.1                    |
| `LDAP_OPT_X_TLS_PROTOCOL_MIN`   | `int`    | 7.1                    |
| `LDAP_OPT_X_TLS_PROTOCOL_MAX`   | `int`    | 8.4                    |
| `LDAP_OPT_X_TLS_RANDOM_FILE`    | `string` | 7.1                    |
| `LDAP_OPT_X_TLS_REQUIRE_CERT`   | `int`    |                        |

`value`  
Valor a establecer para la opción.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | `ldap` ahora acepta `null`. |
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |

## Ejemplos

Verificación de la versión del protocolo

```
<?php
// $ds debe ser una instancia válida de LDAP\Connection
if (ldap_get_option($ds, LDAP_OPT_PROTOCOL_VERSION, $version)) {
    echo "Estamos utilizando el protocolo versión $version\n";
} else {
    echo "No es posible determinar la versión del protocolo.\n";
}
?>

    
```php

## Notas

> [!NOTE]
> Esta función solo está disponible con OpenLDAP 2.x.x O Netscape Directory SDK x.x, y fue añadida en PHP 4.0.4.

## Véase también

`ldap_set_option`
