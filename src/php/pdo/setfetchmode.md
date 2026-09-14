---
title: PDOStatement::setFetchMode
description: Establece el modo de recuperación por defecto para esta consulta
source_url: https://www.php.net/manual/es/pdostatement.setfetchmode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/setfetchmode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 8a910daad
order: 62200
---

PDOStatement::setFetchMode

Establece el modo de recuperación por defecto para esta consulta

## Descripción

```php
public PDOStatement::setFetchMode(int $mode): true
```php

```php
public PDOStatement::setFetchMode(int $mode, int $colno): true
```

```php
public PDOStatement::setFetchMode(int $mode, string $class, array $constructorArgs): true
```php

```php
public PDOStatement::setFetchMode(int $mode, object $object): true
```

## Parámetros

`mode`  
El modo de recuperación debe ser una de las constantes [`PDO::FETCH_*`](#pdo.constants).

`colno`  
Número de la columna.

`class`  
Nombre de la clase.

`constructorArgs`  
Argumentos del constructor.

`object`  
Objeto.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.4.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Definición del modo de recuperación

El siguiente ejemplo muestra cómo PDOStatement::setFetchMode modifica el modo de recuperación por defecto para un objeto PDOStatement.

```php
<?php
$stmt = $dbh->query('SELECT name, colour, calories FROM fruit');
$stmt->setFetchMode(PDO::FETCH_NUM);
foreach ($stmt as $row) {
    print $row[0] . "\t" . $row[1] . "\t" . $row[2] . "\n";
}
?>

    
```

Resultado del ejemplo anterior es similar a:

    apple   red     150
    banana  yellow  250
    orange  orange  300
    kiwi    brown   75
    lemon   yellow  25
    pear    green   150
