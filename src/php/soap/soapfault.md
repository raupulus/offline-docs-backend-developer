---
title: La clase SoapFault
source_url: https://www.php.net/manual/es/class.soapfault.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/soapfault.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_revision: cdb9b8afa
order: 75290
---

## Introducción

Representa un error SOAP.

## Sinopsis de la clase

SoapFault

extends

Exception

Propiedades

public

string

faultstring

public

string

null

faultcode

null

public

string

null

faultcodens

null

public

string

null

faultactor

null

public

mixed

detail

null

public

string

null

\_name

null

public

mixed

headerfault

null

public

string

lang

""

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`_name`  

`detail`  

`faultactor`  

`faultcode`  

`faultcodens`  

`faultstring`  

`headerfault`  

`lang`  
Atributo xml:lang del texto Reason de Soap 1.2.

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.5.0   | Se ha añadido SoapFault::lang. |
