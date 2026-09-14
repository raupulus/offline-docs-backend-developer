---
title: TypeError
source_url: https://www.php.net/manual/es/class.typeerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/typeerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: b905b4cde
order: 4060
---

## Introducción

Una `TypeError` puede ser lanzada cuando: El valor que se define para una propiedad de clase no corresponde al tipo declarado de la propiedad correspondiente., El tipo del argumento que se pasa a la función no corresponde a la declaración del tipo del parámetro correspondiente., Un valor que es devuelto por una función no corresponde al tipo de retorno declarado por la función.

## Sinopsis de la clase

TypeError

extends

Error

Propiedades heredadas

Métodos heredados

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.1.0 | En modo estricto, pasar un número incorrecto de argumentos a una función interna de PHP ya no lanza una `TypeError` genérica. En su lugar, se lanza una `ArgumentCountError` más específica, que extiende `TypeError`. |
