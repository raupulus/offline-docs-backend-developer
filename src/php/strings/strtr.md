---
title: strtr
description: Reemplaza caracteres en un string
source_url: https://www.php.net/manual/es/function.strtr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strtr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 45042fef6
order: 89500
---

strtr

Reemplaza caracteres en un string

## Descripción

```php
strtr(string $string, string $from, string $to): string
```php

Firma alternativa (no soportada con argumentos nombrados):

```php
strtr(string $string, array $replace_pairs): string
```

Si se utilizan tres argumentos, `strtr` devuelve el string `string` después de haber reemplazado cada carácter (de un octeto) del parámetro `from` por su equivalente en el parámetro `to`, cada ocurrencia de `$from[$n]` es reemplazada por `$to[$n]`, donde `$n` es un valor válido para cada argumento.

Si `from` y `to` son de tamaños diferentes, los caracteres adicionales en uno u otro serán ignorados. El tamaño de `string` será el mismo que el de los valores devueltos.

Si solo se utilizan dos argumentos, el segundo debe ser un `array` de la forma `array('from' => 'to', ...)`. El dato devuelto es un `string` en el que todas las ocurrencias de las claves del array han sido reemplazadas por los valores correspondientes. Las claves más largas serán utilizadas primero. Una vez que una subcadena es reemplazada, su nuevo valor no será buscado nuevamente.

En este caso, las claves y los valores pueden tener cualquier tamaño, asumiendo que no hay una clave vacía; así, el tamaño del valor devuelto puede diferir del de `string`. Sin embargo, esta función será más eficiente cuando todas las claves tengan el mismo tamaño.

## Parámetros

`string`  
El string a procesar.

`from`  
Los caracteres de origen.

`to`  
Los caracteres de reemplazo.

`replace_pairs`  
El parámetro `replace_pairs` puede ser utilizado en lugar de `to` y `from` y en este caso, será un array en la forma `array('from' => 'to', ...)`.

Si `replace_pairs` contiene una clave que es un `string` vacío (`""`), el elemento es ignorado; a partir de PHP 8.0.0 se genera una `E_WARNING` en este caso.

## Valores devueltos

Devuelve el string modificado.

## Ejemplos

Ejemplo con `strtr`

```php
<?php
$addr = "The river å";

// Aquí, strtr() reemplaza octeto por octeto, por lo tanto
// se asume aquí codificaciones de un solo octeto:
$addr = strtr($addr, "äåö", "aao");
echo $addr, PHP_EOL;
?>

    
```

El siguiente ejemplo muestra el uso de `strtr` con dos argumentos. Observe la preferencia de los reemplazos (`h` no es utilizado porque hay coincidencias más largas) y cómo el texto reemplazado no es reutilizado posteriormente.

Ejemplo con `strtr` y 2 argumentos

```php
<?php
$trans = array("h" => "-", "hello" => "hi", "hi" => "hello");
echo strtr("hi all, I said hello", $trans);
?>

    
```

El ejemplo anterior mostrará:

    hello all, I said hi

Los dos comportamientos son diferentes. Con tres argumentos, `strtr` reemplazará los octetos; con dos, puede reemplazar subcadenas más largas.

Comparación de comportamiento de `strtr`

```php
<?php
echo strtr("baab", "ab", "01"),"\n";

$trans = array("ab" => "01");
echo strtr("baab", $trans);
?>

    
```

El ejemplo anterior mostrará:

    1001
    ba01

## Véase también

`str_replace`, `preg_replace`
