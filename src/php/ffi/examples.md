---
title: Ejemplos
source_url: https://www.php.net/manual/es/ffi.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 22880
---

## Ejemplos

## Uso básico de FFI

Antes de profundizar en los detalles de la API FFI, echemos un vistazo a algunos ejemplos que demuestran la simplicidad de uso de la API FFI para tareas comunes.

> [!NOTE]
> Algunos de estos ejemplos requieren `libc.so.6` y por lo tanto no funcionarán en sistemas donde esta biblioteca no esté disponible.

Llamada a una función desde una biblioteca compartida

```php
<?php
// crea un objeto FFI, cargando la libc y exportando la función printf()
$ffi = FFI::cdef(
    "int printf(const char *format, ...);", // Declaración C regular
    "libc.so.6");
// llama a la función printf() de C
$ffi->printf("Hello %s!\n", "world");
?>

   
```

El ejemplo anterior mostrará:

    Hello world!

> [!NOTE]
> Tenga en cuenta que algunas funciones C requieren convenciones de llamada específicas, por ejemplo `__fastcall`, `__stdcall` o `__vectorcall`.

Llamada a una función, devolviendo una estructura a través de un argumento

```php
<?php
// crea la ligadura gettimeofday()
$ffi = FFI::cdef("
    typedef unsigned int time_t;
    typedef unsigned int suseconds_t;

    struct timeval {
        time_t      tv_sec;
        suseconds_t tv_usec;
    };

    struct timezone {
        int tz_minuteswest;
        int tz_dsttime;
    };

    int gettimeofday(struct timeval *tv, struct timezone *tz);
", "libc.so.6");
// crea las estructuras de datos C
$tv = $ffi->new("struct timeval");
$tz = $ffi->new("struct timezone");
// llama a la función gettimeofday() de C
var_dump($ffi->gettimeofday(FFI::addr($tv), FFI::addr($tz)));
// accede a los campos de la estructura de datos C
var_dump($tv->tv_sec);
// imprime toda la estructura de datos C
var_dump($tz);
?>

   
```

Resultado del ejemplo anterior es similar a:

    int(0)
    int(1555946835)
    object(FFI\CData:struct timezone)#3 (2) {
      ["tz_minuteswest"]=>
      int(0)
      ["tz_dsttime"]=>
      int(0)
    }

Acceso a variables C existentes

```php
<?php
// crea un objeto FFI, cargando la libc y exportando la variable errno
$ffi = FFI::cdef(
    "int errno;", // Declaración C regular
    "libc.so.6");
// imprime el valor errno de C
var_dump($ffi->errno);
?>

   
```

El ejemplo anterior mostrará:

    int(0)

Creación y modificación de variables C

```php
<?php
// crea una nueva variable C de tipo int
$x = FFI::new("int");
var_dump($x->cdata);

// asignación simple
$x->cdata = 5;
var_dump($x->cdata);

// asignación compuesta
$x->cdata += 2;
var_dump($x->cdata);
?>

   
```

El ejemplo anterior mostrará:

    int(0)
    int(5)
    int(7)

Trabajar con arrays C

```php
<?php
// crea una estructura de datos en C
$a = FFI::new("long[1024]");
// modificación de la estructura como con un array PHP normal
for ($i = 0; $i < count($a); $i++) {
    $a[$i] = $i;
}
var_dump($a[25]);
$sum = 0;
foreach ($a as $n) {
    $sum += $n;
}
var_dump($sum);
var_dump(count($a));
var_dump(FFI::sizeof($a));
?>

    
```

El ejemplo anterior mostrará:

    int(25)
    int(523776)
    int(1024)
    int(8192)

Trabajar con enums en C

```php
<?php
$a = FFI::cdef('typedef enum _zend_ffi_symbol_kind {
    ZEND_FFI_SYM_TYPE,
    ZEND_FFI_SYM_CONST = 2,
    ZEND_FFI_SYM_VAR,
    ZEND_FFI_SYM_FUNC
} zend_ffi_symbol_kind;
');
var_dump($a->ZEND_FFI_SYM_TYPE);
var_dump($a->ZEND_FFI_SYM_CONST);
var_dump($a->ZEND_FFI_SYM_VAR);
?>

   
```

El ejemplo anterior mostrará:

    int(0)
    int(2)
    int(3)

## Funciones de retrollamada

Es posible asignar una clausura PHP a una variable nativa de tipo puntero de función o pasarla como argumento de función:

Asignación de una `Closure` PHP a un puntero de función C

```php
<?php
$zend = FFI::cdef("
    typedef int (*zend_write_func_t)(const char *str, size_t str_length);
    extern zend_write_func_t zend_write;
");

echo "Hello World 1!\n";

$orig_zend_write = clone $zend->zend_write;
$zend->zend_write = function($str, $len) {
    global $orig_zend_write;
    $orig_zend_write("{\n\t", 3);
    $ret = $orig_zend_write($str, $len);
    $orig_zend_write("}\n", 2);
    return $ret;
};
echo "Hello World 2!\n";
$zend->zend_write = $orig_zend_write;
echo "Hello World 3!\n";
?>

    
```

El ejemplo anterior mostrará:

    Hello World 1!
    {
            Hello World 2!
    }
    Hello World 3!

Aunque esto funciona, esta funcionalidad no es soportada por todas las plataformas libffi, no es eficiente y provoca fugas de recursos al final de la petición.

> [!TIP]
> Por lo tanto, se recomienda minimizar el uso de las funciones de retrollamada PHP.

## Un ejemplo completo de PHP/FFI/precarga

`php.ini`

```php
ffi.enable=preload
opcache.preload=preload.php

   
```

`preload.php`

```php
<?php
FFI::load(__DIR__ . "/dummy.h");
opcache_compile_file(__DIR__ . "/dummy.php");
?>

   
```

`dummy.h`

```php
#define FFI_SCOPE "DUMMY"
#define FFI_LIB "libc.so.6"

int printf(const char *format, ...);

   
```

`dummy.php`

```php
<?php
final class Dummy {
    private static $ffi = null;
    function __construct() {
        if (is_null(self::$ffi)) {
            self::$ffi = FFI::scope("DUMMY");
        }
    }
    function printf($format, ...$args) {
       return (int) self::$ffi->printf($format, ...$args);
    }
}
?>

   
```

`test.php`

```php
<?php
$d = new Dummy();
$d->printf("Hello %s!\n", "world");
?>

   
```
