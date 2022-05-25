import arcade

"""My problem is that I'm trying to use sections as UI, and as long as they were without interactive elements, they served that purpose perfectly. But now I tried to make a section with interactivity, but since the first section is processed first, the update does not reach the second section.

If, however, the "broken" section is processed first, then it is naturally not displayed on the screen, because the "working" section is rendered after it.

Is there any way to use the sections as UI, or should I really not do that, because their purpose is to divide the screen?"""

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(500, 500, 500, resizable=True)
        self.views = {}
        self.game_view = None


class BrokenSection(arcade.Section):
    def __init__(self, left: float, bottom: float, width: float, height: float,
                 **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

    def on_draw(self):
        arcade.draw_lrtb_rectangle_filled(0, self.window.width, self.window.height, 0,
                                          color=arcade.color_from_hex_string('#411970'))

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.view.second_section.enabled = False

class WorkingSection(arcade.Section):
    def __init__(self, left: float, bottom: float, width: float, height: float,
                 **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        self.button = self.new_button()

    def new_button(self):
        button_texture = arcade.load_texture(('./assets/button.png'))
        return arcade.Sprite(scale=0.6, texture=button_texture)

    def on_show_section(self):
        self.button.center_x, self.button.center_y = self.window.width * 0.9, self.window.height * 0.9

    def button_draw(self):
        self.button.draw()
        arcade.Text('Show', self.button.center_x, self.button.center_y, font_size=15, anchor_y='center', anchor_x='center')

    def on_draw(self):
        arcade.draw_lrtb_rectangle_filled(0, self.window.width, self.window.height, 0,
                                          color=arcade.color_from_hex_string('#000000'))
        self.button.draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if self.button.collides_with_point((x,y)):
            self.view.second_section.enabled = True


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.first_section = WorkingSection(0,0, self.window.width, self.window.height)
        self.second_section = BrokenSection(0, 0, self.window.width, self.window.height, enabled=False)
        self.section_manager.add_section(self.first_section)
        self.section_manager.add_section(self.second_section)
    def on_draw(self):
        self.clear()






def main():
    window = GameWindow()
    window.center_window()
    view = GameView()
    window.show_view(view)
    arcade.run()


if __name__ == "__main__":
    main()
