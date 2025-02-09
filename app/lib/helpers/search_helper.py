SEARCH_OPTIONS = [ 'limit', 'offset', 'sort_column', 'sort_order' ]

def get_search_options(request):
    options = { key: request.get(key) for key in SEARCH_OPTIONS if key in request }
    options = {
        'limit': 100,
        'offset': None,
        'sort_column': 'updated_at',
        'sort_order': 'desc'
    } | options
    if request.get('skip_limit')==True:
        options['limit'] = None
    elif not options['offset']:
        options['offset'] = get_offset(request.get('page', 1), options['limit'])

    return options

def get_offset(page=1, limit=10):
    return ((page or 1) - 1) * limit

def parse_conditions(conditions):
    return conditions
