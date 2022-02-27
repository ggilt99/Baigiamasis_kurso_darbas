# Python pradedančiųjų kursų baigiamasis_darbas - Random password generator

## Description
This app is used to create a strong random password, which contains randomly selected ASCII characters and digit, length depends on user's choice. Application also allows user to access a database for personal use, such as store, edit and update passwords.

## Description
Fired up application opens the main window:

<img width="603" alt="Screenshot 2022-02-27 at 22 40 14" src="https://user-images.githubusercontent.com/100309347/155899780-9bc68f91-349a-4ba4-988b-68a83e4ab928.png">

The main window is divided into two sections:
	Right sections is some information for the user, such as what is the purpose of application / how passwords are generated and a little guidance on how to generate the password

	The left section requires user involvement. User chooses the length of the password (it should be between 6 and 20 characters long) and presses '**GO**' button. After it is done, a random password appears:

<img width="202" alt="Screenshot 2022-02-27 at 22 41 09" src="https://user-images.githubusercontent.com/100309347/155899897-95e2ee46-2318-482c-9c07-bdb087e5cf95.png">

In order to easily copy password to the clipboard user can press the '**COPY**' button.

A bit further down there are a few more buttons, which extends applications functionality.
	The first one is '**Save to DB**', which evokes a new window:

<img width="259" alt="Screenshot 2022-02-27 at 22 41 25" src="https://user-images.githubusercontent.com/100309347/155899929-ffbd5f0d-4933-43e7-8786-bd1d76015ea4.png">

User is asked for the attributes that will be stored inside the Database. If all the fields are filled succesfully and not left blank, the password is stored safely inside the storage. If some of the fields are left blank user is shown an error message:

<img width="261" alt="Screenshot 2022-02-27 at 23 08 16" src="https://user-images.githubusercontent.com/100309347/155900008-cf03ec69-664e-4d86-913a-5342ff0e49e3.png">

	Another option that is presented to the user is under the '**Show DB**' button, which opens up a new window, with passwords stored inside the database (all passwords shown are just for demonstration purposes):

<img width="502" alt="Screenshot 2022-02-27 at 22 57 05" src="https://user-images.githubusercontent.com/100309347/155900072-bab45454-3fff-4a7c-9fea-02de050a96fc.png">

	And the last functionality can be accessed when '**Edit DB**' button is pressed:

<img width="484" alt="Screenshot 2022-02-27 at 22 57 18" src="https://user-images.githubusercontent.com/100309347/155900093-c74c0aab-80fa-4e7f-8efa-9fab0e68ceaf.png">

New window appears, which lets user either update information or delete stored information. It should be used as it follows:
	Firstly user searches for ID, under which the information is stored, if entry is found it is displayed, 

<img width="488" alt="Screenshot 2022-02-27 at 22 57 29" src="https://user-images.githubusercontent.com/100309347/155900136-89c0a82a-dc44-445d-bf1e-27efd51330e6.png">

	otherwise, an error message pops up:

<img width="486" alt="Screenshot 2022-02-27 at 22 57 49" src="https://user-images.githubusercontent.com/100309347/155900151-15c4b839-7489-4393-91a1-3da6061cb68d.png">

from there user can either update:

<img width="553" alt="Screenshot 2022-02-27 at 22 58 30" src="https://user-images.githubusercontent.com/100309347/155900184-85ce9bbe-29aa-4745-9dae-7404a9479472.png">

or delete entry:

<img width="488" alt="Screenshot 2022-02-27 at 22 58 01" src="https://user-images.githubusercontent.com/100309347/155900194-4b8ba988-9582-495b-99cc-3a2a8a09ee2d.png">

completely wiping it off of the database:


<img width="506" alt="Screenshot 2022-02-27 at 22 58 40" src="https://user-images.githubusercontent.com/100309347/155900204-b281132f-4e74-4441-87e6-56e2e9d8f37f.png">

Overall the program should be used only for personal used as it is not protected by a master password.




