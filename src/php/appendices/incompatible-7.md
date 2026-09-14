---
title: Cambios incompatibles hacia atrás
source_url: https://www.php.net/manual/es/migration80.incompatible.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration80/incompatible.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: b94d63fc0
order: 790
---

## Cambios incompatibles hacia atrás

## Núcleo de PHP

### Comparación de cadenas con números

Las comparaciones no estrictas entre números y cadenas no numéricas ahora funcionan convirtiendo el número a cadena y comparando las cadenas. Las comparaciones entre números y cadenas numéricas continúan funcionando como antes. En particular, esto significa que `0 == "not-a-number"` ahora se considera falso.

| Comparación     | Antes  | Después |
|-----------------|--------|---------|
| `0 == "0"`      | `true` | `true`  |
| `0 == "0.0"`    | `true` | `true`  |
| `0 == "foo"`    | `true` | `false` |
| `0 == ""`       | `true` | `false` |
| `42 == " 42"`   | `true` | `true`  |
| `42 == "42foo"` | `true` | `false` |

### Otros cambios incompatibles

- `match` es ahora una palabra reservada.

- `mixed` ahora es una palabra reservada, por lo que no puede ser utilizada para nombrar una clase, interfaz o trait, y tampoco está permitida en espacios de nombres.

- Los fallos de aserción ahora lanzan una excepción por defecto. Si se desea el comportamiento anterior, se puede establecer `assert.exception=0` en la configuración INI.

- Los métodos con el mismo nombre que la clase ya no se interpretan como constructores. Se debe usar el método [\_\_construct()](#object.construct) en su lugar.

- La posibilidad de llamar a métodos no estáticos de forma estática ha sido eliminada. Por lo tanto, `is_callable` fallará al verificar un método no estático con un nombre de clase (se debe verificar con una instancia de objeto).

- Las conversiones `(real)` y `(unset)` han sido eliminadas.

- La directiva ini [track_errors](#ini.track-errors) ha sido eliminada. Esto significa que `php_errormsg` ya no está disponible. Se puede usar la función `error_get_last` en su lugar.

- La posibilidad de definir constantes insensibles a mayúsculas y minúsculas ha sido eliminada. El tercer argumento de `define` ya no puede ser `true`.

- La posibilidad de especificar un autocargador utilizando una función `__autoload` ha sido eliminada. Se debe usar `spl_autoload_register` en su lugar.

- El argumento `errcontext` ya no se pasará a los manejadores de errores personalizados establecidos con `set_error_handler`.

- `create_function` ha sido eliminada. Se pueden usar funciones anónimas en su lugar.

- `each` ha sido eliminada. Se debe usar [`foreach`](#control-structures.foreach) o `ArrayIterator` en su lugar.

- La posibilidad de desvincular `this` de closures que fueron creadas a partir de un método, utilizando Closure::fromCallable o ReflectionMethod::getClosure, ha sido eliminada.

- La posibilidad de desvincular `this` de closures propias que contienen usos de `this` también ha sido eliminada.

- La posibilidad de usar `array_key_exists` con objetos ha sido eliminada. Se puede usar `isset` o `property_exists` en su lugar.

- El comportamiento de `array_key_exists` en relación con el tipo del parámetro `key` se ha hecho consistente con `isset` y el acceso normal a arrays. Todos los tipos de clave ahora usan las coerciones habituales y las claves de tipo array/object lanzan un `TypeError`.

- Cualquier array que tenga un número \<n\> como su primera clave numérica usará \<n+1\> para su siguiente clave implícita, incluso si \<n\> es negativo.

- El nivel predeterminado de error_reporting es ahora `E_ALL`. Anteriormente excluía `E_NOTICE` y `E_DEPRECATED`.

- [display_startup_errors](#ini.display-startup-errors) está ahora habilitado por defecto.

- Usar `parent` dentro de una clase que no tiene padre ahora resultará en un error fatal en tiempo de compilación.

- El operador `@` ya no silenciará los errores fatales (`E_ERROR`, `E_CORE_ERROR`, `E_COMPILE_ERROR`, `E_USER_ERROR`, `E_RECOVERABLE_ERROR`, `E_PARSE`). Los manejadores de errores que esperan que error_reporting sea `0` cuando se usa `@`, deben ajustarse para usar una verificación de máscara en su lugar:

```php
  <?php
  // Reemplazar
  function my_error_handler($err_no, $err_msg, $filename, $linenum) {
      if (error_reporting() == 0) {
          return; // Silenciado
      }
      // ...
  }

  // Por
  function my_error_handler($err_no, $err_msg, $filename, $linenum) {
      if (!(error_reporting() & $err_no)) {
          return; // Silenciado
      }
      // ...
  }
  ?>

        
  ```

  Además, se debe tener cuidado de que los mensajes de error no se muestren en entornos de producción, lo que puede resultar en fugas de información. Es necesario asegurarse de que `display_errors=Off` se use junto con el registro de errores.

- `#[` ya no se interpreta como el inicio de un comentario, ya que esta sintaxis ahora se usa para atributos.

- Los errores de herencia debidos a firmas de métodos incompatibles (violaciones de LSP) ahora siempre generarán un error fatal. Anteriormente se generaba una advertencia en algunos casos.

- La precedencia del operador de concatenación ha cambiado en relación con los desplazamientos de bits y la suma, así como la resta.

```php
  <?php
  echo "Sum: " . $a + $b;
  // anteriormente se interpretaba como:
  echo ("Sum: " . $a) + $b;
  // ahora se interpreta como:
  echo "Sum:" . ($a + $b);
  ?>

        
  ```

- Los argumentos con un valor predeterminado que se resuelve a `null` en tiempo de ejecución ya no marcarán implícitamente el tipo del argumento como nullable. Se debe usar un tipo nullable explícito o un valor predeterminado `null` explícito en su lugar.

```php
  <?php
  // Reemplazar
  function test(int $arg = CONST_RESOLVING_TO_NULL) {}
  // Por
  function test(?int $arg = CONST_RESOLVING_TO_NULL) {}
  // O
  function test(int $arg = null) {}
  ?>

        
  ```

- Varias advertencias se han convertido en excepciones `Error`:

  Intentar escribir en una propiedad de un no-objeto. Anteriormente esto creaba implícitamente un objeto stdClass para null, false y cadenas vacías., Intentar agregar un elemento a un array cuya clave PHP_INT_MAX ya está en uso., Intentar usar un tipo no válido (array u objeto) como clave de array u offset de cadena., Intentar escribir en un índice de array de un valor escalar., Intentar desempaquetar un valor que no es array/Traversable., Intentar acceder a constantes no calificadas que no están definidas. Anteriormente, el acceso a constantes no calificadas resultaba en una advertencia y se interpretaban como cadenas., Pasar un número incorrecto de argumentos a una función interna no variádica lanzará un `ArgumentCountError`., Pasar tipos no contables inválidos a `count` lanzará un `TypeError`.

  Varios avisos se han convertido en advertencias:

  Intentar leer una variable no definida., Intentar leer una propiedad no definida., Intentar leer una clave de array no definida., Intentar leer una propiedad de un no-objeto., Intentar acceder a un índice de array de un no-array., Intentar convertir un array a cadena., Intentar usar un recurso como clave de array., Intentar usar null, un booleano o un flotante como offset de cadena., Intentar leer un offset de cadena fuera de los límites., Intentar asignar una cadena vacía a un offset de cadena.

- Intentar asignar múltiples bytes a un offset de cadena ahora emitirá una advertencia.

- Los caracteres inesperados en los archivos fuente (como bytes NUL fuera de las cadenas) ahora resultarán en una excepción `ParseError` en lugar de una advertencia de compilación.

- Las excepciones no capturadas ahora pasan por un "cierre limpio", lo que significa que los destructores se llamarán después de una excepción no capturada.

- El error fatal en tiempo de compilación "Only variables can be passed by reference" se ha pospuesto hasta el tiempo de ejecución y se ha convertido en una excepción `Error` "Argument cannot be passed by reference".

- Algunos avisos "Only variables should be passed by reference" se han convertido en la excepción "Argument cannot be passed by reference".

- El nombre generado para las clases anónimas ha cambiado. Ahora incluirá el nombre de la primera clase padre o interfaz:

```php
  <?php
  new class extends ParentClass {};
  // -> ParentClass@anonymous
  new class implements FirstInterface, SecondInterface {};
  // -> FirstInterface@anonymous
  new class {};
  // -> class@anonymous
  ?>

        
  ```

  El nombre mostrado arriba todavía va seguido de un byte NUL y un sufijo único.

- Las referencias a métodos de trait no absolutas en las adaptaciones de alias de trait ahora deben ser inequívocas:

```php
  <?php
  class X {
      use T1, T2 {
          func as otherFunc;
      }
      function func() {}
  }
  ?>

        
  ```

  Si tanto `T1::func()` como `T2::func()` existen, este código era aceptado silenciosamente antes, y se asumía que func se refería a `T1::func`. Ahora generará un error fatal en su lugar, y se debe escribir explícitamente `T1::func` o `T2::func`.

- La firma de los métodos abstractos definidos en traits ahora se verifica contra el método de la clase que los implementa:

```php
  <?php
  trait MyTrait {
      abstract private function neededByTrait(): string;
  }

  class MyClass {
      use MyTrait;

      // Error, debido a la incompatibilidad del tipo de retorno.
      private function neededByTrait(): int { return 42; }
  }
  ?>

        
  ```

- Las funciones deshabilitadas ahora se tratan exactamente como funciones inexistentes. Llamar a una función deshabilitada la reportará como desconocida, y redefinir una función deshabilitada ahora es posible.

- Los envoltorios de flujo `data://` ya no son escribibles, lo que coincide con el comportamiento documentado.

- Los operadores aritméticos y a nivel de bits `+`, `-`, `*`, `/`, `**`, `%`, `<<`, `>>`, `&`, `|`, `^`, `~`, `++`, `--` ahora lanzarán consistentemente un `TypeError` cuando uno de los operandos sea un `array`, `resource` u `object` no sobrecargado. La única excepción a esto es la operación de fusión de arrays `+`, que sigue siendo soportada.

- La conversión de flotante a cadena ahora siempre se comportará de manera independiente de la configuración regional.

```php
  <?php
  setlocale(LC_ALL, "de_DE");
  $f = 3.14;
  echo $f, "\n";
  // Anteriormente: 3,14
  // Ahora:         3.14
  ?>

        
  ```

  Véase `printf`, `number_format` y NumberFormatter para formas de personalizar el formato de números.

- El soporte para el acceso a offsets con llaves (obsoleto) ha sido eliminado.

```php
  <?php
  // En lugar de:
  $array{0};
  $array{"key"};
  // Escribir:
  $array[0];
  $array["key"];
  ?>

        
  ```

- Aplicar el modificador final en un método privado ahora producirá una advertencia a menos que ese método sea el constructor.

- Si el constructor de un objeto llama a `exit`, el destructor del objeto ya no se llamará. Esto coincide con el comportamiento cuando el constructor lanza una excepción.

- Los nombres con espacio de nombres ya no pueden contener espacios en blanco: Mientras que `Foo\Bar` se reconocerá como un nombre con espacio de nombres, `Foo \ Bar` no. Por el contrario, las palabras reservadas ahora están permitidas como segmentos de espacio de nombres, lo que también puede cambiar la interpretación del código: `new\x` ahora es lo mismo que `constant('new\x')`, no `new \x()`.

- Los ternarios anidados ahora requieren paréntesis explícitos.

- `debug_backtrace` y Exception::getTrace ya no proporcionarán referencias a los argumentos. No será posible cambiar los argumentos de una función a través del backtrace.

- El manejo de cadenas numéricas ha sido modificado para ser más intuitivo y menos propenso a errores. Los espacios en blanco finales ahora se permiten en cadenas numéricas por consistencia con la forma en que se tratan los espacios en blanco iniciales. Esto afecta principalmente a:

  La función `is_numeric`, Comparaciones de cadena a cadena, Declaraciones de tipo, Operaciones de incremento y decremento

  El concepto de "cadena numéricamente inicial" ha sido mayormente eliminado; los casos donde esto se mantiene existen para facilitar la migración. Las cadenas que emitían un `E_NOTICE` "A non well-formed numeric value encountered" ahora emitirán un `E_WARNING` "A non-numeric value encountered" y todas las cadenas que emitían un `E_WARNING` "A non-numeric value encountered" ahora lanzarán un `TypeError`. Esto afecta principalmente a:

  Operaciones aritméticas, Operaciones a nivel de bits

  Este cambio de `E_WARNING` a `TypeError` también afecta al `E_WARNING` "Illegal string offset 'string'" para offsets de cadena ilegales. El comportamiento de las conversiones explícitas a int/float desde cadenas no ha cambiado.

- Los métodos mágicos ahora tendrán sus argumentos y tipos de retorno verificados si los tienen declarados. Las firmas deben coincidir con la siguiente lista:

  `__call(string $name, array $arguments): mixed`, `__callStatic(string $name, array $arguments): mixed`, `__clone(): void`, `__debugInfo(): ?array`, `__get(string $name): mixed`, `__invoke(mixed $arguments): mixed`, `__isset(string $name): bool`, `__serialize(): array`, `__set(string $name, mixed $value): void`, `__set_state(array $properties): object`, `__sleep(): array`, `__unserialize(array $data): void`, `__unset(string $name): void`, `__wakeup(): void`

- Las claves de array de `call_user_func_array` ahora se interpretarán como nombres de parámetros, en lugar de ser silenciosamente ignoradas.

- Declarar una función llamada `assert()` dentro de un espacio de nombres ya no está permitido y emite `E_COMPILE_ERROR`. La función `assert` está sujeta a un tratamiento especial por parte del motor, lo que puede llevar a un comportamiento inconsistente al definir una función con espacio de nombres con el mismo nombre.

## Migración de recursos a objetos

Varios `resource`s han sido migrados a `object`s. Las comprobaciones de valores de retorno que utilizan `is_resource` deben ser reemplazadas por comprobaciones de `false`.

- `curl_init` ahora devolverá un objeto `CurlHandle` en lugar de un `resource`. La función `curl_close` ya no tiene efecto; en su lugar, la instancia de `CurlHandle` se destruye automáticamente si ya no es referenciada.

- `curl_multi_init` ahora devolverá un objeto `CurlMultiHandle` en lugar de un `resource`. La función `curl_multi_close` ya no tiene efecto; en su lugar, la instancia de `CurlMultiHandle` se destruye automáticamente si ya no es referenciada.

- `curl_share_init` ahora devolverá un objeto `CurlShareHandle` en lugar de un `resource`. La función `curl_share_close` ya no tiene efecto; en su lugar, la instancia de `CurlShareHandle` se destruye automáticamente si ya no es referenciada.

- `enchant_broker_init` ahora devolverá un objeto `EnchantBroker` en lugar de un `resource`.

- `enchant_broker_request_dict` y `enchant_broker_request_pwl_dict` ahora devolverán un objeto `EnchantDictionary` en lugar de un `resource`.

- La extensión GD ahora utiliza objetos `GdImage` como estructura de datos subyacente para las imágenes, en lugar de `resource`s. La función `imagedestroy` ya no tiene efecto; en su lugar, la instancia de `GdImage` se destruye automáticamente si ya no es referenciada.

- `openssl_x509_read` y `openssl_csr_sign` ahora devolverán un objeto `OpenSSLCertificate` en lugar de un `resource`. La función `openssl_x509_free` está obsoleta y ya no tiene efecto; en su lugar, la instancia de `OpenSSLCertificate` se destruye automáticamente si ya no es referenciada.

- `openssl_csr_new` ahora devolverá un objeto `OpenSSLCertificateSigningRequest` en lugar de un `resource`.

- `openssl_pkey_new` ahora devolverá un objeto `OpenSSLAsymmetricKey` en lugar de un `resource`. La función `openssl_pkey_free` está obsoleta y ya no tiene efecto; en su lugar, la instancia de `OpenSSLAsymmetricKey` se destruye automáticamente si ya no es referenciada.

- `shmop_open` ahora devolverá un objeto `Shmop` en lugar de un `resource`. La función `shmop_close` ya no tiene efecto, y está obsoleta; en su lugar, la instancia de `Shmop` se destruye automáticamente si ya no es referenciada.

- `socket_create`, `socket_create_listen`, `socket_accept`, `socket_import_stream`, `socket_addrinfo_connect`, `socket_addrinfo_bind` y `socket_wsaprotocol_info_import` ahora devolverán un objeto `Socket` en lugar de un `resource`. `socket_addrinfo_lookup` ahora devolverá un array de objetos `AddressInfo` en lugar de `resource`s.

- `msg_get_queue` ahora devolverá un objeto `SysvMessageQueue` en lugar de un `resource`.

- `sem_get` ahora devolverá un objeto `SysvSemaphore` en lugar de un `resource`.

- `shm_attach` ahora devolverá un objeto `SysvSharedMemory` en lugar de un `resource`.

- `xml_parser_create` y `xml_parser_create_ns` ahora devolverán un objeto `XMLParser` en lugar de un `resource`. La función `xml_parser_free` ya no tiene efecto; en su lugar, la instancia de XMLParser se destruye automáticamente si ya no es referenciada.

- Las funciones de [XMLWriter](#book.xmlwriter) ahora aceptan y devuelven, respectivamente, objetos `XMLWriter` en lugar de `resource`s.

- `inflate_init` ahora devolverá un objeto `InflateContext` en lugar de un `resource`.

- `deflate_init` ahora devolverá un objeto `DeflateContext` en lugar de un `resource`.

## COM y .Net (Windows)

La capacidad de importar constantes que no distinguen entre mayúsculas y minúsculas desde bibliotecas de tipos ha sido eliminada. El segundo argumento de `com_load_typelib` ya no puede ser false; [com.autoregister_casesensitive](#ini.com.autoregister-casesensitive) ya no puede ser deshabilitado; los marcadores que no distinguen entre mayúsculas y minúsculas en [com.typelib_file](#ini.com.typelib-file) son ignorados.

## CURL

`CURLOPT_POSTFIELDS` ya no acepta objetos como arrays. Para interpretar un objeto como un array, se debe realizar una conversión explícita con `(array)`. Lo mismo aplica para otras opciones que aceptan arrays.

## Date y Time

`mktime` y `gmmktime` ahora requieren al menos un argumento. Se puede utilizar `time` para obtener la marca de tiempo actual.

## DOM

Las clases no implementadas de la extensión DOM que no tenían comportamiento y contenían datos de prueba han sido eliminadas. Estas clases también han sido eliminadas en la última versión del estándar DOM:

`DOMNameList`, `DomImplementationList`, `DOMConfiguration`, `DomError`, `DomErrorHandler`, `DOMImplementationSource`, `DOMLocator`, `DOMUserDataHandler`, `DOMTypeInfo`, `DOMStringExtend`

Los métodos no implementados de la extensión DOM que no tenían comportamiento han sido eliminados:

DOMNamedNodeMap::setNamedItem, DOMNamedNodeMap::removeNamedItem, DOMNamedNodeMap::setNamedItemNS, DOMNamedNodeMap::removeNamedItemNS, DOMText::replaceWholeText, DOMNode::compareDocumentPosition, DOMNode::isEqualNode, DOMNode::getFeature, DOMNode::setUserData, DOMNode::getUserData, DOMDocument::renameNode

## Enchant

- `enchant_broker_list_dicts`, `enchant_broker_describe` y `enchant_dict_suggest` ahora devolverán un array vacío en lugar de `null`.

## Exif

`read_exif_data` ha sido eliminada; debe usarse `exif_read_data` en su lugar.

## Filtro

- Las flags `FILTER_FLAG_SCHEME_REQUIRED` y `FILTER_FLAG_HOST_REQUIRED` del filtro `FILTER_VALIDATE_URL` han sido eliminadas. El `scheme` y el `host` son (y han sido) siempre requeridos.

- Las fuentes `INPUT_REQUEST` e `INPUT_SESSION` para `filter_input` etc. han sido eliminadas. Nunca fueron implementadas y su uso siempre generaba una advertencia.

## GD

- La función obsoleta `image2wbmp` ha sido eliminada.

- Las funciones obsoletas `png2wbmp` y `jpeg2wbmp` han sido eliminadas.

- El parámetro `mode` predeterminado de `imagecropauto` ya no acepta `-1`. Debe usarse `IMG_CROP_DEFAULT` en su lugar.

- En Windows, `php_gd2.dll` ha sido renombrado a `php_gd.dll`.

## GMP

`gmp_random` ha sido eliminada. Debe usarse `gmp_random_range` o `gmp_random_bits` en su lugar.

## Iconv

Las implementaciones de iconv que no establecen correctamente `errno` en caso de errores ya no son soportadas.

## IMAP

- El argumento no utilizado `default_host` de `imap_headerinfo` ha sido eliminado.

- La función `imap_header`, que es un alias de `imap_headerinfo`, ha sido eliminada.

## Funciones de internacionalización

- La constante obsoleta `INTL_IDNA_VARIANT_2003` ha sido eliminada.

- La constante obsoleta `Normalizer::NONE` ha sido eliminada.

## LDAP

- Las funciones obsoletas `ldap_sort`, `ldap_control_paged_result` y `ldap_control_paged_result_response` han sido eliminadas.

- La interfaz de `ldap_set_rebind_proc` ha cambiado; el parámetro `callback` ya no acepta cadenas vacías; debe usarse `null` en su lugar.

## MBString

- La directiva [mbstring.func_overload](#ini.mbstring.func-overload) ha sido eliminada. Las constantes relacionadas `MB_OVERLOAD_MAIL`, `MB_OVERLOAD_STRING` y `MB_OVERLOAD_REGEX` también han sido eliminadas. Finalmente, las entradas `"func_overload"` y `"func_overload_list"` en `mb_get_info` han sido eliminadas.

- `mb_parse_str` ya no puede usarse sin especificar un array de resultados.

- Se han eliminado varios alias obsoletos de mbregex. Consulte la siguiente lista para saber qué funciones deben usarse en su lugar:

  `mbregex_encoding` → `mb_regex_encoding`, `mbereg` → `mb_ereg`, `mberegi` → `mb_eregi`, `mbereg_replace` → `mb_ereg_replace`, `mberegi_replace` → `mb_eregi_replace`, `mbsplit` → `mb_split`, `mbereg_match` → `mb_ereg_match`, `mbereg_search` → `mb_ereg_search`, `mbereg_search_pos` → `mb_ereg_search_pos`, `mbereg_search_regs` → `mb_ereg_search_regs`, `mbereg_search_init` → `mb_ereg_search_init`, `mbereg_search_getregs` → `mb_ereg_search_getregs`, `mbereg_search_getpos` → `mb_ereg_search_getpos`, `mbereg_search_setpos` → `mb_ereg_search_setpos`

- El modificador `e` para `mb_ereg_replace` ha sido eliminado. Debe usarse `mb_ereg_replace_callback` en su lugar.

- Un argumento de patrón que no sea una cadena para `mb_ereg_replace` ahora será interpretado como una cadena en lugar de un punto de código ASCII. El comportamiento anterior puede restaurarse con una llamada explícita a `chr`.

- El argumento `needle` para `mb_strpos`, `mb_strrpos`, `mb_stripos`, `mb_strripos`, `mb_strstr`, `mb_stristr`, `mb_strrchr` y `mb_strrichr` ahora puede estar vacío.

- El parámetro `is_hex`, que no se utilizaba internamente, ha sido eliminado de `mb_decode_numericentity`.

- El comportamiento heredado de pasar la codificación como tercer argumento en lugar de un desplazamiento para la función `mb_strrpos` ha sido eliminado; en su lugar, debe proporcionarse un desplazamiento explícito de `0` con la codificación como cuarto argumento.

- Los alias de codificación de caracteres `ISO_8859-*` han sido reemplazados por los alias `ISO8859-*` para una mejor interoperabilidad con la extensión iconv. Los alias de mbregex ISO 8859 con guiones bajos (`ISO_8859_*` y `ISO8859_*`) también han sido eliminados.

- `mb_ereg` y `mb_eregi` ahora devolverán `true` booleano en una coincidencia exitosa. Anteriormente devolvían el entero `1` si no se pasaba `matches`, o `max(1, strlen($matches[0]))` si se pasaba `matches`.

## OCI8

- La clase `OCI-Lob` ahora se llama `OCILob`, y la clase `OCI-Collection` ahora se llama `OCICollection` para el cumplimiento de nombres impuesto por las herramientas de anotación de tipos arginfo de PHP 8.

- Varias funciones alias han sido marcadas como obsoletas.

- `oci_internal_debug` y su alias `ociinternaldebug` han sido eliminados.

## ODBC

- `odbc_connect` ya no reutiliza las conexiones.

- El parámetro no utilizado `flags` de `odbc_exec` ha sido eliminado.

## OpenSSL

- `openssl_seal` y `openssl_open` ahora requieren que se pase el parámetro `method`, ya que el valor predeterminado anterior de `"RC4"` se considera inseguro.

## Expresiones regulares (compatibles con Perl)

Al pasar secuencias de escape no válidas, estas ya no se interpretan como literales. Este comportamiento requería anteriormente el modificador `X`, que ahora se ignora.

## PHP Data Objects

- El modo de gestión de errores predeterminado ha sido cambiado de "silent" a "exceptions". Consulte [Errores y gestión de errores](#pdo.error-handling) para más detalles.

- Las firmas de algunos métodos de PDO han cambiado:

  `PDO::query(string $query, ?int $fetchMode = null, mixed ...$fetchModeArgs)`, `PDOStatement::setFetchMode(int $mode, mixed ...$args)`

## PDO ODBC

La directiva `php.ini` [pdo_odbc.db2_instance_name](#ini.pdo-odbc.db2-instance-name) ha sido eliminada.

## PDO MySQL

PDO::inTransaction ahora informa del estado real de la transacción de la conexión, en lugar de una aproximación mantenida por PDO. Si se ejecuta una consulta sujeta a "implicit commit", PDO::inTransaction devolverá posteriormente `false`, ya que la transacción ya no está activa.

## PostgreSQL

- La sintaxis obsoleta de `pg_connect` que utiliza múltiples parámetros en lugar de una cadena de conexión ya no es compatible.

- La firma obsoleta de `pg_lo_import` y `pg_lo_export` que pasa la conexión como último argumento ya no es compatible. La conexión debe pasarse como primer argumento.

- `pg_fetch_all` ahora devuelve un array vacío en lugar de `false` para conjuntos de resultados con cero filas.

## Phar

Los metadatos asociados a un phar ya no se deserializan automáticamente, para corregir posibles vulnerabilidades de seguridad debidas a la instanciación de objetos, la carga automática, etc.

## Reflection

- Las firmas de los métodos

  `ReflectionClass::newInstance($args)`, `ReflectionFunction::invoke($args)`, `ReflectionMethod::invoke($object, $args)`

  han sido cambiadas a:

  `ReflectionClass::newInstance(...$args)`, `ReflectionFunction::invoke(...$args)`, `ReflectionMethod::invoke($object, ...$args)`

  El código que debe ser compatible tanto con PHP 7 como con PHP 8 puede utilizar las siguientes firmas para ser compatible con ambas versiones:

  `ReflectionClass::newInstance($arg = null, ...$args)`, `ReflectionFunction::invoke($arg = null, ...$args)`, `ReflectionMethod::invoke($object, $arg = null, ...$args)`

- El método ReflectionType::\_\_toString ahora devuelve una representación completa de depuración del tipo y ya no está obsoleto. En particular, el resultado incluirá un indicador de nulabilidad para los tipos anulables. El formato del valor de retorno no es estable y puede cambiar entre versiones de PHP.

- Los métodos export() de Reflection han sido eliminados. En su lugar, los objetos de reflexión pueden ser convertidos a string.

- ReflectionMethod::isConstructor y ReflectionMethod::isDestructor ahora también devuelven `true` para los métodos [\_\_construct()](#object.construct) y [\_\_destruct()](#object.destruct) de las interfaces. Anteriormente, esto solo era cierto para los métodos de clases y traits.

- El método ReflectionType::isBuiltin ha sido movido a `ReflectionNamedType`. `ReflectionUnionType` no lo tiene.

## Sockets

- Las constantes obsoletas `AI_IDN_ALLOW_UNASSIGNED` y `AI_IDN_USE_STD3_ASCII_RULES` del parámetro `flags` de `socket_addrinfo_lookup` han sido eliminadas.

## Standard PHP Library (SPL)

- SplFileObject::fgetss ha sido eliminado.

- SplFileObject::seek ahora siempre se posiciona al inicio de la línea. Anteriormente, las posiciones `=1` se posicionaban al inicio de la línea siguiente.

- SplHeap::compare ahora especifica una firma de método. Las clases herederas que implementen este método deben utilizar una firma de método compatible.

- SplDoublyLinkedList::push, SplDoublyLinkedList::unshift y SplQueue::enqueue ahora devuelven `void` en lugar de `true`.

- `spl_autoload_register` ahora siempre lanza un `TypeError` con argumentos no válidos, por lo que el segundo argumento `do_throw` se ignora y se emitirá un aviso si se establece a `false`.

- `SplFixedArray` ahora es un IteratorAggregate y no un Iterator. SplFixedArray::rewind, SplFixedArray::current, SplFixedArray::key, SplFixedArray::next y SplFixedArray::valid han sido eliminados. En su lugar, se ha añadido SplFixedArray::getIterator. Todo código que utilice iteración explícita sobre SplFixedArray debe obtener ahora un Iterator a través de SplFixedArray::getIterator. Esto significa que `SplFixedArray` ahora es seguro de usar en bucles anidados.

## Biblioteca estándar

- `assert` ya no evaluará argumentos de tipo string, en su lugar se tratarán como cualquier otro argumento. Se debe usar `assert($a == $b)` en lugar de `assert('$a == $b')`. La directiva ini [assert.quiet_eval](#ini.assert.quiet-eval) y la constante `ASSERT_QUIET_EVAL` también han sido eliminadas, ya que no tendrían ningún efecto.

- `parse_str` ya no puede utilizarse sin especificar un array de resultados.

- El filtro [string.strip_tags](#filters.string.strip_tags) ha sido eliminado.

- El argumento `needle` de `strpos`, `strrpos`, `stripos`, `strripos`, `strstr`, `strchr`, `strrchr` y `stristr` ahora siempre se interpretará como un string. Anteriormente, los needle que no eran string se interpretaban como un punto de código ASCII. Se puede usar una llamada explícita a `chr` para restaurar el comportamiento anterior.

- El argumento `needle` de `strpos`, `strrpos`, `stripos`, `strripos`, `strstr`, `stristr` y `strrchr` ahora puede estar vacío.

- El argumento `length` de `substr`, `substr_count`, `substr_compare` y `iconv_substr` ahora puede ser `null`. Los valores `null` se comportarán como si no se hubiera proporcionado el argumento de longitud y, por lo tanto, devolverán el resto del string en lugar de un string vacío.

- El argumento `length` de `array_splice` ahora puede ser `null`. Los valores `null` se comportarán de forma idéntica a omitir el argumento, eliminando así todo desde el `offset` hasta el final del array.

- El argumento `args` de `vsprintf`, `vfprintf` y `vprintf` ahora debe ser un array. Anteriormente se aceptaba cualquier tipo.

- La opción `'salt'` de `password_hash` ya no es compatible. Si se usa la opción `'salt'`, se genera una advertencia, la sal proporcionada se ignora y se usa una sal generada automáticamente.

- La función `quotemeta` ahora devuelve un string vacío si se le pasa un string vacío. Anteriormente se devolvía `false`.

- Las siguientes funciones han sido eliminadas:

  `hebrevc`, `convert_cyr_string`, `money_format`, `ezmlm_hash`, `restore_include_path`, `get_magic_quotes_gpc`, `get_magic_quotes_runtime`, `fgetss`

- `FILTER_SANITIZE_MAGIC_QUOTES` ha sido eliminada.

- Llamar a `implode` con los parámetros en orden inverso `($pieces, $glue)` ya no es compatible.

- `parse_url` ahora distingue las consultas y fragmentos ausentes de los vacíos:

  `http://example.com/foo → query = null, fragment = null`, `http://example.com/foo? → query = "", fragment = null`, `http://example.com/foo# → query = null, fragment = ""`, `http://example.com/foo?# → query = "", fragment = ""` Anteriormente, en todos los casos, query y fragment eran `null`.

- `var_dump` y `debug_zval_dump` ahora muestran los números de punto flotante utilizando [serialize_precision](#ini.serialize-precision) en lugar de [precision](#ini.precision). En una configuración predeterminada, esto significa que los números de punto flotante ahora se muestran con total precisión por estas funciones de depuración.

- Si el array devuelto por [\_\_sleep()](#object.sleep) contiene propiedades inexistentes, estas ahora se ignoran silenciosamente. Anteriormente, tales propiedades se habrían serializado como si tuvieran el valor `null`.

- La configuración regional predeterminada al inicio ahora es siempre `"C"`. Ninguna configuración regional se hereda del entorno de forma predeterminada. Anteriormente, `LC_ALL` se establecía en `"C"`, mientras que `LC_CTYPE` se heredaba del entorno. Sin embargo, algunas funciones no respetaban la configuración regional heredada sin una llamada explícita a `setlocale`. Ahora siempre se requiere una llamada explícita a `setlocale` si se desea cambiar un componente de la configuración regional respecto al valor predeterminado.

- El respaldo obsoleto DES en `crypt` ha sido eliminado. Si se pasa un formato de sal desconocido a `crypt`, la función fallará con `*0` en lugar de recurrir a un hash DES débil.

- Especificar rondas fuera de rango para SHA256/SHA512 en `crypt` ahora fallará con `*0` en lugar de ajustar al límite más cercano. Esto coincide con el comportamiento de glibc.

- El resultado de las funciones de ordenación puede haber cambiado si el array contiene elementos que se comparan como iguales.

- Cualquier función que acepte callbacks que no estén especificados explícitamente para aceptar parámetros por referencia ahora emitirá una advertencia si se usa un callback con parámetros por referencia. Los ejemplos incluyen `array_filter` y `array_reduce`. Este ya era el caso para la mayoría, pero no todas, las funciones anteriormente.

- El envolvente de flujo HTTP, tal como lo usan funciones como `file_get_contents`, ahora anuncia HTTP/1.1 en lugar de HTTP/1.0 de forma predeterminada. Esto no cambia el comportamiento del cliente, pero puede hacer que los servidores respondan de manera diferente. Para mantener el comportamiento anterior, se debe establecer la opción de contexto de flujo `'protocol_version'`, p. ej.

```php
  <?php
  $ctx = stream_context_create(['http' => ['protocol_version' => '1.0']]);
  echo file_get_contents('http://example.org', false, $ctx);
  ?>

       
  ```

- Llamar a `crypt` sin una sal explícita ya no es compatible. Para producir un hash fuerte con una sal generada automáticamente, se debe usar `password_hash` en su lugar.

- `substr`, `mb_substr`, `iconv_substr` y `grapheme_substr` ahora ajustan de manera consistente los desplazamientos fuera de los límites al límite del string. Anteriormente, se devolvía `false` en lugar del string vacío en algunos casos.

- En Windows, las funciones de ejecución de programas (`proc_open`, `exec`, `popen`, etc.) que usan el shell, ahora ejecutan de manera consistente `%comspec% /s /c "$commandline"`, lo que tiene el mismo efecto que ejecutar `$commandline` (sin comillas adicionales).

## Sysvsem

- El parámetro `auto_release` de `sem_get` ha sido modificado para aceptar valores bool en lugar de int.

## Tidy

- El parámetro `use_include_path`, que no se usaba internamente, ha sido eliminado de `tidy_repair_string`.

- tidy::repairString y tidy::repairFile se han convertido en métodos estáticos.

## Tokenizer

- Los tokens `T_COMMENT` ya no incluirán un salto de línea al final. El salto de línea será parte del siguiente token `T_WHITESPACE`. Cabe señalar que `T_COMMENT` no siempre va seguido de un espacio en blanco, también puede ir seguido de `T_CLOSE_TAG` o del final del archivo.

- Los nombres con espacio de nombres ahora se representan utilizando los tokens `T_NAME_QUALIFIED` (`Foo\Bar`), `T_NAME_FULLY_QUALIFIED` (`\Foo\Bar`) y `T_NAME_RELATIVE` (`namespace\Foo\Bar`). `T_NS_SEPARATOR` solo se usa para separadores de espacio de nombres independientes, y solo es sintácticamente válido en conjunto con declaraciones de uso de grupo.

## XMLReader

XMLReader::open y XMLReader::xml ahora son métodos estáticos. Todavía pueden llamarse como métodos de instancia, pero las clases herederas deben declararlos como estáticos si sobrescriben estos métodos.

## XML-RPC

La extensión XML-RPC ha sido movida a PECL y ya no forma parte de la distribución de PHP.

## Zip

`ZipArchive::OPSYS_Z_CPM` ha sido eliminada (el nombre era un error tipográfico). Se debe usar `ZipArchive::OPSYS_CPM` en su lugar.

## Zlib

- `gzgetss` ha sido eliminada.

- [zlib.output_compression](#ini.zlib.output-compression) ya no se desactiva automáticamente para `Content-Type: image/*`.

## Paquetes de pruebas de PHP para Windows

El ejecutor de pruebas ha sido renombrado de `run-test.php` a `run-tests.php`, para coincidir con su nombre en php-src.
