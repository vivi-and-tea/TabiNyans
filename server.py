from waitress import serve

from Tabi.wsgi import application

if __name__ == '__main__':
    serve(application)

