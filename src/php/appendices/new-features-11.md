---
title: Nuevas características
source_url: https://www.php.net/manual/es/migration84.new-features.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration84/new-features.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: d7efc6755
order: 1130
---

## Nuevas características

## Núcleo de PHP

### Hooks de propiedad

Las propiedades de los objetos pueden ahora tener lógica adicional asociada con sus operaciones `get` y `set`. Dependiendo del uso, esto puede hacer que la propiedad sea virtual, es decir, no tenga ningún valor de respaldo.

```php
<?php
class Person
{
    // Una propiedad "virtual". No puede ser establecida explícitamente.
    public string $fullName {
        get => $this->firstName . ' ' . $this->lastName;
    }

    // Todas las operaciones de escritura pasan por este hook, y el resultado es lo que se escribe.
    // El acceso de lectura ocurre normalmente.
    public string $firstName {
        set => ucfirst(strtolower($value));
    }

    // Todas las operaciones de escritura pasan por este hook, que debe escribir en el valor de respaldo.
    // El acceso de lectura ocurre normalmente.
    public string $lastName {
        set {
            if (strlen($value) < 2) {
                throw new \InvalidArgumentException('Too short');
            }
            $this->lastName = $value;
        }
    }
}

$p = new Person();

$p->firstName = 'peter';
print $p->firstName; // Imprime "Peter"
$p->lastName = 'Peterson';
print $p->fullName; // Imprime "Peter Peterson"

$p->fullName = "Peter 'Pete' Peterson"; // Lanza Error: "Property Person::$fullName is read-only"

    
```

### Visibilidad Asimétrica de Propiedades

Las propiedades de los objetos pueden ahora tener su visibilidad `set` controlada por separado de la visibilidad `get`.

```php
<?php
class Example
{
    // El primer modificador de visibilidad controla la visibilidad de get, y el segundo modificador
    // controla la visibilidad de set. La visibilidad de get no debe ser más estrecha que la visibilidad de set.
    public protected(set) string $name;

    public function __construct(string $name)
    {
        $this->name = $name;
    }
}

    
```

### Objetos Lazy

Ahora es posible crear objetos cuya inicialización se difiere hasta que sean accedidos. Las bibliotecas y frameworks pueden aprovechar estos objetos lazy para diferir la obtención de datos o dependencias requeridas para la inicialización.

```php
<?php
class Example
{
    public function __construct(private int $data)
    {
    }

    // ...
}

$initializer = static function (Example $ghost): void {
    // Obtener datos o dependencias
    $data = getData();
    // Inicializar
    $ghost->__construct($data);
};

$reflector = new ReflectionClass(Example::class);
$object = $reflector->newLazyGhost($initializer);

    
```

### Atributo `#[\Deprecated]`

El nuevo atributo `Deprecated` puede ser utilizado para marcar funciones, métodos, y constantes de clase como obsoletas. El comportamiento de la funcionalidad obsoleta con este atributo coincide con el comportamiento del mecanismo de obsolescencia existente para la funcionalidad proporcionada por PHP mismo. La única excepción es que el código de error emitido es `E_USER_DEPRECATED` en lugar de `E_DEPRECATED`.

Las obsolescencias existentes en la funcionalidad proporcionada por PHP mismo han sido actualizadas para usar el atributo, mejorando los mensajes de error emitidos al incluir una breve explicación.

### Analizando solicitudes RFC1867 (multipart) en solicitudes HTTP no-POST

Se añadió la función `request_parse_body` que permite analizar solicitudes RFC1867 (multipart) en solicitudes HTTP no-POST.

### Encadenando expresiones [`new`](#language.oop5.basic.new) sin paréntesis

Las nuevas expresiones con argumentos de constructor son ahora desreferenciables, lo que significa que permiten encadenar llamadas a métodos, accesos a propiedades, etc., sin encerrar la expresión entre paréntesis.

### Información de Depuración Mejorada para `WeakReference`

Obtener la información de depuración para `WeakReference` ahora también mostrará el objeto al que hace referencia, o `null` si la referencia ya no es válida.

### Información de Depuración Mejorada para `Closure`

La salida de Closure::\_\_debugInfo ahora incluye el nombre, archivo y línea del `Closure`.

### Definiendo Símbolos Idénticos en Diferentes Bloques de Espacios de Nombres

Salir de un espacio de nombres ahora limpia los símbolos vistos. Esto permite usar un símbolo en un bloque de espacio de nombres, incluso si un bloque de espacio de nombres anterior declaró un símbolo con el mismo nombre.

## cURL

`curl_version` devuelve un valor adicional `feature_list`, que es un array asociativo de todas las características conocidas de cURL, y si están soportadas (`true`) o no (`false`).

Se añadieron las constantes `CURL_HTTP_VERSION_3` y `CURL_HTTP_VERSION_3ONLY` (disponibles desde libcurl 7.66 y 7.88) como opciones disponibles para `CURLOPT_HTTP_VERSION`.

Se añadió `CURLOPT_PREREQFUNCTION` como una opción de cURL que acepta un `callable` para ser llamado después de que se realice la conexión, pero antes de que se envíe la solicitud. Este callable debe devolver `CURL_PREREQFUNC_OK` o `CURL_PREREQFUNC_ABORT` para permitir o abortar la solicitud.

Se añadió `CURLOPT_SERVER_RESPONSE_TIMEOUT`, que anteriormente era conocido como `CURLOPT_FTP_RESPONSE_TIMEOUT`. Ambas constantes tienen el mismo valor.

Se añadió `CURLOPT_DEBUGFUNCTION` como una opción de cURL que acepta un `callable` que se llama durante la vida de la solicitud con el objeto `CurlHandle`, un entero que contiene el tipo de mensaje de depuración, y un string que contiene el mensaje de depuración. El tipo de mensaje de depuración es uno de las siguientes constantes: `CURLINFO_TEXT`, `CURLINFO_HEADER_IN`, `CURLINFO_HEADER_OUT`, `CURLINFO_DATA_IN`, `CURLINFO_DATA_OUT`, `CURLINFO_SSL_DATA_IN`, `CURLINFO_SSL_DATA_OUT` Una vez que se establece esta opción, `CURLINFO_HEADER_OUT` no debe ser establecido porque usa la misma funcionalidad de libcurl.

La función `curl_getinfo` ahora devuelve una clave adicional `posttransfer_time_us`, que contiene el número de microsegundos desde el inicio hasta que se envía el último byte. Cuando se sigue una redirección, el tiempo de cada solicitud se suma. Este valor también puede ser recuperado pasando `CURLINFO_POSTTRANSFER_TIME_T` al parámetro `option` de la función `curl_getinfo`. Esto requiere libcurl 8.10.0 o posterior.

## DOM

Se añadió el espacio de nombres Dom con nuevas clases como contrapartes a las clases DOM existentes (por ejemplo, `Dom\Node` es el nuevo `DOMNode`). Estas clases son compatibles con HTML 5 y cumplen con la especificación WHATWG; resolviendo errores de larga data en la extensión DOM. Las clases DOM antiguas permanecen disponibles para compatibilidad con versiones anteriores.

Se añadió el método DOMNode::compareDocumentPosition con sus constantes asociadas: `DOMNode::DOCUMENT_POSITION_DISCONNECTED`, `DOMNode::DOCUMENT_POSITION_PRECEDING`, `DOMNode::DOCUMENT_POSITION_FOLLOWING`, `DOMNode::DOCUMENT_POSITION_CONTAINS`, `DOMNode::DOCUMENT_POSITION_CONTAINED_BY`, `DOMNode::DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC`

Ahora es posible pasar cualquier callable a DOMXPath::registerPhpFunctions. Además, con DOMXPath::registerPhpFunctionNs, ahora se pueden registrar callbacks que usarán la sintaxis de llamada a función nativa en lugar de usar `php:function('name')`.

## Intl

Se añadió la constante `NumberFormatter::ROUND_HALFODD` para complementar la funcionalidad existente de `NumberFormatter::ROUND_HALFEVEN`.

## OpenSSL

Se añadió soporte para claves basadas en Curve25519 + Curve448. Específicamente, los campos x25519, ed25519, x448 y ed448 son soportados en `openssl_pkey_new`, `openssl_pkey_get_details`, `openssl_sign`, y `openssl_verify` fueron extendidos para soportar esas claves.

Implementar el hashing de contraseñas PASSWORD_ARGON2. Requiere OpenSSL 3.2 y compilación NTS.

## PCRE

La biblioteca pcre2lib incluida ha sido actualizada a la versión 10.44. Como consecuencia, se añadió soporte para JIT en LoongArch, ahora se permiten espacios entre llaves en elementos compatibles con Perl, y se soportan ahora las aserciones de lookbehind de longitud variable.

Con la versión 10.44 de pcre2lib, la longitud máxima de los grupos de captura nombrados ha cambiado de `32` a `128`.

Se añadió soporte para el modificador `r` (PCRE2_EXTRA_CASELESS_RESTRICT), así como el modificador de modo `(?r)`. Cuando se habilita junto con el modificador insensible a mayúsculas y minúsculas (`i`), la expresión bloquea la mezcla de caracteres ASCII y no ASCII.

## PDO

Se añadió soporte para subclases específicas del controlador para soportar mejor las funcionalidades específicas de la base de datos. Las nuevas clases pueden ser instanciadas llamando al método PDO::connect o instanciando una de las subclases específicas del controlador directamente.

Se añadió soporte para analizadores SQL específicos del controlador. Cuando un analizador específico del controlador no está disponible, se usa el analizador predeterminado. El analizador predeterminado soporta: literales entre comillas simples y dobles, con duplicación como mecanismo de escape, comentarios de dos guiones y comentarios de estilo C no anidados

## PDO_MYSQL

Se añadió un analizador personalizado que soporta: literales entre comillas simples y dobles, con duplicación y barra invertida como mecanismo de escape, identificadores de literales con comillas invertidas y con duplicación como mecanismo de escape, dos guiones seguidos de al menos 1 espacio en blanco, comentarios de estilo C no anidados, y comentarios de hash

## PDO_PGSQL

Se añadió un analizador personalizado que soporta: literales entre comillas simples y dobles, con duplicación como mecanismo de escape, literales de string de "escape" de estilo C (`E'string'`), literales de string entre comillas de dólar, dos guiones y comentarios de estilo C (no anidados), soporte para `??` como secuencia de escape para el operador `?`

## PDO_SQLITE

Se añadió un analizador personalizado que soporta: literales entre comillas simples, dobles y comillas invertidas, con duplicación como mecanismo de escape, comillas de corchetes para identificadores, dos guiones y comentarios de estilo C (no anidados)

## Phar

Se añadió soporte para la extensión Unix timestamp para archivos Zip.

## Readline

Se añadió la capacidad de cambiar la ruta `.php_history` a través de la variable de entorno `PHP_HISTFILE`.

## Reflection

`ReflectionAttribute` ahora contiene una propiedad name para mejorar la experiencia de depuración.

ReflectionClassConstant::\_\_toString y ReflectionProperty::\_\_toString ahora devuelven los comentarios doc adjuntos.

Se han añadido múltiples nuevos métodos y constantes relacionados con la característica de objetos lazy: ReflectionClass::newLazyGhost, ReflectionClass::newLazyProxy, ReflectionClass::resetAsLazyGhost, ReflectionClass::resetAsLazyProxy, ReflectionClass::isUninitializedLazyObject, ReflectionClass::initializeLazyObject, ReflectionClass::markLazyObjectAsInitialized, ReflectionClass::getLazyInitializer, ReflectionProperty::skipLazyInitialization, ReflectionProperty::setRawValueWithoutLazyInitialization, `ReflectionClass::SKIP_INITIALIZATION_ON_SERIALIZE`, `ReflectionClass::SKIP_DESTRUCTOR`

## SOAP

Se añadió soporte para la notación clark para espacios de nombres en el mapa de clases. Ahora es posible especificar entradas en un mapa de clases con notación clark para resolver un tipo con un espacio de nombres específico a una clase específica. Por ejemplo: `'{http://example.com}foo' => 'FooClass'`.

Las instancias de DateTimeInterface que se pasan a `xsd:datetime` o elementos similares ahora se serializan como tales en lugar de ser serializadas como un string vacío.

La persistencia de la sesión ahora funciona con un módulo de sesión compartida.

## Estándar

Se añadió un nuevo enum `RoundingMode` con un nombre más claro y una mejor capacidad de descubrimiento en comparación con las constantes `PHP_ROUND_*`. Además, se añadieron cuatro nuevos modos de redondeo que solo están disponibles a través de el nuevo enum `RoundingMode`.

## XSL

Ahora es posible usar parámetros que contengan tanto comillas simples como dobles.

Ahora es posible pasar cualquier callable a XSLTProcessor::registerPhpFunctions.

Se añadieron XSLTProcessor::\$maxTemplateDepth y XSLTProcessor::\$maxTemplateVars para controlar la profundidad de recursión de la evaluación de plantillas XSL.

## Zip

Se añadió la constante `ZipArchive::ER_TRUNCATED_ZIP`, que fue añadida en libzip 1.11.
