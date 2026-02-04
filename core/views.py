from django.shortcuts import render

def home(request):
    context = {
        'template': 'partials/home.html',
    }
    if request.htmx:
        return render(request, "partials/home.html", context)
    return render(request, "base.html", context)

def about(request):
    context = {
        'template': 'partials/about.html',
    }
    if request.htmx:
        return render(request, "partials/about.html", context)
    return render(request, "base.html", context)

def contact(request):
    context = {
        'template': 'partials/contact.html',
    }
    if request.htmx:
        return render(request, 'partials/contact.html', context)
    return render(request, 'base.html', context)

def blog(request):
    context = {
        'template': 'partials/blog.html',
    }
    if request.htmx:
        return render(request, 'partials/blog.html', context)
    return render(request, 'base.html', context)


# we can create a reusable function:
"""
from django.shortcuts import render

def render_page(request, template_name, extra_context=None):
    # generic helper to render a page with HTMX support.
    context = {
        "template": f"partials/{template_name}.html",
    }
    if extra_context:
        context.update(extra_context)

    if request.htmx:
        return render(request, context["template"], context)
    return render(request, "base.html", context)
"""

# usage:
"""
def home(request):
    return render_page(request, "home", {"title": "Home Page"})

def about(request):
    return render_page(request, "about", {"title": "About Us"})
"""