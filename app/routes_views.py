from flask import Blueprint, render_template
from sqlalchemy import desc
from .models import Leitura


views_blueprint = Blueprint('view', __name__)


# Página principal, mostra as leituras salvas no banco de dados
@views_blueprint.route('/')
def route_index():
    leituras = Leitura.query.order_by(desc(Leitura.data_registro)).all()
    return render_template('index.html', leituras=leituras)

