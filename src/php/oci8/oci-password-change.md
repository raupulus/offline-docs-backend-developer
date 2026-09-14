---
title: oci_password_change
description: Modifica la contraseña de un usuario Oracle
source_url: https://www.php.net/manual/es/function.oci-password-change.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-password-change.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 78be3d554
order: 57530
---

oci_password_change

Modifica la contraseña de un usuario Oracle

## Descripción

```php
oci_password_change(resource $connection, string $username, string $old_password, string $new_password): bool
```php

```php
oci_password_change(string $database_name, string $username, string $old_password, string $new_password): resource
```

Modifica la contraseña del usuario `username`.

La función `oci_password_change` es más útil con scripts PHP en línea de comandos, o cuando se utilizan conexiones no persistentes en la aplicación PHP.

## Parámetros

`connection`  
Un identificador de conexión Oracle, devuelto por la función `oci_connect` o la función `oci_pconnect`.

`username`  
El nombre de usuario Oracle.

`old_password`  
La contraseña antigua.

`new_password`  
La nueva contraseña a establecer.

`database_name`  
El nombre de la base de datos.

## Valores devueltos

Cuando `database_name` es proporcionado, `oci_password_change` devuelve `true` en caso de éxito, o `false` si ocurre un error. Cuando `connection` es proporcionado, `oci_password_change` devuelve el recurso de conexión en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `oci_password_change` para cambiar la contraseña de un usuario ya conectado

```php
<?php

$dbase      = 'localhost/orcl';
$user       = 'cj';
$current_pw = 'welcome';
$new_pw     = 'geelong';

$c = oci_pconnect($user, $current_pw, $dbase);
oci_password_change($c, $user, $current_pw, $new_pw);
echo "La nueva contraseña es: " . $new_pw . "\n";

?>

    
```

Ejemplo con `oci_password_change` para conectarse y cambiar la contraseña en una sola etapa

```php
<?php

$dbase      = 'localhost/orcl';
$user       = 'cj';
$current_pw = 'welcome';
$new_pw     = 'geelong';

$c = oci_pconnect($user, $current_pw, $dbase);
if (!$c) {
    $m = oci_error();
    if ($m['code'] == 28001) { // "ORA-28001: La contraseña ha expirado"
        // Conexión y cambio de contraseña en una etapa
        $c = oci_password_change($dbase, $user, $current_pw, $new_pw);
        if ($c) {
            echo "La nueva contraseña es: " . $new_pw . "\n";
        }
    }
}

if (!$c) {  // El error original no era 28001, o el cambio de contraseña falló
    $m = oci_error();
    trigger_error('No se pudo conectar a la base de datos: '. $m['message'], E_USER_ERROR);
}

// Uso de la conexión $c
// ...

?>

    
```

## Notas

> [!NOTE]
> Cambiar la contraseña, con esta función, o directamente en Oracle debe hacerse con precaución. Esto se debe a que las aplicaciones PHP podrían seguir utilizando conexiones persistentes con la contraseña antigua. La mejor práctica es reiniciar todos los servidores web una vez que la contraseña ha sido cambiada.

> [!NOTE]
> Si se actualizan las bibliotecas cliente o la base de datos Oracle desde una versión anterior a 11.2.0.3 a una versión 11.2.0.3 o superior, la función `oci_password_change` puede devolver el error "ORA-1017: invalid username/password" hasta que las versiones del cliente y del servidor sean idénticas.

> [!NOTE]
> La segunda sintaxis de `oci_password_change` está disponible desde la versión de OCI8 1.1.
