from django.shortcuts import render
import os
from django.http import HttpResponse
from .PageParser import PageParser


class PageInfo:
    def __init__(self, name, url):
        self.name = name
        self.url = url


def A11yListView(request):
    page_info_list = []
    # Przygotuj dane z listą stron do wyświetlenia
    file_path = os.path.join(os.path.dirname(__file__), 'urls_kwp.txt')

    with open(file_path, 'r') as file:
        elements = file.readlines()

    for element in elements:
        name = element.split("//")[1]
        name = name.split("/")[0]
        url = element.strip()
        page_info_list.append({'name': name, 'url': url})

    context = {
        'elements': page_info_list,
    }

    return render(request, 'a11y_list.html', context)


def PageDetailsView(request, url):
    parser = PageParser(url)
    elements = parser.get_elements_with_a11y_id()

    context = {
        'elements': elements,
    }

    return render(request, 'page_details.html', context)
