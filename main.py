import PySimpleGUI as sg
import tkinter as tk
import psycopg2


class MainWindow:
    def __init__(self):
        self.uniterm_a = ''
        self.uniterm_b = ''
        self.separator_1 = ''

        self.uniterm_c = ''
        self.uniterm_d = ''
        self.uniterm_e = ''
        self.separator_2 = ''

        self.window = None

        self.draw_uniterm = DrawBasicUniterm(self)

        self.combo_box_side_values = {
            'Lewy Uniterm': 'left',
            'Prawy Uniterm': 'right'
        }

    def set_uniterms_1(self, u_a, u_b, sep):
        self.uniterm_a = u_a
        self.uniterm_b = u_b
        self.separator_1 = sep

        self.window['ua'].update(f'Uniterm A: {self.uniterm_a}')
        self.window['ub'].update(f'Uniterm B: {self.uniterm_b}')
        self.window['sep1'].update(f'Separator: {self.separator_1}')

    def set_uniterms_2(self, u_c, u_d, u_e, sep):
        self.uniterm_c = u_c
        self.uniterm_d = u_d
        self.uniterm_e = u_e
        self.separator_2 = sep

        self.window['uc'].update(f'Uniterm A: {self.uniterm_c}')
        self.window['ud'].update(f'Uniterm B: {self.uniterm_d}')
        self.window['ue'].update(f'Uniterm C: {self.uniterm_e}')
        self.window['sep2'].update(f'Separator: {self.separator_2}')

    def run(self):
        self.window = sg.Window('Operacje na Unitermach',
                                [
                                    [sg.Button(
                                        'Informacje o Programie', key='info')],
                                    [sg.HorizontalSeparator()],
                                    [sg.Text(
                                        'Wartości Unitermu Poziomej Operacji Zrównoleglania')],
                                    [sg.Text(f'Uniterm A: {self.uniterm_a}', key='ua'), sg.Text(f'Uniterm B: {self.uniterm_b}', key='ub'),
                                     sg.Text(f'Separator: {self.separator_1}', key='sep1')],
                                    [sg.Text(
                                        'Wartości Unitermu Pionowej Operacji Eliminacji')],
                                    [sg.Text(f'Uniterm A: {self.uniterm_c}', key='uc'), sg.Text(f'Uniterm B: {self.uniterm_d}', key='ud'),
                                     sg.Text(
                                         f'Uniterm C: {self.uniterm_e}', key='ue'),
                                     sg.Text(f'Separator: {self.separator_2}', key='sep2')],
                                    [sg.HorizontalSeparator()],
                                    [sg.Text('Wczytywanie Danych z Klawiatury')],
                                    [sg.Button(
                                        'Wczytaj Dane Unitermu Poziomej Operacji Zrównoleglania', key='read1')],
                                    [sg.Button(
                                        'Wczytaj Dane Unitermu Pionowej Operacji Eliminacji', key='read2')],
                                    [sg.HorizontalSeparator()],
                                    [sg.Text(
                                        'Baza Danych PostgreSQL')],
                                    [sg.Button(
                                        'Wczytaj Dane Unitermów z Bazy Danych', key='read3')],
                                    [sg.Button(
                                        'Zapisz Dane Unitermów do Bazy Danych', key='save')],
                                    [sg.HorizontalSeparator()],
                                    [sg.Text('Rysowanie Unitermów')],
                                    [sg.Button(
                                        'Rysuj Uniterm Poziomej Operacji Zrównoleglania', key='draw1')],
                                    [sg.Button(
                                        'Rysuj Uniterm Pionowej Operacji Eliminacji', key='draw2')],
                                    [sg.Combo(list(self.combo_box_side_values.keys()), key='side',
                                              default_value='Lewy Uniterm'),
                                     sg.Button('Rysuj Finalny Rezultat', key='draw3')],
                                    *self.draw_uniterm.layout
                                ], finalize=True)

        self.draw_uniterm.setup_canvas()

        while True:
            DatabaseConnection()

            event, values = self.window.read()
            if event in (sg.WINDOW_CLOSED, "Wyjście"):
                break
            elif event == 'info':
                AboutWindow(self).run()
            elif event == 'read1':
                self.window.hide()
                ReadDataFromKeyboardForFirstUniterm(self).run()
                self.window.un_hide()
            elif event == 'read2':
                self.window.hide()
                ReadDataFromKeyboardForSecondUniterm(self).run()
                self.window.un_hide()
            elif event == 'read3':
                DatabaseConnection().get_values_from_database()
            elif event == 'save':
                DatabaseConnection().save_values_into_database(self.uniterm_a, self.uniterm_b,
                                                               self.uniterm_c, self.uniterm_d, self.uniterm_e, self.separator_1, self.separator_2)
            elif event == 'draw1':
                self.draw_uniterm.canvas.delete('all')
                self.draw_uniterm.draw_operation_1(
                    self.uniterm_a, self.uniterm_b, self.separator_1)
            elif event == 'draw2':
                self.draw_uniterm.canvas.delete('all')
                self.draw_uniterm.draw_operation_2(
                    self.uniterm_c, self.uniterm_d, self.uniterm_e, self.separator_2)
            elif event == 'draw3':
                self.draw_uniterm.canvas.delete('all')
                self.draw_uniterm.draw_operation_3(
                    self.uniterm_a, self.uniterm_b, self.uniterm_c, self.uniterm_d, self.uniterm_e, self.separator_1,
                    self.separator_2, self.combo_box_side_values.get(values['side']))

        DatabaseConnection().close_connection()
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
                                    [sg.Text('Podaj wyrażenie A'),
                                     sg.Input(key='-UNITERM_A-')],
                                    [sg.Text('Podaj wyrażenie B'),
                                     sg.Input(key='-UNITERM_B-')],
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
                                    [sg.Text('Podaj wyrażenie A'),
                                     sg.Input(key='-UNITERM_A-')],
                                    [sg.Text('Podaj wyrażenie B'),
                                     sg.Input(key='-UNITERM_B-')],
                                    [sg.Text('Podaj wyrażenie C'),
                                     sg.Input(key='-UNITERM_C-')],
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
        self.layout = [[sg.Canvas(size=(400, 300), key='canvas')]]

    def setup_canvas(self):
        canvas_elem = self.main_window.window['canvas']
        tk_widget = canvas_elem.Widget
        self.canvas = tk.Canvas(tk_widget, width=400, height=300, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def draw_operation_1(self, uniterm_a, uniterm_b, separator_1, x=200, y=100):
        if uniterm_a == '' or uniterm_b == '' or separator_1 == '':
            return

        full_text = f"{uniterm_a}     {separator_1}     {uniterm_b}"

        text_id = self.canvas.create_text(
            x, y, text=full_text, font=('Arial', 16), anchor='center')

        bbox = self.canvas.bbox(text_id)
        text_width = bbox[2] - bbox[0]
        self.canvas.move(text_id, (x - bbox[0] - text_width // 2), 0)

        start_x = bbox[0] - 10
        start_y = y - 25
        line_start = start_x
        line_end = bbox[2] + 10
        vertical_line_height = 10

        self.canvas.create_line(line_start, start_y,
                                line_end, start_y, width=2)
        self.canvas.create_line(
            line_start, start_y, line_start, start_y + vertical_line_height, width=2)
        self.canvas.create_line(
            line_end, start_y, line_end, start_y + vertical_line_height, width=2)

    def draw_operation_2(self, uniterm_c, uniterm_d, uniterm_e, separator_2, x=200, y=100):
        if uniterm_c == '' or uniterm_d == '' or uniterm_e == '' or separator_2 == '':
            return

        values = [uniterm_c, separator_2, uniterm_d, separator_2, uniterm_e]

        spacing = 30
        font_size = 16
        small_tick_size = 10

        line_start_y = y
        line_end_y = y + (len(values) - 1) * spacing

        self.canvas.create_line(x - 10, line_start_y,
                                x - 10, line_end_y, width=2)

        self.canvas.create_line(x - 10 - small_tick_size // 2, line_start_y, x - 10 + small_tick_size // 2,
                                line_start_y, width=2)
        self.canvas.create_line(x - 10 - small_tick_size // 2, line_end_y, x - 10 + small_tick_size // 2, line_end_y,
                                width=2)

        for i, value in enumerate(values):
            self.canvas.create_text(x, y + i * spacing, text=value.strip(), font=("Arial", font_size),
                                    anchor="w")

    def draw_operation_3(self, uniterm_a, uniterm_b, uniterm_c, uniterm_d, uniterm_e, separator_1, separator_2, side):
        if side == 'left':
            self.draw_operation_1(' ', uniterm_b, separator_1)
            self.draw_operation_2(uniterm_c, uniterm_d,
                                  uniterm_e, separator_2, 170, 100)
        elif side == 'right':
            self.draw_operation_1(uniterm_a, ' ', separator_1)
            self.draw_operation_2(uniterm_c, uniterm_d,
                                  uniterm_e, separator_2, 225, 100)


class DatabaseConnection:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="mydatabase", user="postgres", password="password", host="localhost",
                                     port="5432")
        self.cur = self.conn.cursor()

        self.cur.execute('CREATE TABLE IF NOT EXISTS data ('
                         'uniterm_a VARCHAR(255),'
                         'uniterm_b VARCHAR(255),'
                         'uniterm_c VARCHAR(255),'
                         'uniterm_d VARCHAR(255),'
                         'uniterm_e VARCHAR(255),'
                         'separator_1 VARCHAR(255),'
                         'separator_2 VARCHAR(255)'
                         ')')
        self.conn.commit()

    def close_connection(self):
        self.cur.close()
        self.conn.close()

    def get_values_from_database(self):
        self.cur.execute('SELECT * FROM data')
        row = self.cur.fetchall()
        if row:
            MainWindow().set_uniterms_1(row[0][0], row[0][1], row[0][5])
            MainWindow().set_uniterms_2(
                row[0][2], row[0][3], row[0][4], row[0][6])

    def save_values_into_database(self, uniterm_a, uniterm_b, uniterm_c, uniterm_d, uniterm_e, separator_1, separator_2):
        self.cur.execute('DELETE FROM data')
        self.cur.execute('INSERT INTO data (uniterm_a, uniterm_b, uniterm_c, uniterm_d, uniterm_e, separator_1, separator_2)'
                         'VALUES (%s, %s, %s, %s, %s, %s, %s)',
                         (uniterm_a, uniterm_b, uniterm_c, uniterm_d, uniterm_e, separator_1, separator_2))
        self.conn.commit()


if __name__ == "__main__":
    MainWindow().run()
