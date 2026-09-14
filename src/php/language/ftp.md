---
title: Opciones de contexto FTP
description: Lista de opciones de contexto FTP
source_url: https://www.php.net/manual/es/context.ftp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/context/ftp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 099db652f
order: 1990
---

Opciones de contexto FTP

Lista de opciones de contexto FTP

## Descripción

Opciones de contexto para los protocolos `ftp://` y `ftps://`.

## Opciones

`overwrite` `bool`  
Permite sobrescribir los ficheros existentes en el servidor remoto. Solo se aplica en modo de escritura.

Por omisión, `false`.

`resume_pos` `int`  
Posición en el fichero a partir de la cual se inicia la transferencia. Solo se aplica en modo de escritura.

Por omisión, vale `0` (Inicio del fichero).

`proxy` `string`  
URI de la dirección del proxy FTP. Solo se aplica a las operaciones de lectura de ficheros. Por ejemplo: `tcp://squid.example.com:8000`.

## Notas

> [!NOTE]
> Opciones de contexto adicionales pueden ser soportadas por el [transporte subyacente](#transports.inet). Para los flujos `ftp://`, refiérase a las opciones de contexto del transporte `tcp://`. Para los flujos `ftps://`, refiérase a las opciones de contexto del transporte `ssl://`.

## Véase también

[???](#wrappers.ftp), [???](#context.socket), [???](#context.ssl)
