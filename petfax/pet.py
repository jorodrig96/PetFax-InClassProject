from flask import (Blueprint, render_template)
import json 

pets = json.load(open('pets.json', encoding='utf-8'))
print(pets)
bp = Blueprint('pet', __name__, url_prefix='/pets')

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

@bp.route('/<int:id>')
def show(id): 
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)