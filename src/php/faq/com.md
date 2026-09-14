---
title: PHP y COM
source_url: https://www.php.net/manual/es/faq.com.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: faq/com.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: faq
translation_status: ready
translation_revision: e03526531
order: 1430
---

## PHP y COM

PHP puede ser usado para acceder a objetos COM y DCOM en plataformas Win32.

**Q:** He compilado un DLL para calcular algo. ¿Hay alguna forma de ejecutar ese DLL bajo PHP?

**A:** Si se trata de un DLL simple no hay forma aun de ejecutarlo desde PHP. Si el archivo DLL contiene un servidor COM es posible que pueda acceder a él si implementa la interfaz IDispatch.

**Q:** ¿Qué quiere decir 'Unsupported variant type: xxxx (0xxxxx)'?

**A:** Existen docenas de tipos VARIANT y combinaciones de ellos. La mayoría de ellos son soportados pero algunos aun deben ser implementados. Las matrices no están completamente soportadas. Solo las matrices unidimensionales de índice pueden ser pasadas entre PHP y COM. Si encuentra otros tipos que no sean soportados, por favor repórtelos como un bug (si aun no han sido reportados) y ofrezca tanta información como tenga disponible.

**Q:** ¿Es posible manipular objetos visuales en PHP?

**A:** En general es posible, pero ya que PHP es usado frecuentemente como un lenguaje de scripting web, corre en el contexto de servidores web, por lo que objetos visuales nunca aparecerán en el escritorio de los servidores. Si usa PHP para una aplicación de scripting, p.ej. en conjunto con PHP-GTK, no hay limitaciones al acceder y manipular objetos visuales a través de COM.

**Q:** ¿Puedo almacenar un objeto COM en una sesión?

**A:** No, no puede. Las instancias COM son tratadas como recursos y por lo tanto sólo están disponibles en el contexto de un script único.

**Q:** ¿Cómo puedo atrapar errores de COM?

**A:** La extensión COM lanza excepciones `com_exception`, las cuales puede atrapar y luego inspeccionar el miembro `code` para determinar el siguiente paso.

**Q:** ¿Puedo generar archivos DLL desde scripts PHP como puedo en Perl?

**A:** No, desafortunadamente no existe una herramienta de ese tipo disponible para PHP.

**Q:** ¿Qué quiere decir 'Unable to obtain IDispatch interface for CLSID {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}'?

**A:** Este error puede tener varias razones:

- el valor CLSID es incorrecto

- el archivo DLL solicitado no existe

- el componente solicitado no implementa la interfaz IDispatch

**Q:** ¿Cómo puedo ejecutar un objeto COM desde un servidor remoto?

**A:** Exactamente como ejecuta objetos locales. Tan solo debe pasar la IP de la máquina remota como segundo parámetro al constructor COM.

Asegúrese de que ha definido [com.allow_dcom](#ini.com.allow-dcom)`=``true` en su `php.ini`.

**Q:** Recibo 'DCOM is disabled in C:\ruta...\nombre_script.php on line 6', ¿qué puedo hacer?

**A:** Edite su archivo `php.ini` y defina [com.allow_dcom](#ini.com.allow-dcom)`=``true`.

**Q:** ¿Es posible leer/manipular un objeto ActiveX en una página con PHP?

**A:** Esto no tiene nada que ver con PHP. Los objetos ActiveX son cargados en el lado del cliente si son solicitados por el documento HTML. No hay relación con el script PHP y por lo tanto no hay una interacción directa posible con el lado del servidor.

**Q:** ¿Es posible obtener una instancia en ejecución de un componente?

**A:** Esto es posible con la ayuda de monikers. Si desea obtener múltiples referencias a la misma instancia de word, puede crear esa instancia como se muestra:

```php
<?php
$word = new COM("C:\docs\word.doc");
?>

          
```

Esto creará una nueva instancia si no hay una instancia en ejecución disponible, o devolverá un gestor a la instancia en ejecución, si existe.

**Q:** ¿Hay una forma de manejar un evento enviado desde un objeto COM?

**A:** Puede definir el receptor de un evento y asociarlo usando `com_event_sink`. Es posible usar `com_print_typeinfo` para que PHP genere un esqueleto para la clase receptora del evento.

**Q:** Estoy teniendo problemas al intentar invocar un método de un objeto COM el cual expone más de una interfaz. ¿Qué puedo hacer?

**A:** La respuesta es tan simple como poco satisfactoria. No estamos seguros pero parece que no es posible hacer nada.

**Q:** Así que PHP funciona con COM, ¿qué hay de COM+?

**A:** COM+ extiende COM mediante un marco para administrar componentes a través de MTS y MSMQ pero no hay nada especial que PHP deba soportar para usar tales componentes.

**Q:** Si PHP puede manipular objetos COM, ¿podemos imaginar el uso de MTS para manejar recursos de componentes, en conjunto con PHP?

**A:** PHP por sí mismo no maneja transacciones aun. Por lo tanto si un error ocurre no se inicia un proceso rollback. Si usa componentes que soporten transacciones tendrá que implementar la gestión de transacciones usted mismo.
