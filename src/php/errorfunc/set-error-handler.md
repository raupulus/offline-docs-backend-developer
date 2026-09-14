---
title: set_error_handler
description: Especifica una función de usuario como gestor de errores
source_url: https://www.php.net/manual/es/function.set-error-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/errorfunc/functions/set-error-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: errorfunc
translation_status: ready
translation_reviewed: false
translation_revision: 21ce7d7f4
order: 17690
---

set_error_handler

Especifica una función de usuario como gestor de errores

## Descripción

```php
set_error_handler(callable $callback, [int $error_levels]): callable
```php

`set_error_handler` selecciona la función de usuario `callback` para gestionar errores en un script.

Esta función puede ser utilizada para definir gestores de errores personalizados durante la ejecución, por ejemplo en aplicaciones que necesitan limpiar archivos/datos cuando ocurre un error crítico o cuando un error es generado en respuesta a ciertas condiciones (utilizando la función `trigger_error`).

Debe recordarse que la función estándar de tratamiento de errores de PHP es completamente ignorada para los errores de tipos especificados por `error_levels` a menos que la función de retorno devuelva `false`. Los parámetros de la función `error_reporting` no tendrán efecto y el gestor de errores será llamado en cualquier caso. Sin embargo, siempre es posible leer el valor actual de la configuración de [error_reporting](#ini.error-reporting) y hacer que la función de gestión de errores reaccione en consecuencia.

También debe notarse que es responsabilidad del gestor de errores detener la ejecución del script si es necesario llamando a la función `exit`. Si la función del gestor de errores devuelve, la ejecución del script continuará con la instrucción siguiente a la que causó el error.

Los siguientes tipos de errores no pueden ser gestionados con esta función: `E_ERROR`, `E_PARSE`, `E_CORE_ERROR`, `E_CORE_WARNING`, `E_COMPILE_ERROR`, `E_COMPILE_WARNING` independientemente de dónde sean generados, así como la mayoría de los `E_STRICT` del archivo en el cual `set_error_handler` es llamado.

Si un error ocurre antes de que el script sea ejecutado (por ejemplo una descarga de archivo), el gestor de errores personalizado no podrá ser llamado, ya que aún no está registrado.

## Parámetros

`callback`  
Si `null` es proporcionado, el gestor es reestablecido a su estado por defecto. De lo contrario, el gestor es una función de retorno con la siguiente firma:

```php
handler(int $errno, string $errstr, [string $errfile], [int $errline], [array $errcontext]): bool
```

`errno`  
El primer parámetro `errno`, será pasado el nivel de error, en forma de entero.

`errstr`  
El segundo parámetro `errstr`, será pasado el mensaje de error, en forma de string.

`errfile`  
Si el cierre acepta un tercer parámetro, `errfile`, será pasado el nombre del archivo en el cual el error fue identificado, en forma de string.

`errline`  
Si el cierre acepta un cuarto parámetro, `errline`, será pasado el número de línea en la cual el error fue identificado, en forma de entero.

`errcontext`  
Si el cierre acepta un quinto parámetro, `errcontext`, será pasado como un array que apunta a la tabla de símbolos activos en el momento en que el error ocurrió. En otras palabras, `errcontext` contiene un array con todas las variables que existían cuando el error fue generado. Los gestores de errores de usuario no deben modificar el contexto de error.

> [!WARNING]
> Este parámetro es *OBSOLETO* a partir de PHP 7.2.0, y *ELIMINADO* a partir de PHP 8.0.0. Si la función definida este parámetro sin valor por defecto, un error de "too few arguments" será generado al llamarla.

Si la función devuelve `false`, entonces el gestor de errores normal continúa.

`error_levels`  
Sirve como máscara para llamar a la función `callback` de la misma forma que la opción de configuración [error_reporting](#ini.error-reporting) controla los errores que son mostrados. Sin la máscara, `callback` será llamado para todos los errores, independientemente del valor de [error_reporting](#ini.error-reporting).

## Valores devueltos

Devuelve el último gestor de errores (si existe) en forma de `callable`. Si el gestor de errores interno es utilizado, `null` es devuelto.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `errcontext` ha sido eliminado, y ya no será pasado a los cierres de usuario. |
| 7.2.0 | `errcontext` se ha vuelto obsoleto. El uso de este parámetro emite una notificación `E_DEPRECATED`. |

## Ejemplos

Gestor de errores con `set_error_handler` y `trigger_error`

El ejemplo siguiente ilustra la intercepción de errores internos con generación de error y su explotación en una función de usuario:

```php
<?php
// Gestor de errores
function myErrorHandler($errno, $errstr, $errfile, $errline)
{
   if (!(error_reporting() & $errno)) {
        // Este código de error no está incluido en error_reporting(), por lo tanto continúa
        // hasta el gestor de errores estándar de PHP
        return false;
    }

    // $errstr debe ser posiblemente escapado:
    $errstr = htmlspecialchars($errstr);

    switch ($errno) {
    case E_USER_ERROR:
        echo "<b>MI ERROR</b> [$errno] $errstr<br />\n";
        echo "  Error fatal en la línea $errline en el archivo $errfile";
        echo ", PHP " . PHP_VERSION . " (" . PHP_OS . ")<br />\n";
        echo "Detención...<br />\n";
        exit(1);

    case E_USER_WARNING:
        echo "<b>MI ALERTA</b> [$errno] $errstr<br />\n";
        break;

    case E_USER_NOTICE:
        echo "<b>MI AVISO</b> [$errno] $errstr<br />\n";
        break;

    default:
        echo "Tipo de error desconocido: [$errno] $errstr<br />\n";
        break;
    }

    /* No ejecutar el gestor interno de PHP */
    return true;
}

// Función para probar la gestión de error
function scale_by_log($vect, $scale)
{
    if (!is_numeric($scale) || $scale <= 0) {
        trigger_error("log(x) para x <= 0 es indefinido, usted usó: scale = $scale", E_USER_ERROR);
    }

    if (!is_array($vect)) {
        trigger_error("Tipo de entrada incorrecto, se esperaba un array de valores", E_USER_WARNING);
        return null;
    }

    $temp = array();
    foreach($vect as $pos => $value) {
        if (!is_numeric($value)) {
            trigger_error("El valor en la posición $pos no es un número, se utiliza 0 (cero)", E_USER_NOTICE);
            $value = 0;
        }
        $temp[$pos] = log($scale) * $value;
    }
    return $temp;
  }

// Configuración del gestor de errores
$old_error_handler = set_error_handler("myErrorHandler");

// Generación de algunos errores. Comencemos creando un array
echo "vector a\n";
$a = array(2, 3, "foo", 5.5, 43.3, 21.11);
print_r($a);

// Generemos ahora un segundo array
echo "----\nvector b - un aviso (b = log(PI) * a)\n";
/* Valor en la posición $pos no es un número, se utiliza 0 (cero) */
$b = scale_by_log($a, M_PI);
print_r($b);

// Esto es un problema, hemos utilizado una cadena en lugar de un array
echo "----\nvector c - una advertencia\n";
/* Tipo de entrada incorrecto, se esperaba un array de valores */
$c = scale_by_log("no un array", 2.3);
var_dump($c); // NULL

// Esto es un error crítico: el logaritmo de cero o de un número negativo es indefinido
echo "----\nvector d - error fatal\n";
/* log(x) para x <= 0 es indefinido, usted usó: scale = $scale" */
$d = scale_by_log($a, -2.5);
var_dump($d); // Nunca alcanzado
?>

    
```

Resultado del ejemplo anterior es similar a:

    vector a
    Array
    (
        [0] => 2
        [1] => 3
        [2] => foo
        [3] => 5.5
        [4] => 43.3
        [5] => 21.11
    )
    ----
    vector b - un aviso (b = log(PI) * a)
    <b>MI AVISO</b> [1024] El valor en la posición 2 no es un número, se utiliza 0 (cero)<br />
    Array
    (
        [0] => 2.2894597716988
        [1] => 3.4341896575482
        [2] => 0
        [3] => 6.2960143721717
        [4] => 49.566804057279
        [5] => 24.165247890281
    )
    ----
    vector c - una advertencia
    <b>MI ALERTA</b> [512] Entrada incorrecta, se esperaba un array de valores<br />
    NULL
    ----
    vector d - error fatal
    <b>MI ERROR</b> [256] log(x) para x <= 0 es indefinido, usted usó: scale = -2.5<br />
    Error fatal en la línea 36 en el archivo trigger_error.php, PHP 4.0.2 (Linux)<br />
    Abandono...<br />

## Véase también

`ErrorException`, `error_reporting`, `restore_error_handler`, `get_error_handler`, `trigger_error`, [Constantes de nivel de error](#errorfunc.constants)
