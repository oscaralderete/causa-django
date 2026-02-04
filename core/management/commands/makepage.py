from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = "Scaffold a new page with template, view, and route"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Page name")

    def handle(self, *args, **options):
        name = options["name"].lower()
        title = name.title()

        # 1. Create template
        template_dir = os.path.join("templates", "partials")
        os.makedirs(template_dir, exist_ok=True)
        template_path = os.path.join(template_dir, f"{name}.html")
        with open(template_path, "w") as f:
            f.write(f"<h1>{title} Page</h1>\n<p>HTMX content here.</p>")
        self.stdout.write(self.style.SUCCESS(f"Template created: {template_path}"))

        # 2. Append view to views.py
        views_path = os.path.join("core", "views.py")
        with open(views_path, "a") as f:
            f.write(
                f"\n\ndef {name}(request):\n"
                f"    if request.htmx:\n"
                f"        return render(request, 'partials/{name}.html')\n"
                f"    return render(request, 'base.html')\n"
            )
        self.stdout.write(self.style.SUCCESS(f"View added to: {views_path}"))

        # 3. Append route to urls.py
        urls_path = os.path.join("config", "urls.py")
        with open(urls_path, "r") as f:
            content = f.read()

        if "from core import views" not in content:
            content = "from core import views\n" + content

        # Add new path at the end
        if f"path('{name}/'" not in content:
            content = content.rstrip() + f"\n    path('{name}/', views.{name}, name='{name}'),\n"

        with open(urls_path, "w") as f:
            f.write(content)

        self.stdout.write(self.style.SUCCESS(f"Route added to: {urls_path}"))

        self.stdout.write(self.style.SUCCESS(f"Page '{title}' scaffolded successfully!"))

# from django.core.management.base import BaseCommand
# import os

# class Command(BaseCommand):
#     help = "Create a new page with view, template, and route"

#     def add_arguments(self, parser):
#         parser.add_argument("name", type=str, help="Page name")

#     def handle(self, *args, **options):
#         name = options["name"]
#         # Create template
#         template_dir = os.path.join("templates", "partials")
#         os.makedirs(template_dir, exist_ok=True)
#         with open(os.path.join(template_dir, f"{name}.html"), "w") as f:
#             f.write(f"<h1>{name.title()} Page</h1>\n<p>HTMX content here.</p>")

#         # Suggest view + url snippet
#         self.stdout.write(self.style.SUCCESS(
#             f"Page '{name}' created. Add this to views.py:\n\n"
#             f"def {name}(request):\n"
#             f"    if request.htmx:\n"
#             f"        return render(request, 'partials/{name}.html')\n"
#             f"    return render(request, 'base.html')\n\n"
#             f"And add to urls.py:\n"
#             f"path('{name}/', views.{name}, name='{name}')"
#         ))
