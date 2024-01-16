from flask import Flask
from flask_migrate import Migrate
from flask_restful import Resource, Api, reqparse, abort


from models import db, Product


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///pos.db'
migrate = Migrate(app,db)
db.init_app(app)

api = Api(app)

post_args = reqparse.RequestParser()
post_args.add_argument('id', type=int,required=True )
post_args.add_argument('name', type=str, required=True  )
post_args.add_argument('perishable', type=bool, required=True  )
post_args.add_argument('quantity', type=int, required=True  )
post_args.add_argument('price', type=float, required=True  )


patch_args = reqparse.RequestParser()
patch_args.add_argument('id', type=int)
patch_args.add_argument('name', type=str )
patch_args.add_argument('perishable', type=bool)
patch_args.add_argument('quantity', type=int)
patch_args.add_argument('price', type=float)




class Products(Resource):



    def get(self):
        products = Product.query.all()
        response = [product.to_dict() for product in products]
        return response


    def post(self):
        data= post_args.parse_args()
        new_product = Product(**data)
        db.session.add(new_product)
        db.session.commit()
        return new_product.to_dict()


class productById(Resource):


    def get(self, id):
        product = Product.query.get(id)
        if not product:
           abort(404, details =f'products with {id=} does not exist' ) 
        return product.to_dict()


    def patch(self, id):
        product = product.query.get(id)
        if not product:
            abort(404, details =f'products with {id=} does not exist' )

        data =patch_args.parse_args()
        print(data)
        for key, value in data.items():
            if value is None:
                continue
            setattr(product, key, value)
        db.session.commit
        return product.to_dict()




    def delete(self, id):
        product = Product.query.filter_by(id = id).first()
        if not product:
           abort(404, details =f'products with {id=} does not exist' ) 
        
        db.session.delete(product)
        db.sesion.commit()
        return{'detail': f'product  with {id=} has been deleted successfully'}


api.add_resource(Products, '/products')

api.add_resource(productById, '/products/<int:id>')



if __name__ == '__main__':
    app.run()