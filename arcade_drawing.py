"""
This is a sample program to show how to draw using the Arcade library
"""

import arcade

# Open a window
# Set the window title to "Forest"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Forest")

# Set the background color
arcade.set_background_color((45, 125, 220))

# Ready to draw
arcade.start_render()

# Draw the rectangle
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
# Draw tree trunk
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.color.BROWN)
# Draw tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.GREEN)
# Another tree with ellipse crown
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.color.BROWN)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.GREEN)
# Another tree, with a trunk and arc for top
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.color.BROWN)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.GREEN, 0, 180)
# Draw a pine tree using a triangle
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.color.BROWN)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.GREEN)
# Draw a tree using a polygon
arcade.draw_rectangle_filled(500,320, 20, 60, arcade.color.BROWN)
arcade.draw_polygon_filled(((500, 400),
                           (480, 360),
                           (470, 320),
                           (530, 320),
                           (520, 360)
                           ),
                           arcade.csscolor.GREEN)
# Draw the sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)
# Draw rays
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW)

arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW)

# Print a text
arcade.draw_text("Welcome to the Redwood forest", 150, 200, arcade.color.BLACK, 18)



# Finish drawing
arcade.finish_render()

if __name__ == '__main__':
    arcade.run()

