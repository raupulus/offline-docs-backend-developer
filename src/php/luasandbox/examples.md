---
title: Ejemplos
source_url: https://www.php.net/manual/es/luasandbox.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/luasandbox/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: luasandbox
translation_status: ready
translation_reviewed: false
translation_revision: 9c40251a8
order: 43900
---

## Ejemplos

## Uso básico de LuaSandbox

Una vez que se ha compilado PHP con soporte para LuaSandbox, se puede comenzar a utilizar LuaSandbox para ejecutar de manera segura el código Lua proporcionado por el usuario.

Ejecutar código Lua

```php
<?php

$sandbox = new LuaSandbox;
$sandbox->setMemoryLimit( 50 * 1024 * 1024 );
$sandbox->setCPULimit( 10 );

// Registrar algunas funciones en el entorno Lua

function frobnosticate( $v ) {
    return [ $v + 42 ];
}

$sandbox->registerLibrary( 'php', [
    'frobnosticate' => 'frobnosticate',
    'output' => function ( $string ) {
        echo "$string\n";
    },
    'error' => function () {
        throw new LuaSandboxRuntimeError( "Something is wrong" );
    }
] );

// Ejecutar código Lua, incluyendo funciones de retrollamada en PHP y en Lua

$luaCode = <<<EOF
php.output( "Hello, world" );

return "Hi", function ( v )
    return php.frobnosticate( v + 200 )
end
EOF;

list( $hi, $frob ) = $sandbox->loadString( $luaCode )->call();
assert( $frob->call( 4000 ) === [ 4242 ] );

// Las excepciones LuaSandboxRuntimeError lanzadas por PHP pueden ser capturadas en PHP

list( $ok, $message ) = $sandbox->loadString( 'return pcall( php.error )' )->call();
assert( !$ok );
assert( $message === 'Something is wrong' );

?>

   
```
