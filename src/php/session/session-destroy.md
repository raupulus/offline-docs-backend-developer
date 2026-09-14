---
title: session_destroy
description: Destruye una sesión
source_url: https://www.php.net/manual/es/function.session-destroy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-destroy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: false
translation_revision: 682510e91
order: 73770
---

session_destroy

Destruye una sesión

## Descripción

```php
session_destroy(): bool
```php

`session_destroy` destruye todos los datos asociados a la sesión actual. Esta función no destruye las variables globales asociadas a la sesión, de igual manera, no destruye la cookie de sesión. Para acceder nuevamente a las variables de sesión, la función `session_start` debe ser llamada nuevamente.

> [!NOTE]
> No es necesario llamar a `session_destroy` desde el programa generalmente. Limpiar el array \$\_SESSION en lugar de destruir los datos de sesión.

Para destruir completamente una sesión, el identificador de la sesión debe ser eliminado también. Si una cookie es utilizada para propagar el identificador de sesión (comportamiento por omisión), entonces la cookie de sesión debe ser eliminada. La función `setcookie` puede ser utilizada para esto.

Cuando [session.use_strict_mode](#ini.session.use-strict-mode) está activado. No es necesario eliminar las cookies de ID de sesión obsoletas ya que el módulo de sesión no acepta las cookies de ID de sesiones cuando no hay datos asociados con estos ID de sesiones y definirá una nueva cookie de ID de sesión. Activar [session.use_strict_mode](#ini.session.use-strict-mode) es recomendado para todos los sitios.

> [!WARNING]
> La eliminación inmediata de una sesión puede causar resultados inesperados. Cuando hay peticiones simultáneas, otras conexiones pueden perder repentinamente datos de sesión. Por ejemplo peticiones desde JavaScript y/o peticiones desde enlaces URL.
>
> Aunque el módulo de sesión actual no acepta una cookie de ID de sesión vacía, la eliminación inmediata de sesión puede provocar una cookie de ID de sesión vacía debido a una condición de concurrencia lado-cliente (navegador). Esto provocará la creación de muchos ID de sesión innecesarios por el cliente.
>
> Para evitar esto, se debe definir un timestamp en \$\_SESSION y rechazar el acceso a todas las fechas posteriores. O asegurarse de que su aplicación no tenga peticiones simultáneas. Esto también se aplica a `session_regenerate_id`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Destrucción de una sesión con `$_SESSION`

```
<?php
// Inicialización de la sesión.
// Si se utiliza otro nombre
// session_name("otroNombre")
session_start();

// Destruye todas las variables de sesión
$_SESSION = array();

// Si se quiere destruir completamente la sesión, también se debe eliminar
// la cookie de sesión.
// Nota: esto destruirá la sesión y no solo los datos de sesión !
if (ini_get("session.use_cookies")) {
    $params = session_get_cookie_params();
    setcookie(session_name(), '', time() - 42000,
        $params["path"], $params["domain"],
        $params["secure"], $params["httponly"]
    );
}

// Finalmente, se destruye la sesión.
session_destroy();
?>

    
```php

## Véase también

[session.use_strict_mode](#ini.session.use-strict-mode), `session_reset`, `session_regenerate_id`, `unset`, `setcookie`
