from flask import Flask,jsonify,request
from http import HTTPStatus

app = Flask(__name__)

recipes =[{
    "id":1,
    "name":"okra soup",
    "description":"okra is a beautifulsoup",
},{
    "id":2,
    "name":"egusi",
    "description":"egusi is a beautifulsoup",
}]

@app.route('/recipes',methods=['GET'])
def index():
    return jsonify(recipes), HTTPStatus.OK

@app.route('/recipes',methods=['POST'])
def create_recipe():
    data = request.get_json()
    recipe = {
        "id": len(recipes)+1,
        "name": data.get("name",'no name'),
        "description": data.get("description",'no description'),
    }
    recipes.append(recipe)

    print(recipes)
    return jsonify(recipe), HTTPStatus.CREATED

@app.route('/recipes/<int:recipe_id>',methods=['PUT'])
def update_recipe(recipe_id):
    recipe_data = request.get_json()
    recipe = next((recipe for recipe in recipes if recipe["id"] == recipe_id),None)
    if not recipe:
        return jsonify({"message": "recipe not found"}), HTTPStatus.NOT_FOUND
    recipe.update({
       "name": recipe_data.get('name'),
       "description": recipe_data.get('description'),
    })
    print(recipes)
    return jsonify(recipe)

@app.route('/recipes/<int:recipe_id>', methods = ['DELETE'])
def delete_recipe(recipe_id):
     recipe = next((recipe for recipe in recipes if recipe["id"] == recipe_id),None)
     if not recipe: 
        return jsonify({"message": "recipe not found"}), HTTPStatus.NOT_FOUND

if __name__ == '__main__':
    app.run(debug=True)
    pass
