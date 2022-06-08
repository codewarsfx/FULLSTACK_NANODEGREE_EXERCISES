from flask_restful import Resource, Api
from models.model import Recipe,recipes_list
from http import HTTPStatus
from flask import Flask,request,abort,jsonify


app = Flask(__name__)
api = Api(app)


class RecipeList(Resource):
    def get(self):
        data =[]
        for recipe in recipes_list:
            if recipe['isPublished'] == True:
                data.append(recipe)
        return {"data":data}, HTTPStatus.OK
    
    def post(self):
        data = request.get_json()
        new_recipe = Recipe(name=data['name'],description=data['description'])
        recipes_list.append(new_recipe)
        print([recipe.data() for recipe in recipes_list])
        return {'status':'ok'}, HTTPStatus.CREATED
    
class RecipeItem(Resource):
    def get(self,id):
        print(id)
        recipe = next((recipe for recipe in recipes_list if recipe.id==id),None)
        if recipe is None: 
            return {
                "message":"not_found"
            },HTTPStatus.NOT_FOUND
        return recipe.data()


# @app.errorhandler(404)
# def not_found(error):
#     return {
#         "message": "not found",
#         "status": 404,
#     }, HTTPStatus.NOT_FOUND



api.add_resource(RecipeList,'/recipes')
api.add_resource(RecipeItem,'/recipes/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)


