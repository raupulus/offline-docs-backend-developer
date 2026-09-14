---
title: tcpwrap_check
description: Verificación Tcpwrap
source_url: https://www.php.net/manual/es/function.tcpwrap-check.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tcpwrap/functions/tcpwrap-check.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tcpwrap
translation_status: ready
translation_reviewed: true
translation_revision: b8758b060
order: 93850
---

tcpwrap_check

Verificación Tcpwrap

## Descripción

```php
tcpwrap_check(string $daemon, string $address, [string $user], [bool $nodns]): bool
```php

`tcpwrap_check` consulta los ficheros `/etc/hosts.allow` y `/etc/hosts.deny` para verificar si el acceso al servicio `daemon` está permitido o no para un cliente.

## Parámetros

`daemon`  
El nombre del servicio.

`address`  
La dirección remota del cliente. Puede ser una dirección IP o un nombre de dominio.

`user`  
Un nombre de usuario, opcional.

`nodns`  
Si `address` se asemeja a un nombre de dominio, DNS es utilizado para resolverlo en una dirección IP; defina `nodns` a `true` para evitar este comportamiento.

## Valores devueltos

Esta función devuelve `true` si el acceso debe ser autorizado, `false` en caso contrario.

## Ejemplos

Rechazar todas las conexiones desde localhost

Si su fichero `/etc/hosts.deny` contiene :

    php: 127.0.0.1

       

Y su código se asemeja a :

```
<?php
if (!tcpwrap_check('php', $_SERVER['REMOTE_ADDR'])) {
  die('No es bienvenido aquí');
}
?>
             
   
```php

## Véase también

Para más detalles, consulte la página man de hosts_access(3).
