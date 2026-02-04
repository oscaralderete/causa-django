# Causa Python

Cuando desarrollé Causa (https://github.com/CausaWeb/CausaFramework), un framework minimalista para PHP que fue el resultado de experiencias obtenidas "freelanceando" en muchos proyectos hechos con PHP puro. Lo hice porque en mi amplia experiencia sabía que una buena estructura y el uso de las buenas prácticas afectan positivamente a un proyecto, lo hacen escalable y estable.

A poco de haber hecho público y compartido Causa, un feedback recurrente fue: "Cómo hago lo mismo para Python?" de principio indicar que ya existe Unicorn (https://www.django-unicorn.com) que es "el Livewire" de Django, igual que Livewire, Unicorn tiene sus propias reglas y su lifecycle tiene abundantes paralelos con el de Livewire.

Sin embargo tenía en mente desde hace un tiempo hacer un ejercicio de programación para "hacer un Causa para Django" y finalmente lo hice, el repo está ahora disponible en GitHub y espero que les sea útil y se diviertan jugando con el código.

PS: Django a diferencia de Laravel se enfoca en el backend por eso no tenemos Vite o Tailwind en su instalación base, respetando eso este proyecto sólo se enfoca en la parte que gestiona los views y la interacción con HTMX aunque en los paquetes de instalación yo agregué Vite y Tailwind que los dejo ahí por si desean seguir jugando y explorando las posibilidades.

---

## 🚀 Librerías
- Yo comencé agregando Jinja2, Vite, Tailwind y otros, en mi caso en un solo pip agregué lo siguiente a un Django de serie:

```bash
pip install jinja2 django-htmx django-tailwind django-vite django-ninja
```
- Lo siguiente fue crear un 'entry point' o en este caso un template base (base.html) para gestionar que el template correcto se cargue dependiendo si se trata de un request HTMX o no.
- En PHP hay un paquete de Symfony que permite trabajar con el CLI y definir todos los comandos custom que se necesiten, eso no existe en Django pero se hizo lo que se pudo para replicar la creación automática de una página usando el CLI: ./core/management/commands/makepage.py

---

## 🖥️ Vídeo
Preparé un video con la demo, espero que los motive a seguir jugando con el código y los estimule a hacer sus propios desarrollos.
