from Global import *
import tkinter.font
import math


class Renderer:
    def __init__(self, canvas, resolution):
        self.canvas = canvas
        self.resolution = resolution
        self.font = tkinter.font.Font(family="Arial", size=15)
        self.image = tkinter.PhotoImage(file=fix_path("./Images/Pizza.png"))
        self.circle_radius = 80
        self.circle_x = self.resolution[0] / 2
        self.circle_y = 30
        self.circle_center_pos = (self.resolution[0] / 2, self.circle_y + self.circle_radius)
        self.fraction_y = self.circle_y + self.circle_radius * 2 + 10
        self.line_length = 50
        self.line_width = 1
        self.line_padding = 5
        self.top_num = 1
        self.bottom_num = 100

    def update_canvas(self, value):
        self.canvas.delete("all")
        self.bottom_num = value
        self.canvas.create_image(self.circle_x, self.circle_y, image=self.image, anchor="n")
        size = self.get_size(self.canvas.create_text(self.resolution[0] / 2, self.fraction_y,
                                                     text=str(self.top_num),
                                                     fill="black",
                                                     font=self.font,
                                                     anchor="n"))
        self.canvas.create_line(self.resolution[0] / 2 - self.line_length / 2,
                                self.fraction_y + size[1] + self.line_padding / 2,
                                self.resolution[0] / 2 + self.line_length / 2,
                                self.fraction_y + size[1] + self.line_padding / 2,
                                width=self.line_width)
        self.canvas.create_text(self.resolution[0] / 2,
                                self.fraction_y + size[1] + self.line_padding + self.line_width,
                                text=str(self.bottom_num),
                                fill="black",
                                font=self.font,
                                anchor="n")
        if value == 1:  # No need to draw any cuts if the fraction is 1/1.
            return None
        slice_angle = 360 / self.bottom_num
        current_angle = 0
        for cut in range(self.bottom_num):
            current_angle += slice_angle
            point1 = self.circle_center_pos
            point2 = (point1[0] + self.circle_radius * math.cos(math.pi * current_angle / 180),
                      point1[1] + self.circle_radius * math.sin(math.pi * current_angle / 180))
            self.canvas.create_line(point1,
                                    point2,
                                    width=1)

    def get_size(self, object_id):
        bounding_rect = self.canvas.bbox(object_id)
        return bounding_rect[2] - bounding_rect[0], bounding_rect[3] - bounding_rect[1]
