---
title: SoapClient::__construct
description: Constructor SoapClient
source_url: https://www.php.net/manual/es/soapclient.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapclient/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_revision: f309e78f9
order: 75130
---

SoapClient::\_\_construct

Constructor SoapClient

## Descripción

```php
public SoapClient::__construct(string $wsdl, [array $options])
```php

Crea un objeto `SoapClient` para conectarse a un servicio SOAP.

## Parámetros

`wsdl`  
URI del archivo WSDL que describe el servicio, el cual se usa para configurar automáticamente el cliente. Si no se proporciona, el cliente operará en modo no-WSDL.

> [!NOTE]
> Por omisión, el archivo WSDL será almacenado en caché por razones de rendimiento. Para desactivar o configurar este almacenamiento en caché, consulte la sección [SOAP Opciones de configuración](#soap.configuration.list) y la opción [ `cache_wsdl`](#soapclient.construct.options.cache-wsdl)

`options`  
Un array asociativo que especifica opciones adicionales para el cliente SOAP. Si el parámetro `wsdl` se proporciona, esto es opcional; de lo contrario, al menos los parámetros `location` y `url` deben ser proporcionados.

`location` `string`  
La URL del servidor SOAP al que enviar la petición.

Requerido si el parámetro `wsdl` no se proporciona. Si tanto un parámetro `wsdl` como la opción `location` se proporcionan, la opción `location` reemplazará cualquier ubicación especificada en el archivo WSDL.

`uri` `string`  
El espacio de nombres objetivo del servicio SOAP.

Requerido si el parámetro `wsdl` no se proporciona; de lo contrario, se ignora.

`style` `int`  
Especifica el estilo de enlace a utilizar para este cliente, utilizando las constantes `SOAP_RPC` y `SOAP_DOCUMENT`. `SOAP_RPC` indica un enlace de estilo RPC, donde el cuerpo de la petición SOAP contiene un codificado estándar de una llamada de función. `SOAP_DOCUMENT` indica un enlace de estilo documento, donde el cuerpo de la petición SOAP contiene un documento XML con un significado definido por el servicio.

Si el parámetro `wsdl` se proporciona, esta opción se ignora y el estilo se lee desde el archivo WSDL.

Si ni esta opción ni el parámetro `wsdl` se proporcionan, se utiliza el estilo RPC.

`use` `int`  
Especifica el estilo de codificación a utilizar para este cliente, utilizando las constantes `SOAP_ENCODED` o `SOAP_LITERAL`. `SOAP_ENCODED` indica una codificación utilizando los tipos definidos en la especificación SOAP. `SOAP_LITERAL` indica una codificación utilizando un esquema definido.

Si el parámetro `wsdl` se proporciona, esta opción se ignora y la codificación se lee desde el archivo WSDL.

Si esta opción y el parámetro `wsdl` no se proporcionan, se utiliza el estilo "encoded".

`soap_version` `int`  
Especifica la versión del protocolo SOAP a utilizar: `SOAP_1_1` para SOAP 1.1, o `SOAP_1_2` para SOAP 1.2.

Si se omite, se utiliza SOAP 1.1.

`authentication` `int`  
Especifica el método de autenticación al utilizar la autenticación HTTP en las peticiones. El valor puede ser `SOAP_AUTHENTICATION_BASIC` o `SOAP_AUTHENTICATION_DIGEST`.

Si se omite y la opción `login` se proporciona, se utiliza la autenticación HTTP Basic.

`login` `string`  
Nombre de usuario a utilizar con la autenticación HTTP Basic o HTTP Digest.

`password` `string`  
Contraseña a utilizar con la autenticación HTTP Basic o HTTP Digest.

No confundir con `passphrase`, que se utiliza con la autenticación por certificado cliente HTTPS.

`local_cert` `string`  
Ruta hacia un certificado cliente a utilizar con la autenticación HTTPS. Debe ser un archivo codificado en PEM que contenga el certificado y su clave privada.

El archivo también puede incluir una cadena de emisores, que debe venir después del certificado cliente.

También puede ser definido a través de [ `stream_context`](#soapclient.construct.options.stream-context), que también permite especificar un archivo de clave privada distinto.

`passphrase` `string`  
Passphrase para el certificado cliente especificado en la opción `local_cert`.

No confundir con `password`, que se utiliza con la autenticación HTTP Basic o HTTP Digest.

También puede ser definido a través de [ `stream_context`](#soapclient.construct.options.stream-context).

`proxy_host` `string`  
Nombre de host a utilizar como servidor proxy para las peticiones HTTP.

La opción `proxy_port` también debe ser especificada.

`proxy_port` `int`  
Puerto TCP a utilizar al conectarse al servidor proxy especificado en `proxy_host`.

`proxy_login` `string`  
Nombre de usuario opcional para autenticarse con el servidor proxy especificado en `proxy_host`, utilizando la autenticación HTTP Basic.

`proxy_password` `string`  
Contraseña opcional para autenticarse con el servidor proxy especificado en `proxy_host`, utilizando la autenticación HTTP Basic.

`compression` `int`  
Activa la compresión de las peticiones y respuestas SOAP HTTP.

El valor debe ser el resultado de la operación OR a nivel de bits de tres partes: un `SOAP_COMPRESSION_ACCEPT` opcional, para enviar el encabezado "Accept-Encoding"; ya sea `SOAP_COMPRESSION_GZIP` o `SOAP_COMPRESSION_DEFLATE` para indicar el algoritmo de compresión a utilizar; y un número entre 1 y 9 para indicar el nivel de compresión a utilizar en la petición. Por ejemplo, para activar la compresión gzip bidireccional con el nivel de compresión máximo, utilice `SOAP_COMPRESSION_ACCEPT | SOAP_COMPRESSION_GZIP | 9`.

`encoding` `string`  
Define el codificado de caracteres interno. Las peticiones siempre se envían en UTF-8 y se convierten desde y hacia este codificado.

`trace` `bool`  
Captura la información de petición y respuesta, que luego puede ser consultada utilizando los métodos SoapClient::\_\_getLastRequest, SoapClient::\_\_getLastRequestHeaders, SoapClient::\_\_getLastResponse, y SoapClient::\_\_getLastResponseHeaders.

Si se omite, el valor por omisión es `false`

`classmap` `array`  
Utilizado para asociar los tipos definidos en el WSDL con las clases PHP. Debe ser especificado en forma de un `array` asociativo con los nombres de tipos del WSDL como claves y los nombres de clases PHP como valores. Tenga en cuenta que el nombre de tipo de un elemento no necesariamente corresponden al nombre del elemento (etiqueta).

Los nombres de clase proporcionados siempre deben estar completamente calificados con todos los [espacios de nombres](#language.namespaces), y nunca comenzar con un `\`. La forma correcta puede ser generada utilizando [::class](#language.oop5.basic.class.class).

Tenga en cuenta que al crear una clase, el constructor no será llamado, pero los métodos mágicos [\_\_set()](#object.set) y [\_\_get()](#object.get) para las propiedades individuales sí lo serán.

`typemap` `array`  
Utilizado para definir correspondencias de tipos utilizando funciones de devolución de llamada definidas por el usuario. Cada correspondencia de tipo debe ser un array con las claves `type_name` (un `string` que especifica el tipo de elemento XML), `type_ns` (un `string` que contiene la URI del espacio de nombres), `from_xml` (un `callable` que acepta un parámetro de tipo string y devuelve un objeto) y `to_xml` (un `callable` que acepta un parámetro de tipo objeto y devuelve un string).

`exceptions` `bool`  
Define si los errores generan excepciones de tipo `SoapFault`.

Por omisión, es `true`

`connection_timeout` `int`  
Define un tiempo límite en segundos para la conexión al servicio SOAP. Esta opción no define un tiempo límite para los servicios con respuesta lenta. Para limitar el tiempo de espera de las llamadas, la opción de configuración [default_socket_timeout](#ini.default-socket-timeout) está disponible.

`cache_wsdl` `int`  
Si el parámetro `wsdl` se especifica y la opción de configuración [soap.wsdl_cache_enabled](#ini.soap.wsdl-cache-enabled) está activada, esta opción determina el tipo de almacenamiento en caché. Una de las constantes `WSDL_CACHE_NONE`, `WSDL_CACHE_DISK`, `WSDL_CACHE_MEMORY` o `WSDL_CACHE_BOTH`.

Dos tipos de caché están disponibles: la caché en memoria, que almacena en caché el WSDL en la memoria del proceso actual, y la caché en disco, que almacena en caché el WSDL en un archivo en el disco compartido entre todos los procesos. El directorio a utilizar para la caché en disco es determinado por la opción de configuración [soap.wsdl_cache_dir](#ini.soap.wsdl-cache-dir). Las dos cachés tienen la misma vida útil, determinada por la opción de configuración [soap.wsdl_cache_ttl](#ini.soap.wsdl-cache-ttl). La caché en memoria también tiene un número máximo de entradas determinado por la opción de configuración [soap.wsdl_cache_limit](#ini.soap.wsdl-cache-limit).

Si no se especifica, la opción de configuración [ soap.wsdl_cache](#ini.soap.wsdl-cache) será utilizada.

`user_agent` `string`  
El valor a utilizar en el encabezado HTTP `User-Agent` durante las peticiones.

También puede ser definido a través de [ `stream_context`](#soapclient.construct.options.stream-context).

Si no se especifica, el agente de usuario será `"PHP-SOAP/"` seguido del valor de `PHP_VERSION`.

`stream_context` `resource`  
Un [contexto de flujo](#context) creado por `stream_context_create`, que permite definir opciones adicionales.

El contexto puede incluir opciones de contexto [socket](#context.socket), opciones de contexto [SSL](#context.ssl), así como algunas opciones de contexto [HTTP](#context.http) seleccionadas: `content_type`, `header`, `max_redirects`, `protocol_version`, y `user_agent`.

Tenga en cuenta que los siguientes encabezados HTTP son generados automáticamente o a partir de otras opciones, y serán ignorados si se especifican en la opción de contexto `'header'`: `host`, `connection`, `user-agent`, `content-length`, `content-type`, `cookie`, `authorization` y `proxy-authorization`.

`features` `int`  
Una máscara de bits para activar una o más de las siguientes funcionalidades:

`SOAP_SINGLE_ELEMENT_ARRAYS`  
Al decodificar una respuesta en array, el comportamiento por omisión consiste en detectar si un nombre de elemento aparece una sola vez o múltiples veces en un elemento padre particular. Para los elementos que aparecen una sola vez, una propiedad de objeto permite un acceso directo al contenido; para los elementos que aparecen más de una vez, la propiedad contiene un array con el contenido de cada elemento correspondiente.

Si la funcionalidad `SOAP_SINGLE_ELEMENT_ARRAYS` está activada, los elementos que aparecen una sola vez se colocan en un array de un solo elemento, de modo que el acceso sea coherente para todos los elementos. Esto solo tiene efecto al utilizar un WSDL que contenga un esquema para la respuesta. Consulte la sección de ejemplos para una ilustración.

`SOAP_USE_XSI_ARRAY_TYPE`  
Cuando la opción [`use` opción](#soapclient.construct.options.use) o la propiedad WSDL está definida en `encoded`, fuerza a los arrays a utilizar un tipo `SOAP-ENC:Array`, en lugar de un tipo específico del esquema.

`SOAP_WAIT_ONE_WAY_CALLS`  
Esperar una respuesta incluso si el WSDL indica una petición de un solo sentido.

`keep_alive` `bool`  
un valor booleano que define si enviar el encabezado `Connection: Keep-Alive` o `Connection: close`.

Por omisión, es `true`

`ssl_method` `string`  
Especifica la versión del protocolo SSL o TLS a utilizar con las conexiones HTTP seguras, en lugar de la negociación por omisión. Especificar `SOAP_SSL_METHOD_SSLv2` o `SOAP_SSL_METHOD_SSLv3` forzará el uso de SSL 2 o SSL 3, respectivamente. Especificar `SOAP_SSL_METHOD_SSLv23` no tiene ningún efecto; esta constante solo existe por razones de compatibilidad ascendente. A partir de PHP 7.2.0, especificar `SOAP_SSL_METHOD_TLS` tampoco tiene ningún efecto; en versiones anteriores, esto forzaba el uso de TLS 1.0.

Es de notar que las versiones SSL 2 y 3 se consideran no seguras y pueden no ser soportadas por la biblioteca OpenSSL instalada.

Esta opción es **obsoleta** a partir de PHP 8.1.0. Una alternativa más flexible, que permite especificar versiones individuales de TLS, consiste en utilizar la opción [`stream_context`](#soapclient.construct.options.stream-context) con el parámetro de contexto 'crypto_method'.

```
<?php
// Especificar el uso de TLS 1.3 solamente
$context = stream_context_create([
    'ssl' => [
        'crypto_method' => STREAM_CRYPTO_METHOD_TLSv1_3_CLIENT
     ]
]);
$client = new SoapClient("some.wsdl", ['context' => $context]);

            
```php

## Errores/Excepciones

SoapClient::\_\_construct generará un error de tipo `E_ERROR` si las opciones `location` y `uri` no se proporcionan en modo non-WSDL.

Una excepción de tipo `SoapFault` será lanzada si el URI `wsdl` no puede ser cargado.

## Ejemplos

Ejemplo SoapClient::\_\_construct

```
<?php

$client = new SoapClient("some.wsdl");

$client = new SoapClient("some.wsdl", array('soap_version'   => SOAP_1_2));

$client = new SoapClient("some.wsdl", array('login'          => "some_name",
                                            'password'       => "some_password"));

$client = new SoapClient("some.wsdl", array('proxy_host'     => "localhost",
                                            'proxy_port'     => 8080));

$client = new SoapClient("some.wsdl", array('proxy_host'     => "localhost",
                                            'proxy_port'     => 8080,
                                            'proxy_login'    => "some_name",
                                            'proxy_password' => "some_password"));

$client = new SoapClient("some.wsdl", array('local_cert'     => "cert_key.pem"));

$client = new SoapClient(null, array('location' => "http://localhost/soap.php",
                                     'uri'      => "http://test-uri/"));

$client = new SoapClient(null, array('location' => "http://localhost/soap.php",
                                     'uri'      => "http://test-uri/",
                                     'style'    => SOAP_DOCUMENT,
                                     'use'      => SOAP_LITERAL));

$client = new SoapClient("some.wsdl",
  array('compression' => SOAP_COMPRESSION_ACCEPT | SOAP_COMPRESSION_GZIP | 9));

$client = new SoapClient("some.wsdl", array('encoding'=>'ISO-8859-1'));

class MyBook {
    public $title;
    public $author;
}

$client = new SoapClient("books.wsdl", array('classmap' => array('book' => "MyBook")));

$typemap = array(
    array("type_ns"  => "http://schemas.example.com",
         "type_name" => "book",
         "from_xml"  => "unserialize_book",
         "to_xml"    => "serialize_book")
);
$client = new SoapClient("books.wsdl", array('typemap' => $typemap));

?>

    
```php

Utilizando la funcionalidad `SOAP_SINGLE_ELEMENT_ARRAYS`

```
<?php
/* Suponiendo una respuesta como esta, y un WSDL apropiado:

<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns="urn:example">
    <SOAP-ENV:Body>
        <response>
            <collection>
                <item>Single</item>
            </collection>
            <collection>
                <item>First</item>
                <item>Second</item>
            </collection>
        </response>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
*/

echo "Default:\n";

$client = new TestSoapClient(__DIR__ . '/temp.wsdl');
$response = $client->exampleRequest();
var_dump( $response->collection[0]->item );
var_dump( $response->collection[1]->item );

echo "\nWith SOAP_SINGLE_ELEMENT_ARRAYS:\n";

$client = new TestSoapClient(__DIR__ . '/temp.wsdl', ['features' => SOAP_SINGLE_ELEMENT_ARRAYS]);
$response = $client->exampleRequest();
var_dump( $response->collection[0]->item );
var_dump( $response->collection[1]->item );

    
```php

El ejemplo anterior mostrará:

    Default:
    string(6) "Single"
    array(2) {
      [0] =>
      string(5) "First"
      [1] =>
      string(6) "Second"
    }

    With SOAP_SINGLE_ELEMENT_ARRAYS:
    array(1) {
      [0] =>
      string(6) "Single"
    }
    array(2) {
      [0] =>
      string(5) "First"
      [1] =>
      string(6) "Second"
    }
