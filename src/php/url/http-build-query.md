---
title: http_build_query
description: Genera una string de consulta con codificación URL
source_url: https://www.php.net/manual/es/function.http-build-query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/url/functions/http-build-query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: url
translation_status: ready
translation_revision: f72c60319
order: 100230
---

http_build_query

Genera una string de consulta con codificación URL

## Descripción

```php
http_build_query(array $data, [string $numeric_prefix], [string $arg_separator], [int $encoding_type]): string
```php

Genera una string con codificación URL, construida a partir del array indexado o asociativo `data`.

## Parámetros

`data`  
Puede ser un array o un objeto que contiene propiedades.

Si `data` es un array, entonces puede ser un array de una o varias dimensiones.

Si `data` es un objeto, entonces solo los atributos públicos serán utilizados en el resultado.

> [!NOTE]
> El método mágico [\_\_toString()](#object.tostring) no se invoca cuando un objeto es evaluado. Para utilizar la representación en string de un objeto en la cadena de consulta, el objeto debe ser convertido explícitamente a string.

`numeric_prefix`  
Si se utilizan índices numéricos en el array base y `numeric_prefix` es proporcionado, será utilizado para prefijar los nombres de los índices para los elementos del array base solamente.

Esto permite generar nombres de variables válidos si los datos son luego decodificados por PHP o una aplicación CGI.

`arg_separator`  
El separador de argumentos. Si no está definido o es `null`, [arg_separator.output](#ini.arg-separator.output) es utilizado para separar los argumentos.

`encoding_type`  
Por omisión, vale `PHP_QUERY_RFC1738`.

Si `encoding_type` vale `PHP_QUERY_RFC1738`, entonces la codificación se realiza conforme a la [RFC 1738](https://datatracker.ietf.org/doc/html/rfc1738) y los espacios del tipo de medio `application/x-www-form-urlencoded`, que se ve afectado por esta elección, serán codificados en forma de un signo más (`+`).

Si `encoding_type` vale `PHP_QUERY_RFC3986`, entonces la codificación se realiza conforme a la [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986), y los espacios serán codificados como signo de porcentaje (`%20`).

## Valores devueltos

Devuelve una `string` codificada URL.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Antes de PHP 8.4.0, las propiedades BackedEnum de `data` se convertían en objetos, en lugar de sus equivalentes escalares. |
| 8.0.0 | `arg_separator` ahora puede ser nullable. |

## Ejemplos

Uso simple de `http_build_query`

```
<?php
$data = array(
    'foo' => 'bar',
    'baz' => 'boom',
    'cow' => 'milk',
    'null' => null,
    'php' => 'hypertext processor'
);

echo http_build_query($data) . "\n";
echo http_build_query($data, '', '&amp;');

?>

   
```php

El ejemplo anterior mostrará:

    foo=bar&baz=boom&cow=milk&php=hypertext+processor
    foo=bar&amp;baz=boom&amp;cow=milk&amp;php=hypertext+processor

`http_build_query` con array indexado

```
<?php
$data = array('foo', 'bar', 'baz', null, 'boom', 'cow' => 'milk', 'php' => 'hypertext processor');

echo http_build_query($data) . "\n";
echo http_build_query($data, 'myvar_');
?>

   
```php

El ejemplo anterior mostrará:

    0=foo&1=bar&2=baz&4=boom&cow=milk&php=hypertext+processor
    myvar_0=foo&myvar_1=bar&myvar_2=baz&myvar_4=boom&cow=milk&php=hypertext+processor

`http_build_query` con array complejo

```
<?php
$data = array(
    'user' => array(
        'name' => 'Bob Smith',
        'age'  => 47,
        'sex'  => 'M',
        'dob'  => '5/12/1956'
    ),
    'pastimes' => array('golf', 'opera', 'poker', 'rap'),
    'children' => array(
        'bobby' => array('age'=>12, 'sex'=>'M'),
        'sally' => array('age'=>8, 'sex'=>'F')
    ),
    'CEO'
);

echo http_build_query($data, 'flags_');
?>

   
```php

El ejemplo anterior mostrará: (en varias líneas para mayor legibilidad)

    user%5Bname%5D=Bob+Smith&user%5Bage%5D=47&user%5Bsex%5D=M&
    user%5Bdob%5D=5%2F12%2F1956&pastimes%5B0%5D=golf&pastimes%5B1%5D=opera&
    pastimes%5B2%5D=poker&pastimes%5B3%5D=rap&children%5Bbobby%5D%5Bage%5D=12&
    children%5Bbobby%5D%5Bsex%5D=M&children%5Bsally%5D%5Bage%5D=8&
    children%5Bsally%5D%5Bsex%5D=F&flags_0=CEO

       

> [!NOTE]
> Solo los elementos indexados numéricamente ("`CEO`") en el array base son prefijados. Los otros índices numéricos en otros niveles no necesitan serlo para tener nombres válidos.

Uso de `http_build_query` con un objeto

```
<?php
class parentClass {
    public    $pub      = 'publicParent';
    protected $prot     = 'protectedParent';
    private   $priv     = 'privateParent';
    public    $pub_bar  = null;
    protected $prot_bar = null;
    private   $priv_bar = null;

    public function __construct(){
        $this->pub_bar  = new childClass();
        $this->prot_bar = new childClass();
        $this->priv_bar = new childClass();
    }
}

class childClass {
    public    $pub  = 'publicChild';
    protected $prot = 'protectedChild';
    private   $priv = 'privateChild';
}

$parent = new parentClass();

echo http_build_query($parent);
?>

   
```php

El ejemplo anterior mostrará:

    pub=publicParent&pub_bar%5Bpub%5D=publicChild

Uso de `http_build_query` con objetos que contienen [\_\_toString()](#object.tostring)

```
<?php
class Foo {
    public $publicProperty = 'visible';

    public function __toString() {
        return "bar";
    }
}

$params = array(
    'a' => 'b',
    'foo' => new Foo()
);

// Sin conversión, http_build_query lee las propiedades públicas
echo http_build_query($params) . "\n";

// Con conversión explícita, http_build_query usa la salida de __toString()
$params['foo'] = (string) new Foo();
echo http_build_query($params) . "\n";
?>

   
```php

El ejemplo anterior mostrará:

    a=b&foo%5BpublicProperty%5D=visible
    a=b&foo=bar

## Véase también

`parse_str`, `parse_url`, `urlencode`, `array_walk`
