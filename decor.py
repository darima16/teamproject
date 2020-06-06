import math
import turtle
import random


class Ufo:
    def __init__(self, name, x, y, size, color, count_pillars, count_lamps, pillors_down=True, show_name=False,
                 made_in='Russia', engine_grade='Turbo UFO', speed=25):
        self._name = name
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.count_pillars = count_pillars
        self.count_lamps = count_lamps
        self.pillars_down = pillors_down
        self.show_name = show_name
        self.__maid_in = made_in
        self.__engine_grade = engine_grade
        self.speed = speed

    @property
    def engine_grade(self):
        if self.__engine_grade == 'Turbo UFO':
            return 'standart'
        return self.__engine_grade

    @engine_grade.setter
    def engine_grade(self, new_grade):
        if new_grade == '':
            print('Марка двигателя не может быть пустой!')
        else:
            self.__engine_grade = new_grade

    @property
    def set_made_in(self, made_in):
        countries = ['USA', 'Russia']
        if made_in in countries:
            self.__maid_in = made_in
        else:
            self.__maid_in = None

    @property
    def get_made_in(self, made_in):
        return self.__maid_in

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        s = 'Сконструировано НЛО'
        if self.show_name:
            s += ' под названием {name}\n'.format(name=self.name)
        else:
            s += ' с неизвестным названием\n'
        s += 'Координаты НЛО: ({x}; {y})\n'.format(x=self.x, y=self.y)
        s += 'Размер: {size}\n'.format(size=self.size)
        s += 'Размер: {size}\n'.format(size=self.size)
        if self.pillars_down:
            s += 'Опроы опущены\n'
        else:
            s += 'Опроы подняты\n'
        s += 'Количество опор: {count}'.format(count=self.count_pillars)
        s += 'Количество фонарей: {count}'.format(count=self.count_lamps)
        return s

    def __repr__(self):
        return self.__str__()

    def show(self):
        turtle.ht()
        if self.pillars_down:
            for i in range(self.count_pillars):
                lx = self.x - self.size / 2 + i * (self.size / (self.count_pillars - 1))
                turtle.penup()
                turtle.goto(self.x, self.y + self.size/3)
                turtle.pendown()
                turtle.goto(lx, self.y - self.size/6)

        turtle.penup()
        turtle.goto(self.x, self.y - self.size / 12)
        turtle.pendown()
        turtle.fillcolor('black')
        turtle.begin_fill()
        turtle.circle(self.size / 4)
        turtle.end_fill()

        turtle.penup()
        turtle.fillcolor(self.color)
        turtle.goto(self.x - self.size / 2, self.y + self.size / 4)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fd(self.size)
        i = math.pi / 2
        while i <= 3 * math.pi / 2:
            sx = (self.size / 2) * math.sin(i)
            sy = (self.size / 3) * math.cos(i)
            turtle.goto(self.x + sx, self.y + self.size/4 + sy)
            i += math.pi / self.size
        turtle.end_fill()

        turtle.fillcolor('red')
        n = self.count_lamps + 2
        for i in range(1, n - 1):
            dx = self.size / (n - 1)
            turtle.begin_fill()
            turtle.penup()
            turtle.goto(self.x - self.size / 2 + i * dx, self.y + self.size / 14)
            turtle.pendown()
            turtle.circle(dx/4)
            turtle.end_fill()

        turtle.penup()
        if self.show_name:
            turtle.goto(self.x, self.y + self.size / 2)
            turtle.pendown()
            turtle.write(self.name, align='center')
            turtle.penup()
        turtle.goto(0, 0)
        turtle.st()

    def move(self):
        self.x += random.randint(-self.speed, self.speed)
        self.y += random.randint(-self.speed, self.speed)