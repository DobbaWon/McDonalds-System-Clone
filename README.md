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
[x] Modify Last Order on PointOfSale
[x] Order Served Notification on PointOfSale
[ ] Unit Tests & Documentation

When making this project, I opted away from using classes to define the items, orders, etc. This turned out to be a mistake, as I cannot cleanly implement any Meal or Item Modification features without falling into massive spaghetti code, manually adding fields to each individual component instance, more so than I already am doing. This is a project to help me get the hang of Vue, and I want to complete it, so I don't mind bypassing these features, and taking this as a hard-learned lesson to better research and plan my project. 

Maybe in the future I will come back and fix this, increasing the project's complexity by implementing these features and refactoring it to be more Object-Oriented, as I do already plan to come back to this project to not only clean my code when I have learned more, but also to make the project look aesthetically better.
