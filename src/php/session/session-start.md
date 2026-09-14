---
title: session_start
description: Inicia una nueva sesión o reanuda una sesión existente
source_url: https://www.php.net/manual/es/function.session-start.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-start.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: true
translation_revision: 151e61773
order: 73900
---

session_start

Inicia una nueva sesión o reanuda una sesión existente

## Descripción

```php
session_start([array $options]): bool
```php

`session_start` crea una sesión o restaura la encontrada en el servidor, mediante el identificador de sesión pasado en una petición GET, POST o mediante una cookie.

Cuando `session_start` es llamada o cuando una sesión comienza automáticamente, PHP va a llamar a los gestores de apertura y lectura. Estos son gestores internos proporcionados por PHP (como archivos, SQLite o Memcached) o bien gestores personalizados definidos mediante `session_set_save_handler`. La función de lectura va a recuperar toda sesión existente (almacenada en forma serializada) y va a deserializar los datos para poblar \$\_SESSION.

Para utilizar una sesión nombrada, debe llamarse a `session_name` antes de llamar a `session_start`.

Cuando [session.use_trans_sid](#ini.session.use-trans-sid) está activada, la función `session_start` registrará un gestor interno de salida para la reescritura de URLs.

Si un usuario utiliza `ob_gzhandler` o el equivalente `ob_start`, el orden de llamada de las funciones es importante para una salida correcta. Por ejemplo, `ob_gzhandler` debe ser registrado antes de iniciar la sesión.

## Parámetros

`options`  
Si se proporciona, se trata de un array asociativo de opciones que reemplazará [las directivas de configuración de sesión](#session.configuration) actualmente definidas. Las claves no deben incluir el prefijo `session.`.

Además del conjunto normal de directivas de configuración, una opción `read_and_close` puede también ser proporcionada. Si la valor es definido como `true`, esto provoca el cierre inmediato de la sesión después de la lectura, lo que evita cualquier bloqueo innecesario si los datos de sesión no son modificados.

## Valores devueltos

Devuelve `true` si una sesión pudo ser iniciada con éxito, y `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.1.0 | `session_start` ahora devuelve `false` y ya no inicializa `$_SESSION` cuando no ha podido iniciar la sesión. |

## Ejemplos

## Un ejemplo de sesión básica

`page1.php`

```
<?php
// page1.php

session_start();

echo 'Bienvenido a la página número 1';

$_SESSION['favcolor'] = 'green';
$_SESSION['animal']   = 'cat';
$_SESSION['time']     = time();

// Funciona si la cookie ha sido aceptada
echo '<br /><a href="page2.php">página 2</a>';

// O bien, indicando explícitamente el identificador de sesión
echo '<br /><a href="page2.php?' . SID . '">página 2</a>';
?>

    
```php

Después de ver la página `page1.php` con un navegador, la segunda página `page2.php` (cuyo código sigue) va a mostrar mágicamente los datos de sesión. Consulte la referencia sobre las [sesiones](#ref.session) para obtener información sobre la [propagación de identificadores de sesión](#session.idpassing), y el uso de la constante `SID`.

Recuperación de la sesión: `page2.php`

```
<?php
// page2.php

session_start();

echo 'Bienvenido a la página número 2<br />';

echo $_SESSION['favcolor']; // green
echo $_SESSION['animal'];   // cat
echo date('Y m d H:i:s', $_SESSION['time']);

// Podría utilizarse la constante SID aquí, al igual que en la página page1.php
echo '<br /><a href="page1.php">página 1</a>';
?>

    
```php

## Proporcionar opciones a `session_start`

Reemplazo de la duración del cookie

```
<?php
// Esto envía un cookie persistente que dura un día.
session_start([
    'cookie_lifetime' => 86400,
]);
?>

    
```php

Lectura de la sesión y cierre

```
<?php
// Si sabemos que no necesitamos cambiar
// nada en la sesión, podemos simplemente
// leer y cerrar de inmediato para evitar bloquear
// el archivo de sesión y bloquear otras páginas
session_start([
    'cookie_lifetime' => 86400,
    'read_and_close'  => true,
]);

    
```php

## Notas

> [!NOTE]
> Para utilizar sesiones basadas en cookies, `session_start` debe ser llamada antes de mostrar cualquier cosa en el navegador.

> [!NOTE]
> El uso de [`zlib.output_compression`](#ini.zlib.output-compression) es recomendado, en lugar de `ob_gzhandler`.

> [!NOTE]
> Esta función va a emitir varios encabezados HTTP, dependiendo de la configuración. Consulte `session_cache_limiter` para personalizar estos encabezados.

## Véase también

`$_SESSION`, La directiva de configuración [session.auto_start](#ini.session.auto-start), `session_id`
