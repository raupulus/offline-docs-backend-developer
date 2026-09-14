---
title: La clase Pool
source_url: https://www.php.net/manual/es/class.pool.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/pool.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: false
translation_revision: bf92d8bd8
order: 66670
---

## Introducción

Un Pool es un contenedor para, y controlado por, un número ajustable de Workers.

El pooling proporciona un nivel alto de abstracción sobre la funcionalidad Worker, incluyendo la gestión de referencias en el sentido requerido por pthreads.

## Sinopsis de la clase

Pool

Pool

Propiedades

protected

size

protected

class

protected

workers

protected

ctor

protected

last

Métodos

## Propiedades

`size`  
Número máximo de Workers que este pool puede utilizar

`class`  
La clase del Worker

`workers`  
referencias a los Workers

`ctor`  
Los argumentos para el constructor de los nuevos Workers

`last`  
desplazamiento en los workers del último Worker utilizado
