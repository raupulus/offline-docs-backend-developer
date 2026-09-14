---
title: spl_autoload_register
description: Registra una función como implementación de __autoload()
source_url: https://www.php.net/manual/es/function.spl-autoload-register.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/functions/spl-autoload-register.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d4b762e22
order: 82280
---

spl_autoload_register

Registra una función como implementación de \_\_autoload()

## Descripción

```php
spl_autoload_register([callable $callback], [bool $throw], [bool $prepend]): bool
```php

`spl_autoload_register` registra una función en la pila `__autoload` proporcionada. Si la pila no está activa, se activa.

Si el código ya dispone de una función `__autoload`, entonces esta función debe registrar explícitamente la pila \_\_autoload. Esto se debe a que `spl_autoload_register` reemplaza la caché del motor para la función `__autoload` por `spl_autoload` o `spl_autoload_call`.

Si se deben utilizar múltiples funciones de autocarga, la función `spl_autoload_register` está diseñada para ello. Crea una cola de funciones de autocarga y las ejecuta una tras otra, en el orden en que fueron definidas. A diferencia, la función `__autoload` solo puede definirse una vez.

## Parámetros

`callback`  
La función de autoload a registrar. Si es `null`, entonces se registrará la implementación por defecto de la función `spl_autoload`.

```php
callback(string $class): void
```

El `class` no contendrá el backslash inicial de un identificador completamente cualificado.

`throw`  
Este parámetro especifica si `spl_autoload_register` debe lanzar excepciones cuando el `callback` no ha podido ser registrado.

> [!WARNING]
> Este parámetro es ignorado a partir de PHP 8.0.0, y se emitirá un aviso si se define como `false`. `spl_autoload_register` siempre lanzará una `TypeError` con argumentos no válidos.

`prepend`  
Si este parámetro vale `true`, `spl_autoload_register` añadirá la función al principio de la pila del autoloader en lugar de añadirla al final de la pila.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                   |
|---------|-------------------------------|
| 8.0.0   | `callback` ahora es nullable. |

## Ejemplos

Ejemplo con `spl_autoload_register` como reemplazo de una función `__autoload`

```php
<?php

// function __autoload($class) {
//     include 'classes/' . $class . '.class.php';
// }

function my_autoloader($class) {
    include 'classes/' . $class . '.class.php';
}

spl_autoload_register('my_autoloader');

// O, utilizando una función anónima
spl_autoload_register(function ($class) {
    include 'classes/' . $class . '.class.php';
});

?>

    
```

Ejemplo con `spl_autoload_register` donde la clase no es cargada

```php
<?php

namespace Foobar;

class Foo {
    static public function test($class) {
        print '[['. $class .']]';
    }
}

spl_autoload_register(__NAMESPACE__ .'\Foo::test');

new InexistentClass;

?>

    
```

Resultado del ejemplo anterior es similar a:

    [[Foobar\InexistentClass]]
    Fatal error: Class 'Foobar\InexistentClass' not found in ...

El identificador será proporcionado sin el backslash inicial.

```php
<?php

spl_autoload_register(static function ($class) {
    var_dump($class);
});

class_exists('RelativeName');
class_exists('RelativeName\\WithNamespace');
class_exists('\\AbsoluteName');
class_exists('\\AbsoluteName\\WithNamespace');

?>

    
```

El ejemplo anterior mostrará:

    string(12) "RelativeName"
    string(26) "RelativeName\WithNamespace"
    string(12) "AbsoluteName"
    string(26) "AbsoluteName\WithNamespace"

## Véase también

`__autoload`
