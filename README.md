RESTFULAPI implemented in flask-restful and SQLAlchemy

this restfulapi mimic shopping cart, it contains the following features
   adding items to a shopping cart, 
   deleting the items from the shopping cart, 
   viewing the items/particular item added to a shopping cart and 
   updating the existing items in a shopping cart.

Adding a item to a shopping cart is achieved through the resource end point '/item' using POST method
Deleteing a item to a shopping cart is achieved through the resource end point '/item' itself using DELETE method
Viewing a item to a shopping cart is achieved through the resource end point '/item' itself using GET method
Viewing all the items in the shopping cart is achieved through the resource end point '/items'  using GET method
Updating a item to a shopping cart is achieved through the resource end point '/item' using PUT method


it contains the ends points 
/item
/items
/store
/stores

used JWT tokens to authenticate the incoming request.

used SQLAlchemy CRUD method on a database is achieved through few lines of code, used sqlite3, in production it can be changed to PostgreSQL or MySQL with api.config 

The production version will be delpoyed in Amazon EC2, using NGINIX and WGSI.
