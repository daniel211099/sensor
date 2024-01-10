import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

import serial
from datetime import datetime, timedelta
import csv
import time


class SetStateWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Set State Window")

        # Buttons für die verschiedenen Modi
        self.idle_button = tk.Button(self.master, text="IDLE_MODE", command=lambda: self.set_state("IDLE_MODE"))
        self.idle_button.grid(row=0, column=0, padx=10, pady=10)

        self.manual_button = tk.Button(self.master, text="MANUAL_MODE", command=lambda: self.set_state("MANUAL_MODE"))
        self.manual_button.grid(row=1, column=0, padx=10, pady=10)

        self.automatic_button = tk.Button(self.master, text="AUTOMATIC_MODE",
                                          command=lambda: self.set_state("AUTOMATIC_MODE"))
        self.automatic_button.grid(row=2, column=0, padx=10, pady=10)

    def set_state(self, mode):
        query = ""
        if mode == "IDLE_MODE":
            query = f"!STATE {0}\r\n"
        elif mode == "MANUAL_MODE":
            query = f"!STATE {1}\r\n"
        elif mode == "AUTOMATIC_MODE":
            query = f"!STATE {2}\r\n"

        send_message(query)


class SetSpeedWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Set Speed Window")

        # Textbox für die Eingabe der Geschwindigkeit
        self.speed_value = tk.IntVar()
        self.speed_entry = tk.Entry(self.master, textvariable=self.speed_value)
        self.speed_entry.grid(row=0, column=0, padx=10, pady=10)

        # Button zum Setzen der Geschwindigkeit
        self.set_speed_button = tk.Button(self.master, text="Set", command=self.set_speed)
        self.set_speed_button.grid(row=0, column=1, padx=10, pady=10)

    def set_speed(self):
        speed = self.speed_value.get()
        if speed >= 0:
            query = f"!SPEED {speed}\r\n"
            send_message(query)
            messagebox.showinfo("Success", f"Speed set to {speed}")
            self.master.destroy()
        else:
            messagebox.showwarning("Invalid Input", "Geschwindigkeit muss größer gleich 0 sein.")


class ControlParamsWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Control Parameters Window")

        # Textfelder für P-, I- und D-Anteile
        self.p_value = tk.DoubleVar()
        self.i_value = tk.DoubleVar()
        self.d_value = tk.DoubleVar()

        self.p_entry = tk.Entry(self.master, textvariable=self.p_value, width=10)
        self.p_entry.grid(row=0, column=1, padx=5, pady=5)
        self.i_entry = tk.Entry(self.master, textvariable=self.i_value, width=10)
        self.i_entry.grid(row=1, column=1, padx=5, pady=5)
        self.d_entry = tk.Entry(self.master, textvariable=self.d_value, width=10)
        self.d_entry.grid(row=2, column=1, padx=5, pady=5)

        # Buttons für Abfragen von P-, I- und D-Anteilen
        self.p_get_button = tk.Button(self.master, text="?P-Anteil", command=self.get_p)
        self.p_get_button.grid(row=0, column=0, padx=5, pady=5)
        self.i_get_button = tk.Button(self.master, text="?I-Anteil", command=self.get_i)
        self.i_get_button.grid(row=1, column=0, padx=5, pady=5)
        self.d_get_button = tk.Button(self.master, text="?D-Anteil", command=self.get_d)
        self.d_get_button.grid(row=2, column=0, padx=5, pady=5)

        # Buttons für Setzen von P-, I- und D-Anteilen
        self.set_p_button = tk.Button(self.master, text="!P-Anteil", command=self.set_p)
        self.set_p_button.grid(row=0, column=2, padx=5, pady=5)
        self.set_i_button = tk.Button(self.master, text="!I-Anteil", command=self.set_i)
        self.set_i_button.grid(row=1, column=2, padx=5, pady=5)
        self.set_d_button = tk.Button(self.master, text="!D-Anteil", command=self.set_d)
        self.set_d_button.grid(row=2, column=2, padx=5, pady=5)

    def get_p(self):
        query = "?CP\r\n"
        send_message(query)
        self.p_value.set(0.0)

    def get_i(self):
        query = "?CI\r\n"
        send_message(query)
        self.i_value.set(0.0)

    def get_d(self):
        query = "?CD\r\n"
        send_message(query)
        self.d_value.set(0.0)

    def set_p(self):
        query = "!CP " + str(self.p_value.get()) + "\r\n"
        send_message(query)

    def set_i(self):
        query = "!CI " + str(self.i_value.get()) + "\r\n"
        send_message(query)

    def set_d(self):
        query = "!CD " + str(self.d_value.get()) + "\r\n"
        send_message(query)

    def display_message(self, message):
        # Funktion zum Anzeigen von Nachrichten im Textfeld
        print(message)


class MyApp:
    def receive_messages(self):
        try:
            while True:
                response = serial.readline().decode('utf-8').strip()
                if response:
                    self.text_area.insert(tk.END, f"Empfangene Antwort: {response}\n")
                    self.text_area.yview(tk.END)  # Scrollt automatisch zum Ende des Textbereichs

        except KeyboardInterrupt:
            print("\nEmpfangs-Thread wurde beendet.")

    def __init__(self, root):
        self.start_flag = False
        self.start_time = None
        self.messagesDiamExt = []
        self.messagesDiamBack = []

        self.root = root
        self.root.title("UART Control App")

        # Textfeld für empfangene UART-Nachrichten
        self.text_area = scrolledtext.ScrolledText(self.root, width=50, height=10)
        self.text_area.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Buttons für Zustand, Geschwindigkeit und Kontrollparameter setzen
        self.state_button = tk.Button(self.root, text="Set State", command=self.open_set_state_window)
        self.state_button.grid(row=1, column=0, padx=5, pady=5)

        self.speed_button = tk.Button(self.root, text="Set Speed", command=self.set_speed)
        self.speed_button.grid(row=1, column=1, padx=5, pady=5)

        # Buttons für Abfragen von Zustand, Geschwindigkeit und Kontrollparameter
        self.state_get_button = tk.Button(self.root, text="?STATE", command=self.get_state)
        self.state_get_button.grid(row=2, column=0, padx=5, pady=5)

        self.speed_get_button = tk.Button(self.root, text="?SPEED", command=self.get_speed)
        self.speed_get_button.grid(row=2, column=1, padx=5, pady=5)

        self.control_params_get_button = tk.Button(self.root, text="?ControlParams",command=self.open_control_params_window)
        self.control_params_get_button.grid(row=2, column=2, padx=5, pady=5)

        # UART-Verbindung konfigurieren
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

    def open_set_state_window(self):
        # Öffne das Fenster zum Setzen des Zustands
        set_state_window = tk.Toplevel(self.root)
        SetStateWindow(set_state_window)

    def set_speed(self):
        set_speed_window = tk.Toplevel(self.root)
        SetSpeedWindow(set_speed_window)

    def set_control_params(self):
        self.display_message("Set Control parameters button clicked")

    def get_state(self):
        speed_get = "?STATE\r\n"
        send_message(speed_get)

    def get_speed(self):
        speed_get = "?SPEED\r\n"
        send_message(speed_get)

    def open_control_params_window(self):
        # Öffne das Fenster für die Abfrage von P-, I- und D-Anteilen der Kontrollparameter
        control_params_window = tk.Toplevel(self.root)
        ControlParamsWindow(control_params_window)

    def display_message(self, message):
        # Funktion zum Anzeigen von Nachrichten im Textfeld
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.yview(tk.END)


serial = serial.Serial('COM5', 115200, timeout=1)  # 'COM3' entsprechend dem verwendeten COM-Port


def send_message(message):
    serial.write(message.encode())  # Sende die Nachricht als Bytes
    print(f"Nachricht '{message}' wurde gesendet.")


root = tk.Tk()
app = MyApp(root)
root.mainloop()
