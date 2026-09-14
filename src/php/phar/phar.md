---
title: La clase Phar
source_url: https://www.php.net/manual/es/class.phar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_revision: 2b232242b
order: 64430
---

## Introducción

La clase Phar proporciona una interfaz de alto nivel para acceder y crear archivos phar.

## Sinopsis de la clase

Phar

extends

RecursiveDirectoryIterator

implements

Countable

ArrayAccess

Constantes heredadas

Constantes

const

int

Phar::BZ2

const

int

Phar::GZ

const

int

Phar::NONE

const

int

Phar::PHAR

const

int

Phar::TAR

const

int

Phar::ZIP

const

int

Phar::COMPRESSED

const

int

Phar::PHP

const

int

Phar::PHPS

const

int

Phar::MD5

const

int

Phar::OPENSSL

const

int

Phar::OPENSSL_SHA256

const

int

Phar::OPENSSL_SHA512

const

int

Phar::SHA1

const

int

Phar::SHA256

const

int

Phar::SHA512

Métodos

Métodos heredados

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Se añadió el soporte para la extensión de timestamp Unix en archivos basados en Zip. |
| 8.0.0 | Los metadatos ya no se deserializan al abrir el archivo, sino que se posponen hasta que se llama a Phar::getMetadata. |

## Notas

> [!CAUTION]
> Antes de PHP 8.0.0, los metadatos se deserializaban al abrir el archivo. Esto podía provocar vulnerabilidades de seguridad. A partir de PHP 8.0.0, los metadatos solo se deserializan al llamar a Phar::getMetadata, que ofrece opciones para restringir la deserialización por razones de seguridad.
