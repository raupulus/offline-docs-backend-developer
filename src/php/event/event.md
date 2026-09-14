---
title: La clase Event
source_url: https://www.php.net/manual/es/class.event.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/event.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 184764a63
order: 19000
---

## Introducción

La clase `Event` representa y lanza un evento sobre un descriptor de fichero que se ha vuelto listo para una lectura o una escritura; un descriptor de fichero se vuelve listo para una lectura o una escritura (I/O únicamente); un tiempo de espera expirado; una señal ocurriendo; un evento lanzado por el usuario.

Cada evento está asociado con un `EventBase`. Sin embargo, el evento nunca será lanzado hasta que no haya sido *añadido* (a través del método Event::add). Un evento añadido permanece en un estado de *espera* hasta que el evento registrado ocurra, pasándolo así a un estado *activo*. Para gestionar los eventos, el usuario debe registrar una función de retrollamada que será llamada cuando el evento se vuelva activo. Si el evento está configurado como *persistente*, permanecerá en espera. Si no es persistente, ya no estará en espera cuando su función de retrollamada sea ejecutada. El método Event::del *elimina* el evento, y ya no estará en espera. Al llamar al método Event::add, será añadido de nuevo.

## Sinopsis de la clase

Event

final

Event

Constantes

const

int

Event::ET

32

const

int

Event::PERSIST

16

const

int

Event::READ

2

const

int

Event::WRITE

4

const

int

Event::SIGNAL

8

const

int

Event::TIMEOUT

1

Propiedades

public

readonly

bool

pending

Métodos

## Propiedades

`pending`  
Si el evento está en espera. Ver la sección : [Acerca de la persistencia de los eventos](#event.persistence).

## Constantes predefinidas

`Event::ET`  
Indica que el evento debe ser lanzado, si la base de evento subyacente soporta este tipo de evento. Esto afecta la semántica de `Event::READ` y de `Event::WRITE`.

`Event::PERSIST`  
Indica que el evento es persistente. Ver la sección : [Acerca de la persistencia de los eventos](#event.persistence).

`Event::READ`  
Este flag indica que un evento se vuelve activo cuando el descriptor de fichero proporcionado (normalmente, un recurso de flujo o un socket) está listo para una lectura.

`Event::WRITE`  
Este flag indica que un evento se vuelve activo cuando el descriptor de fichero proporcionado (normalmente, un recurso de flujo o un socket) está listo para una escritura.

`Event::SIGNAL`  
Utilizado para implementar una detección de señal. Ver la sección a continuación sobre la construcción de un evento de tipo señal.

`Event::TIMEOUT`  
Este flag indica que un evento se vuelve activo después de la expiración de este tiempo de espera máximo.

El flag `Event::TIMEOUT` es ignorado durante la construcción de un evento: puede ser indicado o no durante la *adición* del evento. Debe ser definido en el argumento `$what` de la función de retrollamada cuando un tiempo de espera máximo haya ocurrido.
