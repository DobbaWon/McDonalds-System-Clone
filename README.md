To Run:
  pip install flask flask-cors python-dotenv mysql-connector-python
  
  ** IN ROOT **
  - npm i
  - npm run dev

  ** IN  BackEnd **
  python app.py


This is a project I have started while I am searching for graduate jobs. This keeps me constantly working around software development while I try to juggle working my part-time job at a full-time schedule, as well as working out, and developing my skills in my other hobbies.

I have chosen Vue because I want to make sure my knowledge of JavaScript Frontend Frameworks is well-rounded, and I want to see what all of the hype is about. I used Vue once already in a group project in my 3rd university year, but I didn't fully understand it. 


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
[x] Add a toggle to outage items, preventing them from being used
[x] Save Order to a database
[x] Make Kitchen Screen Page
[x] Display Orders on Kitchen Screen Page
[x] Serve Button on each Order to delete from Server & Page
[x] Pending Orders to not clutter the Kitchen Screen
[ ] Modify Last Order on PointOfSale

Tasks Made Redundant:
[/] Add Meals which include fries and drink

I've learned through about 3 hours of work trying to implement a meal system without classes, that it is a very object oriented thing to do. No wonder the POS at work was made with C#. I managed to implement it to a small amount, but then realised that scaling up with drinks and fries, and cascading actions on that meal to those items, as well as upgrading the meal, would be an extremely tedious task. Due to this, the meal feature has been removed from my POS, and I have learned a valuable lesson when it comes to choosing a programming language for a project.
