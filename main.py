import tkinter as tk
from tkinter import messagebox
import random
import platform
from cipher_logic import EmojiCipherLogic  # Importing the Backend logic python script


class CipherApp:
    def __init__(self, root):
        self.root = root
        self.logic = EmojiCipherLogic()  # Initialize Backend

        self.root.title("NEURAL EMOJI CIPHER v5.0")
        self.root.geometry("550x750")
        self.root.configure(bg="#020202")

        # Detect OS Font
        self.emoji_font = self._get_emoji_font()

        self._setup_ui()

    def _get_emoji_font(self):
        current_os = platform.system()
        if current_os == "Windows":
            return ("Segoe UI Emoji", 14)
        elif current_os == "Darwin":  # macOS
            return ("Apple Color Emoji", 14)
        else:  # Linux
            return ("DejaVu Sans", 14)

    def _setup_ui(self):
        # Header
        tk.Label(
            self.root,
            text="[ ENCRYPTION TERMINAL ]",
            font=("Courier", 20, "bold"),
            bg="#020202",
            fg="#00ff41",
        ).pack(pady=15)

        # --- Input Section ---
        input_label_frame = tk.Frame(self.root, bg="#020202")
        input_label_frame.pack(fill="x", padx=50)
        tk.Label(
            input_label_frame,
            text="SOURCE INPUT:",
            font=("Courier", 10),
            bg="#020202",
            fg="#00ff41",
        ).pack(side="left")

        tk.Button(
            input_label_frame,
            text="[PASTE]",
            command=self.paste_input,
            font=("Courier", 8),
            bg="#111",
            fg="#00ff41",
            bd=0,
            activebackground="#00ff41",
        ).pack(side="right")

        self.input_box = tk.Text(
            self.root,
            height=6,
            width=40,
            bg="#111",
            fg="#00ff41",
            insertbackground="#00ff41",
            font=self.emoji_font,
            bd=1,
            relief="flat",
        )
        self.input_box.pack(pady=5)

        # --- Logic Buttons ---
        btn_frame = tk.Frame(self.root, bg="#020202")
        btn_frame.pack(pady=15)

        tk.Button(
            btn_frame,
            text="LOCK (Encrypt)",
            command=self.do_encrypt,
            width=15,
            bg="#004400",
            fg="white",
            font=("Courier", 10, "bold"),
            relief="flat",
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            btn_frame,
            text="UNLOCK (Decrypt)",
            command=self.do_decrypt,
            width=15,
            bg="#440000",
            fg="white",
            font=("Courier", 10, "bold"),
            relief="flat",
        ).grid(row=0, column=1, padx=10)

        # --- Output Section ---
        output_label_frame = tk.Frame(self.root, bg="#020202")
        output_label_frame.pack(fill="x", padx=50)
        tk.Label(
            output_label_frame,
            text="PROCESSED OUTPUT:",
            font=("Courier", 10),
            bg="#020202",
            fg="#00ff41",
        ).pack(side="left")

        tk.Button(
            output_label_frame,
            text="[COPY]",
            command=self.copy_output,
            font=("Courier", 8),
            bg="#111",
            fg="#00ff41",
            bd=0,
            activebackground="#00ff41",
        ).pack(side="right")

        self.output_box = tk.Text(
            self.root,
            height=6,
            width=40,
            bg="#0a0a0a",
            fg="#ffffff",
            font=self.emoji_font,
            bd=2,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#00ff41",
        )
        self.output_box.pack(pady=5)

        # --- Status & Utils ---
        self.status = tk.Label(
            self.root,
            text="SYSTEM STATUS: ONLINE",
            font=("Courier", 9),
            bg="#020202",
            fg="#008800",
        )
        self.status.pack(side="bottom", pady=10)

        tk.Button(
            self.root,
            text="CLEAR TERMINAL",
            command=self.clear_fields,
            font=("Courier", 8),
            bg="#020202",
            fg="#444",
            bd=0,
        ).pack(side="bottom")

    # Clipboard Functions
    def copy_output(self):
        content = self.output_box.get("1.0", tk.END).strip()
        if content:
            self.root.clipboard_clear()
            self.root.clipboard_append(content)
            self.status.config(text="STATUS: DATA COPIED", fg="#00ff41")
        else:
            messagebox.showwarning("Empty", "Nothing to copy!")

    def paste_input(self):
        try:
            content = self.root.clipboard_get()
            self.input_box.delete("1.0", tk.END)
            self.input_box.insert(tk.END, content)
            self.status.config(text="STATUS: DATA PASTED", fg="#00ff41")
        except:
            messagebox.showerror("Error", "Clipboard is empty.")

    def clear_fields(self):
        self.input_box.delete("1.0", tk.END)
        self.output_box.delete("1.0", tk.END)
        self.status.config(text="STATUS: TERMINAL WIPED", fg="#444")

    # Animation Connector
    def animate_glitch(self, final_text, step=0):
        glitch_pool = "01@#$%&*X?|/\\"
        if step < 10:
            scrambled = "".join(
                random.choice(glitch_pool) for _ in range(len(final_text))
            )
            self.output_box.delete("1.0", tk.END)
            self.output_box.insert(tk.END, scrambled)
            self.root.after(50, lambda: self.animate_glitch(final_text, step + 1))
        else:
            self.output_box.delete("1.0", tk.END)
            self.output_box.insert(tk.END, final_text)
            self.status.config(text="PROCESS COMPLETE", fg="#00ff41")

    # Core actions calling the Logic class
    def do_encrypt(self):
        text = self.input_box.get("1.0", tk.END).strip()
        if not text:
            return
        result = self.logic.encrypt(text)
        self.status.config(text="ENCRYPTING...", fg="#ffff00")
        self.animate_glitch(result)

    def do_decrypt(self):
        text = self.input_box.get("1.0", tk.END).strip()
        if not text:
            return
        result = self.logic.decrypt(text)
        self.status.config(text="DECRYPTING...", fg="#ffff00")
        self.animate_glitch(result)


if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()
