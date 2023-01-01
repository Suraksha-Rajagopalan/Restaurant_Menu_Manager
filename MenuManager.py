from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operator = ''

food_price = [10, 15, 20, 10, 30, 15, 50, 50]
drink_price = [20, 30, 10, 20, 10, 40, 30, 20]
dessert_price = [50, 70, 80, 45, 60, 55, 60, 70]

def click_buttton(character):
    global operator
    operator = operator+character
    calculator_display.delete(0, END)
    calculator_display.insert(END, operator)

def delete_all():
    global operator
    operator =''
    calculator_display.delete(0, END)

def get_result():
    global operator
    result = str(eval(operator))
    calculator_display.delete(0, END)
    calculator_display.insert(0, result)
    operator = ''

def review_check():
    x = 0
    for b in food_box:
        if food_variables[x].get()==1:
            food_box[x].config(state=NORMAL)
            if food_box[x].get()=='0':
                food_box[x].delete(0, END)
            food_box[x].focus()
        else:
            food_box[x].config(state=DISABLED)
            food_text[x].set('0')
        x += 1

    x = 0
    for b in drink_box:
        if drink_variables[x].get() == 1:
            drink_box[x].config(state=NORMAL)
            if drink_box[x].get()=='0':
                drink_box[x].delete(0, END)
            drink_box[x].focus()
        else:
            drink_box[x].config(state=DISABLED)
            drink_text[x].set('0')
        x += 1

    x = 0
    for b in dessert_box:
       if dessert_variables[x].get() == 1:
           dessert_box[x].config(state=NORMAL)
           if drink_box[x].get() == '0':
               dessert_box[x].delete(0, END)
           dessert_box[x].focus()
       else:
            dessert_box[x].config(state=DISABLED)
            dessert_text[x].set('0')
       x += 1

def total_calculations():
    food_subtotal = 0
    p=0
    for unit in food_text:
        food_subtotal = food_subtotal + (int(unit.get()) * int(food_price[p]))
        p += 1

    drink_subtotal = 0
    p = 0
    for unit in drink_text:
        drink_subtotal = drink_subtotal + (int(unit.get()) * int(drink_price[p]))
        p += 1

    dessert_subtotal = 0
    p = 0
    for unit in dessert_text:
        dessert_subtotal = dessert_subtotal + (int(unit.get()) * int(dessert_price[p]))
        p += 1

    my_subtotal = float(food_subtotal + drink_subtotal + dessert_subtotal)
    my_taxes = float(my_subtotal*0.11)
    my_total = float(my_subtotal+my_taxes)
    food_cost_var.set(f'Rs {round(food_subtotal, 2)}')
    drink_cost_var.set(f'Rs {round(drink_subtotal, 2)}')
    dessert_cost_var.set(f'Rs {round(dessert_subtotal, 2)}')
    subtotal_var.set(f'Rs {my_subtotal}')
    taxes_var.set(f'Rs {round(my_taxes, 2)}')
    total_var.set(f'Rs {round(my_total, 2)}')

def create_invoice():
    invoice_text.delete(1.0, END)
    invoice_number = f'N# - {random.randint(1000, 9999)}'
    my_date = datetime.datetime.now()
    invoice_date = f'{my_date.month}/{my_date.day}/{my_date.year} - {my_date.hour}:{my_date.minute}'
    invoice_text.insert(END, f'Information: \t{invoice_number}\t\t{invoice_date}\n')
    invoice_text.insert(END, f'*'*47+'\n')
    invoice_text.insert(END, f'Items\tQuatity\tItems Cost\n')
    invoice_text.insert(END, f'-'*54+'\n')

    x = 0
    for f in food_text:
        if f.get()!='0':
            invoice_text.insert(END, f'{food_list[x]}\t\t{f.get()}\t'
                                f'Rs {int(f.get()) * food_price[x]}\n')
            x += 1

    x = 0
    for f in drink_text:
        if f.get() != '0':
            invoice_text.insert(END, f'{drink_list[x]}\t\t{f.get()}\t'
                                     f'Rs {int(f.get()) * drink_price[x]}\n')
            x += 1

    x = 0
    for f in dessert_text:
        if f.get() != '0':
            invoice_text.insert(END, f'{dessert_list[x]}\t\t{f.get()}\t'
                                     f'Rs {int(f.get()) * dessert_price[x]}\n')
            x += 1

    invoice_text.insert(END, f'*'*47+'\n')
    invoice_text.insert(END, f'Food Subtotal: \t\t\t{food_cost_var.get()}\n')
    invoice_text.insert(END, f'Drink Subtotal: \t\t\t{drink_cost_var.get()}\n')
    invoice_text.insert(END, f'Dessert Subtotal: \t\t\t{dessert_cost_var.get()}\n')
    invoice_text.insert(END, f'Subtotal: \t\t\t{subtotal_var.get()}\n')
    invoice_text.insert(END, f'Taxes: \t\t\t{taxes_var.get()}\n')
    invoice_text.insert(END, f'Total: \t\t\t{total_var.get()}\n')
    invoice_text.insert(END, 'SEE YOU SOON :)')

def save_invoice():
    invoice_info = invoice_text.get(1.0, END)
    my_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    my_file.write(invoice_info)
    my_file.close()
    messagebox.showinfo('Notification', 'Your invoice is saved')

def reset_all():
    invoice_text.delete(0.1, END)
    for text in food_text:
        text.set('0')
    for text in drink_text:
        text.set('0')
    for text in dessert_text:
        text.set('0')

    for box in food_box:
        box.config(state=DISABLED)
    for box in drink_box:
        box.config(state=DISABLED)
    for box in dessert_box:
        box.config(state=DISABLED)

    for var in food_variables:
        var.set(0)
    for var in drink_variables:
        var.set(0)
    for var in dessert_variables:
        var.set(0)

    food_cost_var.set('')
    drink_cost_var.set('')
    dessert_cost_var.set('')

#Initialize TKinker
application = Tk()

# Window size
application.geometry('1020x630+0+0')

# Prevent from maximizing
application.resizable(False, False)

#Window title
application.title('My Restaurant - Invoicing System')

# Window background color
application.config(bg='burlywood')

# Top panel
top_panel = Frame(application, bd = 1, relief= FLAT)
top_panel.pack(side = TOP)

#Title tag
title_tag = Label(top_panel, text = 'Invoicing System', fg = 'azure4',
                  font = ('Dosis', 58), bg = 'burlywood', width = 27)
title_tag.grid(row = 0, column = 0)

#Left panel
left_panel = Frame(application, bd = 1, relief=FLAT)
left_panel.pack(side=LEFT)

#Cost Panel
cost_panel = Frame(left_panel, bd = 1, relief = FLAT, bg = 'azure4')
cost_panel.pack(side=BOTTOM)

#Food panel
food_panel = LabelFrame(left_panel, text = 'Food', font = ('Dosis', 19, 'bold'),
                        bd = 1, relief=FLAT, fg='azure4')
food_panel.pack(side=LEFT)

#Drink panel
drink_panel = LabelFrame(left_panel, text = 'Drink', font = ('Dosis', 19, 'bold'),
                        bd = 1, relief=FLAT, fg='azure4')
drink_panel.pack(side=LEFT)

#Dessert panel
dessert_panel = LabelFrame(left_panel, text = 'Dessert', font = ('Dosis', 19, 'bold'),
                        bd = 1, relief=FLAT, fg='azure4')
dessert_panel.pack(side=LEFT)

#Right panel
right_panel = Frame(application, bd = 1, relief=FLAT)
right_panel.pack(side=RIGHT)

#Calculator panel
calculator_panel = Frame(right_panel, bd = 1, relief=FLAT, bg = 'burlywood')
calculator_panel.pack()

#Invoice panel
invoice_panel = Frame(right_panel, bd = 1, relief=FLAT, bg = 'burlywood')
invoice_panel.pack()

#buttons panel
buttons_panel = Frame(right_panel, bd = 1, relief=FLAT, bg = 'burlywood')
buttons_panel.pack()

#Product lists
food_list = ['Chicken', 'Lamb', 'Salmon', 'Hake', 'Kebabs', 'Pizza(Cheese Burst)', 'Pizza(Fresh Farm)', 'Pizza(Margerta)']
drink_list = ['Mango juice', 'Lemon juice', 'Oreo shake', 'Chocolate shake', 'Vanilla shake', 'Watermelon juice', 'Orange juice', 'Mango shake']
dessert_list = ['Ice Creams', 'Gulab Jamun', 'Rasgulla', 'Rasmali', 'Vermiceli', 'Casatta', ' Chocolate Mouse', 'Browines']

#Create food items
food_variables = []
food_box = []
food_text = []
counter = 0
for food in food_list:

    #Create checkbuttons
    food_variables.append('')
    food_variables[counter] = IntVar()
    food = Checkbutton(food_panel, text = food.title(), font = ('Dosis', '10', 'bold'),
                       onvalue=1, offvalue=0,
                       variable=food_variables[counter],
                       command=review_check)
    food.grid(row=counter, column=0, sticky=W)

    #Create input boxes
    food_box.append('')
    food_text.append('')
    food_text[counter] = StringVar()
    food_text[counter].set('0')
    food_box[counter] = Entry(food_panel, font = ('Dosis', 10, 'bold'), bd = 1, width = 6, state = DISABLED, textvariable = food_text[counter])
    food_box[counter].grid(row = counter, column=1)


    counter+=1

#Create drink items
drink_variables = []
drink_box = []
drink_text = []
counter1 = 0

#Create checkbuttons
for drink in drink_list:
    drink_variables.append('')
    drink_variables[counter1] = IntVar()
    drink = Checkbutton(drink_panel, text = drink.title(), font = ('Dosis', '10', 'bold'),
                       onvalue=1, offvalue=0,
                        variable=drink_variables[counter1],
                        command=review_check)
    drink.grid(row=counter1, column=0, sticky=W)

    # Create input boxes
    drink_box.append('')
    drink_text.append('')
    drink_text[counter1] = StringVar()
    drink_text[counter1].set('0')
    drink_box[counter1] = Entry(drink_panel, font=('Dosis', 10, 'bold'), bd=1, width=6, state=DISABLED, textvariable=drink_text[counter1])
    drink_box[counter1].grid(row=counter1, column=1)
    counter1+=1

#Create dessert items
dessert_variables = []
dessert_box = []
dessert_text = []
counter2 = 0


#Create checkbuttons
for dessert in dessert_list:
    dessert_variables.append('')
    dessert_variables[counter2] = IntVar()
    dessert = Checkbutton(dessert_panel, text = dessert.title(), font = ('Dosis', '10', 'bold'),
                       onvalue=1, offvalue=0,
                          variable=dessert_variables[counter2],
                          command=review_check)
    dessert.grid(row=counter2, column=0, sticky=W)

    # Create input boxes
    dessert_box.append('')
    dessert_text.append('')
    dessert_text[counter2] = StringVar()
    dessert_text[counter2].set('0')
    dessert_box[counter2] = Entry(dessert_panel, font=('Dosis', 10, 'bold'), bd=1, width=6, state=DISABLED, textvariable=dessert_text[counter2])
    dessert_box[counter2].grid(row=counter2, column=1)
    counter2+=1

#Variables
food_cost_var = StringVar()
drink_cost_var = StringVar()
dessert_cost_var = StringVar()
subtotal_var = StringVar()
taxes_var = StringVar()
total_var = StringVar()


#Cost labels and input fields

food_cost_label = Label(cost_panel, text='Food Cost', font = ('Dosis', 12, 'bold'), bg = 'azure4', fg = 'white')
food_cost_label.grid(row= 0, column=0, padx= 40)
food_cost_text = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd =1, width = 10, state = 'readonly', textvariable = food_cost_var)
food_cost_text.grid(row=0, column= 1, padx =40)

drink_cost_label = Label(cost_panel, text='Drink Cost', font = ('Dosis', 12, 'bold'), bg = 'azure4', fg = 'white')
drink_cost_label.grid(row= 1, column=0, padx=40)
drink_cost_text = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd =1, width = 10, state = 'readonly', textvariable = drink_cost_var)
drink_cost_text.grid(row=1, column= 1, padx=40)

dessert_cost_label = Label(cost_panel, text='Dessert Cost', font = ('Dosis', 12, 'bold'), bg = 'azure4', fg = 'white')
dessert_cost_label.grid(row= 2, column=0)
dessert_cost_text = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd =1, width = 10, state = 'readonly', textvariable = dessert_cost_var)
dessert_cost_text.grid(row=2, column= 1)

subtotal_label = Label(cost_panel, text='Subtotal', font = ('Dosis', 12, 'bold'), bg = 'azure4', fg = 'white')
subtotal_label.grid(row= 0, column=2, padx = 40)
subtotal_text = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd =1, width = 10, state = 'readonly', textvariable = subtotal_var)
subtotal_text.grid(row=0, column= 3, padx = 40)

taxes_label = Label(cost_panel, text='Taxes', font = ('Dosis', 12, 'bold'), bg = 'azure4', fg = 'white')
taxes_label.grid(row= 1, column=2, padx = 40)
taxes_text = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd =1, width = 10, state = 'readonly', textvariable = taxes_var)
taxes_text.grid(row=1, column= 3, padx = 40)

total_label = Label(cost_panel, text='Total Cost', font = ('Dosis', 12, 'bold'), bg = 'azure4', fg = 'white')
total_label.grid(row= 2, column=2, padx = 40)
total_text = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd =1, width = 10, state = 'readonly', textvariable = total_var)
total_text.grid(row=2, column= 3, padx = 40)


#Buttons
buttons = ['total', 'invoice', 'save', 'reset']
created_buttons = []
column = 0
for button in buttons:
    button = Button(buttons_panel, text = button.title(), font=('Dosis', 14, 'bold'), fg ='white', bg= 'azure4', bd =1, width = 5)
    created_buttons.append((button))
    button.grid(row =0, column=column)
    column+=1

created_buttons[0].config(command=total_calculations)
created_buttons[1].config(command=create_invoice)
created_buttons[2].config(command=save_invoice)
created_buttons[3].config(command=reset_all)

#Invoice area
invoice_text = Text(invoice_panel, font=('Dosis', 12, 'bold'), bd = 1, width = 32, height = 10)
invoice_text.grid(row=0, column=0)


#Calculator
calculator_display = Entry(calculator_panel, font=('Dosis', 16, 'bold'), width = 20, bd =1)
calculator_display.grid(row = 0, column=0, columnspan=4)
calculator_buttons = ['7', '8', '9', '+',
                      '4', '5', '6', '-',
                      '1', '2', '3', '*',
                      'CE', 'Delete', '0', '/']
stored_buttons = []

my_row = 1
my_column = 0
for button in calculator_buttons:
    button = Button(calculator_panel, text = button.title(), font =('Dosis', 16, 'bold'), fg = 'white', bg = 'azure4', bd = 1, width =5)
    button.grid(row=my_row, column = my_column)
    stored_buttons.append(button)

    if my_column==3:
        my_row+=1
    my_column+=1
    if my_column==4:
        my_column=0

stored_buttons[0].config(command=lambda:click_buttton('7'))
stored_buttons[1].config(command=lambda:click_buttton('8'))
stored_buttons[2].config(command=lambda:click_buttton('9'))
stored_buttons[3].config(command=lambda:click_buttton('+'))
stored_buttons[4].config(command=lambda:click_buttton('4'))
stored_buttons[5].config(command=lambda:click_buttton('5'))
stored_buttons[6].config(command=lambda:click_buttton('6'))
stored_buttons[7].config(command=lambda:click_buttton('-'))
stored_buttons[8].config(command=lambda:click_buttton('1'))
stored_buttons[9].config(command=lambda:click_buttton('2'))
stored_buttons[10].config(command=lambda:click_buttton('3'))
stored_buttons[11].config(command=lambda:click_buttton('*'))
stored_buttons[12].config(command=get_result)
stored_buttons[13].config(command=delete_all)
stored_buttons[14].config(command=lambda:click_buttton('0'))
stored_buttons[15].config(command=lambda:click_buttton('/'))



#Prevent window from closing
application.mainloop()
