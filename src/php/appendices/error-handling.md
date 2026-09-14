---
title: Modificaciones aportadas a la gestión de errores y excepciones
source_url: https://www.php.net/manual/es/migration70.incompatible.error-handling.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration70/incompatible/error-handling.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 2485376b5
order: 290
---

## Modificaciones aportadas a la gestión de errores y excepciones

Numerosos errores fatales y recuperables se han convertido en excepciones en PHP 7. Estas excepciones de error heredan de la clase `Error`, que a su vez implementa la interfaz `Throwable` (la nueva interfaz base de la que todas las excepciones heredan).

Esto significa que los manejadores de errores personalizados podrían no invocarse, ya que las excepciones se pueden lanzar en su lugar (provocando nuevos errores irrecuperables para las excepciones `Error` no interceptadas).

Una descripción más completa de cómo funcionan los errores en PHP 7 se encuentra [ en la página de errores de PHP 7](#language.errors.php7). Esta guía de migración simplemente enumerará los cambios que afectan la retrocompatibilidad.

### `set_exception_handler` ya no está garantizado para recibir objetos `Exception`

El código que implementa un manejador de excepciones inscrito con `set_exception_handler` usando una declaración de tipo `Exception` provocará un error fatal cuando se lanza un objeto `Error`.

Si el manejador debe funcionar tanto con PHP 5 como con 7, debería eliminar la declaración de tipo del manejador, mientras que el código que se migra para funcionar exclusivamente en PHP 7 puede simplemente reemplazar la declaración de tipo `Exception` por `Throwable`.

```php
<?php
// Código para PHP 5 que fallará.
function handler(Exception $e) { /* ... */ }
set_exception_handler('handler');

// Compatible con PHP 5 y 7.
function handler($e) { /* ... */ }

// Solo PHP 7.
function handler(Throwable $e) { /* ... */ }
?>

   
```

### Los constructores internos lanzan excepciones en caso de fallo

Anteriormente, algunas clases internas devolvían `null` o un objeto inutilizable cuando el constructor fallaba. Todas las clases internas lanzarán ahora una `Exception` en este caso de la misma manera que las clases de usuario.

### Los errores de análisis lanzan una `ParseError`

Los errores del analizador ahora lanzan un objeto `ParseError`. El manejo de errores para `eval` ahora debe incluir un bloque [`catch`](#language.exceptions.catch) que pueda manejar este error.

### Cambios de severidad de los avisos E_STRICT

Todos los avisos `E_STRICT` se han reclasificado a otros niveles. La constante `E_STRICT` se conserva, por lo que las llamadas como `error_reporting(E_ALL|E_STRICT)` no provocarán errores.

| Situación | Nuevo nivel/comportamiento |
|----|----|
| Indexación por un recurso | `E_NOTICE` |
| Métodos estáticos abstractos | Aviso eliminado, no dispara ningún error |
| "Redefinir" un constructor | Aviso eliminado, no dispara ningún error |
| Incompatibilidad de firma durante la herencia | `E_WARNING` |
| Misma propiedad (compatible) en dos rasgos usados | Aviso eliminado, no dispara ningún error |
| Acceso a una propiedad estática de manera no estática | `E_NOTICE` |
| Solo se deben asignar variables por referencia | `E_NOTICE` |
| Solo se deben pasar variables por referencia | `E_NOTICE` |
| Llamada a métodos no estáticos de manera estática | `E_DEPRECATED` |

Cambios de severidad de los avisos `E_STRICT`
