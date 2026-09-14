---
title: ldap_exop
description: Realiza una operación extendida
source_url: https://www.php.net/manual/es/function.ldap-exop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-exop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_revision: '640002785'
order: 43200
---

ldap_exop

Realiza una operación extendida

## Descripción

```php
ldap_exop(LDAP\Connection $ldap, string $request_oid, [string $request_data], [array $controls], [string $response_data], [string $response_oid]): LDAP\Result
```php

Realiza una operación extendida en el `ldap` especificado con `request_oid` el OID de la operación y `request_data` los datos.

> [!WARNING]
> El uso de más de 4 parámetros ha quedado obsoleto, use `ldap_exop_sync` en su lugar.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`request_oid`  
El OID de la petición de operación extendida. Puede ser una de las constantes `LDAP_EXOP_*`, o una cadena con el OID de la operación.

`request_data`  
La operación extendida requiere datos. Puede ser NULL para ciertas operaciones como `LDAP_EXOP_WHO_AM_I`, puede requerir asimismo un codificación BER.

`controls`  
Un array de [controles LDAP](#ldap.controls) a enviar con la solicitud.

`response_data`  
Será rellenado con los datos de respuesta de la operación extendida si se proporcionan. Si no se proporcionan, puede utilizarse `ldap_parse_exop` en el objeto resultado posteriormente para obtener estos datos.

`response_oid`  
Será rellenado con el OID de respuesta si se proporciona, generalmente igual al OID de la solicitud.

## Valores devueltos

Al utilizarse con `response_data`, devuelve `true` en caso de éxito o `false` en caso de error. Al utilizarse sin `response_data`, devuelve un identificador de resultado o `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | El uso de más de 4 parámetros ha quedado obsoleto, use `ldap_exop_sync` en su lugar. |
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 7.3.0 | Se ha añadido el soporte para `controls` |

## Ejemplos

Operación extendida WHOAMI

```
<?php
$ds = ldap_connect("localhost");  // asumiendo que el servidor LDAP está en este host
if ($ds) {
    // enlace con el dn apropiado para dar acceso de actualización
    $bind = ldap_bind($ds, "cn=root, o=My Company, c=US", "secret");
    if (!$bind) {
      echo "No se puede enlazar con el servidor LDAP";
      exit;
    }
    // Llamada a la operación extendida WHOAMI
    $r = ldap_exop($ds, LDAP_EXOP_WHO_AM_I);
    // analiza el objeto resultado
    ldap_parse_exop($ds, $r, $retdata);
    // Salida: string(31) "dn:cn=root, o=My Company, c=US"
    var_dump($retdata);
    // Lo mismo utilizando el parámetro $response_data
    $success = ldap_exop($ds, LDAP_EXOP_WHO_AM_I, NULL, NULL, $retdata, $retoid);
    if ($success) {
      var_dump($retdata);
    }
    ldap_close($ds);
} else {
    echo "No se puede conectar con el servidor LDAP";
}
?>

    
```php

## Véase también

ldap_exop_sync

ldap_exop_whoami

ldap_exop_refresh

ldap_exop_passwd

ldap_parse_result

ldap_parse_exop
