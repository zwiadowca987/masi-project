import PySimpleGUI as sg


class MainWindow:
    def __init__(self):
        self.window = sg.Window('Mateusz Szczerek',
                                [
                                    [sg.Button('Informacje')],
                                    [sg.Button('Wczytaj Dane'), sg.Button(
                                        "Olej Wczytanie Danych")]
                                ])

    def run(self):
        while True:
            event, _ = self.window.read()
            if event in (sg.WINDOW_CLOSED, "Wyjście"):
                break
            elif event == 'Informacje':
                AboutWindow().run()

        self.window.close()


class AboutWindow:
    def __init__(self):
        self.window = sg.Window('Mateusz Szczerek',
                                [
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


if __name__ == "__main__":
    MainWindow().run()

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
#             [sg.Button("Ustawienia"), sg.Button(
#                 "Użytkownicy"), sg.Button("O programie")],
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
#             [sg.Listbox(values=["Jan Kowalski", "Anna Nowak",
#                         "Michał Wiśniewski"], size=(30, 5))],
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
