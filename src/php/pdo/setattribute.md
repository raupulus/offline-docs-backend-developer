---
title: PDO::setAttribute
description: Configura un atributo PDO
source_url: https://www.php.net/manual/es/pdo.setattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo/setattribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 9d792d3c5
order: 61970
---

PDO::setAttribute

Configura un atributo PDO

## Descripción

```php
public PDO::setAttribute(int $attribute, mixed $value): bool
```php

Configura un atributo del gestor de base de datos. Algunos de los atributos genéricos se listan a continuación; algunos controladores disponen de configuraciones adicionales. Cabe señalar que los atributos específicos de un controlador *no deben* ser utilizados con otros controladores.

`PDO::ATTR_CASE`  
Fuerza los nombres de columnas a una casilla particular. Puede tomar una de las siguientes valores:

`PDO::CASE_LOWER`  
Fuerza los nombres de columnas en minúsculas.

`PDO::CASE_NATURAL`  
Deja los nombres de columnas tal como son devueltos por el controlador de base de datos.

`PDO::CASE_UPPER`  
Fuerza los nombres de columnas en mayúsculas.

`PDO::ATTR_ERRMODE`  
El modo para reportar los errores de PDO. Puede tomar una de las siguientes valores:

`PDO::ERRMODE_SILENT`  
Define solo los códigos de error.

`PDO::ERRMODE_WARNING`  
Emite diagnósticos `E_WARNING`.

`PDO::ERRMODE_EXCEPTION`  
Lanza excepciones `PDOException`.

`PDO::ATTR_ORACLE_NULLS`  
> [!NOTE]
> Este atributo está disponible con todos los controladores, no solo Oracle.

Determina si y cómo `null` y las cadenas vacías deben ser convertidas. Puede tomar una de las siguientes valores:

`PDO::NULL_NATURAL`  
No se realiza ninguna conversión.

`PDO::NULL_EMPTY_STRING`  
Las cadenas vacías son convertidas en `null`.

`PDO::NULL_TO_STRING`  
`null` es convertido en cadena vacía.

`PDO::ATTR_STRINGIFY_FETCHES`  
Controla si los valores recuperados (excepto `null`) son convertidos en strings. Acepta un valor de tipo `bool`: `true` para activar y `false` para desactivar (valor por omisión). Los valores `null` permanecen inalterados, excepto si `PDO::ATTR_ORACLE_NULLS` está definido en `PDO::NULL_TO_STRING`.

`PDO::ATTR_STATEMENT_CLASS`  
Configura la clase de resultado derivada de PDOStatement y definida por el usuario. Requiere `array(string classname, array(mixed constructor_args))`.

> [!CAUTION]
> No puede ser utilizado con las instancias persistentes de PDO.

`PDO::ATTR_TIMEOUT`  
Especifica la duración del tiempo límite en segundos. Toma un valor de tipo `int`.

> [!NOTE]
> No todos los controladores soportan esta opción, y su significado puede diferir en función de los controladores. Por ejemplo, SQLite esperará durante este período para obtener un bloqueo de escritura, pero otros controladores pueden interpretar esto como un tiempo límite de conexión o de lectura.

`PDO::ATTR_AUTOCOMMIT`  
> [!NOTE]
> Disponible únicamente para los controladores OCI, Firebird y MySQL.

Determina si cada consulta es autocommit. Toma un valor de tipo `bool`: `true` para activar y `false` para desactivar. Por omisión, `true`.

`PDO::ATTR_EMULATE_PREPARES`  
> [!NOTE]
> Disponible únicamente para los controladores OCI, Firebird y MySQL.

Configura la activación o desactivación de las consultas preparadas emuladas. Algunos controladores no soportan las consultas preparadas nativamente o tienen un soporte limitado. Si se define en `true` PDO siempre emulará las consultas preparadas, de lo contrario PDO intentará utilizar las consultas preparadas nativas. En el caso de que el controlador no pueda preparar la consulta actual, PDO siempre recaerá en la emulación de consultas preparadas.

`PDO::MYSQL_ATTR_USE_BUFFERED_QUERY`  
> [!NOTE]
> Disponible únicamente para el controlador MySQL.

Configura el uso de consultas con búfer. Toma un valor de tipo `bool`: `true` para activar y `false` para desactivar. Por omisión, `true`.

`PDO::ATTR_DEFAULT_FETCH_MODE`  
Define el modo de recuperación. Una descripción de los modos y cómo utilizarlos está disponible en la documentación de PDOStatement::fetch.

## Parámetros

`attribute`  
El atributo a modificar.

`value`  
El valor al que definir el `attribute`, esto puede requerir un tipo específico dependiendo del atributo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`PDO::getAttribute`, `PDOStatement::getAttribute`, `PDOStatement::setAttribute`
