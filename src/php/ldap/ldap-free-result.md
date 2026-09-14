---
title: ldap_free_result
description: Libera la memoria del resultado
source_url: https://www.php.net/manual/es/function.ldap-free-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-free-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: fbc6f9055
order: 43250
---

ldap_free_result

Libera la memoria del resultado

## Descripción

```php
ldap_free_result(LDAP\Result $result): bool
```php

Libera toda la memoria asignada internamente para almacenar el resultado `result_identifier`. Si se omite la llamada a esta función, toda la memoria será liberada automáticamente al finalizar el script.

Típicamente, toda la memoria asignada para el resultado LDAP es liberada al finalizar el script. Si el script realiza búsquedas intensivas, que retornan resultados de gran tamaño, `ldap_free_result` puede ser utilizada para reducir el consumo de memoria.

## Parámetros

`result`  
Una instancia de `LDAP\Result`, devuelta por `ldap_list` o `ldap_search`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `LDAP\Result` ; anteriormente, se esperaba un `resource` `ldap result` válido. |
