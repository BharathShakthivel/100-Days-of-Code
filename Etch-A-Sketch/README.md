## 🖊️ Etch-a-Sketch with Python Turtle

This project is a simple implementation of an **Etch-a-Sketch** game using Python’s built-in [`turtle`](https://docs.python.org/3/library/turtle.html) graphics module.
You can move the turtle around the screen using your keyboard to "draw" patterns, and reset the screen whenever you want.

### 🎮 Controls

* **W** → Move forward
* **S** → Move backward
* **A** → Rotate counter-clockwise (turn left)
* **D** → Rotate clockwise (turn right)
* **C** → Clear the screen & reset the turtle to the center

### 📜 Code Explanation

* `from turtle import Turtle, Screen`
  Imports the **Turtle** class for drawing and **Screen** for creating the canvas.

* `screen.listen()`
  Tells the program to start listening for keyboard input.

* `screen.onkey(key="w", fun=move_forwards)`
  Binds specific keys to functions. For example, pressing **W** calls `move_forwards()`, moving the turtle forward by 10 units.

* Movement functions (`move_forwards`, `move_backwards`, `move_counter_clockwise`, `move_clockwise`)
  Control the turtle’s motion and direction.

* `clear()`
  Clears everything drawn on the screen, sends the turtle back to its starting position (`home()`), and gets it ready to draw again.

* `screen.exitonclick()`
  Keeps the window open until you click anywhere inside it.

### 🚀 How to Run

1. Make sure you have Python installed (≥ 3.7).
2. Save the script as `etch_a_sketch.py`.
3. Run it using:

```bash
python etch_a_sketch.py
```

4. Use the controls above to draw!


