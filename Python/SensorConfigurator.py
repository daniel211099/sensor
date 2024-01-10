import serial
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog, Entry, Label
print("serial-Modulversion:", serial.__version__)
# Konfiguriere die UART-Verbindung
ser = serial.Serial('COM6', 115200, timeout=1)  # 'COM3' entsprechend dem verwendeten COM-Port

# Erstelle ein Tkinter-Fenster
root = tk.Tk()
root.title("UART Nachrichten")

# Erstelle ein Text-Widget für die Anzeige der Nachrichten
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20)
text_area.pack(padx=10, pady=10)

def receive_messages():
    try:
        while True:
            try:
                response = ser.readline().decode('utf-8').strip()
                if response:
                    text_area.insert(tk.END, f"Empfangene Antwort: {response}\n")
                    text_area.yview(tk.END)  # Scrollt automatisch zum Ende des Textbereichs
            except:
                print("Fehler")

    except KeyboardInterrupt:
        print("\nEmpfangs-Thread wurde beendet.")

def send_message(message):
    ser.write(message.encode())  # Sende die Nachricht als Bytes
    print(f"Nachricht '{message}' wurde gesendet.")

def send_custom_command():
    frequency = simpledialog.askinteger("Frequenz eingeben", "Gib die Frequenz (1-200) ein:")
    if frequency is not None:
        if 1 <= frequency <= 200:
            message = f"!FREQ{frequency}\r\n"
            send_message(message)
        else:
            print("Ungültige Frequenz. Bitte gib eine Zahl zwischen 1 und 200 ein.")
# Funktion, um die Calibration-GUI zu erstellen
def create_calibration_gui():
    cal_gui = tk.Toplevel(root)
    cal_gui.title("Calibration")

    # Textfelder für Float-Werte
    label1 = Label(cal_gui, text="Value 1:")
    label1.grid(row=0, column=0, padx=5, pady=5)
    entry1 = Entry(cal_gui)
    entry1.grid(row=0, column=1, padx=5, pady=5)

    label2 = Label(cal_gui, text="Value 2:")
    label2.grid(row=1, column=0, padx=5, pady=5)
    entry2 = Entry(cal_gui)
    entry2.grid(row=1, column=1, padx=5, pady=5)

    label3 = Label(cal_gui, text="Value 3:")
    label3.grid(row=2, column=0, padx=5, pady=5)
    entry3 = Entry(cal_gui)
    entry3.grid(row=2, column=1, padx=5, pady=5)

    label4 = Label(cal_gui, text="Value 4:")
    label4.grid(row=3, column=0, padx=5, pady=5)
    entry4 = Entry(cal_gui)
    entry4.grid(row=3, column=1, padx=5, pady=5)

    label5 = Label(cal_gui, text="Value 5:")
    label5.grid(row=4, column=0, padx=5, pady=5)
    entry5 = Entry(cal_gui)
    entry5.grid(row=4, column=1, padx=5, pady=5)

    # Funktion zum Senden der Curve
    def send_curve():
        values = [entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get()]
        try:
            # Überprüfe, ob alle Werte Floats sind
            float_values = [float(value) for value in values]
            message = f"!curve {' '.join(map(str, float_values))}\r\n"
            send_message(message)
        except ValueError:
            print("Ungültige Werte. Bitte gib gültige Float-Werte ein.")

    # Funktionen für die CAL Reset, CAL End und CAL Set diam Buttons
    def cal_reset():
        send_message("!cal reset\r\n")
    def cal_end():
        send_message("!cal end\r\n")

    def cal_set_diam():
        diam_value = cal_diam_entry.get()
        try:
            float_diam_value = float(diam_value)
            message = f"!CAL {float_diam_value}\r\n"
            send_message(message)
        except ValueError:
            print("Ungültiger Durchmesser. Bitte gib einen gültigen Float-Wert ein.")

    # Button zum Senden der Curve
    send_curve_button = tk.Button(cal_gui, text="Send Curve", command=send_curve)
    send_curve_button.grid(row=5, column=0, columnspan=2, pady=10)

    # Buttons für CAL Reset, CAL End und CAL Set diam
    cal_reset_button = tk.Button(cal_gui, text="CAL Reset", command=cal_reset)
    cal_reset_button.grid(row=6, column=0, pady=5)

    cal_end_button = tk.Button(cal_gui, text="CAL End", command=cal_end)
    cal_end_button.grid(row=6, column=1, pady=5)

    cal_diam_label = Label(cal_gui, text="Diameter:")
    cal_diam_label.grid(row=7, column=0, padx=5, pady=5)
    cal_diam_entry = Entry(cal_gui)
    cal_diam_entry.grid(row=7, column=1, padx=5, pady=5)

    cal_set_diam_button = tk.Button(cal_gui, text="CAL Set diam", command=cal_set_diam)
    cal_set_diam_button.grid(row=8, column=0, columnspan=2, pady=10)
# Starte die Threads
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Erstelle Buttons für die verschiedenen Befehle
freq_button = tk.Button(root, text="?FREQ", command=lambda: send_message("?FREQ\r\n"))
freq_button.pack(side=tk.LEFT, padx=5)

curve_button = tk.Button(root, text="?CURVE", command=lambda: send_message("?CURVE\r\n"))
curve_button.pack(side=tk.LEFT, padx=5)

type_button = tk.Button(root, text="?TYPE", command=lambda: send_message("?TYPE\r\n"))
type_button.pack(side=tk.LEFT, padx=5)

id_button = tk.Button(root, text="?SN", command=lambda: send_message("?SN\r\n"))
id_button.pack(side=tk.LEFT, padx=5)

custom_button = tk.Button(root, text="!FREQ", command=send_custom_command)
custom_button.pack(side=tk.LEFT, padx=5)

# Button für die Calibration-GUI
calibration_button = tk.Button(root, text="Calibration", command=create_calibration_gui)
calibration_button.pack(side=tk.LEFT, padx=5)

# Starte die Tkinter Hauptloop
root.mainloop()

# Warte darauf, dass der Empfangs-Thread beendet wird
receive_thread.join()

# Schließe die UART-Verbindung, wenn das Skript beendet wird
ser.close()
