---
title: Cambios incompatibles con versiones anteriores
source_url: https://www.php.net/manual/es/migration81.incompatible.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration81/incompatible.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: dfd68fd22
order: 860
---

## Cambios incompatibles con versiones anteriores

## Núcleo de PHP

### Restricciones de acceso a \$GLOBALS

El acceso al array `$GLOBALS` está ahora sujeto a un cierto número de restricciones. El acceso en lectura y en escritura a los elementos individuales del array como `$GLOBALS['var']` continúa funcionando como tal. El acceso en lectura al array completo `$GLOBALS` continúa también siendo soportado. Sin embargo, el acceso en escritura al array completo `$GLOBALS` ya no es soportado. Por ejemplo, `array_pop($GLOBALS)` generará un error.

### Uso de variables static en los métodos heredados.

Cuando un método que utiliza variables static es heredado (pero no sobrescrito), el método heredado compartirá ahora las variables.

```php
<?php
class A {
    public static function counter() {
        static $counter = 0;
        $counter++;
        return $counter;
    }
}
class B extends A {}
var_dump(A::counter()); // int(1)
var_dump(A::counter()); // int(2)
var_dump(B::counter()); // int(3), anteriormente int(1)
var_dump(B::counter()); // int(4), anteriormente int(2)
?>

     
```

Esto significa que las variables estáticas en los métodos se comportan ahora de la misma manera que las propiedades estáticas.

### Parámetros opcionales especificados antes de los parámetros requeridos

Un [parámetro opcional](#functions.arguments.default) especificado antes de los parámetros requeridos es ahora siempre tratado como requerido, incluso cuando se llama utilizando [los argumentos nombrados](#functions.named-arguments). A partir de PHP 8.0.0, pero antes de PHP 8.1.0, el código a continuación emite una nota de deprecación en la definición, pero se ejecuta con éxito cuando se llama. A partir de PHP 8.1.0, se lanza un error de la clase `ArgumentCountError`, como sería el caso cuando se llama con argumentos posicionales.

```php
<?php
function makeyogurt($container = "bowl", $flavour)
{
    return "Making a $container of $flavour yogurt.\n";
}
try
{
    echo makeyogurt(flavour: "raspberry");
}
catch (Error $e)
{
    echo get_class($e), ' - ', $e->getMessage(), "\n";
}
?>

     
```

Resultado del ejemplo anterior en PHP 8.0:

    Deprecated: Required parameter $flavour follows optional parameter $container
     in example.php on line 3
    Making a bowl of raspberry yogurt.

         

Resultado del ejemplo anterior en PHP 8.1:

    Deprecated: Optional parameter $container declared before required parameter
     $flavour is implicitly treated as a required parameter in example.php on line 3
    ArgumentCountError - makeyogurt(): Argument #1 ($container) not passed

Tenga en cuenta que un valor por defecto de `null` puede ser utilizado antes de los parámetros requeridos para especificar un [tipo nullable](#language.types.declarations.nullable), pero el parámetro será siempre requerido.

### Compatibilidad de tipos de retorno con clases internas

La mayoría de los métodos internos no finales requieren ahora que los métodos de sobrecarga declaren un tipo de retorno compatible, de lo contrario se emite una nota de deprecación al validar la herencia. En el caso en que el tipo de retorno no pueda ser declarado para un método de sobrecarga debido a preocupaciones de compatibilidad inter-versión de PHP, un atributo `ReturnTypeWillChange` puede ser añadido para suprimir la nota de deprecación.

### Nuevas palabras clave

`readonly` es ahora una palabra clave. Sin embargo, aún puede ser utilizada como nombre de función.

`never` es ahora una palabra reservada, por lo que no puede ser utilizada para nombrar una clase, una interfaz o un trait, y también está prohibido su uso en los namespaces.

## Migración de recurso a objeto

Varios `resource`s han sido migrados a `object`s. Las verificaciones de valor de retorno utilizando `is_resource` deben ser reemplazadas por verificaciones de `false`.

- Las funciones [FileInfo](#book.fileinfo) aceptan y devuelven ahora objetos `finfo` en lugar de `resource`s `fileinfo`.

- Las funciones [FTP](#book.ftp) aceptan y devuelven ahora objetos `FTP\Connection` en lugar de `resource`s `ftp`.

- Las funciones [IMAP](#book.imap) aceptan y devuelven ahora objetos `IMAP\Connection` en lugar de `resource`s `imap`.

- Las funciones [LDAP](#book.ldap) aceptan y devuelven ahora objetos `LDAP\Connection` en lugar de `resource`s `ldap`.

- Las funciones [LDAP](#book.ldap) aceptan y devuelven ahora objetos `LDAP\Result` en lugar de `resource`s `ldap result`.

- Las funciones [LDAP](#book.ldap) aceptan y devuelven ahora objetos `LDAP\ResultEntry` en lugar de `resource`s `ldap result entry`.

- Las funciones [PgSQL](#book.pgsql) aceptan y devuelven ahora objetos `PgSql\Connection` en lugar de `resource`s `pgsql link`.

- Las funciones [PgSQL](#book.pgsql) aceptan y devuelven ahora objetos `PgSql\Result` en lugar de `resource`s `pgsql result`.

- Las funciones [PgSQL](#book.pgsql) aceptan y devuelven ahora objetos `PgSql\Lob` en lugar de `resource`s `pgsql large object`.

- Las funciones [PSpell](#book.pspell) aceptan y devuelven ahora objetos `PSpell\Dictionary` en lugar de `resource`s `pspell`.

- Las funciones [PSpell](#book.pspell) aceptan y devuelven ahora objetos `PSpell\Config` en lugar de `resource`s `pspell config`.

## MySQLi

`mysqli_fetch_fields`, y `mysqli_fetch_field_direct` devolverán ahora `0` para la max_length. Esta información puede ser calculada iterando sobre el conjunto de resultados, y tomando la longitud máxima. Esto es lo que PHP hacía anteriormente de manera interna.

La opción `MYSQLI_STMT_ATTR_UPDATE_MAX_LENGTH` ya no tiene ningún efecto.

La opción `MYSQLI_STORE_RESULT_COPY_DATA` ya no tiene ningún efecto. Pasar un valor al parámetro `mode` de mysqli::store_result ya no tiene ningún efecto.

mysqli::connect devuelve ahora `true` en lugar de `null` en caso de éxito.

El modo de manejo de errores por defecto ha sido cambiado de "silencioso" a "excepciones". Ver la página [Modo de reporte MySQLi](#mysqli-driver.report-mode) para más detalles sobre lo que esto implica, y cómo definir explícitamente este atributo. Para restaurar el comportamiento anterior, utilice : `mysqli_report(MYSQLI_REPORT_OFF);`

Las clases que extienden mysqli_stmt::execute deben ahora especificar el parámetro opcional adicional.

## MySQLnd

La directiva INIT [mysqlnd.fetch_data_copy](#ini.mysqlnd.fetch_data_copy) ha sido eliminada. Esto no debería resultar en cambios de comportamiento visibles para el usuario.

## OpenSSL

Las claves privadas EC serán ahora exportadas en formato PKCS#8 en lugar del formato tradicional, al igual que todas las demás claves.

`openssl_pkcs7_encrypt` y `openssl_cms_encrypt` utilizarán ahora por defecto AES-128-CBC en lugar de RC2-40. El cifrado RC2-40 es considerado como no seguro y no está habilitado por defecto por OpenSSL 3.

## Objetos de datos PHP

`PDO::ATTR_STRINGIFY_FETCHES` transforma ahora los valores de tipo `bool` en `"0"` o `"1"`. Anteriormente, los `bool` no eran transformados en cadenas.

Llamar a PDOStatement::bindColumn con `PDO::PARAM_LOB` enlazará ahora constantemente un stream de resultado cuando `PDO::ATTR_STRINGIFY_FETCHES` no esté activado. Anteriormente, el resultado era o bien un stream o bien una cadena dependiendo del controlador de base de datos utilizado y del momento en que se realizaba el enlace.

### Controlador MySQL

Los enteros y los flotantes en los conjuntos de resultados serán ahora devueltos utilizando los tipos nativos PHP en lugar de `string`s al utilizar las declaraciones preparadas emuladas. Esto corresponde al comportamiento de las declaraciones preparadas nativas. El comportamiento anterior puede ser restaurado activando la opción `PDO::ATTR_STRINGIFY_FETCHES`.

### Controlador SQLite

Los enteros y los flotantes en los conjuntos de resultados serán ahora devueltos utilizando los tipos PHP. El comportamiento anterior puede ser restaurado activando la opción `PDO::ATTR_STRINGIFY_FETCHES`.

## Phar

Para cumplir con la interfaz ArrayAccess, Phar::offsetUnset y PharData::offsetUnset ya no devuelven un `bool`.

## Estándar

`version_compare` ya no acepta las abreviaciones de operadores no documentadas.

`htmlspecialchars`, `htmlentities`, `htmlspecialchars_decode`, `html_entity_decode`, y `get_html_translation_table` utilizan ahora `ENT_QUOTES | ENT_SUBSTITUTE` en lugar de `ENT_COMPAT` por defecto. Esto significa que `'` es escapado en `&#039;` mientras que anteriormente no se hacía nada. Además, el UTF-8 mal formado será reemplazado por un carácter de sustitución Unicode, en lugar de resultar en una cadena vacía.

`debug_zval_dump` muestra ahora el refcount de las referencias con su refcount, en lugar de simplemente anteponer `&` al valor. Esto modela más precisamente la representación de referencia desde PHP 7.0.

`debug_zval_dump` muestra ahora `interned` en lugar de un refcount ficticio para las cadenas internadas y los arrays inmutables.

## Biblioteca Estándar de PHP (Standard PHP Library o SPL)

`SplFixedArray`, será ahora codificado en JSON como un `array`.
