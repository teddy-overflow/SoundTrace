import os
from pathlib import Path

import acoustid


class FingerprintGenerator:
    """Создаёт акустические отпечатки аудиофайлов."""

    def __init__(self):
        # Определяем путь к fpcalc.exe относительно корня проекта.
        self.fpcalc_path = (
            Path(__file__).resolve().parents[3]
            / "tools"
            / "fpcalc.exe"
        )

        # Проверяем, что программа Chromaprint действительно находится по этому пути.
        if not self.fpcalc_path.is_file():
            raise FileNotFoundError(
                f"Не удалось найти fpcalc.exe: {self.fpcalc_path}"
            )

        # Сообщаем pyacoustid, где находится исполняемый файл Chromaprint.
        os.environ["FPCALC"] = str(self.fpcalc_path)

    def generate(self, file_path: str) -> tuple[float, str]:
        """Создаёт отпечаток аудиофайла и возвращает его длительность и отпечаток."""

        # Передаём аудиофайл в pyacoustid.
        # force_fpcalc=True заставляет использовать именно наш fpcalc.exe.
        duration, fingerprint = acoustid.fingerprint_file(
            file_path,
            force_fpcalc=True,
        )

        # Преобразуем отпечаток из байтов в обычную строку.
        if isinstance(fingerprint, bytes):
            fingerprint = fingerprint.decode("utf-8")

        return duration, fingerprint