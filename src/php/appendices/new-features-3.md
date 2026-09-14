---
title: Nuevas características
source_url: https://www.php.net/manual/es/migration71.new-features.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration71/new-features.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: d987f5fea
order: 480
---

## Nuevas características

## Tipos nullables

La declaración de los tipos de parámetro y de valor de retorno ahora se puede marcar como nullable prefijando el nombre del tipo con un signo de interrogación. Esto significa que tanto el tipo especificado como `null` se pueden pasar como argumento, o devolver como valor, respectivamente.

```php
<?php

function testReturnA(): ?string
{
    return 'elePHPant';
}

var_dump(testReturnA());

function testReturnB(): ?string
{
    return null;
}

var_dump(testReturnB());

function test(?string $name)
{
    var_dump($name);
}

test('elePHPant');
test(null);
test();

   
```

El ejemplo anterior mostrará:

    string(9) "elePHPant"
    NULL
    string(9) "elePHPant"
    NULL
    Fatal error: Uncaught ArgumentCountError: Too few arguments to function test(), 0 passed in...

## Funciones void

Se ha introducido el tipo de retorno `void`. Las funciones declaradas con un tipo de retorno void deben omitir la declaración de retorno completamente, o utilizar una declaración de retorno vacía. `null` no es un tipo de retorno válido para una función void.

```php
<?php
function swap(&$left, &$right): void
{
    if ($left === $right) {
        return;
    }

    $tmp = $left;
    $left = $right;
    $right = $tmp;
}

$a = 1;
$b = 2;
var_dump(swap($a, $b), $a, $b);

   
```

El ejemplo anterior mostrará:

    null
    int(2)
    int(1)

Intentar utilizar el valor de retorno de una función void simplemente evalúa a `null`, sin advertencia emitida. La razón para esto es que una advertencia implicaría el uso de una función genérica de orden superior.

## Desestructuración simétrica de arrays

La abreviatura de la sintaxis array `[]` ahora se puede utilizar para desestructurar arrays en asignaciones (incluyendo dentro de `foreach`), en lugar de la sintaxis existente `list`, que se sigue admitiendo.

```php
<?php
$data = [
    [1, 'Tom'],
    [2, 'Fred'],
];

// list() style
list($id1, $name1) = $data[0];

// [] style
[$id1, $name1] = $data[0];

// list() style
foreach ($data as list($id, $name)) {
    // lógica aquí con $id y $name
}

// [] style
foreach ($data as [$id, $name]) {
    // lógica aquí con $id y $name
}

   
```

## Visibilidad de las constantes de clase

Se ha añadido soporte para especificar la visibilidad de las constantes de clase.

```php
<?php
class ConstDemo
{
    const PUBLIC_CONST_A = 1;
    public const PUBLIC_CONST_B = 2;
    protected const PROTECTED_CONST = 3;
    private const PRIVATE_CONST = 4;
}

   
```

## El pseudo-tipo `iterable`

Se ha introducido un nuevo pseudo-tipo (similar a `callable`) llamado `iterable`. Se puede utilizar con los parámetros y retornos tipados, donde acepta arrays u objetos que implementan la interfaz `Traversable`. En cuanto a la subtipificación, los tipos de parámetros de las clases hijas pueden ampliar una declaración de un padre de `array` o `Traversable` en `iterable`. Con los tipos de retorno, las clases hijas pueden restringir el tipo de retorno `iterable` del padre en `array` o un objeto que implemente `Traversable`.

```php
<?php
function iterator(iterable $iter)
{
    foreach ($iter as $val) {
        //
    }
}

   
```

## Captura de múltiples excepciones (Multi-catch)

Ahora pueden especificarse múltiples excepciones por bloque catch utilizando el carácter barra vertical (`|`). Esto es útil cuando diferentes excepciones se manejan de la misma manera.

```php
<?php
try {
    // código
} catch (FirstException | SecondException $e) {
    // maneja las excepciones first y second
}

   
```

## Soporte de claves en `list`

Ahora es posible especificar claves en `list`, o su nueva sintaxis abreviada `[]`. Esto permite la desestructuración de arrays que tienen claves no enteras o no secuenciales.

```php
<?php
$data = [
    ["id" => 1, "name" => 'Tom'],
    ["id" => 2, "name" => 'Fred'],
];

// list() style
list("id" => $id1, "name" => $name1) = $data[0];

// [] style
["id" => $id1, "name" => $name1] = $data[0];

// list() style
foreach ($data as list("id" => $id, "name" => $name)) {
    // lógica aquí con $id y $name
}

// [] style
foreach ($data as ["id" => $id, "name" => $name]) {
    // lógica aquí con $id y $name
}

   
```

## Soporte para índices de string negativos

Se ha añadido soporte para índices de string negativos a las [funciones de manipulación de strings](#book.strings) que aceptan una posición, así como a la [indexación de strings](#language.types.string.substr) con `[]` o `{}`. En tales casos, un índice negativo se interpreta como un desplazamiento desde el final del string.

```php
<?php
var_dump("abcdef"[-2]);
var_dump(strpos("aabbcc", "b", -3));

   
```

El ejemplo anterior mostrará:

    string (1) "e"
    int(3)

Los desplazamientos de string negativos también se admiten con la sintaxis simple de análisis en strings.

```php
<?php
$string = 'bar';
echo "El último carácter de '$string' es '$string[-1]'.\n";
?>

   
```

El ejemplo anterior mostrará:

    El último carácter de 'bar' es 'r'.

## Soporte para AEAD en ext/openssl

Se ha añadido soporte para AEAD (modos GCM y CCM) ampliando las funciones `openssl_encrypt` y `openssl_decrypt` con parámetros adicionales.

## Convertir callables en `Closure`s con Closure::fromCallable

Se ha introducido un nuevo método estático en la clase `Closure` para permitir que los `callable`s se conviertan fácilmente en objetos `Closure`.

```php
<?php
class Test
{
    public function exposeFunction()
    {
        return Closure::fromCallable([$this, 'privateFunction']);
    }

    private function privateFunction($param)
    {
        var_dump($param);
    }
}

$privFunc = (new Test)->exposeFunction();
$privFunc('some value');

   
```

El ejemplo anterior mostrará:

    string(10) "some value"

## Gestión de señales asíncronas

Se ha introducido una nueva función llamada `pcntl_async_signals` para permitir la gestión de señales asíncronas sin utilizar los ticks (lo que introducía mucho sobrecosto).

```php
<?php
pcntl_async_signals(true); // activar las señales asíncronas

pcntl_signal(SIGHUP,  function($sig) {
    echo "SIGHUP\n";
});

posix_kill(posix_getpid(), SIGHUP);

   
```

El ejemplo anterior mostrará:

    SIGHUP

## Soporte para HTTP/2 Server Push en ext/curl

Se ha añadido soporte para HTTP/2 Server Push a la extensión cURL (requiere la versión 7.46 o posterior). Esto se puede aprovechar a través de la función `curl_multi_setopt` con la nueva constante `CURLMOPT_PUSHFUNCTION`. También se han añadido las constantes `CURL_PUSH_OK` y `CURL_PUSH_DENY` para que se pueda aprobar o rechazar la ejecución de la función de retrollamada de HTTP/2 Server Push.

## Opciones del contexto de flujo (Stream Context Options)

Se ha añadido la opción del contexto de flujo [tcp_nodelay](#context.socket.tcp_nodelay).
