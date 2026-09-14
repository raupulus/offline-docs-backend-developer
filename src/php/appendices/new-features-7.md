---
title: Nuevas características
source_url: https://www.php.net/manual/es/migration80.new-features.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration80/new-features.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 497c40ac1
order: 810
---

## Nuevas características

## Núcleo de PHP

### Argumentos nombrados

Se ha añadido soporte para los[Argumentos nombrados](#functions.named-arguments).

### Atributos

Se ha añadido soporte para los [Atributos](#language.attributes).

### Promoción de propiedades en el constructor

Se ha añadido soporte para la [promoción de propiedades en el constructor](#language.oop5.decon.constructor.promotion) (declarar propiedades en la firma del constructor).

### Tipos de unión

Se ha añadido soporte para los [tipos de unión](#language.types.declarations.composite.union).

### Expresión match

Se ha añadido soporte para las [expresiones `match`](#control-structures.match).

### Operador nullsafe

Se ha añadido soporte para el [operador nullsafe](#language.oop5.basic.nullsafe) (`?->`).

### Otras nuevas características

- Se ha añadido la clase [WeakMap](#class.weakmap).

- Se ha añadido la clase `ValueError`.

- Cualquier número de parámetros de función ahora puede ser reemplazado por un argumento variádico, siempre que los tipos sean compatibles. Por ejemplo, el siguiente código ahora está permitido:

```php
  <?php
  class A {
       public function method(int $many, string $parameters, $here) {}
  }
  class B extends A {
       public function method(...$everything) {}
  }
  ?>

        
  ```

- `static` (como en "enlace estático en tiempo de ejecución") ahora puede ser usado como tipo de retorno:

```php
  <?php
  class Test {
       public function create(): static {
            return new static();
       }
  }
  ?>

        
  ```

- Ahora es posible obtener el nombre de la clase de un objeto usando `$object::class`. El resultado es el mismo que `get_class($object)`.

- [`new`](#language.oop5.basic.new) e [`instanceof`](#language.operators.type) ahora pueden ser usados con expresiones arbitrarias, usando `new (expression)(...$args)` y `$obj instanceof (expression)`.

- Se han aplicado algunas correcciones de consistencia en la sintaxis de variables, por ejemplo, escribir `Foo::BAR::$baz` ahora está permitido.

- Se ha añadido la interfaz Stringable, que se implementa automáticamente si una clase define un método [\_\_toString()](#object.tostring).

- Los traits ahora pueden definir métodos privados abstractos. Dichos métodos deben ser implementados por la clase que usa el trait.

- `throw` ahora puede ser usado como una expresión. Esto permite usos como:

```php
  <?php
  $fn = fn() => throw new Exception('Exception in arrow function');
  $user = $session->user ?? throw new Exception('Must have user');

        
  ```

- Ahora se permite una coma final opcional en las listas de parámetros.

```php
  <?php
  function functionWithLongSignature(
      Type1 $parameter1,
      Type2 $parameter2, // <-- This comma is now allowed.
  ) {
  }

        
  ```

- Ahora es posible escribir `catch (Exception)` para capturar una excepción sin almacenarla en una variable.

- Se ha añadido soporte para el tipo `mixed`.

- Los métodos privados declarados en una clase padre ya no imponen ninguna regla de herencia sobre los métodos de una clase hija (con la excepción de los constructores privados finales). El siguiente ejemplo ilustra qué restricciones han sido eliminadas:

```php
  <?php
  class ParentClass {
      private function method1() {}
      private function method2() {}
      private static function method3() {}
      // Throws a warning, as "final" no longer has an effect:
      private final function method4() {}
  }
  class ChildClass extends ParentClass {
      // All of the following are now allowed, even though the modifiers aren't
      // the same as for the private methods in the parent class.
      public abstract function method1() {}
      public static function method2() {}
      public function method3() {}
      public function method4() {}
  }
  ?>

        
  ```

- Se ha añadido `get_resource_id`, que devuelve el mismo valor que `(int) $resource`. Proporciona la misma funcionalidad con una API más clara.

- Se ha añadido `InternalIterator`.

## Fecha y hora

- Se han añadido DateTime::createFromInterface y DateTimeImmutable::createFromInterface.

- Se ha añadido el especificador de formato DateTime `p`, que es igual que `P` pero devuelve `Z` en lugar de `+00:00` para UTC.

## DOM

Se han añadido DOMParentNode y DOMChildNode con nuevas API de recorrido y manipulación.

## Filtro

Se ha añadido `FILTER_VALIDATE_BOOL` como alias de `FILTER_VALIDATE_BOOLEAN`. Se prefiere el nuevo nombre, ya que utiliza el nombre de tipo canónico.

## Enchant

Se han añadido `enchant_dict_add`, `enchant_dict_is_added` y `LIBENCHANT_VERSION`.

## FPM

Se ha añadido una nueva opción `pm.status_listen` que permite obtener el estado desde un endpoint diferente (por ejemplo, un puerto o archivo UDS), lo cual es útil para obtener el estado cuando todos los procesos hijos están ocupados sirviendo peticiones de larga duración.

## Hash

Los objetos `HashContext` ahora pueden ser serializados.

## Funciones de internacionalización

Se han añadido las constantes `IntlDateFormatter::RELATIVE_FULL`, `IntlDateFormatter::RELATIVE_LONG`, `IntlDateFormatter::RELATIVE_MEDIUM` y `IntlDateFormatter::RELATIVE_SHORT`.

## LDAP

Se ha añadido `ldap_count_references`, que devuelve el número de mensajes de referencia en un resultado de búsqueda.

## OPcache

Si la directiva ini opcache.record_warnings está habilitada, OPcache registrará las advertencias en tiempo de compilación y las reproducirá en el siguiente include, incluso si se sirve desde la caché.

## OpenSSL

Se ha añadido soporte para Cryptographic Message Syntax (CMS) ([RFC 5652](https://datatracker.ietf.org/doc/html/rfc5652)) compuesto por funciones para cifrado, descifrado, firma, verificación y lectura. La API es similar a la API de las funciones PKCS \#7 con la adición de nuevas constantes de codificación: `OPENSSL_ENCODING_DER`, `OPENSSL_ENCODING_SMIME` y `OPENSSL_ENCODING_PEM`: `openssl_cms_encrypt` cifra el mensaje en el archivo con los certificados y envía el resultado al archivo proporcionado., `openssl_cms_decrypt` descifra el mensaje S/MIME en el archivo y envía los resultados al archivo proporcionado., `openssl_cms_read` exporta el archivo CMS a un array de certificados PEM., `openssl_cms_sign` firma el mensaje MIME en el archivo con un certificado y una clave y envía el resultado al archivo proporcionado., `openssl_cms_verify` verifica que el bloque de datos está intacto, que el firmante es quien dice ser, y devuelve los certificados de los firmantes.

## Expresiones regulares (compatibles con Perl)

Se ha añadido `preg_last_error_msg`, que devuelve un mensaje legible para el último error PCRE. Complementa a `preg_last_error`, que devuelve un valor entero de enumeración en su lugar.

## Reflexión

- Los siguientes métodos ahora pueden devolver información sobre los valores predeterminados de los parámetros de las funciones internas:

  ReflectionParameter::isDefaultValueAvailable, ReflectionParameter::getDefaultValue, ReflectionParameter::isDefaultValueConstant, ReflectionParameter::getDefaultValueConstantName

## SQLite3

Se han añadido SQLite3::setAuthorizer y las constantes de clase correspondientes para establecer una función de retorno de llamada de usuario que se utilizará para autorizar o no una acción en la base de datos.

## Biblioteca estándar

- Se han añadido `str_contains`, `str_starts_with` y `str_ends_with`, que comprueban si `haystack` contiene, comienza con o termina con `needle`, respectivamente.

- Se ha añadido `fdiv`, que realiza una división de punto flotante según la semántica IEEE 754. La división por cero se considera bien definida y devolverá uno de `Inf`, `-Inf` o `NaN`.

- Se ha añadido `get_debug_type`, que devuelve un tipo útil para mensajes de error. A diferencia de `gettype`, utiliza nombres de tipo canónicos, devuelve nombres de clase para objetos e indica el tipo de recurso para los recursos.

- `printf` y funciones similares ahora soportan los especificadores de formato `%h` y `%H`. Son iguales que `%g` y `%G`, pero siempre usan `"."` como separador decimal, en lugar de determinarlo a través de la configuración regional `LC_NUMERIC`.

- `printf` y funciones similares ahora soportan el uso de `"*"` como ancho o precisión, en cuyo caso el ancho/precisión se pasa como argumento a printf. Esto también permite usar precisión `-1` con `%g`, `%G`, `%h` y `%H`. Por ejemplo, el siguiente código puede usarse para reproducir el formato predeterminado de punto flotante de PHP:

```php
  <?php
  printf("%.*H", (int) ini_get("precision"), $float);
  printf("%.*H", (int) ini_get("serialize_precision"), $float);
  ?>

       
  ```

- `proc_open` ahora soporta descriptores de pseudo-terminal (PTY). Lo siguiente conecta `stdin`, `stdout` y `stderr` al mismo PTY:

```php
  <?php
  $proc = proc_open($command, [['pty'], ['pty'], ['pty']], $pipes);
  ?>

       
  ```

- `proc_open` ahora soporta descriptores de pares de sockets. Lo siguiente conecta un par de sockets distinto a `stdin`, `stdout` y `stderr`:

```php
  <?php
  $proc = proc_open($command, [['socket'], ['socket'], ['socket']], $pipes);
  ?>

       
  ```

  A diferencia de las tuberías, los sockets no sufren problemas de E/S bloqueante en Windows. Sin embargo, no todos los programas pueden funcionar correctamente con sockets stdio.

- Las funciones de ordenamiento ahora son estables, lo que significa que los elementos que se comparan como iguales conservarán su orden original.

- `array_diff`, `array_intersect` y sus variaciones ahora pueden ser usadas con un solo array como argumento. Esto significa que usos como los siguientes ahora son posibles:

```php
  <?php
  // OK even if $excludes is empty:
  array_diff($array, ...$excludes);
  // OK even if $arrays only contains a single array:
  array_intersect(...$arrays);
  ?>

       
  ```

- El parámetro `flag` de `ob_implicit_flush` fue cambiado para aceptar un `bool` en lugar de un `int`.

## Tokenizer

`PhpToken` añade una interfaz basada en objetos al tokenizer. Proporciona una representación más uniforme y ergonómica, siendo al mismo tiempo más eficiente en memoria y más rápida.

## Zip

- La extensión Zip ha sido actualizada a la versión 1.19.1.

- Nuevos ZipArchive::setMtimeName y ZipArchive::setMtimeIndex para establecer la hora de modificación de una entrada.

- Nuevo ZipArchive::registerProgressCallback para proporcionar actualizaciones durante el cierre del archivo.

- Nuevo ZipArchive::registerCancelCallback para permitir la cancelación durante el cierre del archivo.

- Nuevo ZipArchive::replaceFile para reemplazar el contenido de una entrada.

- Nuevo ZipArchive::isCompressionMethodSupported para verificar las características opcionales de compresión.

- Nuevo ZipArchive::isEncryptionMethodSupported para verificar las características opcionales de cifrado.

- Se ha añadido la propiedad `ZipArchive::lastId` para obtener el valor del índice de la última entrada añadida.

- Ahora se pueden verificar los errores después de que un archivo ha sido cerrado usando las propiedades `ZipArchive::status` y `ZipArchive::statusSys`, o el método ZipArchive::getStatusString.

- La opción `'remove_path'` de ZipArchive::addGlob y ZipArchive::addPattern ahora se trata como un prefijo de cadena arbitrario (para mantener la consistencia con la opción `'add_path'`), mientras que anteriormente se trataba como un nombre de directorio.

- Las características opcionales de compresión / cifrado ahora se listan en phpinfo.
