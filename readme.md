### 📖 **Description**

This **Rotating Protractor App** is a graphical tool developed in Python using **Tkinter**. It allows users to visually manipulate two protractors:
1. A **fixed outer protractor** with 0° at the top (north).
2. A **rotating inner protractor** that can be rotated in 10° increments using buttons.

This tool is particularly useful for **measuring angles** or comparing angular positions, for instance, when working with graphical designs or geometrical drawings. 

### 🎯 **Features**
- 🧭 **Fixed Outer Protractor**: Always points 0° at the north.
- 🔄 **Rotating Inner Protractor**: Can rotate by pressing buttons for precise angle measurements.
- 🖊️ **Highlighted Line**: A line from the center to the 0° of the rotating protractor.
- 🧮 **Angle Difference Calculation**: Shows the difference between the fixed and rotating protractors.
- 💻 **Transparency**: The window has adjustable transparency for better visualization on top of drawings.

### 🔧 **Dependencies**

The only library required is **Tkinter**, which is included with Python by default. No external dependencies are necessary.

### 🛠️ **Installation and Usage**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/rotating-protractor-app.git

2. **Run the Python script**: Simply open a terminal and run the script:
   ```bash
   python protractor_app.py

3. **Controls**:
 - Use the ⟲ Left button to rotate the inner protractor counterclockwise by 10°.
 - Use the ⟳ Right button to rotate the inner protractor clockwise by 10°.
 - The angle difference between the two protractors will be displayed below the canvas.