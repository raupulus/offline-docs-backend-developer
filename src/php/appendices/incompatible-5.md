---
title: Cambios incompatibles con versiones anteriores
source_url: https://www.php.net/manual/es/migration73.incompatible.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration73/incompatible.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 620
---

## Cambios incompatibles con versiones anteriores

## Núcleo de PHP

### Interpretación de las Etiquetas de Terminación Heredoc/Nowdoc

Con la introducción de [la sintaxis flexible heredoc / nowdoc](#migration73.new-features.core.heredoc), los `string` doc que contienen la etiqueta de terminación en su cuerpo pueden causar errores de sintaxis o cambiar en interpretación. Por ejemplo en :

```php
<?php
$str = <<<FOO
abcdefg
   FOO
FOO;
?>

     
```

la ocurrencia indentada de `FOO` no tenía significado particular anteriormente. Ahora será interpretada como el final de la `string` heredoc y el `FOO;` siguiente causará un error de sintaxis. Este problema puede siempre ser resuelto eligiendo una etiqueta de terminación que no aparezca en el contenido de la `string`.

### Continue apuntando a Switch genera Advertencias

Las declaraciones `continue` apuntando a las estructuras de flujo de control `switch` generarán ahora una advertencia. En PHP estas declaraciones `continue` son equivalentes a `break`, mientras que se comportan como `continue 2` en otros lenguajes.

```php
<?php
while ($foo) {
    switch ($bar) {
      case "baz":
         continue;
         // Advertencia: "continue" apuntando a switch es equivalente a
         //          "break". ¿Quiso decir "continue 2"?
   }
}
?>

     
```

### Interpretación Estricta de las Claves de Cadenas de Caracteres Enteros en ArrayAccess

Los accesos de `array` del tipo `$obj["123"]`, donde `$obj` implementa `ArrayAccess` y `"123"` es una `string` de `int` literal ya no resultarán en una conversión implícita a `int`, es decir, `$obj->offsetGet("123")` será llamado en lugar de `$obj->offsetGet(123)`. Esto corresponde al comportamiento para los no literales. El comportamiento de los `array` no se ve afectado de ninguna manera, continúan convirtiendo implícitamente claves de `string` a `int`.

### Las Propiedades Estáticas ya no se Separan por la Asignación de Referencia

En PHP, las propiedades estáticas se comparten entre las clases heredadas, a menos que la propiedad estática sea explícitamente reemplazada en una clase hija. Sin embargo, debido a un artefacto de implementación, era posible separar las propiedades estáticas asignando una referencia. Esta laguna ha sido corregida.

```php
<?php
class Test {
    public static $x = 0;
}
class Test2 extends Test { }

Test2::$x = &$x;
$x = 1;

var_dump(Test::$x, Test2::$x);
// Anteriormente: int(0), int(1)
// Ahora:        int(1), int(1)
?>

     
```

### Las referencias devueltas por los arrays y los accesos a las propiedades son inmediatamente descomprimidas

Las referencias devueltas por los arrays y los accesos a las propiedades son ahora descomprimidas en el contexto del acceso. Esto significa que ya no es posible modificar la referencia entre el acceso y el uso del valor accedido:

```php
<?php
$arr = [1];
$ref =& $arr[0];
var_dump($arr[0] + ($arr[0] = 2));
// Anteriormente: int(4), Ahora: int(3)
?>

     
```

Esto hace que el comportamiento de las referencias y no referencias sea coherente. Es de notar que leer y escribir un valor dentro de una única expresión continúa siendo un comportamiento no definido y puede cambiar nuevamente en el futuro.

### La descompresión de argumentos de Traversables con claves no enteras ya no es soportada

La descompresión de argumentos ha dejado de funcionar con `Traversable`s con claves no enteras El siguiente código funcionaba en PHP 5.6-7.2 por accidente.

```php
<?php
function foo(...$args) {
    var_dump($args);
}
function gen() {
    yield 1.23 => 123;
}
foo(...gen());
?>

     
```

### Diversos

La utilidad `ext_skel` ha sido completamente repensada con nuevas opciones y algunas opciones antiguas eliminadas. Esto ahora está escrito en PHP y no tiene ninguna dependencia externa.

El soporte para BeOS ha sido abandonado.

Las excepciones lanzadas debido a una conversión automática de advertencias en excepciones con el modo `EH_THROW` (por ejemplo, algunas excepciones de `DateTime`) ya no llenan el estado de `error_get_last`. Como tales, ahora funcionan de la misma manera que las excepciones lanzadas manualmente.

`TypeError` ahora reporta los tipos incorrectos como `int` y `bool` en lugar de `integer` y `boolean`, respectivamente.

Las variables indefinidas pasadas a `compact` serán ahora reportadas con una notificación.

`getimagesize` y las funciones conexas ahora reportan el tipo MIME de las imágenes BMP como `image/bmp` en lugar de `image/x-ms-bmp`, ya que el primero ha sido registrado con la IANA (ver [RFC 7903](https://datatracker.ietf.org/doc/html/rfc7903)).

`stream_socket_get_name` ahora devuelve las direcciones IPv6 con corchetes. Por ejemplo, `"[::1]:1337"` será devuelto en lugar de `"::1:1337"`.

## BCMath: matemáticas de precisión arbitraria

Todas las advertencias lanzadas por las [funciones BCMath](#ref.bc) ahora utilizan el gestor de errores de PHP. Anteriormente, algunas advertencias se escribían directamente a stderr.

`bcmul` y `bcpow` ahora devuelven los números con la precisión solicitada. Anteriormente, algunos números podían omitir los ceros decimales finales.

## IMAP, POP3 y NNTP

Las autenticaciones `rsh`/`ssh` están deshabilitadas por defecto. Utilice [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) si desea activarlas. Es de notar que la biblioteca IMAP no filtra los nombres de las carpetas antes de pasarlos a los comandos `rsh`/`ssh`, por lo que pasar datos no fiables a esta función con `rsh`/`ssh` activado es peligroso.

## Cadenas de caracteres multioctetos

Debido al soporte de capturas nombradas, las máscaras `mb_ereg_*()` que utilizan capturas nombradas se comportarán de manera diferente. En particular, las capturas nombradas formarán parte de las coincidencias y `mb_ereg_replace` interpretará la sintaxis adicional. Ver [Capturas Nombradas](#migration73.new-features.mbstring.named-captures) para más información.

## Extensión MySQL Mejorada (MySQLi)

Las declaraciones preparadas ahora reportan las fracciones de segundo para las columnas `DATETIME`, `TIME` y `TIMESTAMP` con especificador decimal (por ejemplo `TIMESTAMP(6)` al usar microsegundos). Anteriormente, las fracciones de segundo eran simplemente omitidas de los valores de retorno.

## Funciones MySQL (PDO_MYSQL)

Las declaraciones preparadas ahora reportan las fracciones de segundo para las columnas `DATETIME`, `TIME` y `TIMESTAMP` con especificador decimal (por ejemplo `TIMESTAMP(6)` al usar microsegundos). Anteriormente, las fracciones de segundo eran simplemente omitidas de los valores de retorno. Tenga en cuenta que esto solo afecta el uso de [PDO_MYSQL](#ref.pdo-mysql) con las declaraciones preparadas emuladas desactivadas (por ejemplo, utilizando la funcionalidad nativa de preparación). Las declaraciones que utilizan conexiones que tienen `PDO::ATTR_EMULATE_PREPARES`=`true` (que es por defecto) no se ven afectadas por la corrección de error y ya recuperaban los valores de las fracciones de segundo del motor.

## Reflection

Las exportaciones de [Reflection](#book.reflection) en `string` ahora utilizan `int` y `bool` en lugar de `integer` y `boolean`, respectivamente.

## Biblioteca Estándar de PHP (SPL)

Si un autocargador [SPL](#book.spl) lanza una excepción, los autocargadores siguientes no serán ejecutados. Anteriormente, todos los autocargadores eran ejecutados y las excepciones eran encadenadas.

## SimpleXML

Las operaciones matemáticas que implican los objetos [SimpleXML](#book.simplexml) tratarán ahora el texto como un `int` o un `float`, según lo que sea más apropiado. Anteriormente, los valores eran tratados como un `int` sin condición.

## Cookies entrantes

Desde PHP 7.3.23, los *nombres* de las cookies entrantes ya no se decodifican por URL por razones de seguridad.
