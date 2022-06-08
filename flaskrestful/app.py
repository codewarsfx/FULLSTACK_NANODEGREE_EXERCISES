from flask_restful import Resource, Api
from models.model import Recipe,recipes_list
from http import HTTPStatus
from flask import Flask,request


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
        print(new_recipe.data())
        return {'status':'ok'}, HTTPStatus.CREATED


api.add_resource(RecipeList,'/recipes')


if __name__ == '__main__':
    app.run(debug=True)


