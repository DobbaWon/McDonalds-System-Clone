To Run:
  ** IN ROOT **
  - npm i
  - npm run dev

This is a project I have started while I am searching for graduate jobs. This keeps me constantly working around software development while I try to juggle working my part-time job at a full-time schedule, as well as working out, and developing my skills in my other hobbies.

I have chosen Vue because I want to make sure my knowledge of JavaScript Frontend Frameworks is well-rounded, and I want to see what all of the hype is about. I used Vue once already in a group project in my 3rd university year, but I didn't fully understand it. 

I want to scale up with the complexity as the project grows; it will start with just local variables and a monolithic approach, but will soon contain a database, and I can hopefully separate the services into Docker Containers, to get independant experience working with Docker, as I have some experience in a group project using Docker. 

The project will start as a basic POS, where I will then expand into different layouts for the POS, and then having the orders created and stored by the POS land into a database. This will allow me to work with these orders and display them on a Kitchen Order Screen, and have the ability to serve them off, recall them, hold them, and cycle between displayed orders for these interactions. There will also be an Orders Screen, which contains the full orders for the front counter workers to see, and interact with in similar ways to the KOS. 


Todo List:
[x] Create ItemButtons to store items and display them
[x] Create POSMenu to store and use item buttons
[x] Create POSReceipt to display order details
[x] Create Point Of Sale to display POSMenu and POSReceipt
[x] Emit item data onclick up to the Point Of Sale
[x] Store item data in an order and pass through to Receipt
[x] Replace Receipt with POSOrder until Order is served 
[x] Replace Drink Selections with Pop-up boxes for more choice and encapsulation
[x] Add remove item from order feature
[ ] Add a toggle to outage items, preventing them from being used
[ ] Save Order to a database


Tasks Made Redundant:
[/] Add Meals which include fries and drink

I've learned through about 3 hours of work trying to implement a meal system without classes, that it is a very object oriented thing to do. No wonder the POS at work was made with C#. I managed to implement it to a small amount, but then realised that scaling up with drinks and fries, and cascading actions on that meal to those items, as well as upgrading the meal, would be an extremely tedious task. Due to this, the meal feature has been removed from my POS, and I have learned a valuable lesson when it comes to choosing a programming language for a project.
