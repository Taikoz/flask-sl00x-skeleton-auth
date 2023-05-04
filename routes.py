"""
    Pour ajouter une route
    dans le variable 'routes'
    ajoutez une nouvelle ligne
    --------------------------------
    {"blueprint": <votre_blueprint>, "prefix": <str:le prefix>}
    ----------------------------------
"""

from Routes.User import user_route
from Routes.Home import home_route

routes = [
    {"blueprint": user_route, "prefix": '/user'},
    {"blueprint": home_route, "prefix": '/'},
          ]
