# ColiSave
ColiSave is a CRUD web application created using Django for managing and storing information about horses that have experienced colic. It is intended for use in a veterinary clinic. 
The app is complete with a Machine Learning Model that predicts the outcome of a colic episode with ~80% accuracy.

# Features
The user begins in a Home Page and can navigate through different pages using a Navigation Bar. 
<img width="1439" alt="Screenshot 2024-09-03 at 11 51 53 AM" src="https://github.com/user-attachments/assets/f1b40667-5e26-4898-9ecd-eca4e8224861">


In order to access user information, an account must be created or logged into. Django stores all client and horse information for future use.
<img width="1436" alt="Screenshot 2024-09-03 at 11 52 02 AM" src="https://github.com/user-attachments/assets/d91e2b4e-d498-4ba4-9b15-51f1a3d073cf">

The user can view each horses' information, including predicted outcome, through the dashboard.
Also, the user can add horses and update horse information. Each time this is done, the pre-trained model (a Sequential Neural Network created using Keras) obtains a new prediciton for the outcome of the horse.
<img width="1438" alt="Screenshot 2024-09-03 at 11 50 07 AM" src="https://github.com/user-attachments/assets/330f939b-4d72-4baa-be39-b12eb2b4ff27">
<img width="1440" alt="Screenshot 2024-09-03 at 11 51 25 AM" src="https://github.com/user-attachments/assets/9261a1ae-f9a9-464a-aa22-9b71eb839de4">
<img width="1440" alt="Screenshot 2024-09-03 at 11 51 33 AM" src="https://github.com/user-attachments/assets/1f1e674d-689a-4edc-b510-adda35dc5bf3">


# Credits
This web app was inspired by the following Youtube Videos:

"Build A Simple Machine Learning Web Application with Django | Part 1 and 2" by Ken Bro Tech
[https://www.youtube.com/watch?v=MrRI0ZFoLyc], [https://www.youtube.com/watch?v=sTjL51Gr1wE]

"CRUD mastery with Django | Build a CRM application | Django projects | #1" by Cloud With Django
[https://www.youtube.com/watch?v=pqWyUAT38e0&t=8688s]

"Horse Survival Prediction - Data Every Day #116" by Gabriel Atkin
[https://www.youtube.com/watch?v=oXUDU101e2c]

