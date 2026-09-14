---
title: MongoDB\BSON\toPHP
description: Devuelve la representación en PHP de un valor BSON
source_url: https://www.php.net/manual/es/function.mongodb.bson-tophp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/functions/bson/tophp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 6047c10c1
order: 48790
---

MongoDB\BSON\toPHP

Devuelve la representación en PHP de un valor BSON

> [!WARNING]
> Esta función ha sido *DEPRECADA* a partir de la versión 1.20.0 de la extensión y fue eliminada en la versión 2.0. Las aplicaciones deben usar MongoDB\BSON\Document::toPHP en su lugar.

## Descripción

```php
MongoDB\BSON\toPHP(string $bson, [array $typeMap]): array
```php

Deserializa un documento BSON (es decir, una cadena binaria) a su representación en PHP. El parámetro `typeMap` puede usarse para controlar los tipos de PHP utilizados para convertir matrices y documentos BSON (tanto raíz como incrustados).

> [!WARNING]
> Los documentos BSON pueden contener técnicamente claves duplicadas ya que los documentos se almacenan como una lista de pares clave-valor; sin embargo, las aplicaciones deben abstenerse de generar documentos con claves duplicadas ya que el comportamiento del servidor y del controlador puede ser indefinido. Dado que los objetos y arrays de PHP no pueden tener claves duplicadas, los datos también podrían perderse al decodificar un documento BSON con claves duplicadas.

## Parámetros

`bson` (`string`)  
Valor BSON a deserializar.

`typeMap` (`array`)  
[Configuración del mapa de tipos](#mongodb.persistence.typemaps).

## Valores devueltos

El valor en PHP deserializado.

## Errores/Excepciones

Lanza

MongoDB\Driver\Exception\InvalidArgumentException

si una clase en el mapa de tipos no puede ser instanciada o no implementa

MongoDB\BSON\Unserializable

.

Lanza una excepción

MongoDB\Driver\Exception\UnexpectedValueException

si la entrada no contiene exactamente un documento BSON. Las razones posibles incluyen, pero no se limitan a, BSON inválido, datos adicionales (después de leer un documento BSON), o un error inesperado de

libbson

.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | Esta función ha sido eliminada. |
| PECL mongodb 1.4.0 | Si la entrada contiene un tipo BSON obsoleto no admitido, la extensión ya no registrará una advertencia en el registro de depuración, sino que creará un objeto que represente este tipo. |
| PECL mongodb 1.3.2 | Ya no se lanza `MongoDB\Driver\Exception\UnexpectedValueException` si la entrada contiene un tipo BSON obsoleto no admitido. Tales tipos serán ignorados (como lo eran en versiones anteriores a 1.3.0), aunque la extensión registrará ahora una advertencia en el registro de depuración (ver: [mongodb.debug](#ini.mongodb.debug)). |
| PECL mongodb 1.3.0 | Se lanza `MongoDB\Driver\Exception\UnexpectedValueException` si la entrada contiene un tipo BSON obsoleto no admitido. Anteriormente, tales tipos eran ignorados. |

## Ejemplos

Ejemplo de `MongoDB\BSON\toPHP`

```
<?php

$bson = hex2bin('0e00000010666f6f000100000000');
$value = MongoDB\BSON\toPHP($bson);
var_dump($value);

?>

   
```php

El ejemplo anterior mostrará:

    object(stdClass)#1 (1) {
      ["foo"]=>
      int(1)
    }

## Véase también

MongoDB\BSON\Document::toPHP

MongoDB\BSON\fromPHP

MongoDB BSON
