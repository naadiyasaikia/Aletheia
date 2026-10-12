def handle_input(self, key):
    if key == ord(" "):
        self.basic_attack()
    elif key == ord("j"):
        self.use_skill(0)
    elif key == ord("k"):
        self.use_skill(1)
    elif key == ord("l"):
        self.use_skill(2)