---
title: ldap_exop_passwd
description: Asistencia para la operación extendida PASSWD
source_url: https://www.php.net/manual/es/function.ldap-exop-passwd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-exop-passwd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: 525aa5f19
order: 43160
---

ldap_exop_passwd

Asistencia para la operación extendida PASSWD

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] ldap_exop_passwd(LDAP\Connection $ldap, [string $user], [string $old_password], [string $new_password], [array $controls]): string
```php

Realiza una operación extendida PASSWD.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`user`  
El dn del usuario para cambiar la contraseña.

`old_password`  
La contraseña antigua de este usuario. Puede omitirse según la configuración del servidor.

`new_password`  
La nueva contraseña para este usuario. Puede omitirse o estar vacía para obtener una contraseña generada.

`controls`  
Si se proporciona, un control de solicitud de política de contraseña se envía con la petición y esto se rellena con un array de [Controles LDAP](#ldap.controls) devueltos con la petición.

## Valores devueltos

Devuelve la contraseña generada si `new_password` está vacía u omitida. De lo contrario, devuelve `true` en caso de éxito y `false` en caso de fallo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.0.0 | `controls` ahora acepta `null`; anteriormente, su valor predeterminado era `[]`. |
| 7.3.0 | Se ha añadido el soporte para `controls` |

## Ejemplos

Operación extendida de PASSWD

```
<?php
$ds = ldap_connect("localhost");  // asumiendo que el servidor LDAP está en este host
if ($ds) {
    // asignar el dn correcto para dar acceso de actualización
    $bind = ldap_bind($ds, "cn=root, o=My Company, c=US", "secret");
    if (!$bind) {
      echo "No se puede enlazar al servidor LDAP";
      exit;
    }
    // usar PASSWD EXOP para cambiar la contraseña del usuario por una generada
    $genpw = ldap_exop_passwd($ds, "cn=root, o=My Company, c=US", "secret");
    if ($genpw) {
      // usar la contraseña generada para enlazar
      $bind = ldap_bind($ds, "cn=root, o=My Company, c=US", $genpw);
    }
    // restablece la contraseña a "secret"
    ldap_exop_passwd($ds, "cn=root, o=My Company, c=US", $genpw, "secret");
    ldap_close($ds);
} else {
    echo "No se puede conectar al servidor LDAP";
}
?>

    
```php

## Véase también

`ldap_exop`, `ldap_parse_exop`
