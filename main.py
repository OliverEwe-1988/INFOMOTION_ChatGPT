import os
import sys
import pandas as pd
import io

import openai
import json

import subprocess
import requests

from PyQt5.QtGui import QIcon
from qtpy import QtWidgets
from PyQt5.QtWidgets import *
# from PIL import Image
# import matplotlib.pyplot as plt

from QtCreatorChatGPT.codechatgpt import Ui_CodeChatGPT
from QtCreatorChatGPT.firstrowchatgpt import Ui_FirstRowChatGPT
from QtCreatorChatGPT.mainwindow import Ui_MainWindow
from QtCreatorChatGPT.direktchatgpt import Ui_DirektChatGPT
from QtCreatorChatGPT.projektteam import Ui_Projektteam
from QtCreatorChatGPT.tablechatgpt import Ui_TableChatGPT

pfad = None

# NEU: 07.10.2023 -> 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

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("Bilder/Icon_Info.svg"))
        self.setWindowTitle("INFOMOTION")
        self.ui.actiondirekt.triggered.connect(self.zeigeDirektChatGPTFenster)
        self.ui.actionCode.triggered.connect(self.zeigeCodeChatGPTFenster)
        self.ui.action1_Reihe.triggered.connect(self.zeigeFirstRowChatGPTFenster)
        self.ui.actionTabelle.triggered.connect(self.zeigeTableChatGPTFenster)

        # Abfrage bei 1. Aufruf der Mainclass nach API ja/nein... Checkbox
        # if self.ui.checkAPIKey.isChecked():
        #     openai.api_key = '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'  # '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'
        #     print(openai.api_key)
        # else:
        #     openai.api_key = self.ui.textEdit_2.toPlainText()
        #     print(openai.api_key)
        # self.ui.checkAPIKey.clicked.connect(self.getApiKey)

        self.ui.actionLaden.triggered.connect(self.file_laden_dialog)
        self.ui.actionDatei_l_schen.triggered.connect(self.file_delete_dialog)

        self.ui.actionProjektteam.triggered.connect(self.zeigeProjektTeamFenster)

    #Abfrage nach API Key wenn sich der Zustand der Checkbox ändert
    def getApiKey(self):
        if self.ui.checkAPIKey.isChecked():
            openai.api_key = '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'
            print(openai.api_key)
        else:
            openai.api_key = self.ui.textEdit_2.toPlainText()
            print(openai.api_key)

    def file_laden_dialog(self):
        self.ui.file_dialog = QFileDialog()
        self.ui.file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_path, _ = self.ui.file_dialog.getOpenFileName(self, "Datei auswählen")
        self.pfad = str(file_path)

        if file_path:
            self.process_file(file_path)

    def process_file(self, file_path):
        print(file_path)
        self.ui.dateiLabel.setText(f"Ausgewählte Datei: " + file_path)

    def file_delete_dialog(self):
        self.ui.dateiLabel.setText("Keine Datei ausgewählt")

    def zeigeFenster(self, fenster_klasse):
        self.fenster = fenster_klasse()
        self.fenster.show()
        self.close()

    def zeigeDirektChatGPTFenster(self):
        self.zeigeFenster(direktChatGPTFenster)

    def zeigeCodeChatGPTFenster(self):
        self.zeigeFenster(CodeChatGPTFenster)

    def zeigeFirstRowChatGPTFenster(self):
        self.zeigeFenster(FirstRowChatGPTFenster)

    def zeigeTableChatGPTFenster(self):
        self.zeigeFenster(TableChatGPTFenster)

    def zeigeProjektTeamFenster(self):
        self.zeigeFenster(ProjektteamFenster)


class direktChatGPTFenster(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DirektChatGPT()
        self.ui.setupUi(self)
        if main_window.ui.checkAPIKey.isChecked():
            openai.api_key='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'
        else:
            openai.api_key = main_window.ui.textEdit_2.toPlainText()
        self.setWindowIcon(QIcon("Bilder/Icon_Info.svg"))
        self.setWindowTitle("INFOMOTION - direkt ChatGPT")
        self.dateiLabel = main_window.ui.dateiLabel

        self.ui.pushButton.clicked.connect(self.process_input)

    def process_input(self):

        # input_text = self.ui.direktChatInput.toPlainText()

        # Hier kannst du deinen Code zum Senden der Eingabe an ChatGPT und zum Empfang
        try:
            # print("1")
            # response = openai.Completion.create(
            #     engine="text-davinci-003",
            #     prompt=input_text,
            #     max_tokens=250,  # Anzahl der Tokens in der Antwort
            #     temperature=0.7,  # Steuerung der Antwortvarianz
            #     n=1,  # Anzahl der Antworten, die zurückgegeben werden sollen
            #     stop=None,  # Hier kannst du eine benutzerdefinierte Stop-Bedingung angebe
            # )

            # output = response['choices'][0]['text'].strip()
            # print(output)
            out = "was ist eine Pizza?"

            test = "Eine Pizza ist ein vor dem Backen würzig belegtes Fladenbrot aus einfachem Hefeteig aus der italienischen Küche. Die heutige international verbreitetes Variante mit Tomatensauce und Käse als Basis stammt vermutlich aus Neapel."
            token = len(out) + len(test)  #len(input_text) + len(output)
            # self.ui.direktChatOutput.setPlainText(response['choices'][0]['text'].strip())
            self.ui.direktChatInput.setPlainText(out)
            self.ui.direktChatOutput.setPlainText(test)
            self.ui.direktChatGPTToken.setText(str(token))

        except:
            self.ui.direktChatOutput.setStyleSheet("color: red")
            self.ui.direktChatOutput.setPlainText("Error: Anfrage konnte nicht gesendet werden!")

    def closeEvent(self, event):
        main_window.show()


class CodeChatGPTFenster(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CodeChatGPT()
        if main_window.ui.checkAPIKey.isChecked():
            openai.api_key='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'
        else:
            openai.api_key = main_window.ui.textEdit_2.toPlainText()

        self.output = ""
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon("Bilder/Icon_Info.svg"))
        self.setWindowTitle("INFOMOTION - Code ChatGPT")
        self.ui.pushButton.clicked.connect(self.process_input)
        self.ui.btnCodeChatGPTAusfuehren.clicked.connect(self.ausfuehren_inputCode)
        self.ui.btnCodeChatGPTAusfuehren.hide()

    def process_input(self):


        input_text = "schreib python Code um aus einer Tabelle folgende Frage zu lesen." + self.ui.CodeChatGPTInput.toPlainText() + " aus der Tabelle mit dem Pfad: " + main_window.pfad

        # Hier kannst du deinen Code zum Senden der Eingabe an ChatGPT und zum Empfang
        try:

            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=input_text,
                max_tokens=500,  # Anzahl der Tokens in der Antwort
                temperature=0.7,  # Steuerung der Antwortvarianz
                n=1,  # Anzahl der Antworten, die zurückgegeben werden sollen
                stop=None,  # Hier kannst du eine benutzerdefinierte Stop-Bedingung angebe
            )

            response = str(''
            'import pandas as pd'

            '# Pfad zur CSV-Datei'
            'csv_datei_pfad = r''F:\Entwicklung\InfomotionChatGPT\train.csv'

            '# CSV-Datei mit pandas einlesen'
            'data = pd.read_csv(csv_datei_pfad)'

            '# Annahme, dass die Regionen in einer Spalte namens Region liegen'
            '# Wenn der Spaltenname anders ist, ersetzen Sie Region durch den tatsächlichen Spaltennamen'
            'regionen = data["Region"].unique()'

            '# Anzahl der Regionen ermitteln'
            'anzahl_regionen = len(regionen)'

            'print(f"Es gibt {anzahl_regionen} Regionen in der CSV-Datei.")')

            code =response['choices'][0]['text'].strip()
            output=code
            token = len(input_text) + len(output)

            self.ui.CoderChatGPTToken.setText(str(token))
            # test = "Es gibt 4 Regionen."
            # code = "import pandas as pd \n" \
            #        "\n" \
            #        "# Pfad zur CSV-Datei \n" \
            #        "csv_datei_pfad = r'F:\Entwicklung\InfomotionChatGPT\_train.csv \n" \
            #        "\n" \
            #        "# Annahme, dass die Regionen in einer Spalte namens 'Region' liegen \"\n" \
            #        "regionen = data['Region'].unique() \n" \
            #        "\n" \
            #        "# Anzahl der Regionen ermitteln \n" \
            #        "anzahl_regionen = len(regionen) \n" \
            #        "\n" \
            #        "print(f"'Es gibt {anzahl_regionen} Regionen in der CSV-Datei.'")"


            self.ui.CodeChatGPTOutput.setPlainText(code)
            self.ui.output = output


            if "#" or "with" or "r" in code:
                self.ui.btnCodeChatGPTAusfuehren.show()
            else:
                print("alles ok")

            if self.ui.checkCodeChatGPTshowCode.isChecked():
                self.ui.CodeChatGPTOutput.setPlainText(code)
                self.ui.btnCodeChatGPTAusfuehren.show()
            else:
                self.ausfuehren_inputCode(code)
                print("alles ok")

            self.ausfuehren_inputCode(output)

            if self.ui.checkCodeChatGPTshowCode.isChecked():
                self.ui.CodeChatGPTOutput.setPlainText(output)
            else:
                self.ausfuehren_inputCode(output)

        except KeyError as ke:

            print(f"Ein KeyError ist aufgetreten: {ke}. Überprüfe den Spaltennamen.")


        except Exception as e:

            print(f"Ein anderer Fehler ist aufgetreten: {e}")


    def ausfuehren_inputCode(self, output):
        print("vor exe")

        original_stdout = sys.stdout
        output_buffer = io.StringIO()
        sys.stdout = output_buffer

        code_to_run = self.ui.CodeChatGPTOutput
        code_bytes = code_to_run.toPlainText().encode('utf-8')
        code = code_bytes.decode('utf-8')

        try:

            # exec(code, globals(), ausgabe)
            exec(code)

            # Wiederherstellen der ursprünglichen sys.stdout
            sys.stdout = original_stdout

            # Die Ausgabe des unbekannten Codes ist in output_buffer gespeichert
            output_variable = output_buffer.getvalue()

            self.ui.CodeChatGPTOutput.setText(output_variable)
            self.ui.btnCodeChatGPTAusfuehren.hide()



        except KeyError as ke:

            print(f"Ein KeyError ist aufgetreten: {ke}. Überprüfe den Spaltennamen.")

            # print(f"Verfügbare Spalten: {df.columns.toslist() if 'df' in globals() else 'DataFrame nicht vorhanden'}")

        except Exception as e:

            print(f"Ein anderer Fehler ist aufgetreten: {e}")

        print("nach exec")

    def closeEvent(self, event):
        main_window.show()


class TableChatGPTFenster(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TableChatGPT()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("Bilder/Icon_Info.svg"))
        self.setWindowTitle("INFOMOTION - Table ChatGPT")
        if main_window.ui.checkAPIKey.isChecked():
            openai.api_key='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'
        else:
            openai.api_key = main_window.ui.textEdit_2.toPlainText()

        self.ui.btnTable.clicked.connect(self.process_input)

        # csv_filepath = main_window.pfad  # Replace with your CSV file path

    def process_input(self):

        # csv = pd.read_csv(main_window.pfad)
        # csv=csv.head()  #Sicherheitsfeature um kosten zu sparen
        # json = csv.to_json()

        # input_text = "beantworte die Frage" + self.ui.tableChatGPTInput.toPlainText() + "aus folgende Datei:" + json

        try:
        #     response = openai.Completion.create(
        #         engine="text-davinci-003",
        #         prompt=input_text,
        #         max_tokens=500,  # Anzahl der Tokens in der Antwort
        #         temperature=0.7,  # Steuerung der Antwortvarianz
        #         n=1,  # Anzahl der Antworten, die zurückgegeben werden sollen
        #         stop=None,  # Hier kannst du eine benutzerdefinierte Stop-Bedingung angebe
        #     )

            test = "Es gibt 4 Regionen. (West, South, East, Central)"
            # output = response['choices'][0]['text'].strip()
            token = 26548 #len(input_text) + len(output)
            self.ui.tableChatGPTOutput.setPlainText(test)
            self.ui.TableChatGPTToken.setText(str(token))
        except:
            self.ui.tableChatGPTOutput.setStyleSheet("color: red")
            self.ui.tableChatGPTOutput.setPlainText("Error: Anfrage konnte nicht gesendet werden!")
            print("Anfrage konnte nicht gesendet werden!")

    def closeEvent(self, event):
        main_window.show()


class ProjektteamFenster(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Projektteam()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("Bilder/Icon_Info.svg"))
        self.setWindowTitle("INFOMOTION - Projektteam")

    def closeEvent(self, event):
        main_window.show()


class FirstRowChatGPTFenster(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FirstRowChatGPT()
        if main_window.ui.checkAPIKey.isChecked():
            openai.api_key='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'
        else:
            openai.api_key = main_window.ui.textEdit_2.toPlainText()

        # openai.api_key = main_window.ui.textEdit_2.toPlainText()
        self.output = ""
        self.code=""
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("Bilder/Icon_Info.svg"))
        self.setWindowTitle("INFOMOTION - FirstRow ChatGPT")

        self.ui.pushButton.clicked.connect(self.process_input)
        self.ui.btnFirstRowAusfuehren.clicked.connect(self.ausfuehren_input)
        self.ui.btnFirstRowAusfuehren.hide()
        print("API: ", openai.api_key)

    def process_input(self):

        # first_row = pd.read_csv(main_window.pfad).columns.tolist()

        # print("Erste Reihe: ", first_row)
        # input_text = "schreib python Code um aus einer Tabelle folgende Frage zu lesen."+self.ui.firstRowChatGPTInput.toPlainText() + " aus der Tabelle mit dem Pfad: "+main_window.pfad+" unter verwendung von folgenden Spaltennamen:" +str(first_row)


        # Hier kannst du deinen Code zum Senden der Eingabe an ChatGPT und zum Empfang
        try:
            # self.ui.firstRowChatGPTOutput.setStyleSheet("color: black")
            # response = openai.Completion.create(
            #     engine="text-davinci-003",
            #     prompt=input_text,
            #     max_tokens=250,  # Anzahl der Tokens in der Antwort
            #     temperature=0.7,  # Steuerung der Antwortvarianz
            #     n=1,  # Anzahl der Antworten, die zurückgegeben werden sollen
            #     stop=None,  # Hier kannst du eine benutzerdefinierte Stop-Bedingung angebe
            # )

            # code = response['choices'][0]['text'].strip()
            code ="import pandas as pd \n" \
                  "\n" \
                  "# Pfad zur CSV-Datei \n" \
                  "csv_datei_pfad = r'F:\Entwicklung\InfomotionChatGPT\_train.csv' \n" \
                  "\n" \
                  "# CSV-Datei mit pandas einlesen und nur die benötigten Spalten auswählen \n" \
                  "spalten = ['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Customer ID', \n" \
                  "'Customer Name', 'Segment', 'Country', 'City', 'State', 'Postal Code', 'Region'] \n" \
                  "data = pd.read_csv(csv_datei_pfad, usecols=spalten) \n" \
                  "\n" \
                  "# Anzahl der eindeutigen Regionen in der Spalte 'Region' ermitteln \n" \
                  "anzahl_regionen = data['Region'].nunique() \n" \
                  "\n" \
                  "print(f'Es gibt {anzahl_regionen} Regionen.')"


            # csv_datei_pfad = r'F:\Entwicklung\InfomotionChatGPT\train.csv'

            # CSV-Datei mit pandas einlesen und nur die benötigten Spalten auswählen




            # Anzahl der eindeutigen Regionen in der Spalte 'Region' ermitteln



            output=code
            token = 564 #len(input_text)+len(output)

            if "#" or "width" or "r" in output:
                self.ui.btnFirstRowAusfuehren.show()
            else:
                print("alles ok")

            self.ui.firstRowChatGPTOutput.setPlainText(output)
            self.ui.firstRowToken.setText(str(token))
            # self.ui.output = output

            if self.ui.checkFirstRowShowCode.isChecked():
                self.ui.firstRowChatGPTOutput.setPlainText(output)
            else:
                self.ausfuehren_input(output)
        except:
            self.ui.firstRowChatGPTOutput.setStyleSheet("color: red")
            self.ui.firstRowChatGPTOutput.setPlainText("Error: Anfrage konnte nicht gesendet werden!",)
            print("Anfrage konnte nicht gesendet werden!")


    def ausfuehren_input(self, output):
        print("vor exe")

        # Speichern Sie die aktuelle sys.stdout
        original_stdout = sys.stdout

        # Speichern Sie die aktuelle sys.stdout
        output_buffer = io.StringIO()

        # Speichern Sie die aktuelle sys.stdout
        sys.stdout = output_buffer

        code_to_run = self.ui.firstRowChatGPTOutput
        code_bytes = code_to_run.toPlainText().encode('utf-8')
        code = code_bytes.decode('utf-8')

        try:
            # Versuch den Code auszuführen

            # exec(code, globals(), ausgabe)
            exec(code)

            # Wiederherstellen der ursprünglichen sys.stdout
            sys.stdout = original_stdout

            # Die Ausgabe des unbekannten Codes ist in output_buffer gespeichert
            output_variable = output_buffer.getvalue()

            self.ui.firstRowChatGPTOutput.setText(output_variable)
            self.ui.btnFirstRowAusfuehren.hide()

        except KeyError as ke:

            print(f"Ein KeyError ist aufgetreten: {ke}. Überprüfe den Spaltennamen.")

            # print(f"Verfügbare Spalten: {df.columns.toslist() if 'df' in globals() else 'DataFrame nicht vorhanden'}")

        except Exception as e:

            print(f"Ein anderer Fehler ist aufgetreten: {e}")

        print("nach exec")


    def closeEvent(self, event):
        main_window.show()


app = QApplication(sys.argv)
print(app, "app")
main_window = MainWindow()
# window=direktChatGPT()
main_window.show()
sys.exit(app.exec_())
