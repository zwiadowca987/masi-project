import PySimpleGUI as sg
import tkinter as tk


class MainWindow:
    def __init__(self):
        self.uniterm_a = '1'
        self.uniterm_b = '2'
        self.separator_1 = ','

        self.uniterm_c = '32'
        self.uniterm_d = '32'
        self.uniterm_e = '32'
        self.separator_2 = ';'

        self.window = None

        self.draw_uniterm = DrawBasicUniterm(self)

    def set_uniterms_1(self, u_a, u_b, sep):
        self.uniterm_a = u_a
        self.uniterm_b = u_b
        self.separator_1 = sep

    def set_uniterms_2(self, u_c, u_d, u_e, sep):
        self.uniterm_c = u_c
        self.uniterm_d = u_d
        self.uniterm_e = u_e
        self.separator_2 = sep

    def run(self):
        self.window = sg.Window('Operacje na Unitermach',
                                [
                                    [sg.Button('Informacje')],
                                    [sg.Button('Wczytaj Dane Unitermu Poziomej Operacji Zrównoleglania', key='read1')],
                                    [sg.Button('Wczytaj Dane Unitermu Pionowej Operacji Eliminacji', key='read2')],
                                    [sg.Button('Rysuj Uniterm Poziomej Operacji Zrównoleglania', key='draw1')],
                                    [sg.Button('Rysuj Uniterm Pionowej Operacji Eliminacji', key='draw2')],
                                    [sg.Button('Rysuj Finalny Rezultat', key='draw3')],
                                    *self.draw_uniterm.layout
                                ], finalize=True)

        self.draw_uniterm.setup_canvas()

        while True:
            event, _ = self.window.read()
            if event in (sg.WINDOW_CLOSED, "Wyjście"):
                break
            elif event == 'Informacje':
                AboutWindow(self).run()
            elif event == 'read1':
                self.window.hide()
                ReadDataFromKeyboardForFirstUniterm(self).run()
                self.window.un_hide()
            elif event == 'read2':
                self.window.hide()
                ReadDataFromKeyboardForSecondUniterm(self).run()
                self.window.un_hide()
            elif event == 'draw1':
                self.draw_uniterm.canvas.delete('all')
                self.draw_uniterm.draw_operation_1(
                    self.uniterm_a, self.uniterm_b, self.separator_1, 200, 100)
            elif event == 'draw2':
                self.draw_uniterm.canvas.delete('all')
                self.draw_uniterm.draw_operation_2(
                    self.uniterm_c, self.uniterm_d, self.uniterm_e, self.separator_2, 200, 100)
            elif event == 'draw3':
                self.draw_uniterm.canvas.delete('all')
                self.draw_uniterm.draw_operation_3(
                    self.uniterm_a, self.uniterm_b, self.uniterm_c, self.uniterm_d, self.uniterm_e, self.separator_1,
                    self.separator_2, 'left')

        self.window.close()


class AboutWindow:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = sg.Window('O Programie',
                                [
                                    [sg.Text('Autor: Mateusz Szczrek (98176)')],
                                    [sg.Text('Numer Tematu: 22')],
                                    [sg.Text(
                                        'Temat: Modelowanie i analiza systemu informatycznego realizującego zamianę unitermu poziomej operacji zrównoleglania na pionową operację eliminacji unitermów')],
                                    [sg.Button('Zamknij')]
                                ])

    def run(self):
        while True:
            event, _ = self.window.read()
            if event in (sg.WINDOW_CLOSED, 'Zamknij'):
                break

        self.window.close()


class ReadDataFromKeyboardForFirstUniterm:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = sg.Window('Wczytywanie Danych',
                                [
                                    [sg.Text('Powiedzmy że dane się wczytują')],
                                    [sg.Text('Podaj wyrażenie A'), sg.Input(key='-UNITERM_A-')],
                                    [sg.Text('Podaj wyrażenie B'), sg.Input(key='-UNITERM_B-')],
                                    [sg.Text('Wybierz separator'),
                                     sg.Combo([',', ';'], default_value=',', key='-SEPARATOR-')],
                                    [sg.Button('Zapisz'), sg.Button('Anuluj')]
                                ], modal=True)

    def run(self):
        while True:
            event, values = self.window.read()
            if event in (sg.WINDOW_CLOSED, 'Anuluj'):
                break
            if event == 'Zapisz':
                self.main_window.set_uniterms_1(
                    values['-UNITERM_A-'], values['-UNITERM_B-'], values['-SEPARATOR-'])
                sg.popup('Zapisano')

            self.window.close()


class ReadDataFromKeyboardForSecondUniterm:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = sg.Window('Wczytywanie Danych',
                                [
                                    [sg.Text('Powiedzmy że dane się wczytują')],
                                    [sg.Text('Podaj wyrażenie A'), sg.Input(key='-UNITERM_A-')],
                                    [sg.Text('Podaj wyrażenie B'), sg.Input(key='-UNITERM_B-')],
                                    [sg.Text('Podaj wyrażenie C'), sg.Input(key='-UNITERM_C-')],
                                    [sg.Text('Wybierz separator'),
                                     sg.Combo([',', ';'], default_value=',', key='-SEPARATOR-')],
                                    [sg.Button('Zapisz'), sg.Button('Anuluj')]
                                ], modal=True)

    def run(self):
        while True:
            event, values = self.window.read()
            if event in (sg.WINDOW_CLOSED, 'Anuluj'):
                break
            if event == 'Zapisz':
                self.main_window.set_uniterms_2(
                    values['-UNITERM_A-'], values['-UNITERM_B-'], values['-UNITERM_C-'], values['-SEPARATOR-'])
                sg.popup('Zapisano')

            self.window.close()


class DrawBasicUniterm:
    def __init__(self, main_window):
        self.canvas = None
        self.main_window = main_window
        self.layout = [[sg.Canvas(size=(400, 300), key='canvas_in')]]

    def setup_canvas(self):
        canvas_elem = self.main_window.window['canvas_in']
        tk_widget = canvas_elem.Widget
        self.canvas = tk.Canvas(tk_widget, width=400, height=300, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def draw_operation_1(self, uniterm_a, uniterm_b, separator_2, x, y):
        if uniterm_a == '' or uniterm_b == '' or separator_2 == '':
            return

        full_text = f"{uniterm_a} {separator_2} {uniterm_b}"

        text_id = self.canvas.create_text(x, y, text=full_text, font=('Arial', 16), anchor='center')

        bbox = self.canvas.bbox(text_id)
        text_width = bbox[2] - bbox[0]
        self.canvas.move(text_id, (x - bbox[0] - text_width // 2), 0)

        start_x = bbox[0]
        start_y = y - 25
        line_start = start_x
        line_end = bbox[2]
        vertical_line_height = 10

        self.canvas.create_line(line_start, start_y, line_end, start_y, width=2)
        self.canvas.create_line(line_start, start_y, line_start, start_y + vertical_line_height, width=2)
        self.canvas.create_line(line_end, start_y, line_end, start_y + vertical_line_height, width=2)

    def draw_operation_2(self, uniterm_c, uniterm_d, uniterm_e, separator_2, x, y):
        if uniterm_c == '' or uniterm_d == '' or uniterm_e == '' or separator_2 == '':
            return

        values = [uniterm_c, separator_2, uniterm_d, separator_2, uniterm_e]

        spacing = 30
        font_size = 16
        small_tick_size = 10

        line_start_y = y
        line_end_y = y + (len(values) - 1) * spacing

        self.canvas.create_line(x - 10, line_start_y, x - 10, line_end_y, width=2)

        self.canvas.create_line(x - 10 - small_tick_size // 2, line_start_y,
                                x - 10 + small_tick_size // 2, line_start_y, width=2)
        self.canvas.create_line(x - 10 - small_tick_size // 2, line_end_y, x - 10 + small_tick_size // 2,
                                line_end_y, width=2)

        for i, value in enumerate(values):
            self.canvas.create_text(x, y + i * spacing, text=value.strip(), font=("Arial", font_size),
                                    anchor="w")

    def draw_operation_3(self, uniterm_a, uniterm_b, uniterm_c, uniterm_d, uniterm_e, separator_1, separator_2, side):
        self.canvas.delete('all')

        if uniterm_a == '' or uniterm_b == '' or uniterm_c == '' or uniterm_d == '' or uniterm_e == '' or separator_1 == '' or separator_2 == '' or side not in ['left', 'right']:
            return

        start_x, start_y = 200, 100
        spacing = 30
        font_size = 16

        # Rysowanie jednostek
        if side == 'left':
            values = [uniterm_c, separator_2, uniterm_d, separator_2, uniterm_e]
            result_x = start_x - 100

            # Rysujemy pionową linię i teksty dla lewego 'side'
            self._draw_vertical_uniterm(result_x, start_y + spacing, values, font_size)

            # Rysujemy drugi tekst uniterm_b (na prawo od linii)
            self.canvas.create_text(start_x + 100, start_y + 2 * spacing, text=uniterm_b, font=("Arial", font_size), anchor="w")

            # Rysujemy poziomą linię między jednostkami
            self.canvas.create_line(result_x + 10, start_y + 2 * spacing, start_x + 90, start_y + 2 * spacing, width=2)

        elif side == 'right':
            # Rysujemy tekst uniterm_a na lewo
            self.canvas.create_text(start_x - 100, start_y + 2 * spacing, text=uniterm_a, font=("Arial", font_size), anchor="w")

            values = [uniterm_c, separator_2, uniterm_d, separator_2, uniterm_e]
            result_x = start_x + 100

            # Rysujemy pionową linię i teksty dla prawego 'side'
            self._draw_vertical_uniterm(result_x, start_y + spacing, values, font_size)

            # Rysujemy poziomą linię między jednostkami
            self.canvas.create_line(start_x - 90, start_y + 2 * spacing, result_x - 10, start_y + 2 * spacing, width=2)

    def _draw_vertical_uniterm(self, x, y, values, font_size):
        spacing = 30
        small_tick_size = 10
        line_start_y = y  # Start rysowania linii w miejscu, gdzie chcemy ją ustawić
        line_end_y = y + (len(values) - 1) * spacing

        # Rysowanie pionowej linii
        self.canvas.create_line(x - 10, line_start_y, x - 10, line_end_y, width=2)

        # Małe kreski na górze i dole pionowej linii
        self.canvas.create_line(x - 10 - small_tick_size // 2, line_start_y,
                                x - 10 + small_tick_size // 2, line_start_y, width=2)
        self.canvas.create_line(x - 10 - small_tick_size // 2, line_end_y, x - 10 + small_tick_size // 2,
                                line_end_y, width=2)

        # Rysowanie wartości pionowo, zaczynając od pozycji `y`
        for i, value in enumerate(values):
            self.canvas.create_text(x, y + i * spacing, text=value.strip(), font=("Arial", font_size), anchor="w")



if __name__ == "__main__":
    MainWindow().run()

# # Funkcja rysująca wynik na drugim canvas
# def draw_result(canvas, values):
#     canvas.delete("all")  # Czyszczenie poprzednich rysunków
#
#     if not values:
#         return
#
#     start_x, start_y = 50, 50
#     spacing = 30
#     font_size = 16
#     small_tick_size = 5  # Długość małych kresek na pionowej linii
#
#     result_x = start_x + 20
#     result_y = start_y
#     line_start_y = result_y
#     line_end_y = result_y + (len(values) - 1) * spacing
#     canvas.create_line(result_x - 10, line_start_y, result_x - 10, line_end_y, width=2)
#
#     canvas.create_line(result_x - 10 - small_tick_size // 2, line_start_y, result_x - 10 + small_tick_size // 2, line_start_y, width=2)
#     canvas.create_line(result_x - 10 - small_tick_size // 2, line_end_y, result_x - 10 + small_tick_size // 2, line_end_y, width=2)
#
#     for i, value in enumerate(values):
#         canvas.create_text(result_x, result_y + i * spacing, text=value.strip(), font=("Arial", font_size), anchor="w")

# # Tworzenie układu GUI
# layout = [
#     [sg.Button("Wprowadź wartości", key="-POPUP-")],
#     [sg.Text("Podaj trzy wartości do zamiany (rozdzielone spacją):"), sg.InputText(key='-INPUT-REPLACE-')],
#     [sg.Text("Wybierz wartość do zamiany:"), sg.Combo(["Pierwsza", "Druga"], default_value="Pierwsza", key='-REPLACE-OPTION-')],
#     [sg.Text("Separator:"), sg.Combo([",", ";"], default_value=",", key='-SEPARATOR-')],
#     [sg.Button("Generuj"), sg.Button("Pokaż wynik"), sg.Button("Reset"), sg.Button("Zamknij")],
#     [sg.Canvas(size=(400, 150), key="-CANVAS-IN-")],
#     [sg.Canvas(size=(400, 150), key="-CANVAS-OUT-")]
# ]
#
# # Tworzenie okna
# window = sg.Window("Dynamiczne Wyrażenia Matematyczne", layout, finalize=True)
#
# # Pobranie referencji do tkinterowych canvasów
# canvas_in_elem = window["-CANVAS-IN-"].Widget
# canvas_in = tk.Canvas(canvas_in_elem, width=400, height=150, bg="white")
# canvas_in.pack(fill=tk.BOTH, expand=True)
#
# canvas_out_elem = window["-CANVAS-OUT-"].Widget
# canvas_out = tk.Canvas(canvas_out_elem, width=400, height=150, bg="white")
# canvas_out.pack(fill=tk.BOTH, expand=True)
#
# values_in = []
# values_out = []
# separator = ","
#
# # Pętla zdarzeń
# while True:
#     event, values = window.read()
#
#     if event == sg.WIN_CLOSED or event == "Zamknij":
#         break
#
#     if event == "-POPUP-":
#         val1, val2 = get_two_values()
#         if val1 and val2:
#             window['-INPUT-REPLACE-'].update(f"{val1} {val2}")
#
#     if event == "Generuj":
#         values_in = values['-INPUT-REPLACE-'].split()
#         separator = values['-SEPARATOR-']
#         if len(values_in) == 2:
#             draw_expressions(canvas_in, values_in, separator)
#         canvas_out.delete("all")  # Czyszczenie drugiego canvas
#
#     if event == "Pokaż wynik":
#         if len(values_in) == 2 and values['-INPUT-REPLACE-']:
#             replace_values = values['-INPUT-REPLACE-'].split()
#             if len(replace_values) == 3:
#                 replace_index = 0 if values['-REPLACE-OPTION-'] == "Pierwsza" else 1
#                 values_out = values_in[:]
#                 values_out[replace_index] = " ".join(replace_values)
#                 draw_result(canvas_out, values_out)
#
#     if event == "Reset":
#         values_in = []
#         values_out = []
#         canvas_in.delete("all")
#         canvas_out.delete("all")
#
# window.close()


# import PySimpleGUI as sg
# import tkinter as tk

# def get_two_values():
#     layout = [
#         [sg.Text("Podaj pierwszą wartość:"), sg.InputText(key='-POPUP1-')],
#         [sg.Text("Podaj drugą wartość:"), sg.InputText(key='-POPUP2-')],
#         [sg.Button("OK"), sg.Button("Anuluj")]
#     ]
#     window = sg.Window("Wprowadź wartości", layout)
#     event, values = window.read()
#     window.close()
#     return (values['-POPUP1-'], values['-POPUP2-']) if event == "OK" else (None, None)


# def draw_expressions(canvas, values, separator):
#     canvas.delete("all")
#     if len(values) != 2:
#         return
#     start_x, start_y = 50, 50
#     spacing = 30
#     font_size = 16
#     vertical_line_height = 10
#     full_expression = f" {separator} ".join(values)
#     text_id = canvas.create_text(0, 0, text=full_expression, font=("Arial", font_size), anchor="w")
#     text_width = canvas.bbox(text_id)[2] - canvas.bbox(text_id)[0]
#     start_x = (400 - text_width) // 2
#     line_start = start_x
#     line_end = start_x + text_width
#     canvas.create_line(line_start, start_y, line_end, start_y, width=2)
#     canvas.create_line(line_start, start_y, line_start, start_y + vertical_line_height, width=2)
#     canvas.create_line(line_end, start_y, line_end, start_y + vertical_line_height, width=2)
#     canvas.create_text(start_x + text_width // 2, start_y + spacing, text=full_expression, font=("Arial", font_size), anchor="center")


# def draw_result(canvas, base_values, replace_values, replace_index):
#     canvas.delete("all")
#     if len(replace_values) != 3:
#         return
#     start_x, start_y = 50, 50
#     spacing = 30
#     font_size = 16
#     small_tick_size = 5
#     result_x = start_x + 20
#     result_y = start_y
#     line_start_y = result_y
#     line_end_y = result_y + (len(replace_values) - 1) * spacing
#     canvas.create_line(result_x - 10, line_start_y, result_x - 10, line_end_y, width=2)
#     canvas.create_line(result_x - 10 - small_tick_size // 2, line_start_y, result_x - 10 + small_tick_size // 2, line_start_y, width=2)
#     canvas.create_line(result_x - 10 - small_tick_size // 2, line_end_y, result_x - 10 + small_tick_size // 2, line_end_y, width=2)
#     new_values = base_values[:]
#     new_values[replace_index] = replace_values[0]
#     text = " , ".join(new_values)
#     text_id = canvas.create_text(result_x, result_y, text=text, font=("Arial", font_size), anchor="w")
#     text_width = canvas.bbox(text_id)[2] - canvas.bbox(text_id)[0]
#     line_start = result_x
#     line_end = result_x + text_width
#     canvas.create_line(line_start, result_y - 10, line_end, result_y - 10, width=2)
#     canvas.create_line(line_start, result_y - 10, line_start, result_y, width=2)
#     canvas.create_line(line_end, result_y - 10, line_end, result_y, width=2)
#     for i, value in enumerate(replace_values):
#         new_values = base_values[:]
#         new_values[replace_index] = value
#         text = " , ".join(new_values)
#         canvas.create_text(result_x, result_y + i * spacing, text=text, font=("Arial", font_size), anchor="w")

# layout = [
#     [sg.Button("Wprowadź wartości", key="-POPUP-")],
#     [sg.Text("Podaj trzy wartości do zamiany (rozdzielone spacją):"), sg.InputText(key='-REPLACEMENTS-')],
#     [sg.Text("Wybierz wartość do zamiany:"), sg.Combo(["Pierwsza", "Druga"], default_value="Pierwsza", key='-REPLACE-OPTION-')],
#     [sg.Text("Separator:"), sg.Combo([",", ";"], default_value=",", key='-SEPARATOR-')],
#     [sg.Button("Generuj"), sg.Button("Pokaż wynik"), sg.Button("Reset"), sg.Button("Zamknij")],
#     [sg.Canvas(size=(400, 150), key="-CANVAS-IN-")],
#     [sg.Canvas(size=(400, 150), key="-CANVAS-OUT-")]
# ]

# window = sg.Window("Dynamiczne Wyrażenia", layout, finalize=True)
# canvas_in = tk.Canvas(window["-CANVAS-IN-"].Widget, width=400, height=150, bg="white")
# canvas_in.pack(fill=tk.BOTH, expand=True)
# canvas_out = tk.Canvas(window["-CANVAS-OUT-"].Widget, width=400, height=150, bg="white")
# canvas_out.pack(fill=tk.BOTH, expand=True)

# values_in = []
# separator = ","

# while True:
#     event, values = window.read()
#     if event in (sg.WIN_CLOSED, "Zamknij"):
#         break
#     if event == "-POPUP-":
#         val1, val2 = get_two_values()
#         if val1 and val2:
#             values_in = [val1, val2]
#             draw_expressions(canvas_in, values_in, separator)
#     if event == "Generuj":
#         separator = values['-SEPARATOR-']
#         draw_expressions(canvas_in, values_in, separator)
#     if event == "Pokaż wynik":
#         replace_values = values['-REPLACEMENTS-'].split()
#         replace_index = 0 if values['-REPLACE-OPTION-'] == "Pierwsza" else 1
#         draw_result(canvas_out, values_in, replace_values, replace_index)
#     if event == "Reset":
#         values_in = []
#         canvas_in.delete("all")
#         canvas_out.delete("all")

# window.close()


# import PySimpleGUI as sg

# class MainWindow:
#     """Główne okno aplikacji."""
#     def __init__(self):
#         self.layout = [
#             [sg.Text("Witaj w aplikacji!")],
#             [sg.Button("Ustawienia"), sg.Button("Użytkownicy"), sg.Button("O programie")],
#             [sg.Button("Wyjście")]
#         ]
#         self.window = sg.Window("Główne Okno", self.layout)

#     def run(self):
#         while True:
#             event, _ = self.window.read()
#             if event in (sg.WINDOW_CLOSED, "Wyjście"):
#                 break
#             elif event == "Ustawienia":
#                 self.window.hide()
#                 SettingsWindow(self).run()
#                 self.window.un_hide()
#             elif event == "Użytkownicy":
#                 self.window.hide()
#                 UserWindow(self).run()
#                 self.window.un_hide()
#             elif event == "O programie":
#                 self.window.hide()
#                 AboutWindow(self).run()
#                 self.window.un_hide()

#         self.window.close()

# class SettingsWindow:
#     """Okno ustawień."""
#     def __init__(self, main_window):
#         self.main_window = main_window
#         self.layout = [
#             [sg.Text("Ustawienia aplikacji")],
#             [sg.Checkbox("Tryb ciemny"), sg.Checkbox("Powiadomienia")],
#             [sg.Button("Zapisz"), sg.Button("Powrót")]
#         ]
#         self.window = sg.Window("Ustawienia", self.layout)

#     def run(self):
#         while True:
#             event, _ = self.window.read()
#             if event in (sg.WINDOW_CLOSED, "Powrót"):
#                 break
#             elif event == "Zapisz":
#                 sg.popup("Ustawienia zapisane!")
#         self.window.close()

# class UserWindow:
#     """Okno listy użytkowników."""
#     def __init__(self, main_window):
#         self.main_window = main_window
#         self.layout = [
#             [sg.Text("Lista użytkowników")],
#             [sg.Listbox(values=["Jan Kowalski", "Anna Nowak", "Michał Wiśniewski"], size=(30, 5))],
#             [sg.Button("Powrót")]
#         ]
#         self.window = sg.Window("Użytkownicy", self.layout)

#     def run(self):
#         while True:
#             event, _ = self.window.read()
#             if event in (sg.WINDOW_CLOSED, "Powrót"):
#                 break
#         self.window.close()

# class AboutWindow:
#     """Okno informacji o aplikacji."""
#     def __init__(self, main_window):
#         self.main_window = main_window
#         self.layout = [
#             [sg.Text("Aplikacja wersja 1.0")],
#             [sg.Text("Stworzona przez: Twoje Imię")],
#             [sg.Button("Powrót")]
#         ]
#         self.window = sg.Window("O programie", self.layout)

#     def run(self):
#         while True:
#             event, _ = self.window.read()
#             if event in (sg.WINDOW_CLOSED, "Powrót"):
#                 break
#         self.window.close()

# if __name__ == "__main__":
#     MainWindow().run()

# import PySimpleGUI as sg
# import tkinter as tk
#
# # Funkcja do wyświetlania popupu do wprowadzania dwóch wartości
# def get_two_values():
#     popup_layout = [
#         [sg.Text("Podaj pierwszą wartość:"), sg.InputText(key='-POPUP1-')],
#         [sg.Text("Podaj drugą wartość:"), sg.InputText(key='-POPUP2-')],
#         [sg.Button("OK"), sg.Button("Anuluj")]
#     ]
#     popup_window = sg.Window("Wprowadź wartości", popup_layout)
#     event, values = popup_window.read()
#     popup_window.close()
#
#     if event == "OK":
#         return values['-POPUP1-'], values['-POPUP2-']
#     return None, None
#
# # Funkcja rysująca wyrażenia na pierwszym canvas
# def draw_expressions(canvas, values, separator):
#     canvas.delete("all")  # Czyszczenie poprzednich rysunków
#
#     if len(values) != 2:
#         return
#
#     start_x, start_y = 50, 50
#     spacing = 30
#     font_size = 16
#     vertical_line_height = 10  # Wysokość pionowych kreseczek
#
#     full_expression = f" {separator} ".join(values)
#     text_id = canvas.create_text(0, 0, text=full_expression, font=("Arial", font_size), anchor="w")
#     text_width = canvas.bbox(text_id)[2] - canvas.bbox(text_id)[0]
#
#     start_x = (400 - text_width) // 2  # Wyśrodkowanie
#
#     line_start = start_x
#     line_end = start_x + text_width
#     canvas.create_line(line_start, start_y, line_end, start_y, width=2)
#
#     canvas.create_line(line_start, start_y, line_start, start_y + vertical_line_height, width=2)
#     canvas.create_line(line_end, start_y, line_end, start_y + vertical_line_height, width=2)
#
#     canvas.create_text(start_x + text_width // 2, start_y + spacing, text=full_expression, font=("Arial", font_size), anchor="center")
#
# # Funkcja rysująca wynik na drugim canvas
# def draw_result(canvas, values):
#     canvas.delete("all")  # Czyszczenie poprzednich rysunków
#
#     if not values:
#         return
#
#     start_x, start_y = 50, 50
#     spacing = 30
#     font_size = 16
#     small_tick_size = 5  # Długość małych kresek na pionowej linii
#
#     result_x = start_x + 20
#     result_y = start_y
#     line_start_y = result_y
#     line_end_y = result_y + (len(values) - 1) * spacing
#     canvas.create_line(result_x - 10, line_start_y, result_x - 10, line_end_y, width=2)
#
#     canvas.create_line(result_x - 10 - small_tick_size // 2, line_start_y, result_x - 10 + small_tick_size // 2, line_start_y, width=2)
#     canvas.create_line(result_x - 10 - small_tick_size // 2, line_end_y, result_x - 10 + small_tick_size // 2, line_end_y, width=2)
#
#     for i, value in enumerate(values):
#         canvas.create_text(result_x, result_y + i * spacing, text=value.strip(), font=("Arial", font_size), anchor="w")
#
# # Tworzenie układu GUI
# layout = [
#     [sg.Button("Wprowadź wartości", key="-POPUP-")],
#     [sg.Text("Podaj trzy wartości do zamiany (rozdzielone spacją):"), sg.InputText(key='-INPUT-REPLACE-')],
#     [sg.Text("Wybierz wartość do zamiany:"), sg.Combo(["Pierwsza", "Druga"], default_value="Pierwsza", key='-REPLACE-OPTION-')],
#     [sg.Text("Separator:"), sg.Combo([",", ";"], default_value=",", key='-SEPARATOR-')],
#     [sg.Button("Generuj"), sg.Button("Pokaż wynik"), sg.Button("Reset"), sg.Button("Zamknij")],
#     [sg.Canvas(size=(400, 150), key="-CANVAS-IN-")],
#     [sg.Canvas(size=(400, 150), key="-CANVAS-OUT-")]
# ]
#
# # Tworzenie okna
# window = sg.Window("Dynamiczne Wyrażenia Matematyczne", layout, finalize=True)
#
# # Pobranie referencji do tkinterowych canvasów
# canvas_in_elem = window["-CANVAS-IN-"].Widget
# canvas_in = tk.Canvas(canvas_in_elem, width=400, height=150, bg="white")
# canvas_in.pack(fill=tk.BOTH, expand=True)
#
# canvas_out_elem = window["-CANVAS-OUT-"].Widget
# canvas_out = tk.Canvas(canvas_out_elem, width=400, height=150, bg="white")
# canvas_out.pack(fill=tk.BOTH, expand=True)
#
# values_in = []
# values_out = []
# separator = ","
#
# # Pętla zdarzeń
# while True:
#     event, values = window.read()
#
#     if event == sg.WIN_CLOSED or event == "Zamknij":
#         break
#
#     if event == "-POPUP-":
#         val1, val2 = get_two_values()
#         if val1 and val2:
#             window['-INPUT-REPLACE-'].update(f"{val1} {val2}")
#
#     if event == "Generuj":
#         values_in = values['-INPUT-REPLACE-'].split()
#         separator = values['-SEPARATOR-']
#         if len(values_in) == 2:
#             draw_expressions(canvas_in, values_in, separator)
#         canvas_out.delete("all")  # Czyszczenie drugiego canvas
#
#     if event == "Pokaż wynik":
#         if len(values_in) == 2 and values['-INPUT-REPLACE-']:
#             replace_values = values['-INPUT-REPLACE-'].split()
#             if len(replace_values) == 3:
#                 replace_index = 0 if values['-REPLACE-OPTION-'] == "Pierwsza" else 1
#                 values_out = values_in[:]
#                 values_out[replace_index] = " ".join(replace_values)
#                 draw_result(canvas_out, values_out)
#
#     if event == "Reset":
#         values_in = []
#         values_out = []
#         canvas_in.delete("all")
#         canvas_out.delete("all")
#
# window.close()

# import PySimpleGUI as sg
# import tkinter as tk

# def get_two_values():
#     layout = [
#         [sg.Text("Podaj pierwszą wartość:"), sg.InputText(key='-POPUP1-')],
#         [sg.Text("Podaj drugą wartość:"), sg.InputText(key='-POPUP2-')],
#         [sg.Button("OK"), sg.Button("Anuluj")]
#     ]
#     window = sg.Window("Wprowadź wartości", layout)
#     event, values = window.read()
#     window.close()
#     return (values['-POPUP1-'], values['-POPUP2-']) if event == "OK" else (None, None)

# def draw_expressions(canvas, values, separator):
#     canvas.delete("all")
#     if len(values) != 2:
#         return
#     start_x, start_y = 50, 50
#     spacing = 30
#     font_size = 16
#     vertical_line_height = 10
#     full_expression = f" {separator} ".join(values)
#     text_id = canvas.create_text(0, 0, text=full_expression, font=("Arial", font_size), anchor="w")
#     text_width = canvas.bbox(text_id)[2] - canvas.bbox(text_id)[0]
#     start_x = (400 - text_width) // 2
#     line_start = start_x
#     line_end = start_x + text_width
#     canvas.create_line(line_start, start_y, line_end, start_y, width=2)
#     canvas.create_line(line_start, start_y, line_start, start_y + vertical_line_height, width=2)
#     canvas.create_line(line_end, start_y, line_end, start_y + vertical_line_height, width=2)
#     canvas.create_text(start_x + text_width // 2, start_y + spacing, text=full_expression, font=("Arial", font_size), anchor="center")

# def draw_result(canvas, base_values, replace_values, replace_index):
#     canvas.delete("all")
#     if len(replace_values) != 3:
#         return
#     start_x, start_y = 50, 50
#     spacing = 30
#     font_size = 16
#     small_tick_size = 5
#     result_x = start_x + 20
#     result_y = start_y
#     line_start_y = result_y
#     line_end_y = result_y + (len(replace_values) - 1) * spacing
#     canvas.create_line(result_x - 10, line_start_y, result_x - 10, line_end_y, width=2)
#     canvas.create_line(result_x - 10 - small_tick_size // 2, line_start_y, result_x - 10 + small_tick_size // 2, line_start_y, width=2)
#     canvas.create_line(result_x - 10 - small_tick_size // 2, line_end_y, result_x - 10 + small_tick_size // 2, line_end_y, width=2)
#     new_values = base_values[:]
#     new_values[replace_index] = replace_values[0]
#     text = " , ".join(new_values)
#     text_id = canvas.create_text(result_x, result_y, text=text, font=("Arial", font_size), anchor="w")
#     text_width = canvas.bbox(text_id)[2] - canvas.bbox(text_id)[0]
#     line_start = result_x
#     line_end = result_x + text_width
#     canvas.create_line(line_start, result_y - 10, line_end, result_y - 10, width=2)
#     canvas.create_line(line_start, result_y - 10, line_start, result_y, width=2)
#     canvas.create_line(line_end, result_y - 10, line_end, result_y, width=2)
#     for i, value in enumerate(replace_values):
#         new_values = base_values[:]
#         new_values[replace_index] = value
#         text = " , ".join(new_values)
#         canvas.create_text(result_x, result_y + i * spacing, text=text, font=("Arial", font_size), anchor="w")

# layout = [
#     [sg.Button("Wprowadź wartości", key="-POPUP-")],
#     [sg.Text("Podaj trzy wartości do zamiany (rozdzielone spacją):"), sg.InputText(key='-REPLACEMENTS-')],
#     [sg.Text("Wybierz wartość do zamiany:"), sg.Combo(["Pierwsza", "Druga"], default_value="Pierwsza", key='-REPLACE-OPTION-')],
#     [sg.Text("Separator:"), sg.Combo([",", ";"], default_value=",", key='-SEPARATOR-')],
#     [sg.Button("Generuj"), sg.Button("Pokaż wynik"), sg.Button("Reset"), sg.Button("Zamknij")],
#     [sg.Canvas(size=(400, 150), key="-CANVAS-IN-")],
#     [sg.Canvas(size=(400, 150), key="-CANVAS-OUT-")]
# ]

# window = sg.Window("Dynamiczne Wyrażenia", layout, finalize=True)
# canvas_in = tk.Canvas(window["-CANVAS-IN-"].Widget, width=400, height=150, bg="white")
# canvas_in.pack(fill=tk.BOTH, expand=True)
# canvas_out = tk.Canvas(window["-CANVAS-OUT-"].Widget, width=400, height=150, bg="white")
# canvas_out.pack(fill=tk.BOTH, expand=True)

# values_in = []
# separator = ","

# while True:
#     event, values = window.read()
#     if event in (sg.WIN_CLOSED, "Zamknij"):
#         break
#     if event == "-POPUP-":
#         val1, val2 = get_two_values()
#         if val1 and val2:
#             values_in = [val1, val2]
#             draw_expressions(canvas_in, values_in, separator)
#     if event == "Generuj":
#         separator = values['-SEPARATOR-']
#         draw_expressions(canvas_in, values_in, separator)
#     if event == "Pokaż wynik":
#         replace_values = values['-REPLACEMENTS-'].split()
#         replace_index = 0 if values['-REPLACE-OPTION-'] == "Pierwsza" else 1
#         draw_result(canvas_out, values_in, replace_values, replace_index)
#     if event == "Reset":
#         values_in = []
#         canvas_in.delete("all")
#         canvas_out.delete("all")

# window.close()

# import PySimpleGUI as sg

# class MainWindow:
#     """Główne okno aplikacji."""
#     def __init__(self):
#         self.layout = [
#             [sg.Text("Witaj w aplikacji!")],
#             [sg.Button("Ustawienia"), sg.Button("Użytkownicy"), sg.Button("O programie")],
#             [sg.Button("Wyjście")]
#         ]
#         self.window = sg.Window("Główne Okno", self.layout)

#     def run(self):
#         while True:
#             event, _ = self.window.read()
#             if event in (sg.WINDOW_CLOSED, "Wyjście"):
#                 break
#             elif event == "Ustawienia":
#                 self.window.hide()
#                 SettingsWindow(self).run()
#                 self.window.un_hide()
#             elif event == "Użytkownicy":
#                 self.window.hide()
#                 UserWindow(self).run()
#                 self.window.un_hide()
#             elif event == "O programie":
#                 self.window.hide()
#                 AboutWindow(self).run()
#                 self.window.un_hide()

#         self.window.close()

# class SettingsWindow:
#     """Okno ustawień."""
#     def __init__(self, main_window):
#         self.main_window = main_window
#         self.layout = [
#             [sg.Text("Ustawienia aplikacji")],
#             [sg.Checkbox("Tryb ciemny"), sg.Checkbox("Powiadomienia")],
#             [sg.Button("Zapisz"), sg.Button("Powrót")]
#         ]
#         self.window = sg.Window("Ustawienia", self.layout)

#     def run(self):
#         while True:
#             event, _ = self.window.read()
#             if event in (sg.WINDOW_CLOSED, "Powrót"):
#                 break
#             elif event == "Zapisz":
#                 sg.popup("Ustawienia zapisane!")
#         self.window.close()

# class UserWindow:
#     """Okno listy użytkowników."""
#     def __init__(self, main_window):
#         self.main_window = main_window
#         self.layout = [
#             [sg.Text("Lista użytkowników")],
#             [sg.Listbox(values=["Jan Kowalski", "Anna Nowak", "Michał Wiśniewski"], size=(30, 5))],
#             [sg.Button("Powrót")]
#         ]
#         self.window = sg.Window("Użytkownicy", self.layout)

#     def run(self):
#         while True:
#             event, _ = self.window.read()
#             if event in (sg.WINDOW_CLOSED, "Powrót"):
#                 break
#         self.window.close()

# class AboutWindow:
#     """Okno informacji o aplikacji."""
#     def __init__(self, main_window):
#         self.main_window = main_window
#         self.layout = [
#             [sg.Text("Aplikacja wersja 1.0")],
#             [sg.Text("Stworzona przez: Twoje Imię")],
#             [sg.Button("Powrót")]
#         ]
#         self.window = sg.Window("O programie", self.layout)

#     def run(self):
#         while True:
#             event, _ = self.window.read()
#             if event in (sg.WINDOW_CLOSED, "Powrót"):
#                 break
#         self.window.close()

# if __name__ == "__main__":
#     MainWindow().run()

# import PySimpleGUI as sg
# import tkinter as tk
#
# # Funkcja do wyświetlania popupu do wprowadzania dwóch wartości
# def get_two_values():
#     popup_layout = [
#         [sg.Text("Podaj pierwszą wartość:"), sg.InputText(key='-POPUP1-')],
#         [sg.Text("Podaj drugą wartość:"), sg.InputText(key='-POPUP2-')],
#         [sg.Button("OK"), sg.Button("Anuluj")]
#     ]
#     popup_window = sg.Window("Wprowadź wartości", popup_layout)
#     event, values = popup_window.read()
#     popup_window.close()
#
#     if event == "OK":
#         return values['-POPUP1-'], values['-POPUP2-']
#     return None, None
#
# # Funkcja rysująca wyrażenia na pierwszym canvas
# def draw_expressions(canvas, values, separator):
#     canvas.delete("all")  # Czyszczenie poprzednich rysunków
#
#     if len(values) != 2:
#         return
#
#     start_x, start_y = 50, 50
#     spacing = 30
#     font_size = 16
#     vertical_line_height = 10  # Wysokość pionowych kreseczek
#
#     full_expression = f" {separator} ".join(values)
#     text_id = canvas.create_text(0, 0, text=full_expression, font=("Arial", font_size), anchor="w")
#     text_width = canvas.bbox(text_id)[2] - canvas.bbox(text_id)[0]
#
#     start_x = (400 - text_width) // 2  # Wyśrodkowanie
#
#     line_start = start_x
#     line_end = start_x + text_width
#     canvas.create_line(line_start, start_y, line_end, start_y, width=2)
#
#     canvas.create_line(line_start, start_y, line_start, start_y + vertical_line_height, width=2)
#     canvas.create_line(line_end, start_y, line_end, start_y + vertical_line_height, width=2)
#
#     canvas.create_text(start_x + text_width // 2, start_y + spacing, text=full_expression, font=("Arial", font_size), anchor="center")
#
# # Funkcja rysująca wynik na drugim canvas
# def draw_result(canvas, values):
#     canvas.delete("all")  # Czyszczenie poprzednich rysunków
#
#     if not values:
#         return
#
#     start_x, start_y = 50, 50
#     spacing = 30
#     font_size = 16
#     small_tick_size = 5  # Długość małych kresek na pionowej linii
#
#     result_x = start_x + 20
#     result_y = start_y
#     line_start_y = result_y
#     line_end_y = result_y + (len(values) - 1) * spacing
#     canvas.create_line(result_x - 10, line_start_y, result_x - 10, line_end_y, width=2)
#
#     canvas.create_line(result_x - 10 - small_tick_size // 2, line_start_y, result_x - 10 + small_tick_size // 2, line_start_y, width=2)
#     canvas.create_line(result_x - 10 - small_tick_size // 2, line_end_y, result_x - 10 + small_tick_size // 2, line_end_y, width=2)
#
#     for i, value in enumerate(values):
#         canvas.create_text(result_x, result_y + i * spacing, text=value.strip(), font=("Arial", font_size), anchor="w")
#
# # Tworzenie układu GUI
# layout = [
#     [sg.Button("Wprowadź wartości", key="-POPUP-")],
#     [sg.Text("Podaj trzy wartości do zamiany (rozdzielone spacją):"), sg.InputText(key='-INPUT-REPLACE-')],
#     [sg.Text("Wybierz wartość do zamiany:"), sg.Combo(["Pierwsza", "Druga"], default_value="Pierwsza", key='-REPLACE-OPTION-')],
#     [sg.Text("Separator:"), sg.Combo([",", ";"], default_value=",", key='-SEPARATOR-')],
#     [sg.Button("Generuj"), sg.Button("Pokaż wynik"), sg.Button("Reset"), sg.Button("Zamknij")],
#     [sg.Canvas(size=(400, 150), key="-CANVAS-IN-")],
#     [sg.Canvas(size=(400, 150), key="-CANVAS-OUT-")]
# ]
#
# # Tworzenie okna
# window = sg.Window("Dynamiczne Wyrażenia Matematyczne", layout, finalize=True)
#
# # Pobranie referencji do tkinterowych canvasów
# canvas_in_elem = window["-CANVAS-IN-"].Widget
# canvas_in = tk.Canvas(canvas_in_elem, width=400, height=150, bg="white")
# canvas_in.pack(fill=tk.BOTH, expand=True)
#
# canvas_out_elem = window["-CANVAS-OUT-"].Widget
# canvas_out = tk.Canvas(canvas_out_elem, width=400, height=150, bg="white")
# canvas_out.pack(fill=tk.BOTH, expand=True)
#
# values_in = []
# values_out = []
# separator = ","
#
# # Pętla zdarzeń
# while True:
#     event, values = window.read()
#
#     if event == sg.WIN_CLOSED or event == "Zamknij":
#         break
#
#     if event == "-POPUP-":
#         val1, val2 = get_two_values()
#         if val1 and val2:
#             window['-INPUT-REPLACE-'].update(f"{val1} {val2}")
#
#     if event == "Generuj":
#         values_in = values['-INPUT-REPLACE-'].split()
#         separator = values['-SEPARATOR-']
#         if len(values_in) == 2:
#             draw_expressions(canvas_in, values_in, separator)
#         canvas_out.delete("all")  # Czyszczenie drugiego canvas
#
#     if event == "Pokaż wynik":
#         if len(values_in) == 2 and values['-INPUT-REPLACE-']:
#             replace_values = values['-INPUT-REPLACE-'].split()
#             if len(replace_values) == 3:
#                 replace_index = 0 if values['-REPLACE-OPTION-'] == "Pierwsza" else 1
#                 values_out = values_in[:]
#                 values_out[replace_index] = " ".join(replace_values)
#                 draw_result(canvas_out, values_out)
#
#     if event == "Reset":
#         values_in = []
#         values_out = []
#         canvas_in.delete("all")
#         canvas_out.delete("all")
#
# window.close()


# import PySimpleGUI as sg
# import tkinter as tk
#
# def get_two_values():
#     layout = [
#         [sg.Text("Podaj pierwszą wartość:"), sg.InputText(key='-POPUP1-')],
#         [sg.Text("Podaj drugą wartość:"), sg.InputText(key='-POPUP2-')],
#         [sg.Button("OK"), sg.Button("Anuluj")]
#     ]
#     window = sg.Window("Wprowadź wartości", layout)
#     event, values = window.read()
#     window.close()
#     return (values['-POPUP1-'], values['-POPUP2-']) if event == "OK" else (None, None)
#
# def draw_expressions(canvas, values, separator):
#     canvas.delete("all")
#     if len(values) != 2:
#         return
#     start_x, start_y = 50, 50
#     spacing = 30
#     font_size = 16
#     vertical_line_height = 10
#     full_expression = f" {separator} ".join(values)
#     text_id = canvas.create_text(0, 0, text=full_expression, font=("Arial", font_size), anchor="w")
#     text_width = canvas.bbox(text_id)[2] - canvas.bbox(text_id)[0]
#     start_x = (400 - text_width) // 2
#     line_start = start_x
#     line_end = start_x + text_width
#     canvas.create_line(line_start, start_y, line_end, start_y, width=2)
#     canvas.create_line(line_start, start_y, line_start, start_y + vertical_line_height, width=2)
#     canvas.create_line(line_end, start_y, line_end, start_y + vertical_line_height, width=2)
#     canvas.create_text(start_x + text_width // 2, start_y + spacing, text=full_expression, font=("Arial", font_size), anchor="center")
#
# def draw_result(canvas, base_values, replace_values, replace_index):
#     canvas.delete("all")
#     if len(replace_values) != 3:
#         return
#     start_x, start_y = 50, 50
#     spacing = 30
#     font_size = 16
#     small_tick_size = 5
#     result_x = start_x + 20
#     result_y = start_y
#     line_start_y = result_y
#     line_end_y = result_y + (len(replace_values) - 1) * spacing
#     canvas.create_line(result_x - 10, line_start_y, result_x - 10, line_end_y, width=2)
#     canvas.create_line(result_x - 10 - small_tick_size // 2, line_start_y, result_x - 10 + small_tick_size // 2, line_start_y, width=2)
#     canvas.create_line(result_x - 10 - small_tick_size // 2, line_end_y, result_x - 10 + small_tick_size // 2, line_end_y, width=2)
#     new_values = base_values[:]
#     new_values[replace_index] = replace_values[0]
#     text = " , ".join(new_values)
#     text_id = canvas.create_text(result_x, result_y, text=text, font=("Arial", font_size), anchor="w")
#     text_width = canvas.bbox(text_id)[2] - canvas.bbox(text_id)[0]
#     line_start = result_x
#     line_end = result_x + text_width
#     canvas.create_line(line_start, result_y - 10, line_end, result_y - 10, width=2)
#     canvas.create_line(line_start, result_y - 10, line_start, result_y, width=2)
#     canvas.create_line(line_end, result_y - 10, line_end, result_y, width=2)
#     for i, value in enumerate(replace_values):
#         new_values = base_values[:]
#         new_values[replace_index] = value
#         text = " , ".join(new_values)
#         canvas.create_text(result_x, result_y + i * spacing, text=text, font=("Arial", font_size), anchor="w")
#
# layout = [
#     [sg.Button("Wprowadź wartości", key="-POPUP-")],
#     [sg.Text("Podaj trzy wartości do zamiany (rozdzielone spacją):"), sg.InputText(key='-REPLACEMENTS-')],
#     [sg.Text("Wybierz wartość do zamiany:"), sg.Combo(["Pierwsza", "Druga"], default_value="Pierwsza", key='-REPLACE-OPTION-')],
#     [sg.Text("Separator:"), sg.Combo([",", ";"], default_value=",", key='-SEPARATOR-')],
#     [sg.Button("Generuj"), sg.Button("Pokaż wynik"), sg.Button("Reset"), sg.Button("Zamknij")],
#     [sg.Canvas(size=(400, 150), key="-CANVAS-IN-")],
#     [sg.Canvas(size=(400, 150), key="-CANVAS-OUT-")]
# ]
#
# window = sg.Window("Dynamiczne Wyrażenia", layout, finalize=True)
# canvas_in = tk.Canvas(window["-CANVAS-IN-"].Widget, width=400, height=150, bg="white")
# canvas_in.pack(fill=tk.BOTH, expand=True)
# canvas_out = tk.Canvas(window["-CANVAS-OUT-"].Widget, width=400, height=150, bg="white")
# canvas_out.pack(fill=tk.BOTH, expand=True)
#
# values_in = []
# separator = ","
#
# while True:
#     event, values = window.read()
#     if event in (sg.WIN_CLOSED, "Zamknij"):
#         break
#     if event == "-POPUP-":
#         val1, val2 = get_two_values()
#         if val1 and val2:
#             values_in = [val1, val2]
#             draw_expressions(canvas_in, values_in, separator)
#     if event == "Generuj":
#         separator = values['-SEPARATOR-']
#         draw_expressions(canvas_in, values_in, separator)
#     if event == "Pokaż wynik":
#         replace_values = values['-REPLACEMENTS-'].split()
#         replace_index = 0 if values['-REPLACE-OPTION-'] == "Pierwsza" else 1
#         draw_result(canvas_out, values_in, replace_values, replace_index)
#     if event == "Reset":
#         values_in = []
#         canvas_in.delete("all")
#         canvas_out.delete("all")
#
# window.close()
