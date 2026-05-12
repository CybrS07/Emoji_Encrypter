# cipher_logic.py


class EmojiCipherLogic:
    def __init__(self):
        # Mapping dictionary
        self.EMOJI_CIPHER = {  # major vulnerability as if map is once cracked the attacker can decrypt messages
            "a": "👽",
            "b": "👾",
            "c": "💀",
            "d": "👺",
            "e": "👻",
            "f": "🧛",
            "g": "🧟",
            "h": "🔪",
            "i": "🩸",
            "j": "💉",
            "k": "💊",
            "l": "🔥",
            "m": "🌑",
            "n": "🌩️",
            "o": "🛸",
            "p": "🗝️",
            "q": "🪙",
            "r": "⚖️",
            "s": "💣",
            "t": "🔌",
            "u": "🦇",
            "v": "🦉",
            "w": "🌘",
            "x": "🥀",
            "y": "🌫️",
            "z": "⚰️",
            " ": "⬛",
            "0": "0️⃣",
            "1": "1️⃣",
            "2": "2️⃣",
            "3": "3️⃣",
            "4": "4️⃣",
            "5": "5️⃣",
            "6": "6️⃣",
            "7": "7️⃣",
            "8": "8️⃣",
            "9": "9️⃣",
            ".": "📍",
            "!": "⚠️",
            "?": "❔",
        }
        self.REVERSE_CIPHER = {v: k for k, v in self.EMOJI_CIPHER.items()}
        # Sort by length descending to handle multi-character emojis (like number blocks) correctly
        self.sorted_emojis = sorted(self.REVERSE_CIPHER.keys(), key=len, reverse=True)

    def encrypt(self, text):
        text = text.lower()
        return "".join(self.EMOJI_CIPHER.get(c, c) for c in text)

    def decrypt(self, text):
        decrypted = ""
        temp_text = text

        while temp_text:
            found = False
            for emoji in self.sorted_emojis:
                if temp_text.startswith(emoji):
                    decrypted += self.REVERSE_CIPHER[emoji]
                    temp_text = temp_text[len(emoji) :]
                    found = True
                    break
            if not found:
                decrypted += temp_text[0]
                temp_text = temp_text[1:]
        return decrypted
