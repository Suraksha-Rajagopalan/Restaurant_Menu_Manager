<div align = center><h1><strong>🍦🍕🍋Restaurant Menu Manager🍋🍕🍦</strong></h1></div>

<div align = center>
<img src ="https://user-images.githubusercontent.com/91787553/210555412-cd21d837-37cb-4229-a340-495fce0b1bcc.png">
</div>

Here is a restaurant menu manager, where in we can select the items they we want to order and the bill, with invoice, receipt to save and reset option is available.

Here's how each of the following option works.

## For TOTAL

<div align = center>
<img src = "https://user-images.githubusercontent.com/91787553/210557921-bc235b17-26d3-4f69-9113-fb1d3f1c7c50.png">
</div>

## For INVOICE
<div align = center>
<img src = "https://user-images.githubusercontent.com/91787553/210558173-964fb16f-3c74-472b-a252-a1672b1afcd3.png">
</div>

## For RESET
<div align = center>
<img src = "https://user-images.githubusercontent.com/91787553/210558911-f2c1cff6-022e-4416-8014-0fb04ec13352.png">
</div>

## ABOUT tkinter

The tkinter package( “ Tk interface ”) is the standard Python interface to the Tcl/ Tk GUI toolkit. Both Tk and tkinter are available on utmost Unix platforms, including macOS, as well as on Windows systems.

Running python- m tkinter from the command line should open a window demonstrating a simple Tk interface, letting you know that tkinter is duly installed on your system, and also showing what interpretation of Tcl/ Tk is installed, so you can read the Tcl/ Tk attestation specific to that interpretation.
Tkinter supports a range of Tcl/ Tk performances, erected either with or without thread support. The sanctioned Python double release packets Tcl Tk8.6 threaded. See the source law for the, tkinter module for further information about supported performances.

Tkinter isn't a thin wrapper, but adds a fair quantum of its own sense to make the experience more pythonic. This attestation will concentrate on these additions and changes, and relate to the sanctioned Tcl/ Tk attestation for details that are unchanged.

Tkinter is a good choice because of the following reasons:

- Easy to learn.
- Use very little code to make a functional desktop application.
- Layered design.
- Portable across all operating systems including Windows, macOS, and Linux.
- Pre-installed with the standard Python library.

To import the package:

```python
from tkinter import *
from tkinter import ttk
```

A sample code of "Hello World" using the package:

```python
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
```

## More about the package:

<h2>
<a href = "https://realpython.com/python-gui-tkinter/">tkinker-1</a><br>
<a href = "https://www.geeksforgeeks.org/python-gui-tkinter/">tkinker-2</a><br>
<a href = "https://pythonbasics.org/tkinter/">tkinker-3</a>
</h2>
