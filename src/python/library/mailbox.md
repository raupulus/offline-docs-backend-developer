---
title: '"mailbox" --- Manipulate mailboxes in various formats'
source_url: https://docs.python.org/es/3
source_path: library/mailbox.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3160
---

# "mailbox" --- Manipulate mailboxes in various formats

**Código fuente:** Lib/mailbox.py

======================================================================

This module defines two classes, "Mailbox" and "Message", for
accessing and manipulating on-disk mailboxes and the messages they
contain. "Mailbox" offers a dictionary-like mapping from keys to
messages. "Message" extends the "email.message" module's "Message"
class with format-specific state and behavior. Supported mailbox
formats are Maildir, mbox, MH, Babyl, and MMDF.

Ver también:

  Módulo "email"
     Representar y manipular mensajes.

## "Mailbox" objects

class mailbox.Mailbox

   Un buzón de correo, que se puede inspeccionar y modificar.

   The "Mailbox" class defines an interface and is not intended to be
   instantiated.  Instead, format-specific subclasses should inherit
   from "Mailbox" and your code should instantiate a particular
   subclass.

   The "Mailbox" interface is dictionary-like, with small keys
   corresponding to messages. Keys are issued by the "Mailbox"
   instance with which they will be used and are only meaningful to
   that "Mailbox" instance. A key continues to identify a message even
   if the corresponding message is modified, such as by replacing it
   with another message.

   Messages may be added to a "Mailbox" instance using the set-like
   method "add()" and removed using a "del" statement or the set-like
   methods "remove()" and "discard()".

   "Mailbox" interface semantics differ from dictionary semantics in
   some noteworthy ways. Each time a message is requested, a new
   representation (typically a "Message" instance) is generated based
   upon the current state of the mailbox. Similarly, when a message is
   added to a "Mailbox" instance, the provided message
   representation's contents are copied. In neither case is a
   reference to the message representation kept by the "Mailbox"
   instance.

   The default "Mailbox" *iterator* iterates over message
   representations, not keys as the default "dictionary" iterator
   does. Moreover, modification of a mailbox during iteration is safe
   and well-defined. Messages added to the mailbox after an iterator
   is created will not be seen by the iterator. Messages removed from
   the mailbox before the iterator yields them will be silently
   skipped, though using a key from an iterator may result in a
   "KeyError" exception if the corresponding message is subsequently
   removed.

   Advertencia:

     Be very cautious when modifying mailboxes that might be
     simultaneously changed by some other process.  The safest mailbox
     format to use for such tasks is "Maildir"; try to avoid using
     single-file formats such as "mbox" for concurrent writing.  If
     you're modifying a mailbox, you *must* lock it by calling the
     "lock()" and "unlock()" methods *before* reading any messages in
     the file or making any changes by adding or deleting a message.
     Failing to lock the mailbox runs the risk of losing messages or
     corrupting the entire mailbox.

   "Mailbox" instances have the following methods:

   add(message)

      Añade *message* al buzón de correo y retorna la clave que se le
      ha asignado.

      El parámetro *message* puede ser una instancia "Message", una
      instancia "email.message.Message", una cadena, una cadena de
      bytes o un objeto tipo archivo (que debe estar abierto en modo
      binario). Si *message* es una instancia de la subclase "Message"
      con el formato apropiado (por ejemplo, si es una instancia
      "mboxMessage" y ésta es una instancia "mbox"), se utiliza su
      información de formato específico. En caso contrario, se
      utilizan valores por defecto razonables para la información
      específica del formato.

      Distinto en la versión 3.2: Se añadió el soporte para la entrada
      binaria.

   remove(key)
   __delitem__(key)
   discard(key)

      Borre el mensaje correspondiente a la *key* del buzón de correo.

      Si no existe tal mensaje, se lanza una excepción "KeyError" si
      el método se llamó "remove()" o "__delitem__()" pero no se lanza
      una excepción si el método se llamó "discard()". El
      comportamiento de "discard()" puede ser preferido si el formato
      de buzón subyacente soporta la modificación concurrente por
      otros procesos.

   __setitem__(key, message)

      Reemplaza el mensaje correspondiente a *key* por *message*.
      Levante una excepción "KeyError" si ningún mensaje ya
      corresponde a *key*.

      Al igual que "add()", el parámetro *message* puede ser una
      instancia "Message", una instancia "email.message.Message", una
      cadena, una cadena de bytes, o un objeto tipo archivo (que debe
      estar abierto en modo binario). Si *message* es una instancia de
      la subclase "Message" con el formato apropiado (por ejemplo, si
      es una instancia "mboxMessage" y ésta es una instancia "mbox"),
      se utiliza su información de formato específico. En caso
      contrario, la información específica del formato del mensaje que
      actualmente corresponde a *key* se deja sin cambios.

   iterkeys()

      Return an *iterator* over all keys

   keys()

      The same as "iterkeys()", except that a "list" is returned
      rather than an *iterator*

   itervalues()
   __iter__()

      Return an *iterator* over representations of all messages. The
      messages are represented as instances of the appropriate format-
      specific "Message" subclass unless a custom message factory was
      specified when the "Mailbox" instance was initialized.

      Nota:

        El comportamiento de "__iter__()" es diferente al de los
        diccionarios, que iteran sobre las claves.

   values()

      The same as "itervalues()", except that a "list" is returned
      rather than an *iterator*

   iteritems()

      Return an *iterator* over (*key*, *message*) pairs, where *key*
      is a key and *message* is a message representation. The messages
      are represented as instances of the appropriate format-specific
      "Message" subclass unless a custom message factory was specified
      when the "Mailbox" instance was initialized.

   items()

      The same as "iteritems()", except that a "list" of pairs is
      returned rather than an *iterator* of pairs.

   get(key, default=None)
   __getitem__(key)

      Return a representation of the message corresponding to *key*.
      If no such message exists, *default* is returned if the method
      was called as "get()" and a "KeyError" exception is raised if
      the method was called as "__getitem__()". The message is
      represented as an instance of the appropriate format-specific
      "Message" subclass unless a custom message factory was specified
      when the "Mailbox" instance was initialized.

   get_message(key)

      Retorna una representación del mensaje correspondiente a *key*
      como una instancia de la subclase "Message" específica del
      formato, o lanza una excepción "KeyError" si no existe tal
      mensaje.

   get_bytes(key)

      Retorna una representación en bytes del mensaje correspondiente
      a *key*, o lanza una excepción "KeyError" si no existe tal
      mensaje.

      Added in version 3.2.

   get_string(key)

      Retorna una representación en cadena del mensaje correspondiente
      a *key*, o lanza una excepción "KeyError" si no existe tal
      mensaje.  El mensaje se procesa a través de
      "email.message.Message" para convertirlo en una representación
      limpia de 7 bits.

   get_file(key)

      Return a *file-like* representation of the message corresponding
      to *key*, or raise a "KeyError" exception if no such message
      exists.  The file-like object behaves as if open in binary mode.
      This file should be closed once it is no longer needed.

      Distinto en la versión 3.2: The file object really is a *binary
      file*; previously it was incorrectly returned in text mode.
      Also, the *file-like object* now supports the *context manager*
      protocol: you can use a "with" statement to automatically close
      it.

      Nota:

        Unlike other representations of messages, *file-like*
        representations are not necessarily independent of the
        "Mailbox" instance that created them or of the underlying
        mailbox.  More specific documentation is provided by each
        subclass.

   __contains__(key)

      Retorna "True" si "key" corresponde a un mensaje, si no "False".

   __len__()

      Retorna un recuento de los mensajes en el buzón de correo.

   clear()

      Borrar todos los mensajes del buzón.

   pop(key, default=None)

      Return a representation of the message corresponding to *key*
      and delete the message. If no such message exists, return
      *default*. The message is represented as an instance of the
      appropriate format-specific "Message" subclass unless a custom
      message factory was specified when the "Mailbox" instance was
      initialized.

   popitem()

      Return an arbitrary (*key*, *message*) pair, where *key* is a
      key and *message* is a message representation, and delete the
      corresponding message. If the mailbox is empty, raise a
      "KeyError" exception. The message is represented as an instance
      of the appropriate format-specific "Message" subclass unless a
      custom message factory was specified when the "Mailbox" instance
      was initialized.

   update(arg)

      Parameter *arg* should be a *key*-to-*message* mapping or an
      iterable of (*key*, *message*) pairs. Updates the mailbox so
      that, for each given *key* and *message*, the message
      corresponding to *key* is set to *message* as if by using
      "__setitem__()". As with "__setitem__()", each *key* must
      already correspond to a message in the mailbox or else a
      "KeyError" exception will be raised, so in general it is
      incorrect for *arg* to be a "Mailbox" instance.

      Nota:

        A diferencia de los diccionarios, los argumentos de las
        palabras clave no están soportados.

   flush()

      Write any pending changes to the filesystem. For some "Mailbox"
      subclasses, changes are always written immediately and "flush()"
      does nothing, but you should still make a habit of calling this
      method.

   lock()

      Adquiera un aviso exclusivo de bloqueo en el buzón de correo
      para que otros procesos sepan que no deben modificarlo. Un
      "ExternalClashError" se lanza si el bloqueo no está disponible.
      Los mecanismos de bloqueo particulares utilizados dependen del
      formato del buzón de correo.  Deberías *siempre* bloquear el
      buzón antes de hacer cualquier modificación a su contenido.

   unlock()

      Libera el bloqueo del buzón de correo, si lo hay.

   close()

      Flush the mailbox, unlock it if necessary, and close any open
      files. For some "Mailbox" subclasses, this method does nothing.

### "Maildir" objects

class mailbox.Maildir(dirname, factory=None, create=True)

   Una subclase de "Mailbox"  para los buzones de correo en formato
   Maildir. El parámetro *factory* es un objeto invocable que acepta
   una representación de mensaje tipo archivo (que se comporta como si
   se abriera en modo binario) y retorna una representación
   personalizada. Si *factory* es "None", "MaildirMessage" se utiliza
   como representación de mensaje por defecto. Si *create* es "True",
   el buzón se crea si no existe.

   Si *create* es "True" y la ruta de *dirname* existe, será tratado
   como un *maildir* existente sin intentar verificar su diseño de
   directorio.

   Es por razones históricas que *dirname* es nombrado como tal en
   lugar de *path*.

   Maildir es un formato de buzón de correo basado en un directorio
   inventado para el agente de transferencia de correo qmail y ahora
   ampliamente soportado por otros programas. Los mensajes en un buzón
   de correo de Maildir se almacenan en archivos separados dentro de
   una estructura de directorio común. Este diseño permite que los
   buzones de Maildir sean accedidos y modificados por múltiples
   programas no relacionados sin corrupción de datos, por lo que el
   bloqueo de archivos es innecesario.

   Los buzones de correo de Maildir contienen tres subdirectorios, a
   saber: "tmp", "new", y "cur". Los mensajes se crean momentáneamente
   en el subdirectorio "tmp" y luego se mueven al subdirectorio "new"
   para finalizar la entrega. Un agente de usuario de correo puede
   posteriormente mover el mensaje al subdirectorio "cur" y almacenar
   la información sobre el estado del mensaje en una sección especial
   "info" adjunta a su nombre de archivo.

   Folders of the style introduced by the Courier mail transfer agent
   are also supported. Any subdirectory of the main mailbox is
   considered a folder if "'.'" is the first character in its name.
   Folder names are represented by "Maildir" without the leading
   "'.'". Each folder is itself a Maildir mailbox but should not
   contain other folders. Instead, a logical nesting is indicated
   using "'.'" to delimit levels, e.g., "Archived.2005.07".

   colon

      La especificación Maildir requiere el uso de dos puntos ("':'")
      en ciertos nombres de archivos de mensajes. Sin embargo, algunos
      sistemas operativos no permiten este carácter en los nombres de
      archivo, si desea utilizar un formato similar a Maildir en dicho
      sistema operativo, debe especificar otro carácter para
      utilizarlo en su lugar. El signo de exclamación ("'!'") es una
      elección popular. Por ejemplo:

         import mailbox
         mailbox.Maildir.colon = '!'

      The "colon" attribute may also be set on a per-instance basis.

   Distinto en la versión 3.13: "Maildir" now ignores files with a
   leading dot.

   "Maildir" instances have all of the methods of "Mailbox" in
   addition to the following:

   list_folders()

      Retorna una lista con los nombres de todas las carpetas.

   get_folder(folder)

      Return a "Maildir" instance representing the folder whose name
      is *folder*. A "NoSuchMailboxError" exception is raised if the
      folder does not exist.

   add_folder(folder)

      Create a folder whose name is *folder* and return a "Maildir"
      instance representing it.

   remove_folder(folder)

      Elimina la carpeta cuyo nombre es *folder*. Si la carpeta
      contiene algún mensaje, se lanzará una excepción "NotEmptyError"
      y la carpeta no se borrará.

   clean()

      Borra los archivos temporales del buzón de correo que no han
      sido accedidos en las últimas 36 horas. La especificación
      Maildir dice que los programas de lectura de correo deben hacer
      esto ocasionalmente.

   get_flags(key)

      Return as a string the flags that are set on the message
      corresponding to *key*. This is the same as
      "get_message(key).get_flags()" but much faster, because it does
      not open the message file. Use this method when iterating over
      the keys to determine which messages are interesting to get.

      If you do have a "MaildirMessage" object, use its "get_flags()"
      method instead, because changes made by the message's
      "set_flags()", "add_flag()" and "remove_flag()" methods are not
      reflected here until the mailbox's "__setitem__()" method is
      called.

      Added in version 3.13.

   set_flags(key, flags)

      On the message corresponding to *key*, set the flags specified
      by *flags* and unset all others. Calling
      "some_mailbox.set_flags(key, flags)" is similar to

         one_message = some_mailbox.get_message(key)
         one_message.set_flags(flags)
         some_mailbox[key] = one_message

      but faster, because it does not open the message file.

      If you do have a "MaildirMessage" object, use its "set_flags()"
      method instead, because changes made with this mailbox method
      will not be visible to the message object's method,
      "get_flags()".

      Added in version 3.13.

   add_flag(key, flag)

      On the message corresponding to *key*, set the flags specified
      by *flag* without changing other flags. To add more than one
      flag at a time, *flag* may be a string of more than one
      character.

      Considerations for using this method versus the message object's
      "add_flag()" method are similar to those for "set_flags()"; see
      the discussion there.

      Added in version 3.13.

   remove_flag(key, flag)

      On the message corresponding to *key*, unset the flags specified
      by *flag* without changing other flags. To remove more than one
      flag at a time, *flag* may be a string of more than one
      character.

      Considerations for using this method versus the message object's
      "remove_flag()" method are similar to those for "set_flags()";
      see the discussion there.

      Added in version 3.13.

   get_info(key)

      Return a string containing the info for the message
      corresponding to *key*. This is the same as
      "get_message(key).get_info()" but much faster, because it does
      not open the message file. Use this method when iterating over
      the keys to determine which messages are interesting to get.

      If you do have a "MaildirMessage" object, use its "get_info()"
      method instead, because changes made by the message's
      "set_info()" method are not reflected here until the mailbox's
      "__setitem__()" method is called.

      Added in version 3.13.

   set_info(key, info)

      Set the info of the message corresponding to *key* to *info*.
      Calling "some_mailbox.set_info(key, flags)" is similar to

         one_message = some_mailbox.get_message(key)
         one_message.set_info(info)
         some_mailbox[key] = one_message

      but faster, because it does not open the message file.

      If you do have a "MaildirMessage" object, use its "set_info()"
      method instead, because changes made with this mailbox method
      will not be visible to the message object's method,
      "get_info()".

      Added in version 3.13.

   Some "Mailbox" methods implemented by "Maildir" deserve special
   remarks:

   add(message)
   __setitem__(key, message)
   update(arg)

      Advertencia:

        Estos métodos generan nombres de archivo únicos basados en el
        ID del proceso actual. Cuando se utilizan varios hilos, pueden
        producirse conflictos de nombres no detectados y causar la
        corrupción del buzón de correo a menos que se coordinen los
        hilos para evitar que se utilicen estos métodos para manipular
        el mismo buzón de correo simultáneamente.

   flush()

      Todos los cambios en los buzones de Maildir se aplican
      inmediatamente, así que este método no hace nada.

   lock()
   unlock()

      Los buzones de Maildir no admiten (o requieren) bloqueo, por lo
      que estos métodos no hacen nada.

   close()

      "Maildir" instances do not keep any open files and the
      underlying mailboxes do not support locking, so this method does
      nothing.

   get_file(key)

      Dependiendo de la plataforma del host, puede que no sea posible
      modificar o eliminar el mensaje subyacente mientras el archivo
      retornado permanezca abierto.

Ver también:

  pagina web maildir de Courier
     Una especificación del formato. Describe una extensión común para
     admitir carpetas.

  Utilizando el formato maildir
     Notas sobre Maildir por su inventor. Incluye un esquema
     actualizado de creación de nombres y detalles sobre la "info" de
     la semántica".

### "mbox" objects

class mailbox.mbox(path, factory=None, create=True)

   Una subclase de "Mailbox" para los buzones de correo en formato
   mbox. El parámetro *factory* es un objeto invocable que acepta una
   representación de mensaje tipo archivo (que se comporta como si se
   abriera en modo binario) y retorna una representación
   personalizada. Si *factory* es "None", "mboxMessage" se utiliza
   como representación de mensaje por defecto. Si *create* es "True",
   el buzón de correo se crea si no existe.

   El formato mbox es el formato clásico para almacenar correo en
   sistemas Unix. Todos los mensajes de un buzón de correo mbox se
   almacenan en un único archivo con el comienzo de cada mensaje
   indicado por una línea cuyos cinco primeros caracteres son "From".

   Several variations of the mbox format exist to address perceived
   shortcomings in the original. In the interest of compatibility,
   "mbox" implements the original format, which is sometimes referred
   to as *mboxo*. This means that the *Content-Length* header, if
   present, is ignored and that any occurrences of "From " at the
   beginning of a line in a message body are transformed to ">From "
   when storing the message, although occurrences of ">From " are not
   transformed to "From " when reading the message.

   Some "Mailbox" methods implemented by "mbox" deserve special
   remarks:

   get_bytes(key, from_=False)

      Note: This method has an extra parameter (*from_*) compared with
      other classes. The first line of an mbox file entry is the Unix
      "From " line. If *from_* is False, the first line of the file is
      dropped.

   get_file(key, from_=False)

      Using the file after calling "flush()" or "close()" on the
      "mbox" instance may yield unpredictable results or raise an
      exception.

      Note: This method has an extra parameter (*from_*) compared with
      other classes. The first line of an mbox file entry is the Unix
      "From " line. If *from_* is False, the first line of the file is
      dropped.

   get_string(key, from_=False)

      Note: This method has an extra parameter (*from_*) compared with
      other classes. The first line of an mbox file entry is the Unix
      "From " line. If *from_* is False, the first line of the file is
      dropped.

   lock()
   unlock()

      Se utilizan tres mecanismos de bloqueo---el bloqueo por puntos
      y, si está disponible, las llamadas del sistema "flock()" y
      "lockf()".

Ver también:

  pagina web mbox de tin
     Una especificación del formato, con detalles sobre el bloqueo.

  Configurando el correo de Netscape en Unix: Por qué el formato de
  longitud de contenido es malo
     Un argumento para usar el formato original mbox en lugar de una
     variación.

  "mbox" es una familia de varios formatos de buzón de correo
  mutuamente incompatibles
     Una historia de variaciones de mbox.

### "MH" objects

class mailbox.MH(path, factory=None, create=True)

   Una subclase de "Mailbox" para los buzones de correo en formato MH.
   El parámetro *factory* es un objeto invocable que acepta una
   representación de mensaje tipo archivo (que se comporta como si se
   abriera en modo binario) y retorna una representación
   personalizada. Si *factory* es "None", "MHMessage" se utiliza como
   representación de mensaje por defecto. Si *create* es "True", el
   buzón de correo se crea si no existe.

   MH es un formato de buzón de correo basado en un directorio
   inventado para el Sistema de Manejo de Mensajes MH, un agente de
   usuario de correo. Cada mensaje de un buzón de correo MH reside en
   su propio archivo. Un buzón de correo MH puede contener otros
   buzones de correos MH (llamados *folders*) además de los mensajes.
   Las carpetas pueden anidarse indefinidamente. Los buzones de correo
   MH también soportan *sequences*, que son listas con nombre usadas
   para agrupar lógicamente los mensajes sin moverlos a subcarpetas.
   Las secuencias se definen en un archivo llamado ".mh_sequences" en
   cada carpeta.

   The "MH" class manipulates MH mailboxes, but it does not attempt to
   emulate all of **mh**'s behaviors. In particular, it does not
   modify and is not affected by the "context" or ".mh_profile" files
   that are used by **mh** to store its state and configuration.

   "MH" instances have all of the methods of "Mailbox" in addition to
   the following:

   Distinto en la versión 3.13: Supported folders that don't contain a
   ".mh_sequences" file.

   list_folders()

      Retorna una lista con los nombres de todas las carpetas.

   get_folder(folder)

      Return an "MH" instance representing the folder whose name is
      *folder*. A "NoSuchMailboxError" exception is raised if the
      folder does not exist.

   add_folder(folder)

      Create a folder whose name is *folder* and return an "MH"
      instance representing it.

   remove_folder(folder)

      Elimina la carpeta cuyo nombre es *folder*. Si la carpeta
      contiene algún mensaje, se lanzará una excepción "NotEmptyError"
      y la carpeta no se borrará.

   get_sequences()

      Retorna un diccionario de nombres de secuencias mapeadas a
      listas clave. Si no hay secuencias, se retorna el diccionario
      vacío.

   set_sequences(sequences)

      Re-define las secuencias que existen en el buzón de correo
      basado en *sequences*, un diccionario de nombres mapeados a
      listas de claves, como las retornadas por "get_sequences()".

   pack()

      Renombra los mensajes en el buzón de correo según sea necesario
      para eliminar los huecos en la numeración.  Las entradas en la
      lista de secuencias se actualizan correspondientemente.

      Nota:

        Las llaves ya emitidas quedan invalidadas por esta operación y
        no deben utilizarse posteriormente.

   Some "Mailbox" methods implemented by "MH" deserve special remarks:

   remove(key)
   __delitem__(key)
   discard(key)

      Estos métodos borran inmediatamente el mensaje. No se utiliza la
      convención del MH de marcar un mensaje para borrarlo poniendo
      una coma en su nombre.

   lock()
   unlock()

      Se utilizan tres mecanismos de bloqueo---el bloqueo por puntos
      y, si está disponible, las llamadas del sistema "flock()" y
      "lockf()". Para los buzones de correos MH, bloquear el buzón de
      correo significa bloquear el archivo ".mh_sequences" y, sólo
      durante la duración de cualquier operación que les afecte,
      bloquear los archivos de mensajes individuales.

   get_file(key)

      Dependiendo de la plataforma anfitriona, puede que no sea
      posible eliminar el mensaje subyacente mientras el archivo
      retornado permanezca abierto.

   flush()

      Todos los cambios en los buzones de correos de Maildir se
      aplican inmediatamente, así que este método no hace nada.

   close()

      "MH" instances do not keep any open files, so this method is
      equivalent to "unlock()".

Ver también:

  nmh - Sistema de Manejo de Mensajes
     Página principal de **nmh**, una versión actualizada del original
     **mh**.

  MH & nmh: Correo electrónico para usuarios y programadores
     Un libro con licencia GPL sobre **mh** y **nmh**, con alguna
     información sobre el formato del buzón.

### "Babyl" objects

class mailbox.Babyl(path, factory=None, create=True)

   Una subclase de "Mailbox" para los buzones en formato Babyl. El
   parámetro *factory* es un objeto invocable que acepta una
   representación de mensaje tipo archivo (que se comporta como si se
   abriera en modo binario) y retorna una representación
   personalizada. Si *factory* es "None", "BabylMessage" se utiliza
   como representación de mensaje por defecto. Si *create* es "True",
   el buzón se crea si no existe.

   Babyl es un formato de buzón de un solo archivo usado por el agente
   de usuario de correo de Rmail incluido en Emacs. El comienzo de un
   mensaje se indica con una línea que contiene los dos caracteres
   Control-Underscore ("'\037'") y Control-L ("'\014'"). El final de
   un mensaje se indica con el comienzo del siguiente mensaje o, en el
   caso del último mensaje, una línea que contiene un carácter
   Control-Underscore ("'\037'").

   Los mensajes en un buzón de correo de Babyl tienen dos juegos de
   encabezados, los encabezados originales y los llamados encabezados
   visibles. Los encabezados visibles son típicamente un subconjunto
   de los encabezados originales que han sido reformateados o
   abreviados para ser más atractivos. Cada mensaje de un buzón de
   correo de Babyl también tiene una lista de *labels*, o cadenas
   cortas que registran información adicional sobre el mensaje, y una
   lista de todas las etiquetas definidas por el usuario que se
   encuentran en el buzón de correo se mantiene en la sección de
   opciones de Babyl.

   "Babyl" instances have all of the methods of "Mailbox" in addition
   to the following:

   get_labels()

      Retorna una lista de los nombres de todas las etiquetas
      definidas por el usuario utilizadas en el buzón de correo.

      Nota:

        Los mensajes actuales se inspeccionan para determinar qué
        etiquetas existen en el buzón de correo en lugar de consultar
        la lista de etiquetas en la sección de opciones de Babyl, pero
        la sección de Babyl se actualiza cada vez que se modifica el
        buzón de correo.

   Some "Mailbox" methods implemented by "Babyl" deserve special
   remarks:

   get_file(key)

      En los buzones de correos de Babyl, los encabezados de un
      mensaje no se almacenan contiguamente al cuerpo del mensaje.
      Para generar una representación tipo archivo, las cabeceras y el
      cuerpo se copian juntos en una instancia "io.BytesIO", que tiene
      una API idéntica a la de un archivo. Como resultado, el objeto
      similar a un archivo es verdaderamente independiente del buzón
      de correo subyacente, pero no ahorra memoria en comparación con
      una representación en cadena.

   lock()
   unlock()

      Se utilizan tres mecanismos de bloqueo---el bloqueo por puntos
      y, si está disponible, las llamadas del sistema "flock()" y
      "lockf()".

Ver también:

  Formato de la versión 5 de los archivos de Babyl
     Una especificación del formato Babyl.

  Leyendo el correo con Rmail
     El manual de Rmail, con cierta información sobre la semántica
     Babyl.

### "MMDF" objects

class mailbox.MMDF(path, factory=None, create=True)

   Una subclase de "Mailbox" para buzones de correos en formato MMDF.
   El parámetro *factory* es un objeto al que se puede llamar que
   acepta una representación de mensaje similar a un archivo (que se
   comporta como si se abriera en modo binario) y retorna una
   representación personalizada. Si *factory* es "None", "MMDFMessage"
   se utiliza como representación de mensaje predeterminada. Si
   *create* es "True", el buzón de correo se crea si no existe.

   MMDF es un formato de buzón de correo de un solo archivo inventado
   para el centro de distribución de memorandos multicanal, un agente
   de transferencia de correo. Cada mensaje está en la misma forma que
   un mensaje de mbox, pero está entre corchetes antes y después por
   líneas que contienen cuatro caracteres Control-A ("'\001'"). Al
   igual que con el formato mbox, el principio de cada mensaje se
   indica mediante una línea cuyos primeros cinco caracteres son "From
   ", pero las apariciones adicionales de "From" no se transforman en
   ">From" al almacenar mensajes porque las líneas de separador de
   mensajes adicionales impiden confundir tales ocurrencias para los
   inicios de los mensajes posteriores.

   Some "Mailbox" methods implemented by "MMDF" deserve special
   remarks:

   get_bytes(key, from_=False)

      Note: This method has an extra parameter (*from_*) compared with
      other classes. The first line of an mbox file entry is the Unix
      "From " line. If *from_* is False, the first line of the file is
      dropped.

   get_file(key, from_=False)

      Using the file after calling "flush()" or "close()" on the
      "MMDF" instance may yield unpredictable results or raise an
      exception.

      Note: This method has an extra parameter (*from_*) compared with
      other classes. The first line of an mbox file entry is the Unix
      "From " line. If *from_* is False, the first line of the file is
      dropped.

   lock()
   unlock()

      Se utilizan tres mecanismos de bloqueo---el bloqueo por puntos
      y, si está disponible, las llamadas del sistema "flock()" y
      "lockf()".

Ver también:

  Página web de mmdf de tin
     Una especificación del formato MMDF de la documentación de tin,
     un lector de noticias.

  MMDF
     Un artículo de Wikipedia que describe el Centro de Distribución
     de Memorandos Multicanal.

## "Message" objects

class mailbox.Message(message=None)

   A subclass of the "email.message" module's "Message". Subclasses of
   "mailbox.Message" add mailbox-format-specific state and behavior.

   If *message* is omitted, the new instance is created in a default,
   empty state. If *message* is an "email.message.Message" instance,
   its contents are copied; furthermore, any format-specific
   information is converted insofar as possible if *message* is a
   "Message" instance. If *message* is a string, a byte string, or a
   file, it should contain an **RFC 5322**-compliant message, which is
   read and parsed.  Files should be open in binary mode, but text
   mode files are accepted for backward compatibility.

   El estado y los comportamientos específicos del formato que ofrecen
   las subclases varían, pero en general sólo se admiten las
   propiedades que no son específicas de un buzón de correo concreto
   (aunque presumiblemente las propiedades son específicas de un
   formato de buzón de correo concreto). Por ejemplo, no se conservan
   las compensaciones de archivos para los formatos de buzón de correo
   de un solo archivo ni los nombres de archivo para los formatos de
   buzón de correo basados en directorios, porque sólo son aplicables
   al buzón de correo original. Pero sí se conservan las declaraciones
   tales como si un mensaje ha sido leído por el usuario o marcado
   como importante, porque se aplican al propio mensaje.

   There is no requirement that "Message" instances be used to
   represent messages retrieved using "Mailbox" instances. In some
   situations, the time and memory required to generate "Message"
   representations might not be acceptable. For such situations,
   "Mailbox" instances also offer string and file-like
   representations, and a custom message factory may be specified when
   a "Mailbox" instance is initialized.

### "MaildirMessage" objects

class mailbox.MaildirMessage(message=None)

   Un mensaje con comportamientos específicos de Maildir. El parámetro
   *message* tiene el mismo significado que con el constructor
   "Message".

   Típicamente, una aplicación de agente de usuario de correo mueve
   todos los mensajes del subdirectorio "new" al subdirectorio "cur"
   después de la primera vez que el usuario abre y cierra el buzón de
   coreo, registrando que los mensajes son antiguos, tanto si han sido
   leídos como si no. Cada mensaje en "cur" tiene una sección "info"
   añadida a su nombre de archivo para almacenar información sobre su
   estado. (Algunos lectores de correo también pueden añadir una
   sección "info" a los mensajes en "new".)  La sección "info" puede
   tomar una de dos formas: puede contener "2", seguido de una lista
   de flags estandarizados (por ejemplo, "2,FR") o puede contener "1",
   seguido de la llamada información experimental. Los flags
   normalizados para los mensajes de Maildir son los siguientes:

   +--------+-----------+----------------------------------+
   | Flag   | Signific  | Explicación                      |
   |        | ado       |                                  |
   |========|===========|==================================|
   | D      | Borrador  | Bajo composición                 |
   +--------+-----------+----------------------------------+
   | F      | Marcada   | Marcado como importante          |
   +--------+-----------+----------------------------------+
   | P      | Aprobado  | Enviado, reenviado o rebotado    |
   +--------+-----------+----------------------------------+
   | R      | Contesta  | Contestado a                     |
   |        | do        |                                  |
   +--------+-----------+----------------------------------+
   | S      | Visto     | Leído                            |
   +--------+-----------+----------------------------------+
   | T      | Destruido | Marcado para su posterior        |
   |        |           | eliminación                      |
   +--------+-----------+----------------------------------+

   "MaildirMessage" instances offer the following methods:

   get_subdir()

      Retorna "new" (si el mensaje debe ser almacenado en el
      subdirectorio "new") o "cur" (si el mensaje debe ser almacenado
      en el subdirectorio "cur").

      Nota:

        A message is typically moved from "new" to "cur" after its
        mailbox has been accessed, whether or not the message has been
        read. A message "msg" has been read if ""S" in
        msg.get_flags()" is "True".

   set_subdir(subdir)

      Establece el subdirectorio en el que debe almacenarse el
      mensaje. El parámetro *subdir* debe ser "new" o "cur".

   get_flags()

      Retorna una cadena que especifica los flags que están
      actualmente establecidos. Si el mensaje cumple con el formato
      estándar de Maildir, el resultado es la concatenación en orden
      alfabético de cero o una ocurrencia de cada una de los flags
      "'D'", "'F'", "'P'", "'R'", "'S'", y "'T'". La cadena vacía se
      retorna si no hay flags o si "info" contiene semántica
      experimental.

   set_flags(flags)

      Establece los flags especificados por *flags* y desactiva todas
      las demás.

   add_flag(flag)

      Establece lo(s) flag(s) especificado(s) por *flags* sin cambiar
      otros flags. Para añadir más de un indicador a la vez, *flag*
      puede ser una cadena de más de un carácter. La "info" actual se
      sobrescribe si contiene o no información experimental en lugar
      de flags.

   remove_flag(flag)

      Unset the flag(s) specified by *flag* without changing other
      flags. To remove more than one flag at a time, *flag* may be a
      string of more than one character.  If "info" contains
      experimental information rather than flags, the current "info"
      is not modified.

   get_date()

      Retorna la fecha de entrega del mensaje como un número de punto
      flotante que representa los segundos desde la época.

   set_date(date)

      Establece la fecha de entrega del mensaje en *date*, un número
      de punto flotante que representa los segundos desde la época.

   get_info()

      Retorna una cadena que contiene la "info" de un mensaje. Esto es
      útil para acceder y modificar la "info" que es experimental (es
      decir, no una lista de flags).

   set_info(info)

      Establece "info" en *info*, que debería ser una cadena.

When a "MaildirMessage" instance is created based upon an
"mboxMessage" or "MMDFMessage" instance, the *Status* and *X-Status*
headers are omitted and the following conversions take place:

+----------------------+------------------------------------------------+
| Estado resultante    | Estado "mboxMessage" o "MMDFMessage"           |
|======================|================================================|
## | subdirectorio "cur"  | flag O                                         |

## | flag F               | flag F                                         |

## | flag R               | flag A                                         |

## | flag S               | flag R                                         |

## | flag T               | flag D                                         |

When a "MaildirMessage" instance is created based upon an "MHMessage"
instance, the following conversions take place:

+---------------------------------+----------------------------+
| Estado resultante               | Estado "MHMessage"         |
|=================================|============================|
| subdirectorio "cur"             | Secuencia "*unseen*" (no   |
## |                                 | vista)                     |

| subdirectorio "cur" e indicador | no hay una secuencia       |
## | S                               | "*unseen*" (invisible)     |

| flag F                          | secuencia "*flagged*"      |
## |                                 | (marcada)                  |

| flag R                          | Secuencia "*replied*"      |
## |                                 | (respondida)               |

When a "MaildirMessage" instance is created based upon a
"BabylMessage" instance, the following conversions take place:

+---------------------------------+---------------------------------+
| Estado resultante               | Estado "BabylMessage"           |
|=================================|=================================|
## | subdirectorio "cur"             | etiqueta "*unseen*" (invisible) |

| subdirectorio "cur" e indicador | no hay una etiqueta "*unseen*"  |
## | S                               | (invisible)                     |

| flag P                          | etiqueta "*forwarded*" o        |
## |                                 | "*resent*" (reenviado)          |

| flag R                          | etiqueta de "*answered*"        |
## |                                 | (contestado)                    |

## | flag T                          | etiqueta "deleted" (borrado)    |

### "mboxMessage" objects

class mailbox.mboxMessage(message=None)

   Un mensaje con comportamientos específicos de mbox. El parámetro
   *message* tiene el mismo significado que con el constructor
   "Message".

   Los mensajes en un buzón de correo de mbox se almacenan juntos en
   un solo archivo. La dirección del sobre del remitente y la hora de
   entrega se almacenan normalmente en una línea que comienza con
   "From" que se utiliza para indicar el comienzo de un mensaje,
   aunque hay una variación considerable en el formato exacto de estos
   datos entre las implementaciones de mbox. Los flags del estado del
   mensaje, como por ejemplo si ha sido leído o marcado como
   importante, se almacenan típicamente en las cabeceras *Status* y
   *X-Status*.

   Los flags convencionales para los mensajes de mbox son los
   siguientes:

   +--------+------------+----------------------------------+
   | Flag   | Significa  | Explicación                      |
   |        | do         |                                  |
   |========|============|==================================|
   | R      | Leído      | Leído                            |
   +--------+------------+----------------------------------+
   | O      | Antiguo    | Anteriormente detectado por MUA  |
   +--------+------------+----------------------------------+
   | D      | Borrado    | Marcado para su posterior        |
   |        |            | eliminación                      |
   +--------+------------+----------------------------------+
   | F      | Marcada    | Marcado como importante          |
   +--------+------------+----------------------------------+
   | A      | Respondido | Contestado a                     |
   +--------+------------+----------------------------------+

   Los flags "R" y "O" se almacenan en el encabezado *Status* y los
   flags "D", "F" y "A" se almacenan en el encabezado *X-Status*. Los
   flags y los encabezados aparecen típicamente en el orden
   mencionado.

   "mboxMessage" instances offer the following methods:

   get_from()

      Retorna una cadena que representa la línea "From" que marca el
      inicio del mensaje en un buzón de correo de mbox. El "From"
      inicial y la nueva línea final están excluidas.

   set_from(from_, time_=None)

      Set the "From " line to *from_*, which should be specified
      without a leading "From " or trailing newline. For convenience,
      *time_* may be specified and will be formatted appropriately and
      appended to *from_*. If *time_* is specified, it should be a
      "time.struct_time" instance, a tuple suitable for passing to
      "time.strftime()", or "True" (to use "time.gmtime()").

   get_flags()

      Retorna una cadena que especifica los flags que están
      actualmente establecidos. Si el mensaje cumple con el formato
      convencional, el resultado es la concatenación en el siguiente
      orden de cero o una ocurrencia de cada uno de los flags "'R'",
      "'O'", "'D'", "'F'", and "'A'".

   set_flags(flags)

      Establece los flags especificadas por *flags* y desactiva todos
      las demás. El parámetro *flags* debe ser la concatenación en
      cualquier orden de cero o más ocurrencias de cada uno de los
      flags "'R'", "'O'", "'D'", "'F'", and "'A'".

   add_flag(flag)

      Establece lo(s) flag(s) especificado(s) por *flag* sin cambiar
      otros flags. Para añadir más de un indicador a la vez, *flag*
      puede ser una cadena de más de un carácter.

   remove_flag(flag)

      Unset the flag(s) specified by *flag* without changing other
      flags. To remove more than one flag at a time, *flag* may be a
      string of more than one character.

When an "mboxMessage" instance is created based upon a
"MaildirMessage" instance, a "From " line is generated based upon the
"MaildirMessage" instance's delivery date, and the following
conversions take place:

+-------------------+---------------------------------+
| Estado resultante | Estado de "MaildirMessage"      |
|===================|=================================|
## | flag R            | flag S                          |

## | flag O            | subdirectorio "cur"             |

## | flag D            | flag T                          |

## | flag F            | flag F                          |

## | flag A            | flag R                          |

When an "mboxMessage" instance is created based upon an "MHMessage"
instance, the following conversions take place:

+---------------------+----------------------------+
| Estado resultante   | Estado "MHMessage"         |
|=====================|============================|
| flag R y flag O     | no hay una secuencia       |
## |                     | "*unseen*" (invisible)     |

| flag O              | Secuencia "*unseen*" (no   |
## |                     | vista)                     |

| flag F              | secuencia "*flagged*"      |
## |                     | (marcada)                  |

| flag A              | Secuencia "*replied*"      |
## |                     | (respondida)               |

When an "mboxMessage" instance is created based upon a "BabylMessage"
instance, the following conversions take place:

+---------------------+-------------------------------+
| Estado resultante   | Estado "BabylMessage"         |
|=====================|===============================|
| flag R y flag O     | no hay una etiqueta           |
## |                     | "*unseen*" (invisible)        |

| flag O              | etiqueta "*unseen*"           |
## |                     | (invisible)                   |

## | flag D              | etiqueta "deleted" (borrado)  |

| flag A              | etiqueta de "*answered*"      |
## |                     | (contestado)                  |

When a "mboxMessage" instance is created based upon an "MMDFMessage"
instance, the "From " line is copied and all flags directly
correspond:

+-------------------+------------------------------+
| Estado resultante | Estado de "MMDFMessage"      |
|===================|==============================|
## | flag R            | flag R                       |

## | flag O            | flag O                       |

## | flag D            | flag D                       |

## | flag F            | flag F                       |

## | flag A            | flag A                       |

### "MHMessage" objects

class mailbox.MHMessage(message=None)

   Un mensaje con comportamientos específicos de la HM. El parámetro
   *message* tiene el mismo significado que con el constructor
   "Message".

   Los mensajes de MH no soportan marcas o flags en el sentido
   tradicional, pero sí secuencias, que son agrupaciones lógicas de
   mensajes arbitrarios. Algunos programas de lectura de correo
   (aunque no los estándares **mh** y **nmh**) usan secuencias de
   manera muy similar a los flags que se usan con otros formatos, como
   sigue:

   +------------+--------------------------------------------+
   | Secuencia  | Explicación                                |
   |============|============================================|
   | *unseen*   | No leído, pero previamente detectado por   |
   | (no visto) | la MUA                                     |
   +------------+--------------------------------------------+
   | *replied*  | Contestado a                               |
   | (contesta  |                                            |
   | do)        |                                            |
   +------------+--------------------------------------------+
   | *flagged*  | Marcado como importante                    |
   | (marcado)  |                                            |
   +------------+--------------------------------------------+

   "MHMessage" instances offer the following methods:

   get_sequences()

      Retorna una lista de los nombres de las secuencias que incluyen
      este mensaje.

   set_sequences(sequences)

      Establece la lista de secuencias que incluyen este mensaje.

   add_sequence(sequence)

      Añade *sequence* a la lista de secuencias que incluyen este
      mensaje.

   remove_sequence(sequence)

      Elimina *sequence* de la lista de secuencias que incluyen este
      mensaje.

When an "MHMessage" instance is created based upon a "MaildirMessage"
instance, the following conversions take place:

+----------------------+---------------------------------+
| Estado resultante    | Estado de "MaildirMessage"      |
|======================|=================================|
| Secuencia "*unseen*" | no hay indicador S              |
## | (no vista)           |                                 |

| Secuencia            | flag R                          |
| "*replied*"          |                                 |
## | (respondida)         |                                 |

| secuencia            | flag F                          |
| "*flagged*"          |                                 |
## | (marcada)            |                                 |

When an "MHMessage" instance is created based upon an "mboxMessage" or
"MMDFMessage" instance, the *Status* and *X-Status* headers are
omitted and the following conversions take place:

+----------------------+------------------------------------------------+
| Estado resultante    | Estado "mboxMessage" o "MMDFMessage"           |
|======================|================================================|
| Secuencia "*unseen*" | sin indicador R                                |
## | (no vista)           |                                                |

| Secuencia            | flag A                                         |
| "*replied*"          |                                                |
## | (respondida)         |                                                |

| secuencia            | flag F                                         |
| "*flagged*"          |                                                |
## | (marcada)            |                                                |

When an "MHMessage" instance is created based upon a "BabylMessage"
instance, the following conversions take place:

+----------------------+-------------------------------+
| Estado resultante    | Estado "BabylMessage"         |
|======================|===============================|
| Secuencia "*unseen*" | etiqueta "*unseen*"           |
## | (no vista)           | (invisible)                   |

| Secuencia            | etiqueta de "*answered*"      |
| "*replied*"          | (contestado)                  |
## | (respondida)         |                               |

### "BabylMessage" objects

class mailbox.BabylMessage(message=None)

   Un mensaje con comportamientos específicos de Babyl. El parámetro
   *message* tiene el mismo significado que con el constructor
   "Message".

   Ciertas etiquetas de mensajes, llamadas *attributes*, están
   definidas por convención para tener significados especiales. Los
   atributos son los siguientes:

   +-------------+--------------------------------------------+
   | Etiqueta    | Explicación                                |
   |=============|============================================|
   | *unseen*    | No leído, pero previamente detectado por   |
   | (no visto)  | la MUA                                     |
   +-------------+--------------------------------------------+
   | *deleted*   | Marcado para su posterior eliminación      |
   | (borrado)   |                                            |
   +-------------+--------------------------------------------+
   | *filed*     | Copiado a otro archivo o buzón de correo   |
   | (archivado) |                                            |
   +-------------+--------------------------------------------+
   | *answered*  | Contestado a                               |
   | (contestad  |                                            |
   | o)          |                                            |
   +-------------+--------------------------------------------+
   | *forwarded* | Reenviado                                  |
   | (reenviado) |                                            |
   +-------------+--------------------------------------------+
   | *edited*    | Modificado por el usuario                  |
   | (editado)   |                                            |
   +-------------+--------------------------------------------+
   | *resent*    | Reenviado                                  |
   | (reenviado) |                                            |
   +-------------+--------------------------------------------+

   By default, Rmail displays only visible headers. The "BabylMessage"
   class, though, uses the original headers because they are more
   complete. Visible headers may be accessed explicitly if desired.

   "BabylMessage" instances offer the following methods:

   get_labels()

      Retorna una lista de etiquetas en el mensaje.

   set_labels(labels)

      Establece la lista de etiquetas del mensaje en *labels*.

   add_label(label)

      Añade *label* a la lista de etiquetas del mensaje.

   remove_label(label)

      Eliminar *label* de la lista de etiquetas del mensaje.

   get_visible()

      Return a "Message" instance whose headers are the message's
      visible headers and whose body is empty.

   set_visible(visible)

      Establece los encabezados visibles del mensaje para que sean los
      mismos que los del *message*.  El parámetro *visible* debe ser
      una instancia "Message", una instancia "email.message.Message",
      una cadena, o un objeto tipo archivo (que debe estar abierto en
      modo texto).

   update_visible()

      When a "BabylMessage" instance's original headers are modified,
      the visible headers are not automatically modified to
      correspond. This method updates the visible headers as follows:
      each visible header with a corresponding original header is set
      to the value of the original header, each visible header without
      a corresponding original header is removed, and any of *Date*,
      *From*, *Reply-To*, *To*, *CC*, and *Subject* that are present
      in the original headers but not the visible headers are added to
      the visible headers.

When a "BabylMessage" instance is created based upon a
"MaildirMessage" instance, the following conversions take place:

+---------------------+---------------------------------+
| Estado resultante   | Estado de "MaildirMessage"      |
|=====================|=================================|
| etiqueta "*unseen*" | no hay indicador S              |
## | (invisible)         |                                 |

| etiqueta "deleted"  | flag T                          |
## | (borrado)           |                                 |

| etiqueta de         | flag R                          |
| "*answered*"        |                                 |
## | (contestado)        |                                 |

| etiqueta            | flag P                          |
| "*forwarded*"       |                                 |
## | (reenviado)         |                                 |

When a "BabylMessage" instance is created based upon an "mboxMessage"
or "MMDFMessage" instance, the *Status* and *X-Status* headers are
omitted and the following conversions take place:

+--------------------+------------------------------------------------+
| Estado resultante  | Estado "mboxMessage" o "MMDFMessage"           |
|====================|================================================|
| etiqueta           | sin indicador R                                |
| "*unseen*"         |                                                |
## | (invisible)        |                                                |

| etiqueta "deleted" | flag D                                         |
## | (borrado)          |                                                |

| etiqueta de        | flag A                                         |
| "*answered*"       |                                                |
## | (contestado)       |                                                |

When a "BabylMessage" instance is created based upon an "MHMessage"
instance, the following conversions take place:

+--------------------+----------------------------+
| Estado resultante  | Estado "MHMessage"         |
|====================|============================|
| etiqueta           | Secuencia "*unseen*" (no   |
| "*unseen*"         | vista)                     |
## | (invisible)        |                            |

| etiqueta de        | Secuencia "*replied*"      |
| "*answered*"       | (respondida)               |
## | (contestado)       |                            |

### "MMDFMessage" objects

class mailbox.MMDFMessage(message=None)

   Un mensaje con comportamientos específicos de MMDF. El parámetro
   *message* tiene el mismo significado que con el constructor
   "Message".

   Al igual que los mensajes en un buzón de correo de mbox, los
   mensajes MMDF se almacenan con la dirección del remitente y la
   fecha de entrega en una línea inicial que comienza con "From".  De
   la misma manera, los flags que indican el estado del mensaje se
   almacenan típicamente en las cabeceras *Status* y *X-Status*.

   Los flags convencionales para los mensajes MMDF son idénticos a las
   de los mensajes de mbox y son los siguientes:

   +--------+------------+----------------------------------+
   | Flag   | Significa  | Explicación                      |
   |        | do         |                                  |
   |========|============|==================================|
   | R      | Leído      | Leído                            |
   +--------+------------+----------------------------------+
   | O      | Antiguo    | Anteriormente detectado por MUA  |
   +--------+------------+----------------------------------+
   | D      | Borrado    | Marcado para su posterior        |
   |        |            | eliminación                      |
   +--------+------------+----------------------------------+
   | F      | Marcada    | Marcado como importante          |
   +--------+------------+----------------------------------+
   | A      | Respondido | Contestado a                     |
   +--------+------------+----------------------------------+

   Los flags "R" y "O" se almacenan en el encabezado *Status* y los
   flags "D", "F" y "A" se almacenan en el encabezado *X-Status*. Los
   flags y los encabezados aparecen típicamente en el orden
   mencionado.

   "MMDFMessage" instances offer the following methods, which are
   identical to those offered by "mboxMessage":

   get_from()

      Retorna una cadena que representa la línea "From" que marca el
      inicio del mensaje en un buzón de correo de mbox. El "From"
      inicial y la nueva línea final están excluidas.

   set_from(from_, time_=None)

      Set the "From " line to *from_*, which should be specified
      without a leading "From " or trailing newline. For convenience,
      *time_* may be specified and will be formatted appropriately and
      appended to *from_*. If *time_* is specified, it should be a
      "time.struct_time" instance, a tuple suitable for passing to
      "time.strftime()", or "True" (to use "time.gmtime()").

   get_flags()

      Retorna una cadena que especifica los flags que están
      actualmente establecidos. Si el mensaje cumple con el formato
      convencional, el resultado es la concatenación en el siguiente
      orden de cero o una ocurrencia de cada uno de los flags "'R'",
      "'O'", "'D'", "'F'", and "'A'".

   set_flags(flags)

      Establece los flags especificadas por *flags* y desactiva todos
      las demás. El parámetro *flags* debe ser la concatenación en
      cualquier orden de cero o más ocurrencias de cada uno de los
      flags "'R'", "'O'", "'D'", "'F'", and "'A'".

   add_flag(flag)

      Establece lo(s) flag(s) especificado(s) por *flag* sin cambiar
      otros flags. Para añadir más de un indicador a la vez, *flag*
      puede ser una cadena de más de un carácter.

   remove_flag(flag)

      Unset the flag(s) specified by *flag* without changing other
      flags. To remove more than one flag at a time, *flag* may be a
      string of more than one character.

When an "MMDFMessage" instance is created based upon a
"MaildirMessage" instance, a "From " line is generated based upon the
"MaildirMessage" instance's delivery date, and the following
conversions take place:

+-------------------+---------------------------------+
| Estado resultante | Estado de "MaildirMessage"      |
|===================|=================================|
## | flag R            | flag S                          |

## | flag O            | subdirectorio "cur"             |

## | flag D            | flag T                          |

## | flag F            | flag F                          |

## | flag A            | flag R                          |

When an "MMDFMessage" instance is created based upon an "MHMessage"
instance, the following conversions take place:

+---------------------+----------------------------+
| Estado resultante   | Estado "MHMessage"         |
|=====================|============================|
| flag R y flag O     | no hay una secuencia       |
## |                     | "*unseen*" (invisible)     |

| flag O              | Secuencia "*unseen*" (no   |
## |                     | vista)                     |

| flag F              | secuencia "*flagged*"      |
## |                     | (marcada)                  |

| flag A              | Secuencia "*replied*"      |
## |                     | (respondida)               |

When an "MMDFMessage" instance is created based upon a "BabylMessage"
instance, the following conversions take place:

+---------------------+-------------------------------+
| Estado resultante   | Estado "BabylMessage"         |
|=====================|===============================|
| flag R y flag O     | no hay una etiqueta           |
## |                     | "*unseen*" (invisible)        |

| flag O              | etiqueta "*unseen*"           |
## |                     | (invisible)                   |

## | flag D              | etiqueta "deleted" (borrado)  |

| flag A              | etiqueta de "*answered*"      |
## |                     | (contestado)                  |

When an "MMDFMessage" instance is created based upon an "mboxMessage"
instance, the "From " line is copied and all flags directly
correspond:

+-------------------+------------------------------+
| Estado resultante | Estado de "mboxMessage"      |
|===================|==============================|
## | flag R            | flag R                       |

## | flag O            | flag O                       |

## | flag D            | flag D                       |

## | flag F            | flag F                       |

## | flag A            | flag A                       |

## Excepciones

The following exception classes are defined in the "mailbox" module:

exception mailbox.Error

   The base class for all other module-specific exceptions.

exception mailbox.NoSuchMailboxError

   Se lanza cuando se espera un buzón de correo pero no se encuentra,
   como cuando se instancia una subclase "Mailbox" con una ruta que no
   existe (y con el parámetro *create* establecido en "False"), o
   cuando se abre una carpeta que no existe.

exception mailbox.NotEmptyError

   Se lanza cuando un buzón de correo no está vacío, pero se espera
   que lo esté, como cuando se elimina una carpeta que contiene
   mensajes.

exception mailbox.ExternalClashError

   Raised when some mailbox-related condition beyond the control of
   the program causes it to be unable to proceed, such as when failing
   to acquire a lock that another program already holds, or when a
   uniquely generated file name already exists.

exception mailbox.FormatError

   Se lanza cuando los datos de un archivo no pueden ser analizados,
   como cuando una instancia "MH" intenta leer un archivo
   ".mh_sequences" corrupto.

## Ejemplos

Un simple ejemplo de impresión de los temas de todos los mensajes en
un buzón de correo que parecen interesantes:

   import mailbox
   for message in mailbox.mbox('~/mbox'):
       subject = message['subject']       # Could possibly be None.
       if subject and 'python' in subject.lower():
           print(subject)

Para copiar todo el correo de un buzón de Babyl a un buzón de MH,
convirtiendo toda la información de formato específico que puede ser
convertida:

   import mailbox
   destination = mailbox.MH('~/Mail')
   destination.lock()
   for message in mailbox.Babyl('~/RMAIL'):
       destination.add(mailbox.MHMessage(message))
   destination.flush()
   destination.unlock()

Este ejemplo clasifica el correo de varias listas de correo en
diferentes buzones, teniendo cuidado de evitar la corrupción del
correo debido a la modificación simultánea por otros programas, la
pérdida de correo debido a la interrupción del programa, o la
terminación prematura debido a mensajes malformados en el buzón:

   import mailbox
   import email.errors

   list_names = ('python-list', 'python-dev', 'python-bugs')

   boxes = {name: mailbox.mbox('~/email/%s' % name) for name in list_names}
   inbox = mailbox.Maildir('~/Maildir', factory=None)

   for key in inbox.iterkeys():
       try:
           message = inbox[key]
       except email.errors.MessageParseError:
           continue                # The message is malformed. Just leave it.

       for name in list_names:
           list_id = message['list-id']
           if list_id and name in list_id:
               # Get mailbox to use
               box = boxes[name]

               # Write copy to disk before removing original.
               # If there's a crash, you might duplicate a message, but
               # that's better than losing a message completely.
               box.lock()
               box.add(message)
               box.flush()
               box.unlock()

               # Remove original message
               inbox.lock()
               inbox.discard(key)
               inbox.flush()
               inbox.unlock()
               break               # Found destination, so stop looking.

   for box in boxes.itervalues():
       box.close()
