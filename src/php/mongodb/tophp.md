---
title: MongoDB\BSON\Document::toPHP
description: Devuelve la representación PHP del documento BSON
source_url: https://www.php.net/manual/es/mongodb-bson-document.tophp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/document/tophp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 6047c10c1
order: 47690
---

MongoDB\BSON\Document::toPHP

Devuelve la representación PHP del documento BSON

## Descripción

```php
final public MongoDB\BSON\Document::toPHP([array $typeMap]): array
```php

Deserializa el documento BSON en su representación PHP. El parámetro `typeMap` puede ser utilizado para controlar los tipos PHP utilizados para convertir los arrays y documentos BSON (raíz e integrados).

> [!WARNING]
> Los documentos BSON pueden contener técnicamente claves duplicadas ya que los documentos se almacenan como una lista de pares clave-valor; sin embargo, las aplicaciones deben abstenerse de generar documentos con claves duplicadas ya que el comportamiento del servidor y del controlador puede ser indefinido. Dado que los objetos y arrays de PHP no pueden tener claves duplicadas, los datos también podrían perderse al decodificar un documento BSON con claves duplicadas.

## Parámetros

`typeMap` (`array`)  
[Configuración del mapa de tipos](#mongodb.persistence.typemaps).

## Valores devueltos

El valor decodificado PHP.

> [!NOTE]
> Cuando se encuentra un valor codificado como un entero de 64 bits en el documento BSON, el valor de retorno de este método será una instancia de `MongoDB\BSON\Int64`.

## Errores/Excepciones

Lanza una

MongoDB\Driver\Exception\InvalidArgumentException

si un tipo en el mapa de tipos no puede ser instanciado o no implementa

MongoDB\BSON\Unserializable

.

## Véase también

MongoDB\BSON\toPHP

Tipos BSON
