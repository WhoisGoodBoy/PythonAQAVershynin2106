class Traffic_light:
    def __init__(self):
        self.__color = 'Green'
    def __str__(self):
        return f'Hi I`m traffic_light instance, and my current color_status is {self.__color}'

traffic_light_1 = Traffic_light()
print(traffic_light_1)