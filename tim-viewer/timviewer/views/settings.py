from pyramid.view import view_config

@view_config(route_name='settings', request_method='GET', renderer='timviewer:templates/settings.pt')
def settings(request):
  author_name = request.matchdict['authorname']
  return { 'author_name':author_name,
           'feature_name':None,
           'api_endpoint':request.registry.settings['mi.api.endpoint'],
           'theme': request.registry.settings['mi.theme.main'] }
