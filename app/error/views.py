from app.error import error


@error.errorhandler(404)
def page_not_found():
    return '404'


@error.errorhandler(200)
def page_not_found():
    return '404'