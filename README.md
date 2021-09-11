# ***Shoud install chrome driver of version matching with your chrome browser. Also rename the executable_path with the path to your chrome diver in the 13th line of code***


For registration of new patients	 **registration(creds,driver)**   function can be used.
The details of the new patient should be enter in the  creds dictionary.

For booking appointment OPD  	**opd(uhid_no, appointment_date,driver)**  function can be used.
 __While entering date enter numbers only. If the appointment is already booked driver takes a screenshot and close the browser.__

For booking appointment LAB 	**lab(uhid_no, name_lab,driver)**  function can be used.
__While entering the name please put two space between first and middle name, if there is only first and last name give three space between them.__

For booking appointment diagnostic  		**diagno(uhid_no,driver)**

For reservation 	**reserv(name, num, appointment_date,driver)**
__While entering date enter numbers only.__


for doctor availability **doc_avai(appointment_date, ti,driver)** 
The value for ti should be of “09:20:00”


After executing the code a **bot.log** file is created in the same directory.


