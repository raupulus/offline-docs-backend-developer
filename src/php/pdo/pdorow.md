---
title: La clase PDORow
source_url: https://www.php.net/manual/es/class.pdorow.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdorow.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_revision: 812ed835f
order: 62000
---

## Introducción

Representa una línea de un conjunto de resultados devuelto por PDOStatement::fetch llamado con el modo de recuperación `PDO::FETCH_LAZY`.

Los objetos de esta clase no pueden ser instanciados y no son serializables.

La clase `PDORow` permite acceder a los datos devueltos como si los modos `PDO::FETCH_OBJ` y `PDO::FETCH_BOTH` fueran utilizados. Esto significa que los datos devueltos pueden ser accedidos como propiedades de objeto, y como un array indexado por el nombre de la columna y un número de posición de columna.

> [!CAUTION]
> Acceder a una propiedad no definida devuelve `null` sin emitir un mensaje de advertencia.

## Sinopsis de la clase

final

PDORow

Propiedades

public

string

queryString

## Propiedades

`queryString`  
La consulta utilizada por `PDOStatement` que ha devuelto el objeto `PDORow`.

## Errores/Excepciones

Genera un error de tipo `Error` cuando se intenta escribir o `unset` una propiedad.
