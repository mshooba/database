from flask_restx import Api

authorizations = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'x-access-token'
    }
}

api = Api(
    version='1.0',
    title='Flask/Fauna REST API',
    description='A simple Flask/Fauna REST API',
    authorizations=authorizations
)