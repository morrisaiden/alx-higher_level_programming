"""
  Class base that  manage id attribute in all classes and
  to avoid duplicating the same code (by extension, same bugs)
"""
import json
import os
import csv


class Base:
    """
        Defines a class named Base which manages the id attribute for all classes in the project.
        The __init__ method initializes instances of the class, assigning a unique id if not provided.
        Arguments:
            @id: The id for a specific instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
          Defines a static method to_json_string that converts a list of dictionaries into a JSON string.
        """
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
            Defines a static method from_json_string that converts a JSON string into a list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Defines a class method save_to_file that writes the
            string representation of objects to a JSON file.
        """
        file_name = cls.__name__ + ".json"

        content = []
        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_dict = json.loads(cls.to_json_string(item))
                content.append(json_dict)

        with open(file_name, mode="w") as fd:
            json.dump(content, fd)

    @classmethod
    def create(cls, **dictionary):
        """
           Defines a class method create that returns an instance with attributes set based on a dictionary.
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            r2 = Rectangle(3, 8)
        elif cls.__name__ == "Square":
            r2 = Square(5)
        r2.update(**dictionary)
        return (r2)

    @classmethod
    def load_from_file(cls):
        """
            Defines a class method load_from_file that loads instances from a JSON file.
        """
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, encoding="UTF8") as fd:
                content = cls.from_json_string(fd.read())
        except:
            return []

        instances = []

        for instance in content:
            tmp = cls.create(**instance)
            instances.append(tmp)

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
            Defines a static method draw using the turtle module to draw rectangles and squares.
        """
        import turtle

        turtle.penup()
        turtle.pensize(10)
        turtle.bgcolor("black")
        turtle.color("teal")
        turtle.hideturtle()
        turtle.goto(-300, 300)
        turtle.speed(0)

        for instance in list_rectangles:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 200
            else:
                move_by = instance.width + 30
            x_cordinate = round(turtle.xcor(), 5)
            turtle.goto(x_cordinate + move_by, 300)

        turtle.goto(-300, 100)
        for instance in list_squares:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 100
            else:
                move_by = instance.width + 30
            x_cordinate = round(turtle.xcor(), 5)
            turtle.goto(x_cordinate + move_by, 100)

        turtle.exitonclick()

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            Defines a class method save_to_file_csv that writes objects to a CSV file.
        """
        file_name = cls.__name__ + ".csv"

        with open(file_name, mode="w", newline='', encoding="UTF8") as fd:
            write_this = csv.writer(fd, delimiter=" ")

            if cls.__name__ == "Rectangle":
                for item in list_objs:
                    string = ""
                    item = item.to_dictionary()
                    string += (str(item["id"]) + "," +
                               str(item["width"]) + "," +
                               str(item["height"]) + "," +
                               str(item["x"]) + "," + str(item["y"]))
                    write_this.writerow(string)

            if cls.__name__ == "Square":
                for item in list_objs:
                    string = ""
                    item = item.to_dictionary()
                    string += (str(item["id"]) + "," +
                               str(item["size"]) + "," +
                               str(item["x"]) + "," + str(item["y"]))
                    write_this.writerow(string)

    @classmethod
    def load_from_file_csv(cls):
        """
           Defines a class method load_from_file_csv that currently returns an empty list.
        """
        return ([])