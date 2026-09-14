---
title: assert_options
description: Define/recupere diferentes opciones de aserciones
source_url: https://www.php.net/manual/es/function.assert-options.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/assert-options.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 38720
---

assert_options

Define/recupere diferentes opciones de aserciones

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.3.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
assert_options(int $option, [mixed $value]): mixed
```php

`assert_options` permite modificar las diversas opciones de la función `assert`, o simplemente conocer la configuración actual.

> [!NOTE]
> El uso de `assert_options` no se recomienda en favor de definir y recuperar las directivas `php.ini` [zend.assertions](#ini.zend.assertions) y [assert.exception](#ini.assert.exception) con `ini_set` y `ini_get`, respectivamente.

## Parámetros

`option`  
| Opción | Directiva | Valor por omisión | Descripción |
|----|----|----|----|
| ASSERT_ACTIVE | assert.active | 1 | Activa la evaluación de la función `assert` |
| ASSERT_EXCEPTION | assert.exception | 1 | Lanza una `AssertionError` para cada aserción fallida |
| ASSERT_WARNING | assert.warning | 1 | Genera una alerta PHP para cada aserción falsa |
| ASSERT_BAIL | assert.bail | 0 | Termina la ejecución en caso de aserción falsa |
| ASSERT_QUIET_EVAL | assert.quiet_eval | 0 | Desactiva el informe de error durante la evaluación de una aserción. Eliminada a partir de PHP 8.0.0 |
| ASSERT_CALLBACK | assert.callback | (`null`) | Función de devolución de llamada del usuario, para el tratamiento de aserciones falsas |

Opciones de aserciones

`value`  
Un nuevo valor, opcional, para la opción.

La función de devolución de llamada definida mediante `ASSERT_CALLBACK` o [assert.callback](#ini.assert.callback) debería tener la siguiente firma:

```php
assert_callback(string $file, int $line, string $assertion, [string $description]): void
```

`file`  
El fichero donde `assert` fue llamado.

`line`  
La línea donde `assert` fue llamado.

`assertion`  
Antes de PHP 8.0.0, el primer parámetro de la función `assert` era la aserción pasada, pero solo cuando la aserción se proporcionaba como string. (Si la aserción era una condición booleana, este parámetro era una cadena vacía.) A partir de PHP 8.0.0, este parámetro es siempre `null`.

`description`  
La descripción que se proporcionó a `assert`.

Pasar una cadena vacía como `value` restablece la función de retrollamada assert.

## Valores devueltos

Devuelve el valor original de la opción.

## Errores/Excepciones

Si `option` no es una opción válida, se lanza una `ValueError`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | `assert_options` ahora está obsoleto. |
| 8.0.0 | Si `option` no es una opción válida, se lanza una `ValueError`. Anteriormente, se devolvía `false`. |

## Ejemplos

Ejemplo con `assert_options`

```php
<?php
// Esta es nuestra función para manejar
// los errores de aserción
function assert_failure($file, $line, $assertion, $message)
{
    echo "La aserción $assertion en $file en la línea $line ha fallado: $message";
}

// Esta es nuestra función de prueba
function test_assert($parameter)
{
    assert(is_bool($parameter));
}

// Define nuestras opciones de aserción
assert_options(ASSERT_ACTIVE,   true);
assert_options(ASSERT_BAIL,     true);
assert_options(ASSERT_WARNING,  false);
assert_options(ASSERT_CALLBACK, 'assert_failure');

// Una aserción que debe fallar
test_assert(1);

// Esto nunca se alcanza, ya que ASSERT_BAIL
// es true
echo 'Nunca alcanzado';
?>

    
```

## Véase también

`assert`
