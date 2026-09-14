---
title: La clase MongoDB\BSON\Persistable
source_url: https://www.php.net/manual/es/class.mongodb-bson-persistable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/persistable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48260
---

## Introducción

Las clases pueden implementar esta interfaz para tener la posibilidad de utilizar los ODM automáticos (los objetos de mapeo de documentos) de esta extensión. Durante la serialización, la extensión inyectará una propiedad \_\_pclass que contiene el nombre de la clase PHP en los datos devueltos por `MongoDB\BSON\Serializable::bsonSerialize`. Durante la deserialización, la misma propiedad \_\_pclass se utilizará para solicitar a la clase PHP (independientemente de la configuración [type map](#mongodb.persistence.typemaps)) que se construya antes de que se invoque `MongoDB\BSON\Unserializable::bsonUnserialize`. Ver [???](#mongodb.persistence) para más información.

> [!NOTE]
> Aunque `MongoDB\BSON\Serializable::bsonSerialize` quiera devolver un array secuencial, la inyección de la propiedad \_\_pclass hará que el objeto se serialice como documento BSON.

## Sinopsis de la interfaz

MongoDB\BSON\Persistable

MongoDB\BSON\Persistable

MongoDB\BSON\Unserializable

MongoDB\BSON\Serializable

Métodos

Métodos heredados
