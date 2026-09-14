---
title: session_create_id
description: Crear un nuevo ID de sesión
source_url: https://www.php.net/manual/es/function.session-create-id.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-create-id.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: false
translation_revision: f5c124bef
order: 73750
---

session_create_id

Crear un nuevo ID de sesión

## Descripción

```php
session_create_id([string $prefix]): string
```php

`session_create_id` se utiliza para crear un nuevo ID de sesión para la sesión actual. Esto devuelve un ID de sesión sin colisión.

Si la sesión no está activa, la verificación de colisión se omite.

El ID de sesión se crea de acuerdo con los parámetros php.ini.

Es importante utilizar el mismo ID de usuario de su servidor web para el script de la tarea de Recogida de Basura (Garbage Collection). De lo contrario, se pueden tener problemas de permisos, especialmente con los gestores de guardado de ficheros.

## Parámetros

`prefix`  
Si `prefix` está especificado, el nuevo ID de sesión se prefiere con `prefix`. No todos los caracteres están permitidos en el ID de sesión. Los caracteres entre `[a-z A-Z 0-9]` están permitidos. La longitud máxima es de 256 caracteres.

## Valores devueltos

`session_create_id` devuelve un nuevo ID de sesión sin colisión para la sesión actual. Si se utiliza sin una sesión activa, la verificación de colisión se omite. En caso de error, `false` se devuelve.

## Ejemplos

Ejemplo de `session_create_id` con `session_regenerate_id`

```
<?php
// Mi función de inicio de sesión soporta la gestión de marcas de tiempo
function my_session_start() {
    session_start();
    // No permite el uso de antiguos ID de sesión
    if (!empty($_SESSION['deleted_time']) && $_SESSION['deleted_time'] < time() - 180) {
        session_destroy();
        session_start();
    }
}

// Mi función de regeneración de ID
function my_session_regenerate_id() {
    // Llamada a session_create_id() cuando la sesión está activa
    // para asegurarse de que no hay colisión.
    if (session_status() != PHP_SESSION_ACTIVE) {
        session_start();
    }
    // ADVERTENCIA: Nunca utilizar cadenas confidenciales como prefijo
    $newid = session_create_id('myprefix-');
    // Establece la marca de tiempo de eliminación.
    // Los datos de sesión no deben eliminarse inmediatamente por ciertas razones.
    $_SESSION['deleted_time'] = time();
    // Termina la sesión
    session_commit();
    // Asegúrese de aceptar los ID de sesión definidos por el usuario
    // NOTA: Debe activar use_strict_mode para operaciones normales.
    ini_set('session.use_strict_mode', 0);
    // Definir un nuevo ID de sesión personalizado
    session_id($newid);
    // Inicio con un ID de sesión personalizado
    session_start();
}

// Asegúrese de que use_strict_mode esté activado.
// use_strict_mode es obligatorio por razones de seguridad.
ini_set('session.use_strict_mode', 1);
my_session_start();

// El ID de sesión debe regenerarse cuando
//  - Un usuario se conecta
//  - Un usuario se desconecta
//  - Ha transcurrido un cierto período de tiempo
my_session_regenerate_id();

// Lógica de aplicación
?>

    
```php

## Véase también

`session_regenerate_id`, `session_start`, [session.use_strict_mode](#ini.session.use-strict-mode), SessionHandler::create_sid
