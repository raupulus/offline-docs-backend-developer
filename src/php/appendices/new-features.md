---
title: Nuevas características
source_url: https://www.php.net/manual/es/migration56.new-features.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration56/new-features.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: c9b1de1c1
order: 210
---

## Nuevas características

## Expresiones de constante

Ahora es posible proporcionar una expresión escalar que involucre números, literales de tipo `string` y/o constantes en contextos donde anteriormente PHP esperaba un valor estático, tales como declaraciones de constantes o propiedades y argumentos predeterminados de funciones.

```php
<?php
const UNO = 1;
const DOS = UNO * 2;

class C {
    const TRES = DOS + 1;
    const UN_TERCIO = UNO / self::TRES;
    const RESULTADO = 'El valor de TRES es '.self::TRES;

    public function f($a = UNO + self::TRES) {
        return $a;
    }
}

echo (new C)->f()."\n";
echo C::RESULTADO;
?>

   
```

El ejemplo anterior mostrará:

    4
    El valor de TRES es 3

También es posible definir una constante `array` usando la palabra clave `const`:

```php
<?php
const ARR = ['a', 'b'];

echo ARR[0];
?>

   
```

El ejemplo anterior mostrará:

    a

## Funciones variádicas vía el operador de descomposición `...`

Las [funciones variádicas](#functions.variable-arg-list) ahora se pueden implementar usando el operador de descomposición `...`, en lugar de usar la función `func_get_args`.

```php
<?php
function f($req, $opt = null, ...$params) {
    // $params es un array que contiene los argumentos restantes.
    printf('$req: %d; $opt: %d; Número de argumentos: %d'."\n",
           $req, $opt, count($params));
}

f(1);
f(1, 2);
f(1, 2, 3);
f(1, 2, 3, 4);
f(1, 2, 3, 4, 5);
?>

   
```

El ejemplo anterior mostrará:

    $req: 1; $opt: 0; Número de argumentos: 0
    $req: 1; $opt: 2; Número de argumentos: 0
    $req: 1; $opt: 2; Número de argumentos: 1
    $req: 1; $opt: 2; Número de argumentos: 2
    $req: 1; $opt: 2; Número de argumentos: 3

## Desempaquetado de argumentos vía el operador de descomposición `...`

Los [arrays](#language.types.array) y los objetos Traversable se pueden desempaquetar en la lista de argumentos al llamar a una función usando el operador de descomposición `...`. Este método es conocido como el operador splat en otros lenguajes como Ruby.

```php
<?php
function add($a, $b, $c) {
    return $a + $b + $c;
}

$operators = [2, 3];
echo add(1, ...$operators);
?>

   
```

El ejemplo anterior mostrará:

    6

## Exponenciación vía el operador `**`

Se ha añadido un operador `**` asociativo a la derecha para soportar la exponenciación, en conjunción con el operador de asignación `**=`.

```php
<?php
printf("2 ** 3 ==      %d\n", 2 ** 3);
printf("2 ** 3 ** 2 == %d\n", 2 ** 3 ** 2);

$a = 2;
$a **= 3;
printf("a ==           %d\n", $a);
?>

   
```

El ejemplo anterior mostrará:

    2 ** 3 ==      8
    2 ** 3 ** 2 == 512
    a ==           8

## `use function` y `use const`

El operador [`use`](#language.namespaces.importing) se ha extendido para admitir la importación de funciones y constantes, además de clases. Esto se hace usando las construcciones `use function` y `use const`, respectivamente.

```php
<?php
namespace Name\Space {
    const FOO = 42;
    function f() { echo __FUNCTION__."\n"; }
}

namespace {
    use const Name\Space\FOO;
    use function Name\Space\f;

    echo FOO."\n";
    f();
}
?>

   
```

El ejemplo anterior mostrará:

    42
    Name\Space\f

## phpdbg

PHP ahora incluye un depurador interactivo llamado phpdbg, implementado como un módulo SAPI. Para obtener más información, véase la [documentación de phpdbg](#book.phpdbg).

## Codificación de caracteres predeterminada

[default_charset](#ini.default-charset) ahora se usa como el conjunto de caracteres predeterminado para las funciones `htmlentities`, `html_entity_decode` y `htmlspecialchars`. Se debe tener en cuenta que si las configuraciones de codificación (ahora obsoletas) de iconv y mbstring están definidas, estas tendrán prioridad sobre la configuración de default_charset para las funciones iconv y mbstring, respectivamente.

El valor predeterminado para esta configuración es `UTF-8`.

## [`php://input`](#wrappers.php.input) es reutilizable

[`php://input`](#wrappers.php.input) ahora se puede volver a abrir y leer tantas veces como sea necesario. Este nuevo mecanismo también ha permitido reducir significativamente la cantidad de memoria requerida durante las operaciones POST.

## Subida de archivos grandes

Ahora se aceptan archivos de más de 2 Gigabytes.

## [GMP](#book.gmp) soporta la sobrecarga de operadores

Los objetos [GMP](#book.gmp) ahora soportan la sobrecarga de operadores y el cambio de tipo a tipos escalares. Esto permite un código más expresivo usando GMP:

```php
<?php
$a = gmp_init(42);
$b = gmp_init(17);

if (version_compare(PHP_VERSION, '5.6', '<')) {
    echo gmp_intval(gmp_add($a, $b)), PHP_EOL;
    echo gmp_intval(gmp_add($a, 17)), PHP_EOL;
    echo gmp_intval(gmp_add(42, $b)), PHP_EOL;
} else {
    echo $a + $b, PHP_EOL;
    echo $a + 17, PHP_EOL;
    echo 42 + $b, PHP_EOL;
}
?>

   
```

El ejemplo anterior mostrará:

    59
    59
    59

## `hash_equals` para la comparación de `string` para evitar ataques de temporización

Se ha añadido la función `hash_equals` para comparar dos `string` en tiempo constante. Esto debería usarse para evitar ataques de temporización, por ejemplo, al probar el hash de una contraseña creada vía la función `crypt` (suponiendo que no pueda usar las funciones `password_hash` y `password_verify`, que no son sensibles a los ataques de temporización).

```php
<?php
$expected  = crypt('12345', '$2a$07$usesomesillystringforsalt$');
$correct   = crypt('12345', '$2a$07$usesomesillystringforsalt$');
$incorrect = crypt('1234',  '$2a$07$usesomesillystringforsalt$');

var_dump(hash_equals($expected, $correct));
var_dump(hash_equals($expected, $incorrect));
?>

   
```

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

## `__debugInfo()`

Se ha añadido el método mágico [\_\_debugInfo()](#language.oop5.magic.debuginfo) para permitir a los objetos cambiar las propiedades y valores que se muestran cuando el objeto se muestra usando la función `var_dump`.

```php
<?php
class C {
    private $prop;

    public function __construct($val) {
        $this->prop = $val;
    }

    public function __debugInfo() {
        return [
            'propSquared' => $this->prop ** 2,
        ];
    }
}

var_dump(new C(42));
?>

   
```

El ejemplo anterior mostrará:

    object(C)#1 (1) {
      ["propSquared"]=>
      int(1764)
    }

## Algoritmo de hashing gost-crypto

Se ha añadido el algoritmo de hashing `gost-crypto`. Implementa la función de hashing GOST, usando las tablas CryptoPro S-box como se especifica en la [RFC 4357, sección 11.2](https://datatracker.ietf.org/doc/html/rfc4357).

## Mejoras SSL/TLS

Se han realizado diversas mejoras en el soporte SSL/TLS en PHP 5.6. Esto incluye [la activación de forma predeterminada de la verificación de pares](#migration56.incompatible.peer-verification), el soporte para la coincidencia de huellas digitales de certificados, la mitigación de ataques de renegociación TLS, así como varias nuevas [opciones de contexto SSL](#context.ssl) que permiten un control mucho más granular sobre la configuración del protocolo y la verificación al usar flujos cifrados.

Estos cambios se describen en detalle en la sección sobre los [cambios OpenSSL en PHP 5.6.x](#migration56.openssl) de la guía de migración.

## Soporte async [pgsql](#book.pgsql)

La extensión [pgsql](#book.pgsql) ahora soporta conexiones y consultas asíncronas, habilitando un comportamiento no bloqueante al interactuar con una base de datos PostgreSQL. Las conexiones asíncronas pueden establecerse vía la constante `PGSQL_CONNECT_ASYNC`, y las nuevas funciones `pg_connect_poll`, `pg_socket`, `pg_consume_input` y `pg_flush` pueden ser usadas para manejar las conexiones y consultas asíncronas.
