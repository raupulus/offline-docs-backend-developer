---
title: PDO::lastInsertId
description: Devuelve el identificador de la última fila insertada o el valor de una
  secuencia
source_url: https://www.php.net/manual/es/pdo.lastinsertid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo/lastinsertid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: true
translation_revision: 0d4322bcc
order: 61920
---

PDO::lastInsertId

Devuelve el identificador de la última fila insertada o el valor de una secuencia

## Descripción

```php
public PDO::lastInsertId([string $name]): string
```php

Devuelve el identificador de la última fila insertada, o el último valor de una secuencia de objetos, dependiendo del driver utilizado. Por ejemplo, [PDO_PGSQL](#ref.pdo-pgsql) permite especificar el nombre de cualquier objeto secuencia para el argumento `name`.

> [!NOTE]
> Este método puede no devolver un resultado significativo según los drivers PDO utilizados, ya que la base de datos empleada puede no soportar la noción de campos auto-incrementados o de secuencias.

## Parámetros

`name`  
Nombre de la secuencia de objetos desde la cual debe devolverse el identificador.

## Valores devueltos

Si no se especifica un nombre de secuencia para el argumento `name`, PDO::lastInsertId devuelve una cadena que representa el identificador de la última fila insertada en la base de datos.

Si se especifica un nombre de secuencia para el argumento `name`, PDO::lastInsertId devuelve una cadena que representa el último valor de la secuencia de objetos especificada.

Si el driver PDO no soporta esta funcionalidad, PDO::lastInsertId lanzará un SQLSTATE `IM001`.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_WARNING`.

Lanza una excepción `PDOException` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_EXCEPTION`.
