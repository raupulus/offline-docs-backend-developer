---
title: PDO::prepare
description: Prepara una consulta para su ejecución y devuelve un objeto
source_url: https://www.php.net/manual/es/pdo.prepare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo/prepare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 61930
---

PDO::prepare

Prepara una consulta para su ejecución y devuelve un objeto

## Descripción

```php
public PDO::prepare(string $query, [array $options]): PDOStatement
```php

Prepara una consulta SQL para ser ejecutada por el método PDOStatement::execute. El modelo de declaración puede contener cero o más parámetros nombrados (:nombre) o marcadores (?) para los cuales los valores reales serán sustituidos cuando la consulta sea ejecutada. El uso tanto de parámetros nombrados como de marcadores es imposible en un modelo de declaración; solo uno u otro estilo de parámetro. Utilícese estos parámetros para ligar las entradas del usuario, no se incluyan directamente en la consulta.

Debe incluirse un marcador con un nombre único para cada valor que se desee pasar en la consulta al llamar a PDOStatement::execute. No puede utilizarse un marcador con dos nombres idénticos en una consulta preparada, a menos que el modo de emulación esté activo.

> [!NOTE]
> Los marcadores de parámetros pueden representar únicamente un literal de datos completo. Ni una parte de literal, ni una palabra clave, ni un identificador, ni cualquier otra consulta arbitraria pueden ser ligados utilizando los parámetros. Por ejemplo, no puede asociarse múltiples valores a un solo marcador de nombre entrante, en la cláusula IN() de una consulta SQL.

Llamar a PDO::prepare y PDOStatement::execute para las consultas que deben ser ejecutadas varias veces con diferentes valores de parámetros optimiza el rendimiento de la aplicación permitiendo al controlador negociar del lado del cliente y/o servidor con la caché de consultas y las meta-informaciones. Además, llamar a PDO::prepare y PDOStatement::execute ayuda a prevenir ataques por inyección SQL eliminando la necesidad de proteger los parámetros manualmente.

PDO emula las consultas preparadas / los parámetros ligados para los controladores que no los soportan nativamente, y puede también reescribir los parámetros nombrados o los marcadores en algo más apropiado, si el controlador soporta un estilo y no el otro.

> [!NOTE]
> El analizador utilizado para las declaraciones preparadas emuladas y para reescribir los parámetros nombrados o del estilo de punto de interrogación soporta el escape backslash no estándar para las comillas simples y dobles. Esto significa que las comillas finales que son precedidas por un backslash no serán reconocidas como tales, lo que puede resultar en una mala detección de los parámetros causando que la declaración preparada falle al ser ejecutada. Un contorno es no utilizar las consultas emuladas para tales consultas SQL, y evitar reescribir los parámetros utilizando un estilo de parámetro que es soportado nativamente por el controlador.

A partir de PHP 7.4.0, los puntos de interrogación pueden ser escapados duplicándolos. Esto significa que la cadena `??` será traducida en `?` al enviar la consulta a la base de datos.

## Parámetros

`query`  
Debe ser un modelo de consulta SQL válido para el servidor de base de datos objetivo.

`options`  
Este array contiene una o más parejas clave=\>valor para definir los valores de los atributos para el objeto PDOStatement que esta método devuelve. Puede utilizarse esto para definir el valor `PDO::ATTR_CURSOR` a `PDO::CURSOR_SCROLL` para solicitar un cursor desplazable. Algunos controladores tienen opciones específicas que pueden ser definidas en el momento de la preparación.

## Valores devueltos

Si el servidor de base de datos prepara con éxito esta consulta, PDO::prepare devuelve un objeto `PDOStatement`. Si el servidor de base de datos no logra preparar la consulta, PDO::prepare devuelve `false` o emite una excepción `PDOException` (siguiendo el [gestor de errores](#pdo.error-handling)).

> [!NOTE]
> La emulación de consultas preparadas no comunica con el servidor de base de datos. También, la función PDO::prepare no verifica la consulta.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_WARNING`.

Lanza una excepción `PDOException` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_EXCEPTION`.

## Ejemplos

Modelo de declaración SQL con parámetros nombrados

```
<?php
/* Ejecuta una consulta preparada pasando un array de valores */
$sql = 'SELECT nombre, color, calorias
    FROM fruta
WHERE calorias < :calorias AND color = :color';
$sth = $dbh->prepare($sql, [PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY]);
$sth->execute(['calorias' => 150, 'color' => 'red']);
$red = $sth->fetchAll();
/* Las claves del array pueden ser prefijadas con dos puntos ":" también (opcional) */
$sth->execute([':calorias' => 175, ':color' => 'yellow']);
$yellow = $sth->fetchAll();
?>

    
```php

Modelo de declaración SQL con marcadores

```
<?php
/* Ejecuta una consulta preparada pasando un array de valores */
$sth = $dbh->prepare('SELECT nombre, color, calorias
    FROM fruta
    WHERE calorias < ? AND color = ?');
$sth->execute([150, 'rojo']);
$red = $sth->fetchAll();
$sth->execute([175, 'amarillo']);
$yellow = $sth->fetchAll();
?>

    
```php

Modelo de declaración SQL con un punto de interrogación escapado

```
<?php
/* nota: esto solo es válido para bases de datos PostgreSQL */
$sth = $dbh->prepare('SELECT * FROM issues WHERE tag::jsonb ?? ?');
$sth->execute(['feature']);
$featureIssues = $sth->fetchAll();
$sth->execute(['performance']);
$performanceIssues = $sth->fetchAll();
?>

    
```php

## Véase también

PDO::exec, PDO::query, PDOStatement::execute
