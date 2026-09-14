---
title: CommonMark\CQL::__invoke
description: Ejecución de CQL
source_url: https://www.php.net/manual/es/commonmark-cql.invoke.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cmark/commonmark/cql/invoke.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cmark
translation_status: ready
translation_reviewed: false
translation_revision: 876a6a393
order: 6940
---

CommonMark\CQL::\_\_invoke

Ejecución de CQL

## Descripción

```php
public CommonMark\CQL::__invoke(CommonMark\Node $root, callable $handler)
```php

Debe invocar la función CQL actual en el `root` dado, ejecutando el `handler` dado a la entrada de un `CommonMark\Node`

## Parámetros

`root`  
el nodo raíz de un árbol

`handler`  
Debe tener el prototipo:

```php
handler(CommonMark\Node $root, CommonMark\Node $entering): bool
```

Si `handler` no devuelve (void), o devuelve `null`, el CQL continuará ejecutándose, Si el gestor devuelve un valor verdadero, el CQL continuará ejecutándose, Si el gestor devuelve un valor falso, el CQL se detendrá
