from pathlib import Path


class AudioValidator:
    """Проверяет аудиофайлы перед обработкой."""

    SUPPORTED_FORMATS = {
        ".mp3",
        ".wav",
        ".flac",
        ".ogg",
        ".m4a",
    }

    def validate(self, file_path: str) -> tuple[bool, str]:
        """Проверяет существование файла и его формат."""

        path = Path(file_path)

        if not path.exists():
            return False, "Файл не найден."

        if not path.is_file():
            return False, "Указанный путь не является файлом."

        if path.suffix.lower() not in self.SUPPORTED_FORMATS:
            return False, "Неподдерживаемый формат аудиофайла."

        return True, "Файл прошёл проверку."