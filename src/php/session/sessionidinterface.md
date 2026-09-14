---
title: La interfaz SessionIdInterface
source_url: https://www.php.net/manual/es/class.sessionidinterface.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionidinterface.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: true
translation_revision: 4d17b7b49
order: 74120
---

## Introducción

`SessionIdInterface` es una interfaz que define métodos opcionales para la creación de un gestor de sesión personalizado. Con el fin de pasar un gestor de sesión personalizado a la función `session_set_save_handler` utilizando su invocación OOP, la clase puede implementar esta interfaz.

Se debe tener en cuenta que estos métodos están destinados a ser llamados de manera interna por PHP, y no desde el espacio de usuario.

## Sinopsis de la interfaz

SessionIdInterface

Métodos
