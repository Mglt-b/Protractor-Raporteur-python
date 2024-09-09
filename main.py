import tkinter as tk
from math import cos, sin, radians

class ProtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x50")
        self.root.title("Rapporteur d'Angles Rotatif")

        # Initialisation du canvas
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        # Variables pour les deux rapporteurs
        self.rotation_angle = 0
        self.outer_radius = 150
        self.inner_radius = 100
        self.origin_x, self.origin_y = 200, 200

        # Boutons pour contrôler la rotation
        button_frame = tk.Frame(self.root)
        button_frame.pack(side='bottom', pady=10)
        
        rotate_left_button = tk.Button(button_frame, text="⟲ Gauche", command=self.rotate_left)
        rotate_left_button.pack(side='left', padx=10)

        rotate_right_button = tk.Button(button_frame, text="⟳ Droite", command=self.rotate_right)
        rotate_right_button.pack(side='right', padx=10)

        # Affichage de la différence d'angle
        self.angle_label = tk.Label(self.root, text="Angle: 0°", font=('Arial', 12))
        self.angle_label.pack(pady=10)

        # Dessiner le rapporteur fixe et initial
        self.draw_protractor(fixed=True)  # Dessine le rapporteur fixe (extérieur)
        self.draw_protractor(fixed=False)  # Dessine le rapporteur rotatif (intérieur)

    def draw_protractor(self, fixed=False):
        """Dessine un rapporteur, fixe (extérieur) ou rotatif (intérieur)"""
        if fixed:
            radius = self.outer_radius
            angle_offset = 0  # Pas de rotation pour le rapporteur extérieur
            color = 'black'  # Couleur du rapporteur fixe
        else:
            radius = self.inner_radius
            angle_offset = self.rotation_angle  # Rotation pour le rapporteur intérieur
            color = 'red'  # Couleur du rapporteur rotatif

        # Efface l'ancien rapporteur rotatif (interne uniquement)
        if not fixed:
            self.canvas.delete("rotatif")

        # Dessiner le rapporteur (extérieur ou intérieur)
        self.canvas.create_oval(self.origin_x - radius, self.origin_y - radius,
                                self.origin_x + radius, self.origin_y + radius, outline=color, tags='rotatif' if not fixed else '')

        # Dessiner les graduations chaque 10 degrés
        for angle in range(0, 360, 10):
            rotated_angle = (angle + angle_offset) % 360
            angle_rad = radians((90 - rotated_angle) % 360)  # Toujours avec 0° au nord

            # Définir la longueur des graduations
            if angle % 30 == 0:
                line_length = 20
                font_size = 10
                font_bold = 'bold'
            else:
                line_length = 10
                font_size = 8
                font_bold = 'normal'

            # Calculer les positions des lignes de graduation
            start_x = self.origin_x + radius * cos(angle_rad)
            start_y = self.origin_y - radius * sin(angle_rad)
            end_x = self.origin_x + (radius - line_length) * cos(angle_rad)
            end_y = self.origin_y - (radius - line_length) * sin(angle_rad)
            self.canvas.create_line(start_x, start_y, end_x, end_y, fill=color, tags='rotatif' if not fixed else '')

            # Dessiner les chiffres pour les multiples de 30
            if angle % 30 == 0:
                text_x = self.origin_x + (radius - 30) * cos(angle_rad)
                text_y = self.origin_y - (radius - 30) * sin(angle_rad)
                self.canvas.create_text(text_x, text_y, text=str(angle), font=('Arial', font_size, font_bold), fill=color, tags='rotatif' if not fixed else '')

        # Dessiner un point au centre (commun pour les deux)
        self.canvas.create_oval(self.origin_x - 5, self.origin_y - 5, self.origin_x + 5, self.origin_y + 5, fill='red')

        # Si c'est le rapporteur rotatif, dessiner un trait entre le 0° et le centre
        if not fixed:
            zero_angle_rad = radians(90 - self.rotation_angle)  # 0° correspond au haut du rapporteur
            end_x = self.origin_x + radius * cos(zero_angle_rad)
            end_y = self.origin_y - radius * sin(zero_angle_rad)
            self.canvas.create_line(self.origin_x, self.origin_y, end_x, end_y, fill='blue', width=2, tags='rotatif')

        # Mise à jour de l'affichage de l'angle
        self.update_angle_label()

    def rotate_left(self):
        """Fait pivoter le rapporteur intérieur de 10 degrés vers la gauche"""
        self.rotation_angle = (self.rotation_angle - 5) % 360
        self.draw_protractor(fixed=False)

    def rotate_right(self):
        """Fait pivoter le rapporteur intérieur de 10 degrés vers la droite"""
        self.rotation_angle = (self.rotation_angle + 5) % 360
        self.draw_protractor(fixed=False)

    def update_angle_label(self):
        """Met à jour l'affichage de la différence d'angle entre le rapporteur fixe et rotatif"""
        difference_angle = (360 + self.rotation_angle) % 360  # Différence d'angle (rapporteur extérieur - intérieur)
        difference_angle2 = (360 + 180 + self.rotation_angle) % -360  # Différence d'angle (rapporteur extérieur - intérieur)
        difference_angle3 = (360 + 180 + self.rotation_angle) % 360  # Différence d'angle (rapporteur extérieur - intérieur)

        self.angle_label.config(text=f"Angle: {difference_angle}°\n{difference_angle2}°\n{difference_angle3}°")


# Créer la fenêtre tkinter
root = tk.Tk()
root.attributes('-alpha', 0.6)  # Ajoute la transparence à 60%
app = ProtractorApp(root)

# Lancer l'application
root.mainloop()
