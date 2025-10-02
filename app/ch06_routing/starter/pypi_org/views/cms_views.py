import flask

from pypi_org.infrastructure.view_modifiers import response
import pypi_org.services.cms_service as cms_service

blueprint = flask.Blueprint('cms', __name__, template_folder='templates')

@blueprint.route('/<path:full_url>', methods=['GET'])
@response(template_file='cms/page.html')
def cms_page(full_url : str):
    page = cms_service.get_page(full_url)
    if not page:
        return flask.abort(404)
    return page
    # return flask.render_template('home/index.html', packages=test_packages)