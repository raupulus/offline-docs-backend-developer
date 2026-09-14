---
title: session_regenerate_id
description: Reemplaza el identificador de sesión actual por uno nuevo
source_url: https://www.php.net/manual/es/function.session-regenerate-id.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-regenerate-id.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: true
translation_revision: b9c73a59a
order: 73840
---

session_regenerate_id

Reemplaza el identificador de sesión actual por uno nuevo

## Descripción

```php
session_regenerate_id([bool $delete_old_session]): bool
```php

`session_regenerate_id` reemplazará el identificador de sesión actual por uno nuevo, generado automáticamente, manteniendo los valores de sesión.

Cuando la opción [session.use_trans_sid](#ini.session.use-trans-sid) está activa, la salida para visualización debe comenzar después de la llamada a la función `session_regenerate_id`. De lo contrario, se utilizará el antiguo ID de sesión.

> [!WARNING]
> Actualmente, session_regenerate_id no maneja adecuadamente una red inestable. Por ejemplo, redes móviles y WiFi. Por lo tanto, puede encontrarse una pérdida de sesión al llamar a session_regenerate_id.
>
> No se deben destruir los antiguos datos de sesión inmediatamente, sino que se debe utilizar el timestamp de destrucción y controlar el acceso al antiguo ID de sesión. De lo contrario, el acceso simultáneo a la página puede provocar un estado inconsistente, o quizás se haya perdido la sesión, o puede provocar un acceso concurrente lado-cliente (navegador) y puede crear muchos ID de sesión innecesariamente. La eliminación inmediata de datos de sesión también desactiva la detección y prevención de ataques de secuestro de sesión.

## Parámetros

`delete_old_session`  
Si se debe borrar el antiguo archivo de sesión asociado o no. No se debe eliminar la antigua sesión si se necesita evitar accesos concurrentes causados por la eliminación o detectar/evitar ataques de secuestro de sesión.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `session_regenerate_id`

```
<?php
// Nota: este código no funciona completamente, es un ejemplo!

session_start();

// Verificar el timestamp de destrucción
if (isset($_SESSION['destroyed'])
    && $_SESSION['destroyed'] < time() - 300) {
    // No debería ocurrir habitualmente. Esto podría ser una ataque
    // o debido a una red inestable. Elimine todo el estado de
    // autenticación de esta sesión de usuario.
    remove_all_authentication_flag_from_active_sessions($_SESSION['userid']);
    throw(new DestroyedSessionAccessException);
}

$old_sessionid = session_id();

// Definir el timestamp de destrucción
$_SESSION['destroyed'] = time(); // session_regenerate_id () registra los antiguos datos de sesión

// Simplemente llamar a session_regenerate_id() puede provocar pérdida de sesión, etc.
// Ver el ejemplo siguiente.
session_regenerate_id();

// La nueva sesión no necesita el timestamp de destrucción
unset($_SESSION['destroyed']);

$new_sessionid = session_id();

echo "Sesión antigua: $old_sessionid<br />";
echo "Sesión nueva: $new_sessionid<br />";

print_r($_SESSION);
?>

    
```php

El módulo de sesión actual no maneja adecuadamente una red inestable. Se debe gestionar el ID de sesión para evitar la pérdida de sesión por session_regenerate_id.

Evitar la pérdida de sesión por `session_regenerate_id`

```
<?php
// Nota: este código no funciona completamente, es un ejemplo!
// my_session_start() y my_session_regenerate_id() evitan sesiones perdidas
// por red inestable. Además, este código puede evitar la explotación de
// sesión robada por atacantes.

function my_session_start() {
    session_start();
    if (isset($_SESSION['destroyed'])) {
       if ($_SESSION['destroyed'] < time()-300) {
           // No debería ocurrir habitualmente. Esto podría ser una
           // ataque o debido a una red inestable. Elimine todo el estado
           // de autenticación de esta sesión de usuario.
            remove_all_authentication_flag_from_active_sessions($_SESSION['userid']);
           throw(new DestroyedSessionAccessException);
       }
       if (isset($_SESSION['new_session_id'])) {
           // No ha expirado completamente. Podría ser pérdida de cookie por red inestable.
           // Intente nuevamente definir la cookie de ID de sesión adecuada.
           // Nota: no intente redefinir el ID de sesión si
           // desea eliminar el estado de autenticación.
           session_commit();
           session_id($_SESSION['new_session_id']);
           // El nuevo ID de sesión debe existir
           session_start();
           return;
       }
   }
}

function my_session_regenerate_id() {
    // El nuevo ID de sesión es requerido para definir el ID de sesión adecuado
    // cuando el ID de sesión no está definido debido a una red inestable.
    $new_session_id = session_create_id();
    $_SESSION['new_session_id'] = $new_session_id;

    // Define el timestamp de destrucción
    $_SESSION['destroyed'] = time();

    // Escribe y cierra la sesión actual
    session_commit();

    // Inicia la sesión con un nuevo ID
    session_id($new_session_id);
    ini_set('session.use_strict_mode', 0);
    session_start();
    ini_set('session.use_strict_mode', 1);

    // La nueva sesión no lo necesita
    unset($_SESSION['destroyed']);
    unset($_SESSION['new_session_id']);
}
?>

    
```php

## Véase también

`session_id`, `session_create_id`, `session_start`, `session_destroy`, `session_reset`, `session_name`
