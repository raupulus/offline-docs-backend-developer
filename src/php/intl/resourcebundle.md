---
title: La clase ResourceBundle
source_url: https://www.php.net/manual/es/class.resourcebundle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/resourcebundle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 42430
---

## Introducción

Las aplicaciones localizadas suelen necesitar manipular datos que deben ser personalizados según una configuración local específica, por ejemplo: mensajes, etiquetas, strings de formato. ICU permite definir recursos que la aplicación podrá cargar con una configuración local una vez para todas: todos los accesos posteriores se realizarán mediante una interfaz única no dependiente de la configuración local considerada.

Esta clase permite el acceso a los archivos de datos de ICU. Estos archivos representan arrays binarios que ICU utiliza para almacenar los datos localizados.

Los bundles de recursos ICU soportan recursos simples y complejos. Los recursos complejos son contenedores que pueden ser indexados numéricamente o literalmente (como los arrays PHP). Los recursos simples, en cambio, pueden ser de tipo string, integer, binario o array numérico.

`ResourceBundle` soporta el acceso directo a los datos mediante la sintaxis de arrays así como la iteración gracias a [foreach](#control-structures.foreach). Estas posibilidades también existen mediante los métodos. El resultado será un valor PHP para los recursos simples, o un objeto `ResourceBundle` para los recursos complejos. Los recursos son de solo lectura.

## Sinopsis de la clase

ResourceBundle

implements

IteratorAggregate

Countable

Métodos

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | La clase `ResourceBundle` ahora implementa IteratorAggregate. Anteriormente, solo Traversable estaba implementada. |
| 7.4.0 | La clase `ResourceBundle` ahora implementa Countable. |

## Véase también

[ Configuración de recursos ICU ](https://unicode-org.github.io/icu/userguide/locale/resources.html), [ICU Data](https://unicode-org.github.io/icu/userguide/icu_data/)
