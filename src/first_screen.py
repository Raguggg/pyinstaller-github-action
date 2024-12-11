import logging
import random
from pathlib import Path

import customtkinter

from .utils import FloatSpinbox

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.__basic_setup()
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar_frame = SideBarFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

    def __basic_setup(self):
        self.current_dir: Path = Path(__file__).resolve().parent.parent
        self.assert_dir = self.current_dir / "assets"
        # configure window
        self.title("Sample exe")
        self.geometry("1445x800")
        icon_file: Path = self.assert_dir / "icon.ico"
        if icon_file.exists():
            try:
                self.iconbitmap(icon_file)
            except Exception as _:
                pass


class SideBarFrame(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.setup_init()

    def setup_init(self):
        self.grid_rowconfigure(10, weight=1)
        self.logo_label = customtkinter.CTkLabel(
            self,
            text="Home",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.logo_label.grid(row=0, column=0, padx=30, pady=(20, 10))

        # label for delay
        self.delay_label = customtkinter.CTkLabel(
            self,
            text="Delay in seconds Range:",
            anchor="w",
            font=customtkinter.CTkFont(size=10, weight="bold"),
        )
        self.delay_label.grid(row=2, column=0, padx=20, pady=(10, 0))
        self.delay_val_min = FloatSpinbox(self, step_size=1, start=20, end=999)
        self.delay_val_min.grid(row=3, column=0, padx=20, pady=(10, 0))
        self.delay_val_max = FloatSpinbox(self, step_size=1, start=20, end=999)
        self.delay_val_max.set(37)
        self.delay_val_max.grid(row=4, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_label = customtkinter.CTkLabel(
            self, text="Appearance Mode:", anchor="w"
        )

        self.appearance_mode_label.grid(row=11, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_optionemenu.grid(row=12, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(
            self, text="UI Scaling:", anchor="w"
        )
        self.scaling_label.grid(row=13, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(
            self,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event,
        )
        self.scaling_optionemenu.grid(row=14, column=0, padx=20, pady=(10, 20))
        self.appearance_mode_optionemenu.set("System")
        self.scaling_optionemenu.set("100%")

    def get_delay_value(self) -> float:
        min_val: float = 20.0
        max_val: float = 37.0
        min_val_get = self.delay_val_min.get()
        max_val_get = self.delay_val_max.get()
        if min_val_get:
            min_val = min_val_get
        if max_val_get:
            max_val = max_val_get

        # genreate random number between min and max
        return random.uniform(min_val, max_val)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


if __name__ == "__main__":
    app = App()
    app.mainloop()
