---
title: exit
description: Terminar el script en curso con un código de estado o un mensaje
source_url: https://www.php.net/manual/es/function.exit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/exit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: 2312f826e
order: 47070
---

exit

Terminar el script en curso con un código de estado o un mensaje

## Descripción

```php
exit([string $status]): never
```php

Termina el script actual. Las [funciones de cierre](#function.register-shutdown-function) y los [destructores de objetos](#language.oop5.decon.destructor) siempre se ejecutarán incluso si `exit` es llamado. Sin embargo, los bloques [`finally`](#language.exceptions.finally) nunca se ejecutan.

Un código de salida de `0` se utiliza para indicar que el programa ha completado sus tareas correctamente. Cualquier otro valor indica que ocurrió un error durante la ejecución.

`exit` es una función especial, ya que dispone de un token dedicado en el analizador sintáctico. Puede ser utilizada como una instrucción (es decir, sin paréntesis) para terminar el script con el código de estado por defecto.

> [!CAUTION]
> No es posible desactivar o crear una función en un espacio de nombres que reemplace la función global `exit`.

## Parámetros

`status`  
Si `status` es un string, esta función muestra `status` justo antes de salir. El código de salida devuelto por PHP es `0`.

Si `status` es un `int`, el código de salida devuelto por PHP será `status`.

> [!NOTE]
> Los códigos de salida deben estar comprendidos entre `0` y `254`. El código de salida `255` está reservado por PHP y no debe ser utilizado.

> [!WARNING]
> Antes de PHP 8.4.0, `exit` no respetaba la [lógica habitual de manipulación de tipos](#language.types.type-juggling.function) de PHP ni la declaración [`strict_types`](#language.types.declarations.strict).
>
> Cualquier valor no `int` era convertido a `string`, incluyendo los valores de tipo `resource` y `array`. A partir de PHP 8.4.0, la función sigue la gestión estándar de tipos y genera una TypeError para los valores no válidos.

## Valores devueltos

Como esta función termina el script PHP, ningún valor es devuelto.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `exit` es ahora una verdadera función, por lo tanto sigue la lógica habitual de [manipulación de tipos](#language.types.type-juggling.function), es afectada por la declaración [`strict_types`](#language.types.declarations.strict), puede ser llamada con argumentos nombrados y ser utilizada como una [función variable](#functions.variable-functions). |
| 8.4.0 | Una llamada a `exit` sin parámetros dentro de [funciones de cierre](#function.register-shutdown-function) o de [destructores de objetos](#language.oop5.decon.destructor) restablece ahora el código de salida a `0`; anteriormente se conservaba el código de salida establecido por una llamada anterior a `exit`. |

## Ejemplos

Ejemplo básico de la función `exit`

```
<?php

// salir del programa normalmente
exit();
exit(0);

// salir con un código de error
exit(1);

?>
```php

Ejemplo de `exit` con un `string`

```
<?php

$filename = '/path/to/data-file';
$file = fopen($filename, 'r')
    or exit("no se puede abrir el archivo ($filename)");
?>

   
```php

Ejemplo de ejecución de funciones de cierre y destructores de objetos

```
<?php
class Foo
{
    public function __destruct()
    {
        echo 'Destructor : ' . __METHOD__ . '()' . PHP_EOL;
    }
}

function shutdown()
{
    echo 'Cierre : ' . __FUNCTION__ . '()' . PHP_EOL;
}

$foo = new Foo();
register_shutdown_function('shutdown');

exit();
echo 'Esto nunca será mostrado.';
?>

   
```php

El ejemplo anterior mostrará:

    Cierre : shutdown()
    Destrucción : Foo::__destruct()

`exit` como instrucción

```
<?php

// salir del programa normalmente con el código de salida 0
exit;

?>

   
```php

## Notas

> [!WARNING]
> Antes de PHP 8.4.0, `exit` era una construcción del lenguaje y no una función, por lo tanto no era posible llamarla utilizando [funciones variables](#functions.variable-functions), o [argumentos nombrados](#functions.named-arguments).

## Véase también

register_shutdown_function

Funciones de cierre

destructores de objetos
