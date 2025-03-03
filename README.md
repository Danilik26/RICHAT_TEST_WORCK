Test task

There are 3 main applications, the items application for processing one item, the Items model is described as in the task

The second application for working with a group of orders, implemented by combining Items positions in a many-to-many relationship and calculating the total cost, in Stripe the price of all positions that are associated with the Orders model will be indicated, the name of the payment will be by order id

The third application is an API for Stripe,
everything is implemented on stripe.checkout.Session.create

launch on the local machine occurs through the standard Django server, you can create data for testing through the admin panel, or go to the url http://..../start_data/, 4 Items records and 2 Orders records will be created
there is a docker-compoze assembly, postgresql was used as a database

There is also one unit test in the orders application