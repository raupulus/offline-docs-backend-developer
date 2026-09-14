---
title: snmp_read_mib
description: Lee y analiza un fichero MIB en el árbol activo MIB
source_url: https://www.php.net/manual/es/function.snmp-read-mib.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/functions/snmp-read-mib.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_reviewed: false
translation_revision: '409067254'
order: 74700
---

snmp_read_mib

Lee y analiza un fichero MIB en el árbol activo MIB

## Descripción

```php
snmp_read_mib(string $filename): bool
```php

Esta función se utiliza para cargar MIBs adicionales, es decir, específicas de los fabricantes, de modo que los OIDs legibles por humanos como `VENDOR-MIB::foo.1` en lugar de los OIDs numéricos puedan ser utilizados.

El orden de carga de los MIBs es importante; la biblioteca Net-SNMP mostrará alertas si los objetos referenciados no pueden ser resueltos.

## Parámetros

`filename`  
El nombre del fichero MIB.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `snmp_read_mib`

```
<?php
 print_r( snmprealwalk('localhost', 'public', '.1.3.6.1.2.1.2.3.4.5') );

 snmp_read_mib('./FOO-BAR-MIB.txt');
 print_r( snmprealwalk('localhost', 'public', 'FOO-BAR-MIB::someTable') );
?>

   
```php

El ejemplo a continuación mostrará algo como: Array ( \[iso.3.6.1.2.1.2.3.4.5.0\] =\> Gauge32: 6 ) Array ( \[FOO-BAR-MIB::someTable.0\] =\> Gauge32: 6 )
