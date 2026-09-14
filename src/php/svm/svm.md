---
title: La clase SVM
source_url: https://www.php.net/manual/es/class.svm.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svm/svm.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svm
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 89730
---

## Introducción

## Sinopsis de la clase

SVM

SVM

Constantes

const

int

SVM::C_SVC

0

const

int

SVM::NU_SVC

1

const

int

SVM::ONE_CLASS

2

const

int

SVM::EPSILON_SVR

3

const

int

SVM::NU_SVR

4

const

int

SVM::KERNEL_LINEAR

0

const

int

SVM::KERNEL_POLY

1

const

int

SVM::KERNEL_RBF

2

const

int

SVM::KERNEL_SIGMOID

3

const

int

SVM::KERNEL_PRECOMPUTED

4

const

int

SVM::OPT_TYPE

101

const

int

SVM::OPT_KERNEL_TYPE

102

const

int

SVM::OPT_DEGREE

103

const

int

SVM::OPT_SHRINKING

104

const

int

SVM::OPT_PROBABILITY

105

const

int

SVM::OPT_GAMMA

201

const

int

SVM::OPT_NU

202

const

int

SVM::OPT_EPS

203

const

int

SVM::OPT_P

204

const

int

SVM::OPT_COEF_ZERO

205

const

int

SVM::OPT_C

206

const

int

SVM::OPT_CACHE_SIZE

207

Métodos

## Constantes predefinidas

## Constantes SVM

`SVM::C_SVC`  
El tipo básico C_SVC SVM. Es el tipo por defecto. Un buen punto de partida.

`SVM::NU_SVC`  
El tipo NU_SVC usa una diferente y más flexible ponderación de errores.

`SVM::ONE_CLASS`  
Una clase de tipo SVM. Guía simplemente a una clase, usando valores extremos como ejemplos negativos.

`SVM::EPSILON_SVR`  
Un tipo SVM para regresión (prediciento un valor más que símplemente una clase)

`SVM::NU_SVR`  
Un tipo de regresión SVM al estilo NU.

`SVM::KERNEL_LINEAR`  
Un núcleo muy simple, puede funcionar bien con problemas de clasificación de documentos grandes.

`SVM::KERNEL_POLY`  
Un núcleo polinómico

`SVM::KERNEL_RBF`  
El común nucleo Gaussiano RBD. Maneja bien problemas no lineales y es un buen estándar para la clasificación.

`SVM::KERNEL_SIGMOID`  
Un núcleo basado en la función sigmoid. Usando esta, SVM se hace muy similar a sigmoid de dos capas basado en redes neuronales.

`SVM::KERNEL_PRECOMPUTED`  
Un núcleo precalculado - actualmente sin soporte.

`SVM::OPT_TYPE`  
La clave de opciones para el tipo SVM

`SVM::OPT_KERNEL_TYPE`  
La clave opcional para el tipo de núcleo

`SVM::OPT_DEGREE`  

`SVM::OPT_SHRINKING`  
Parámetro de formación, booleano, para cualquier uso de reducciones heurísticas.

`SVM::OPT_PROBABILITY`  
Parámetro de formación, booleano, para recaudar y estimar el uso de probabilidades.

`SVM::OPT_GAMMA`  
Parámetro algorítmico para usar Poly, RBF y Sigmoid como tipos de núcleo.

`SVM::OPT_NU`  
La clave de opción para el parámetro NU, solo usado en tipos NU\_ SVM.

`SVM::OPT_EPS`  
La clave para la opción del parámetro Epsilon, Usada en regresiones epsilon.

`SVM::OPT_P`  
Parámetro de formación usado por regresiones Episilon SVR

`SVM::OPT_COEF_ZERO`  
Parámetro para el algoritmo de núcleos poly y sigmoid

`SVM::OPT_C`  
La opción para el parámetro de coste que controla la compensación entre errores y generalidad - efectivamente la sanción por la clasificación errónea de los ejemplos de formación.

`SVM::OPT_CACHE_SIZE`  
Tamaño de la memoria caché, en MB.
