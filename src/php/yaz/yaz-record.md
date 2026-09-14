---
title: yaz_record
description: Devuelve un registro
source_url: https://www.php.net/manual/es/function.yaz-record.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-record.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_reviewed: false
translation_revision: f9c4a68ef
order: 107900
---

yaz_record

Devuelve un registro

## Descripción

```php
yaz_record(resource $id, int $pos, string $type): string
```php

La función `yaz_record` inspecciona un registro del conjunto resultado actual que está en la posición especificada por el parámetro `pos`.

## Parámetros

`id`  
El recurso de conexión devuelto por `yaz_connect`.

`pos`  
La posición del registro. Las posiciones de los registros en el conjunto resultado están numeradas con 1, 2, ... \$hits donde \$hits es el contador devuelto por `yaz_hits`.

`type`  
El parámetro `type` especifica la forma del registro devuelto.

> [!NOTE]
> Es la aplicación responsable de asegurar realmente que los registros son devueltos en el formato correcto por el servidor Z39.50/SRW. El type indicado únicamente especifica una conversión que se realizará en el lado cliente (en PHP/YAZ).

Además de la conversion del registro transferido a un string/array, PHP/YAZ también puede realizar una conversión de mapa de caracteres del registro. Esto es recomendado especialmente para USMARC/MARC21 puesto que éstos se devuelven habitualmente en el mapa de caracteres MARC-8 que no está soportado por navegadores, etc. Para especificar una conversión, añadir `; charset=`\<from\>`,`\<to\> donde \<from\> es el mapa de caracteres original del registro y \<to\> es el mapa de caracteres resultante (desde el punto de vista PHP).

`string`  
El registro se devuelve como un string de visualización simple. En este modo, todos los registros MARC se convierten a un formato línea a línea ya que ISO2709 es difícilmente legible. Los registros XML y SUTRS se devuelven en su formato original. GRS-1 se devuelve en un (feo) formato línea a línea.

Este formato es adecuado si los registros se mostrarán de forma rápida - para depuración - o porque no es factible realizar una visualización adecuada.

`xml`  
El registro se devuelve como un string XML si es posible. En este modo, todos los registros MARC se convierten en [MARCXML](http://www.loc.gov/standards/marcxml/). Los registros XML y SUTRS se devuelven en su formato original. GRS-1 no está soportado.

Este formato es parecido a `string` excepto por los registros MARC que se convierten a MARCXML

Este formato es adecuado si los registros se procesan posteriormente por un interpretador XML o un procesador XSLT .

`raw`  
El registro se devuelve como un string en su formato original. Este tipo es adecuado para MARC, XML y SUTRS. No funciona con GRS-1.

Los registros MARC se devuelven como un string ISO2709. XML y SUTRS son devueltos como strings.

`syntax`  
La sintaxis del registro se devuelve como un string, p.e. `USmarc`, `GRS-1`, `XML`, etc.

`database`  
El nombre de la base de datos asociada con el registro en la posición, se devuelve como un string.

`array`  
El registro se devuelve como un array que refleja la estructura GRS-1. Este tipo es adecuado para MARC y GRS-1. XML, SUTRS no están soportados y si el registro actual es XML o SUTRS se devolverá un string vacío.

El array devuelto consiste en una lista correspondiente a cada hoja/nodo interno de GRS-1. Cada lista de elementos consiste en una sublista con el primer elemento *path* y *data* (si los datos están disponibles).

El camino de acceso, que es un string, contiene una lista de tres componentes (del registro estructurado GRS-1) de la raíz a la hoja. Cada componente es un par de tipo etiqueta/valor de etiqueta de la forma `(`\<type\>`,` \<value\>

Las etiguqetas normalmente tienen un tipo tag 3. MARC también puede ser devuelto como un array (se convierten a GRS-1 internamente).

## Valores devueltos

Devuelve el registro que se encuentra en la posición `pos` o un string vacío si no existe ningún registro en la posición indicada.

Si no hay registro en la posición indicada en la base de datos, se devolverá un string vacío.

## Ejemplos

Array para registro GRS-1

Considerar este registro GRS-1 :

    (4,52)Robert M. Pirsig
    (4,70)
          (4,90)
                (2,7)Transworld Publishers, ltd.

        

Este registro tiene dos nodos a nivel de raíz. El primer elemento del nivel raíz es (4,52) \[tipo tag 4, valor de tag 52\], y tiene datos `Robert M. Pirsig`. El segundo elemento en el nivel raíz (4,70) tiene un subárbol con un elemento simple (4,90). (4,90) tiene a su vez otro subárbol (2,7) con datos `Transworld Publishers, ltd.`.

Si este registro está presente en la posición \$p, entonces

```
<?php

$ar = yaz_record($id, $p, "array");
print_r($ar);

?>

    
```php

mostrará:

    Array
    (
        [0] => Array
            (
                [0] => (4,52)
                [1] => Robert M. Pirsig
            )
        [1] => Array
            (
                [0] => (4,70)
            )
        [2] => Array
            (
                [0] => (4,70)(4,90)
            )
        [3] => Array
            (
                [0] => (4,70)(4,90)(2,7)
                [1] => Transworld Publishers, ltd.
            )
    )

Trabajar con MARCXML

El siguiente fragmento de PHP devuelve un registro MARC21/USMARC como MARCXML. El registro original se devuelve en marc-8 (desconocido para muchos interpretadores XML), así que lo convertimos a UTF-8 (que todos los interpretadores XML deben soportar).

```
<?php
$rec = yaz_record($id, $p, "xml; charset=marc-8,utf-8");
?>

    
```php

El registro `$rec` puede ser procesado con el procesador Sablotron XSLT de la forma siguiente:

```
<?php

$xslfile = 'display.xsl';
$processor = xslt_create();
$parms = array('/_xml' => $rec);
$res = xslt_process($processor, 'arg:/_xml', $xslfile, NULL, $parms);
xslt_free($processor);
$res = preg_replace("'</?html[^>]*>'", '', $res);
echo $res;

?>

    
```php
