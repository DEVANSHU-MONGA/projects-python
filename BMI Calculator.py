from tkinter import *
root = Tk()
root.title("BMI Calculator")
root.geometry("520x700+300+100")
root.resizable(False, False)
root.configure(bg="#f0f1f5")

def calculate_bmi(event=None):
    try:
        height_val = float(Height.get())
        weight_val = float(Weight.get())

        if height_unit.get() == 'Feet':
            height_val = height_val * 30.48  # Convert feet to cm
        if weight_unit.get() == 'Pounds':
            weight_val = weight_val * 0.453592  # Convert pounds to kg

        bmi = weight_val / (height_val / 100) ** 2
        bmi_result.set(f'BMI: {bmi:.2f}')

        if bmi <= 18.5:
            label2.config(text="Underweight!", font=("Cascadia 25 bold"))
            label3.config(text="You have lower weight than normal body!", font=("Cascadia 15 bold"))
        elif bmi > 18.5 and bmi <= 25:
            label2.config(text="Normal!", font=("Cascadia 25 bold"))
            label3.config(text="It indicates that you are healthy!", font=("Cascadia 15 bold"))
        elif bmi > 25 and bmi <= 30:
            label2.config(text="Overweight!", font=("Cascadia 25 bold"))
            label3.config(text="It indicates that a person is slightly overweight!\nA doctor may advise to lose some weight.", font=("Cascadia 12 bold"))
        else:
            label2.config(text="Obesity!", font=("Cascadia 25 bold"))
            label3.config(text="It indicates obesity!\nA doctor may advise to lose weight.", font=("Cascadia 12 bold"))
    except ValueError:
        bmi_result.set("Invalid input")
        label2.config(text="")
        label3.config(text="")

def clear_fields():
    Height.set("")
    Weight.set("")
    bmi_result.set("")
    label2.config(text="")
    label3.config(text="")



label = Label(root, text="BMI CALCULATOR", font=("Cascadia 25 bold"), bg="powder blue", width=27, height=2, bd=9, relief=SUNKEN)
label.pack()

Label(root, width=92, height=20, bg="lightblue").pack(side=BOTTOM)
Label(root, width=30, height=12, bg="white", bd=5, relief=SUNKEN).place(x=20, y=100)
Label(root, width=30, height=12, bg="white", bd=5, relief=SUNKEN).place(x=290, y=100)

height_unit = StringVar(value='Centimeters')
weight_unit = StringVar(value='Kilograms')

current_value = DoubleVar()
current_value2 = DoubleVar()

def get_current_value():
    return '{:.2f}'.format(current_value.get())

def get_current_value2():
    return '{:.2f}'.format(current_value2.get())

def slider_changed(event):
    Height.set(get_current_value())

def slider_changed2(event):
    Weight.set(get_current_value2())


slider = Scale(root, from_=0, to=220, orient="horizontal", command=slider_changed, variable=current_value)
slider.place(x=80, y=230)

slider2 = Scale(root, from_=0, to=200, orient="horizontal", command=slider_changed2, variable=current_value2)
slider2.place(x=360, y=230)

Height = StringVar()
Weight = StringVar()
bmi_result = StringVar()

height_entry = Entry(root, textvariable=Height, width=5, font="arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER)
height_entry.place(x=35, y=160)
Height.set(get_current_value())

weight_entry = Entry(root, textvariable=Weight, width=5, font="arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER)
weight_entry.place(x=305, y=160)
Weight.set(get_current_value2())

height_label = Label(root, text="Height", font=("arial", 12), bg="#f0f1f5", fg="#000")
height_label.place(x=45, y=120)

weight_label = Label(root, text="Weight", font=("arial", 12), bg="#f0f1f5", fg="#000")
weight_label.place(x=315, y=120)

height_unit_label = Label(root, text="Unit", font=("arial", 12), bg="#f0f1f5", fg="#000")
height_unit_label.place(x=35, y=300)

weight_unit_label = Label(root, text="Unit", font=("arial", 12), bg="#f0f1f5", fg="#000")
weight_unit_label.place(x=305, y=300)

height_unit_cm = Radiobutton(root, text='Centimeters', variable=height_unit, value='Centimeters', bg="#f0f1f5", font=("arial 10 bold"))
height_unit_cm.place(x=35, y=330)
height_unit_ft = Radiobutton(root, text='Feet', variable=height_unit, value='Feet', bg="#f0f1f5", font=("arial 10 bold"))
height_unit_ft.place(x=35, y=360)

weight_unit_kg = Radiobutton(root, text='Kilograms', variable=weight_unit, value='Kilograms', bg="#f0f1f5", font=("arial 10 bold"))
weight_unit_kg.place(x=305, y=330)
weight_unit_lb = Radiobutton(root, text='Pounds', variable=weight_unit, value='Pounds', bg="#f0f1f5", font=("arial 10 bold"))
weight_unit_lb.place(x=305, y=360)

calculate_button = Button(root, text="View Report", command=calculate_bmi, width=15, height=2, font="Cascadia 10 bold", bg="#1f6e68", bd=5, fg="white")
calculate_button.place(x=80, y=400)

clear_button = Button(root, text="Clear", command=clear_fields, width=15, height=2, font="arial 10 bold", bg="#1f6e68", bd=5, fg="white")
clear_button.place(x=300, y=400)

bmi_label = Label(root, textvariable=bmi_result, font=("arial 30 bold"), bg="lightblue", fg="#fff")
bmi_label.place(x=185, y=450)

label2 = Label(root, font=("arial", 20), bg="lightblue", fg="#3b3a3a")
label2.place(x=180, y=500)

label3 = Label(root, font=("arial", 14), bg="lightblue", fg="#000")
label3.place(x=125, y=550)

root.bind('<Return>', calculate_bmi)

root.mainloop()
