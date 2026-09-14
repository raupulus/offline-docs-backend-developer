---
title: session_set_save_handler
description: Configura las funciones de almacenamiento de sesiones
source_url: https://www.php.net/manual/es/function.session-set-save-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-set-save-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: false
translation_revision: ca23605a1
order: 73890
---

session_set_save_handler

Configura las funciones de almacenamiento de sesiones

## Descripción

```php
session_set_save_handler(callable $open, callable $close, callable $read, callable $write, callable $destroy, callable $gc, [callable $create_sid], [callable $validate_sid], [callable $update_timestamp]): bool
```php

Es posible registrar el siguiente prototipo:

```php
session_set_save_handler(object $sessionhandler, [bool $register_shutdown]): bool
```

`session_set_save_handler` configura las funciones de almacenamiento de sesiones, y permite elegir funciones de usuario para guardar y leer todas las sesiones. Esta función es muy práctica cuando se necesita guardar los datos de sesión utilizando una técnica diferente al sistema de archivos proporcionado por defecto, por ejemplo, el almacenamiento en base de datos.

## Parámetros

Esta función tiene dos prototipos.

`sessionhandler`  
Una instancia de una clase que implementa una o más de las siguientes interfaces: SessionHandlerInterface, y opcionalmente SessionIdInterface, y/o SessionUpdateTimestampHandlerInterface, como la clase `SessionHandler`, para el registro como manejador de sesión.

`register_shutdown`  
Registra la función `session_write_close` como función `register_shutdown_function`.

o

`open`  
Una función de retorno con la siguiente firma:

```php
open(string $savePath, string $sessionName): bool
```php

La función de retorno `open` funciona como un constructor en una clase, y se ejecuta cuando la sesión se abre. Es la primera función de retorno ejecutada cuando la sesión comienza automáticamente o manualmente con la función `session_start`. El valor devuelto es `true` en caso de éxito o `false` si ocurre un error.

`close`  
Una función de retorno con la siguiente firma:

```php
close(): bool
```

La función de retorno `close` funciona como un destructor en una clase, y se ejecuta una vez que la función de retorno write de la sesión ha terminado de ejecutarse. También es llamada cuando la función `session_write_close` es llamada. El valor devuelto es `true` en caso de éxito, o `false` si ocurre un error.

`read`  
Una función de retorno con la siguiente firma:

```php
read(string $sessionId): string
```php

La función de retorno `read` debe siempre devolver un string serializado que contenga los datos de sesión codificados o un string vacío si no hay datos que leer.

Esta función de retorno es llamada internamente por PHP cuando la sesión comienza o cuando la función `session_start` es llamada. Antes de que esta función de retorno sea invocada, PHP invocará la función de retorno `open`.

El valor devuelto por esta función de retorno debe ser exactamente del mismo formato de serialización que el pasado para el almacenamiento a la función de retorno `write`. El valor devuelto será deserializado automáticamente por PHP y utilizado para poblar la variable superglobal `$_SESSION`. Aunque los datos se asemejen fuertemente a los emitidos por la función `serialize`, note que es un formato diferente, que es especificado mediante la opción de configuración [session.serialize_handler](#ini.session.serialize-handler).

`write`  
Una función de retorno con la siguiente firma:

```php
write(string $sessionId, string $data): bool
```

La función de retorno `write` es llamada cuando la sesión debe ser guardada y cerrada. Esta función de retorno recibe el identificador de la sesión actual así como una versión serializada del contenido de la variable superglobal `$_SESSION`. El método de serialización utilizado internamente por PHP es especificado mediante la opción de configuración [session.serialize_handler](#ini.session.serialize-handler).

Los datos de sesión serializados pasados a esta función de retorno deben ser almacenados utilizando el identificador de sesión proporcionado. Al recuperar estos datos, la función de retorno `read` debe devolver el valor exacto, originalmente pasado a la función de retorno `write`.

Esta función de retorno es invocada cuando PHP se detiene o explícitamente cuando la función `session_write_close` es llamada. Note que después de la ejecución de esta función, PHP ejecutará internamente la función de retorno `close`.

> [!NOTE]
> El manejador de escritura no se ejecuta hasta que el flujo de salida no haya sido cerrado. Por lo tanto, la salida de las peticiones de depuración del manejador "write" nunca será mostrada en el navegador. Si la salida de depuración es necesaria, se sugiere que sea dirigida a un archivo.

`destroy`  
Una función de retorno con la siguiente firma:

```php
destroy(string $sessionId): bool
```php

Esta función de retorno es ejecutada cuando una sesión es destruida con la función `session_destroy` o con `session_regenerate_id` con el parámetro de destrucción definido a `true`. El valor devuelto debe ser `true` en caso de éxito, o `false` si ocurre un error.

`gc`  
Una función de retorno con la siguiente firma:

```php
gc(int $lifetime): bool
```

La función de retorno del recolector de basura es invocada internamente por PHP periódicamente para purgar los datos de sesión antiguos. La frecuencia es controlada por las opciones de configuración [session.gc_probability](#ini.session.gc-probability) y [session.gc_divisor](#ini.session.gc-divisor). El valor de la duración de vida pasado a esta función de retorno puede ser definido mediante la opción de configuración [session.gc_maxlifetime](#ini.session.gc-maxlifetime). El valor devuelto debe ser `true` en caso de éxito, o `false` si ocurre un error.

`create_sid`  
Una función de retorno con la siguiente firma:

```php
create_sid(): string
```php

Esta función de retorno es ejecutada cuando se necesita un nuevo ID de sesión. No se proporcionan parámetros, y el valor devuelto debe ser un string que es un ID de sesión válido para su manejador.

`validate_sid`  
Una función de retorno con la siguiente firma:

```php
validate_sid(string $key): bool
```

Esta función de retorno es ejecutada cuando una sesión va a comenzar, un ID de sesión es proporcionado y [session.use_strict_mode](#ini.session.use-strict-mode) está activado. `key` es el ID de sesión a validar. Un ID de sesión es válido, si una sesión con este ID ya existe. El valor de retorno debe ser `true` en caso de éxito, `false` en caso de fallo.

`update_timestamp`  
Una función de retorno con la siguiente firma:

```php
update_timestamp(string $key, string $val): bool
```php

Esta función de retorno es ejecutada cuando una sesión es actualizada. `key` es el ID de sesión, `val` son los datos de sesión. El valor de retorno debe ser `true` en caso de éxito, `false` en caso de fallo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Llamar a `session_set_save_handler` con más de dos argumentos está ahora obsoleto. En su lugar, use la firma de dos argumentos. |

## Ejemplos

Manejador de sesión personalizado: ver el código completo en la documentación sobre la interfaz `SessionHandlerInterface`.

Solo mostramos la invocación aquí, el ejemplo completo puede verse en la documentación de la interfaz `SessionHandlerInterface`.

Note que aquí utilizamos el prototipo orientado a objetos con `session_set_save_handler` y registramos la función de cierre utilizando el flag en el parámetro de la función. Esto es generalmente preferible al registrar objetos como manejadores de guardado de sesión.

```
<?php
class MySessionHandler implements SessionHandlerInterface
{
    // implementación de la interfaz aquí
}

$handler = new MySessionHandler();
session_set_save_handler($handler, true);
session_start();

// proceso para definir y recuperar los valores por sus claves desde $_SESSION

    
```php

## Notas

> [!WARNING]
> Los manejadores de escritura `write` y cierre `close` son llamados después de la destrucción de los objetos, y por lo tanto, no pueden utilizar los objetos ni lanzar excepciones. Las excepciones no pueden ser atrapadas ni mostradas, y la ejecución solo se detendrá de manera inesperada.
>
> Es posible llamar a `session_write_close` desde el destructor para resolver este problema pero la forma más elegante es registrar la función de cierre tal como se describe arriba.

> [!WARNING]
> El directorio de trabajo actual cambia según las SAPIs si la sesión es cerrada al final del script. Es posible cerrar la sesión más tarde, gracias a la función `session_write_close`.

## Véase también

La directiva de configuración [session.save_handler](#ini.session.save-handler), La directiva de configuración [session.serialize_handler](#ini.session.serialize-handler)., `register_shutdown_function`, `session_register_shutdown`, Ver [save_handler.inc](https://github.com/php/php-src/blob/master/ext/session/tests/save_handler.inc) para una implementación procedimental completa
