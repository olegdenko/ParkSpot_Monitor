from django.shortcuts import render


def main(request):
    """
    Renders the main page.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered main page.
    """
    return render(request, 'main_app/index.html', {"title": "Main page"})