import tkinter
from tkinter import *
from tkinter import IntVar
from tkinter.ttk import Combobox
import units1
import volume
from volume import units


window = Tk()
window.title("Miles to Kms Converter")
window.minsize(600, 225)
window.config(padx=15, pady=25)

# Entry

user_entry = Entry(width=10)
user_entry.insert(END, string=f'{0}')
user_entry.grid(row=0, column=1)
user_entry.get()
user_entry.focus()

# Text
label_to = Label(text="Unit", font=("Arial", "12", "bold"))
label_to.grid(row=1, column=3)
label_to.config(padx=25)


label_conversion = Label(text="is equal to", font=("Arial", "12", "bold"))
label_conversion.grid(row=1, column=0)
label_conversion.config(padx=15, pady=10)

label_converted = Label(text="0", width= 15, font=("Arial", "12", "bold"))
label_converted.grid(row=1, column=1)
label_converted.config(padx=40, pady=10)


# Button Calculate

volume_list = []
get_volume_list = (units[0].keys())
x = get_volume_list
for item in x:
    volume_list.append(item)


converts_to_list_line = ["km", "mile", "foot", "meter", "inch", "yard"]
temperature_list = ["celsius", "fahrenheit", "kelvin"]


def radio_used():
    if radio_state.get() == 1:
        converts_to_list = converts_to_list_line
    elif radio_state.get() == 2:
        converts_to_list = volume_list
    else:
        converts_to_list = temperature_list

    from_unit = Combobox(values=converts_to_list, width=15)
    # from_unit.bind("<<ComboboxSelected>>", change_from_label)
    from_unit.current(0)
    from_unit.grid(row=6, column=0)
    unit_label_hide = Label(text="", font=("Arial", "12", "bold"))
    unit_label_hide.grid(row=4, column=0)
    unit_label_from = Label(text="From", font=("Arial", "12", "bold"))
    unit_label_from.grid(row=5, column=0)
    unit_label_from.config(padx=1, pady=1)

    # To

    to_unit = Combobox(values=converts_to_list, width=15)
    to_unit.current(0)
    to_unit.grid(row=6, column=3)
    # from_unit.bind("<<ComboboxSelected>>", change_to_label)
    to_unit_label_hide = Label(text="", font=("Arial", "12", "bold"))
    to_unit_label_hide.grid(row=4, column=3)
    to_unit_label = Label(text="To", font=("Arial", "12", "bold"))
    to_unit_label.grid(row=5, column=3)
    to_unit_label.config(padx=1, pady=1)

    def convert():
        input_value = user_entry.get()
        unit_from = from_unit.get()
        unit_to = to_unit.get()
        unit_list = list(units1.units)
        unit_volume = list(volume.units)

        if unit_from == "celsius" and unit_to == "fahrenheit":
            convert_unit = ((int(input_value) * 9) / 5) + 32
            output = "{0:.3f}".format(convert_unit)
            label_converted.config(text=output)
        elif unit_from == "celsius" and unit_to == "kelvin":
            convert_unit = (int(input_value) + 273)
            output = "{0:.3f}".format(convert_unit)
            label_converted.config(text=output)
        elif unit_from == "fahrenheit" and unit_to == "celsius":
            convert_unit = (((int(input_value) - 32) * 5) / 9)
            output = "{0:.3f}".format(convert_unit)
            label_converted.config(text=output)
        elif unit_from == "fahrenheit" and unit_to == "kelvin":
            convert_unit = (((int(input_value) - 32) * 5 / 9) + 273)
            output = "{0:.3f}".format(convert_unit)
            label_converted.config(text=output)
        elif unit_from == "kelvin" and unit_to == "celsius":
            convert_unit = (int(input_value) - 273)
            output = "{0:.3f}".format(convert_unit)
            label_converted.config(text=output)
        elif unit_from == "kelvin" and unit_to == "fahrenheit":
            convert_unit = (((int(input_value) - 273) * 9 / 5) + 32)
            output = "{0:.3f}".format(convert_unit)
            label_converted.config(text=output)
        else:
            for i in range(len(unit_list)):
                if unit_from in unit_list[i]:
                    factor = unit_list[i][unit_from][unit_to]
                    if factor:
                        convert_unit = float(input_value) * factor
                        output = "{0:.3f}".format(convert_unit)
                        label_converted.config(text=output)
                        break
            else:
                # If the loop didn't hit the `break` statement, the unit wasn't found
                label_converted.config(text="Unit not found.")
        return None

    button = Button(text="Calculate", command=convert)
    button.grid(row=2, column=1)


button_hide = Button(text="Calculate")
button_hide.grid(row=2, column=1)
radio_state = IntVar()
# radio_state.set(1)
button_line = Radiobutton(text="length", variable=radio_state, value=1, command=radio_used)
button_volume = Radiobutton(text="Volume", variable=radio_state, value=2, command=radio_used)
button_temp = Radiobutton(text="Temperature", variable=radio_state, value=3, command=radio_used)


button_volume.grid(row=0, column=3)

button_temp.grid(row=1, column=3)

button_line.grid(row=2, column=3)

# from_unit.bind("<<ComboboxSelected>>", change_from_label)
#
unit_label_hide = Label(text="", font=("Arial", "12", "bold"))
unit_label_hide.grid(row=4, column=0)
unit_label_hide.config(padx=35, pady=1)

#
# # To
#
# from_unit.bind("<<ComboboxSelected>>", change_to_label)
to_unit_label_hide = Label(text="", font=("Arial", "12", "bold"))
to_unit_label_hide.grid(row=4, column=3)
to_unit_label_hide.config(padx=35, pady=1)


window.mainloop()
