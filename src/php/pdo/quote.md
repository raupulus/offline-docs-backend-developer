---
title: PDO::quote
description: Protege una cadena para usarla en una consulta SQL PDO
source_url: https://www.php.net/manual/es/pdo.quote.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo/quote.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_revision: c142be811
order: 61950
---

PDO::quote

Protege una cadena para usarla en una consulta SQL PDO

## Descripción

```php
public PDO::quote(string $string, [int $type]): string
```php

PDO::quote coloca comillas simples alrededor de una cadena de entrada y protege los caracteres especiales presentes en la cadena de entrada, utilizando el estilo de protección apropiado al controlador actual.

Si se utiliza esta función para construir consultas SQL, se *recomienda encarecidamente* usar PDO::prepare para preparar las consultas SQL con parámetros vinculados en lugar de usar PDO::quote para interpretar las entradas del usuario en la consulta SQL. Las consultas preparadas con parámetros vinculados no solo son más portables, flexibles y seguras, sino también más rápidas de ejecutar que interpretar las consultas, ya que los lados cliente y servidor pueden almacenar en caché una versión compilada de la consulta.

No todos los controladores PDO implementan este método (como PDO_ODBC). Utilice consultas preparadas en su lugar.

> [!CAUTION]
> El juego de caracteres debe ser definido ya sea a nivel del servidor, o durante la conexión a la base de datos (dependiendo del driver utilizado) para que afecte al método PDO::quote. Ver la [documentación específica del driver](#pdo.drivers) para más información.

## Parámetros

`string`  
La cadena a proteger.

`type`  
El tipo de datos para los drivers que tienen estilos particulares de protección. Proporciona una pista al tipo de dato para los controladores que tienen un estilo de escape diferente. Por ejemplo `PDO_PARAM_LOB` indica al controlador que escape datos binarios.

## Valores devueltos

Devuelve una cadena protegida, que es teóricamente segura para usar en una consulta SQL. Devuelve `false` si el controlador no soporta este tipo de protecciones.

## Ejemplos

Protección de una cadena normal

```
<?php
$conn = new PDO('sqlite:/home/lynn/music.sql3');

/* Cadena simple */
$string = 'Nice';
print "Cadena no escapada : $string\n";
print "Cadena escapada : " . $conn->quote($string) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    Cadena no escapada : Nice
    Cadena escapada: 'Nice'

Protección de una cadena peligrosa

```
<?php
$conn = new PDO('sqlite:/home/lynn/music.sql3');

/* Cadena peligrosa */
$string = 'Cadena \' particular';
print "Cadena no escapada : $string\n";
print "Cadena escapada :" . $conn->quote($string) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    Cadena no escapada : Cadena ' particular
    Cadena escapada : 'Cadena '' particular'

Protección de una cadena compleja

```
<?php
$conn = new PDO('sqlite:/home/lynn/music.sql3');

/* Cadena compleja */
$string = "Co'mpl''exe \"ch'\"aîne";
print "Cadena no escapada : $string\n";
print "Cadena escapada : " . $conn->quote($string) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    Cadena no escapada: Co'mpl''exe "ch'"aîne
    Cadena escapada: 'Co''mpl''''exe "ch''"aîne'

## Véase también

PDO::prepare, PDOStatement::execute
