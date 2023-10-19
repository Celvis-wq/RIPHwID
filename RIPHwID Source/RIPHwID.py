# RIPHwID source
# Celvis

# Import
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageTk
import sys
from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QWidget, QMainWindow, QApplication
from PyQt5.QtCore import QTimer

# Button Function
def toggleButtonStateAssist():
    global buttonEnabledAssist
    if buttonEnabledAssist:
        buttonEnabledAssist = False
        button1.config(bg='white')
        buttonImage.paste((0, 0, 0), checkmarkArea)
        if buttonEnabledSettings:
            alertLabel.setText("Begin RIPHwID has been disabled")
    else:
        buttonEnabledAssist = True
        button1.config(bg='yellow')
        buttonImage.paste((0, 255, 0), checkmarkArea)
        if buttonEnabledSettings:
            alertLabel.setText("Begin RIPHwID has been enabled")

def toggleButtonStateSettings():
    global buttonEnabledSettings
    if buttonEnabledSettings:
        buttonEnabledSettings = False
        buttonSettings.config(bg='white')
        buttonImageSettings.paste((0, 0, 0), checkmarkAreaSettings)
    else:
        buttonEnabledSettings = True
        buttonSettings.config(bg='yellow')
        buttonImageSettings.paste((0, 255, 0), checkmarkAreaSettings)
        if buttonEnabledAssist and enableAlerts:
            alertLabel.setText("Button has been enabled")

def toggleAlertStatus():
    global enableAlerts
    if buttonEnabledSettings:
        enableAlerts = True
        alertLabel.setText("Alerts have been enabled")
    else:
        enableAlerts = False
        alertLabel.setText("Alerts have been disabled")

# button states
buttonEnabledAssist = False
buttonEnabledSettings = False
enableAlerts = False

# window
root = tk.Tk()
root.title("RIPHwID")
root.geometry("500x300")

# tab style
style = ttk.Style()
style.configure("TNotebook.Tab", background='#5D3FD3', bordercolor='#5D3FD3')
style.configure("TNotebook", background='#5D3FD3')

# Create the Notebook (tabs) using Tkinter
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# Tab 1: Assist
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Assist")

# Set the background color for tab1 content area (Assist)
tab1ContentFrame = tk.Frame(tab1, bg='#5D3FD3')
tab1ContentFrame.pack(fill=tk.BOTH, expand=True)

# Create a "Begin RIPHwID" button in the first tab using Tkinter
button1 = tk.Button(tab1ContentFrame, text="Begin RIPHwID", command=toggleButtonStateAssist, bg='white')
button1.pack(pady=20)

# Create a green checkmark image
checkmarkImage = Image.new('RGB', (20, 20), 'white')
draw = ImageDraw.Draw(checkmarkImage)
draw.line([(5, 10), (9, 15), (15, 5)], fill='green', width=2)
buttonImage = ImageTk.PhotoImage(checkmarkImage)

# Create an area on the button to display the checkmark
checkmarkArea = (10, 5, 30, 25)

# Tab 2: Test
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Test")

# Set the background color for tab2 content area (Test)
tab2ContentFrame = tk.Frame(tab2, bg='#5D3FD3')
tab2ContentFrame.pack(fill=tk.BOTH, expand=True)

# Tab 3: Spoof
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Spoof")

# Set the background color for tab3 content area (Spoof)
tab3ContentFrame = tk.Frame(tab3, bg='#5D3FD3')
tab3ContentFrame.pack(fill=tk.BOTH, expand=True)

# Tab 4: Settings
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Settings")

# Set the background color for tab4 content area (Settings)
tab4ContentFrame = tk.Frame(tab4, bg='#5D3FD3')
tab4ContentFrame.pack(fill=tk.BOTH, expand=True)

# Create a "Enable Alerts" button in the "Settings" tab using Tkinter
buttonSettings = tk.Button(tab4ContentFrame, text="Enable Alerts", command=toggleButtonStateSettings, bg='white')
buttonSettings.pack(pady=20)

# Create a green checkmark image for the "Settings" button
checkmarkImageSettings = Image.new('RGB', (20, 20), 'white')
drawSettings = ImageDraw.Draw(checkmarkImageSettings)
drawSettings.line([(5, 10), (9, 15), (15, 5)], fill='green', width=2)
buttonImageSettings = ImageTk.PhotoImage(checkmarkImageSettings)

# Create an area on the "Settings" button to display the checkmark
checkmarkAreaSettings = (10, 5, 30, 25)

# Create a label for displaying alerts using PyQt5
class AlertApp(QMainWindow):
    def __init__(self):
        super().__init__(None)  # Use None as the parent
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Alerts')
        self.setGeometry(100, 100, 400, 50)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout(self.centralWidget)

        self.alertLabel = QLabel(self)
        self.alertLabel.setText('')
        self.layout.addWidget(self.alertLabel)

        self.timer = QTimer()
        self.timer.timeout.connect(self.clearAlert)

    def clearAlert(self):
        self.alertLabel.setText('')
        self.timer.stop()

# Initialize the PyQt5 application
app = QApplication(sys.argv)
window = AlertApp()
window.show()

root.mainloop()
sys.exit(app.exec_())


"""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageTk

# Function to toggle the button state and appearance in the "Assist" tab
def toggleButtonStateAssist():
    global buttonEnabledAssist
    if buttonEnabledAssist:
        buttonEnabledAssist = False
        button1.config(bg='white')
        buttonImage.paste((0, 0, 0), checkmarkArea)
        if buttonEnabledSettings:
            alertLabel.config(text="Begin RIPHwID has been disabled", fg="red")
    else:
        buttonEnabledAssist = True
        button1.config(bg='yellow')
        buttonImage.paste((0, 255, 0), checkmarkArea)
        if buttonEnabledSettings:
            alertLabel.config(text="Begin RIPHwID has been enabled", fg="green")

# Function to toggle the button state and appearance in the "Settings" tab
def toggleButtonStateSettings():
    global buttonEnabledSettings
    if buttonEnabledSettings:
        buttonEnabledSettings = False
        buttonSettings.config(bg='white')
        buttonImageSettings.paste((0, 0, 0), checkmarkAreaSettings)
    else:
        buttonEnabledSettings = True
        buttonSettings.config(bg='yellow')
        buttonImageSettings.paste((0, 255, 0), checkmarkAreaSettings)
        if buttonEnabledAssist:
            alertLabel.config(text="Button has been enabled", fg="green")

# Function to clear the alert message
def clearAlert():
    alertLabel.config(text="")

# Initialize button states
buttonEnabledAssist = False
buttonEnabledSettings = False

# Create the main window
root = tk.Tk()
root.title("RIPHwID")
root.geometry("500x300")

# Create a style for the tabs
style = ttk.Style()
style.configure("TNotebook.Tab", background='#5D3FD3', bordercolor='#5D3FD3')
style.configure("TNotebook", background='#5D3FD3')

# Create the Notebook (tabs)
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# Tab 1: Assist
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Assist")

# Set the background color for tab1 content area (Assist)
tab1ContentFrame = tk.Frame(tab1, bg='#5D3FD3')
tab1ContentFrame.pack(fill=tk.BOTH, expand=True)

# Create a "Begin RIPHwID" button in the first tab
button1 = tk.Button(tab1ContentFrame, text="Begin RIPHwID", command=toggleButtonStateAssist, bg='white')
button1.pack(pady=20)

# Create a green checkmark image
checkmarkImage = Image.new('RGB', (20, 20), 'white')
draw = ImageDraw.Draw(checkmarkImage)
draw.line([(5, 10), (9, 15), (15, 5)], fill='green', width=2)
buttonImage = ImageTk.PhotoImage(checkmarkImage)

# Create an area on the button to display the checkmark
checkmarkArea = (10, 5, 30, 25)

# Tab 2: Test
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Test")

# Set the background color for tab2 content area (Test)
tab2ContentFrame = tk.Frame(tab2, bg='#5D3FD3')
tab2ContentFrame.pack(fill=tk.BOTH, expand=True)

# Tab 3: Spoof
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Spoof")

# Set the background color for tab3 content area (Spoof)
tab3ContentFrame = tk.Frame(tab3, bg='#5D3FD3')
tab3ContentFrame.pack(fill=tk.BOTH, expand=True)

# Tab 4: Settings
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Settings")

# Set the background color for tab4 content area (Settings)
tab4ContentFrame = tk.Frame(tab4, bg='#5D3FD3')
tab4ContentFrame.pack(fill=tk.BOTH, expand=True)

# Create a "Enable Alerts" button in the "Settings" tab
buttonSettings = tk.Button(tab4ContentFrame, text="Enable Alerts", command=toggleButtonStateSettings, bg='white')
buttonSettings.pack(pady=20)

# Create a green checkmark image for the "Settings" button
checkmarkImageSettings = Image.new('RGB', (20, 20), 'white')
drawSettings = ImageDraw.Draw(checkmarkImageSettings)
drawSettings.line([(5, 10), (9, 15), (15, 5)], fill='green', width=2)
buttonImageSettings = ImageTk.PhotoImage(checkmarkImageSettings)

# Create an area on the "Settings" button to display the checkmark
checkmarkAreaSettings = (10, 5, 30, 25)

# Create a label for displaying alerts
alertLabel = tk.Label(tab4ContentFrame, text="", fg="black")
alertLabel.pack(pady=10)

root.mainloop()
"""