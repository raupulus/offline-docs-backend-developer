---
title: ldap_exop_sync
description: Efectúa una operación extendida
source_url: https://www.php.net/manual/es/function.ldap-exop-sync.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-exop-sync.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: 9faf0215d
order: 43180
---

ldap_exop_sync

Efectúa una operación extendida

## Descripción

```php
ldap_exop_sync(LDAP\Connection $ldap, string $request_oid, [string $request_data], [array $controls], [string $response_data], [string $response_oid]): LDAP\Result
```php

Efectúa una operación extendida en el `ldap` especificado con `request_oid` el OID de la operación y `request_data` los datos.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`request_oid`  
El OID de la petición de operación extendida. Puede ser una de las constantes `LDAP_EXOP_*`, o una cadena con el OID de la operación.

`request_data`  
Los datos de la petición de operación extendida. Puede ser `null` para algunas operaciones como `LDAP_EXOP_WHO_AM_I`, y también puede necesitar estar codificado en BER.

`controls`  
Un array de [controles LDAP](#ldap.controls) a enviar con la solicitud.

`response_data`  
Será rellenado con los datos de respuesta de la operación extendida si se proporcionan. Si no se proporcionan, puede utilizarse `ldap_parse_exop` en el objeto resultado posteriormente para obtener estos datos.

`response_oid`  
Será rellenado con el OID de respuesta si se proporciona, generalmente igual al OID de la solicitud.

## Valores devueltos

Al utilizarse con `response_data`, devuelve `true` en caso de éxito o `false` en caso de error. Al utilizarse sin `response_data`, devuelve un identificador de resultado o `false` en caso de error.

## Véase también

ldap_exop

ldap_exop_whoami

ldap_exop_refresh

ldap_exop_passwd

ldap_parse_result

ldap_parse_exop
