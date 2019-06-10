RESTFULAPI implemented in flask-restful and SQLAlchemy

this restfulapi mimic shopping cart, it contains the following features<br/>
   adding items to a shopping cart<br/> 
   deleting the items from the shopping cart.<br/>
   viewing the items/particular item added to a shopping cart and<br/>
   updating the existing items in a shopping cart.<br/>

Adding a item to a shopping cart is achieved through the resource end point '/item' using POST method.<br/>
Deleteing a item to a shopping cart is achieved through the resource end point '/item' itself using DELETE method.<br/>
Viewing a item to a shopping cart is achieved through the resource end point '/item' itself using GET method.<br/>
Viewing all the items in the shopping cart is achieved through the resource end point '/items'  using GET method.<br/>
Updating a item to a shopping cart is achieved through the resource end point '/item' using PUT method.<br/>


it contains the ends points<br/> 
/item<br/>
/items<br/>
/store<br/>
/stores<br/>

used JWT tokens to authenticate the incoming request.<br/>

used SQLAlchemy CRUD method on a database is achieved through few lines of code, used sqlite3, in production it can be changed to PostgreSQL or MySQL with api.config <br/>

The production version will be deployed in Amazon EC2, using NGINIX and WGSI.<br/>
