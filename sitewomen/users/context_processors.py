menu = [{'title': 'Про сайт', 'url_name': 'about'},
        {'title': 'Добавити статтю', 'url_name': 'add_page'},
        {'title': 'Зворотній зв`язок', 'url_name': 'contact'},
        ]

def get_women_context(request):
    return {'mainmenu': menu}