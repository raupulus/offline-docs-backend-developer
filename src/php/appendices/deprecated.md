---
title: Funcionalidades obsoletas en PHP 5.6.x
source_url: https://www.php.net/manual/es/migration56.deprecated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration56/deprecated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 3e08a8aae
order: 180
---

## Funcionalidades obsoletas en PHP 5.6.x

## Llamada desde un contexto incompatible

Llamar a métodos desde un contexto incompatible ahora está obsoleto y generará un error `E_DEPRECATED` en lugar de un `E_STRICT`. El soporte para estas llamadas se eliminará en una versión futura de PHP.

Un ejemplo de este tipo de llamada es:

```php
<?php
class A {
    function f() { echo get_class($this); }
}

class B {
    function f() { A::f(); }
}

(new B)->f();
?>

   
```

El ejemplo anterior mostrará:

    Deprecated: Non-static method A::f() should not be called statically, assuming $this from incompatible context in - on line 7
    B

## `$HTTP_RAW_POST_DATA` y `always_populate_raw_post_data`

`always_populate_raw_post_data` ahora genera un error `E_DEPRECATED` cuando se rellena la variable `$HTTP_RAW_POST_DATA`. El código nuevo debe usar [`php://input`](#wrappers.php.input) en lugar de `$HTTP_RAW_POST_DATA`, que se eliminará en una versión futura de PHP. Se puede cambiar al nuevo comportamiento (en el cual `$HTTP_RAW_POST_DATA` nunca se define, por lo que no se generará ninguna alerta de nivel `E_DEPRECATED`) configurando `always_populate_raw_post_data` con el valor `-1`.

## Configuración de codificación [iconv](#book.iconv) y [mbstring](#book.mbstring)

Las opciones de configuración de [iconv](#book.iconv) y [mbstring](#book.mbstring) relacionadas con la codificación se han declarado obsoletas en favor de la opción [`default_charset`](#ini.default-charset). Las opciones obsoletas son:

- [`iconv.input_encoding`](#ini.iconv.input-encoding)

- [`iconv.output_encoding`](#ini.iconv.output-encoding)

- [`iconv.internal_encoding`](#ini.iconv.internal-encoding)

- [`mbstring.http_input`](#ini.mbstring.http-input)

- [`mbstring.http_output`](#ini.mbstring.http-output)

- [`mbstring.internal_encoding`](#ini.mbstring.internal-encoding)
