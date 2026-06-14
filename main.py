import mss
import cv2
import numpy as np
import pyautogui
import time
from pynput import keyboard

class GridBot:
    def __init__(self, grid_template_path, template_o_path, template_x_path, template_ok_button_path, rows, cols):
        # Загружаем шаблон всей сетки
        self.template_grid = cv2.imread(grid_template_path, 0)
        self.template_o = cv2.imread(template_o_path, 0)
        self.template_x = cv2.imread(template_x_path, 0)
        self.template_h, self.template_w = self.template_grid.shape
        self.template_button = cv2.imread(template_ok_button_path, 0)

        self.rows = rows  # например, 9 для крестиков-ноликов
        self.cols = cols  # например, 9

        # Размер одной клетки (вычисляем из размеров шаблона)
        self.cell_w = 63  # self.template_w // cols
        self.cell_h = 63  # self.template_h // rows

        print(f"Размер клетки: {self.cell_w} x {self.cell_h}")

    def find_grid_on_screen(self):
        grid_pos = self.find_matched(self.template_grid)

        if grid_pos:
            print("Сетка найдена ", grid_pos)
            return grid_pos
        else:
            print("Сетка не найдена!")
            return None

    def find_matched(self, template_img, source_image=None):
        with mss.MSS() as sct:
            # Скриншот всего экрана

            if source_image is None:
                screenshot = sct.grab(sct.monitors[1])
                source_image = np.array(screenshot)

            gray = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)

            # Ищем шаблон всей сетки
            result = cv2.matchTemplate(gray, template_img, cv2.TM_CCOEFF_NORMED)

            # Находим лучшее совпадение
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            if max_val > 0.8:  # 80% уверенности
                # max_loc = (x, y) левого верхнего угла шаблона на экране
                grid_x, grid_y = max_loc
                return grid_x, grid_y
            else:
                return None

    def get_image_at(self, x, y, width, height):
        """Возвращает изображение области экрана с координатами (x, y) и размером width x height"""
        with mss.MSS() as sct:
            zone = {
                "left": int(x),
                "top": int(y),
                "width": int(width),
                "height": int(height)
            }
            screenshot = sct.grab(zone)
            return np.array(screenshot)

    def get_all_cell_coords(self):
        """Возвращает матрицу с координатами центров всех клеток"""
        pos = self.find_grid_on_screen()
        if not pos:
            return None

        grid_x, grid_y = pos
        cells = []

        grid_x += 2
        grid_y += 2

        for row in range(self.rows):
            row_cells = []
            for col in range(self.cols):
                # Центр клетки

                if col > 0:
                    offset_x = 5 * col
                else:
                    offset_x = 0

                if row > 0:
                    offset_y = 1
                else:
                    offset_y = 0

                cell_x = grid_x + offset_x + col * self.cell_w  # + self.cell_w #// 2
                cell_y = grid_y - offset_y + row * self.cell_h  # + self.cell_h #// 2
                row_cells.append((cell_x, cell_y))
            cells.append(row_cells)

        return cells

    def click_cell(self, cell):
        x, y,_ = cell
        pyautogui.click(x, y)

    def get_cells(self):
        cell_coords = self.get_all_cell_coords()
        if cell_coords:
            for row_index, row in enumerate(cell_coords):
                for cell_index, cell in enumerate(row):
                    cell_image = bot.get_image_at(cell[0], cell[1], 63, 63)
                    file_name = "screen_shots/row_" + str(row_index) + "_cell_" + str(cell_index) + ".png"
                    cv2.imwrite(file_name, cell_image)

                    value = "N"

                    x_found = bot.find_matched(self.template_x, cell_image)
                    if x_found:
                        value = "X"
                    else:
                        o_found = bot.find_matched(self.template_o, cell_image)
                        if o_found:
                            value = "O"

                    row[cell_index] = cell + (value,)
        return cell_coords

    def click_ok_button(self):
        ok_coords = self.find_matched(self.template_button)

        if ok_coords is None:
            return

        x, y = ok_coords

        pyautogui.click(x+20, y+5)

    def get_cell_to_click(self):
        cells = self.get_cells()

        if cells is None:
            return None

        print("CELLS: ", cells)

        for cells_row in cells:
            for cell in cells_row:
                print(cell)
                if cell[2] == 'N':
                    return cell

        return None

    def run(self):
        self.click_ok_button()

        cell = self.get_cell_to_click()

        if cell is None:
            return

        self.click_cell(cell)

def on_press(key):
    global running
    if key == keyboard.Key.esc:
        print("EXIT")
        running = False

bot = GridBot(grid_template_path="template_grid.png",
              template_o_path="template_o.png",
              template_x_path="template_x.png",
              template_ok_button_path="ok_button.png",
              rows=3,
              cols=3
              )

listener = keyboard.Listener(on_press=on_press)
listener.start()


running = True

while running:
    bot.run()

    time.sleep(1)