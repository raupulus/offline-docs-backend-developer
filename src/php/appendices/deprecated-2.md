---
title: Funcionalidades obsoletas en PHP 7.0.x
source_url: https://www.php.net/manual/es/migration70.deprecated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration70/deprecated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: a8599f426
order: 280
---

## Funcionalidades obsoletas en PHP 7.0.x

## Constructores de estilo PHP 4

Los constructores de estilo PHP 4 (métodos con el mismo nombre que la clase en la que están definidos) están obsoletos y serán eliminados en el futuro. PHP 7 emite `E_DEPRECATED` si el constructor de estilo PHP 4 es el único constructor definido en la clase. Las clases que implementan un método `__construct` no se ven afectadas por este cambio.

```php
<?php
class foo {
    function foo() {
        echo 'Soy el constructor';
    }
}
?>

   
```

El ejemplo anterior mostrará:

    Deprecated: Methods with the same name as their class will not be constructors in a future version of PHP; foo has a deprecated constructor in example.php on line 3

## Llamadas estáticas a métodos no estáticos

Las llamadas [estáticas](#language.oop5.static) a métodos que no están declarados con la palabra clave `static` están obsoletas y se pueden eliminar en el futuro.

```php
<?php
class foo {
    function bar() {
        echo '¡No soy estático!';
    }
}

foo::bar();
?>

   
```

El ejemplo anterior mostrará:

    Deprecated: Non-static method foo::bar() should not be called statically in - on line 8
    ¡No soy estático!

## La opción salt de la función `password_hash`

La opción salt de la función `password_hash` está obsoleta para evitar que los desarrolladores generen sus propios salts (generalmente no seguros). La función genera criptográficamente un salt seguro en ausencia de un salt proporcionado por el desarrollador. Por lo tanto, generar un salt a medida ya no será necesario.

## La opción `capture_session_meta` del contexto SSL

La opción `capture_session_meta` del contexto SSL está obsoleta. Los metadatos SSL ahora están disponibles a través de la función `stream_get_meta_data`.

## Obsolescencia en [LDAP](#book.ldap)

Las siguientes funciones están obsoletas:

- `ldap_sort`
