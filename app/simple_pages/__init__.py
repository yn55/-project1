"""Error page document for simple pages"""
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_pages = Blueprint('simple_page', __name__,
                         template_folder='templates', static_folder='static')


@simple_pages.route('/', defaults={'page': 'index'})
@simple_pages.route('/<page>')
def show(page):         #pylint: disable= inconsistent-return-statements
    """Error page for simple pages"""
    try:
        return render_template('%s.html' % page)    #pylint: disable= consider-using-f-string
    except TemplateNotFound:
        abort(404)
