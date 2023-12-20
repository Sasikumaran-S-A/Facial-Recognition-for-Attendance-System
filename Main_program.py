import Program_Functions
from time import sleep


# './Photos' should have only photos format as file and any folders is allowed and name of the image file is the name of the person, also the name of the person should be less than 50 character (not necessary)
# Don't try to add or remove any file or folder in the directory while running the program
# Light environment is perferred

# >>> Features:
# 01. It ask each time what to do
# 02. If any wrong input is given it will ask again, at any time
# 03. If required folder is not there it will create like './Photos' and './Photos/Needs to Remove', also 'haarcascade_frontalface_default.xml' is necessary file, if it is not there it will ask to download
# 04. 'q' can be pressed to exit the process while entering the no. of person or person name or while taking photo in registering(only in image frame), while taking attendance also(only in image frame)
# 05. Encodes the stored photo and store it in list, at initial itself, also if it is found to have image with no face or with more than one image it will move that photo to './Photos/Needs to Remove' folder, in that folder if same name is present it will store in different name
# 06. Always while encoding, only the face is encoded
# 07. If a person is recognised once, they will not be recognised again
# 08. The newly encoded image will be added to the existing list, so time is saved in this while recognising again
# 09. While registering if the person name is already in Photos folder it will not acccept
# 10. The photo is taken only if 'p' is pressed on the image frame
# 11. Image window will be shown while taking photo also while taking attendance
# 12. If taken Photo taken have no face or more than one face it will not accept, saying to retake, if only one face detected it will store in './Photos' folder
# 13. Creates a .csv file if it is not present in that particular date for storing data like name-data-time of the recognised face at each time, or data will append to the file if it is already created
# 14. output with name, date and time is shown while recognising
# 15. Says if no face is registered
# 16. Ends the recognising process if all the members in the registered list is recognised
# 17. A blue box will appear on the any face in the image window while taking attendance
# 18. Shows the name and present status in image window


def Initial(known_face_encodings,known_face_names,recognised_faces):                                                  # Initializing Function
    sleep(1)
    print("\n####\nFor Registering face, Enter 1  \nFor Attendance, Enter 2 \nFor Exit, Enter 0\n####\n")             # For input
    Input = input('Give your input : ')
    print()
    if Input=='1':
        print(">> Enter 'p' on the frame to take photo <<\n")
        return_tuple = Program_Functions.Take_Photo(known_face_names)                                                 # To update the existing list of face encodings and face names
        known_face_encodings.extend(return_tuple[0])
        known_face_names.extend(return_tuple[1])
        return Initial(known_face_encodings,known_face_names,recognised_faces)
    elif Input=='2':
        recognised_faces = Program_Functions.Face_rec(known_face_encodings,known_face_names,recognised_faces)         # To get recognised names
        return Initial(known_face_encodings,known_face_names,recognised_faces)
    elif Input=='0':
        print("Thank You! See you Soon...\n")                                                                         # End<<
        exit
    else:
        print("#### Please Give The Correct Value ####")                                                              # If other than 1, 2, 0 is given
        return Initial(known_face_encodings,known_face_names,recognised_faces)


print("\n---Facial Recognition for Attendance System---")                                                             # Start<<
print("\n<< To Stop Enter 'q' at any time >>")
print("<< Please Wait for Sometime >>")


if Program_Functions.Initializing():                                                                                  # For checking the requirements
    object1 = Program_Functions.face_encodings()
    known_face_encodings,known_face_names = object1.known_face_encodings()                                            # To get the registered face encodings at the begining itself

    Initial(known_face_encodings,known_face_names,[])                                                                 # To start the function
else:
    exit