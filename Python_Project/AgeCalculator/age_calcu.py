import ipywidgets as widget
from datetime import date

def cal_age(dob):

    today = date.today()
    try:
        age = today.year - dob.year -((today.month,today.day) < (dob.month,dob.day))
        if age >= 1:
            print("you'are {} years old".format(age))
        else:
            print("Age should be greater than one")

    except Exception as e:
        print("Pick Date of Birth")

    
# create ipy widget
dob = widget.DatePicker(description = "Birth Date",disabled=False)
out = widget.interactive_output(cal_age,{'dob':dob})
widget.HBox([widget.VBox([dob]),out])