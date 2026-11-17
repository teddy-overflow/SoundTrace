from soundtrace.services.audio_validator import AudioValidator


def test_valid_audio_file(tmp_path):
    """Проверяет, что непустой файл с поддерживаемым расширением проходит проверку."""

    # Создаём тестовый MP3-файл во временной папке.
    audio_file = tmp_path / "song.mp3"

    # Записываем несколько байтов, чтобы файл не был пустым.
    audio_file.write_bytes(b"fake audio data")

    # Создаём объект валидатора и проверяем файл.
    validator = AudioValidator()
    is_valid, message = validator.validate(str(audio_file))

    # Проверяем, что файл признан допустимым.
    assert is_valid is True
    assert message == "Файл прошёл проверку."


def test_file_does_not_exist(tmp_path):
    """Проверяет обработку пути к несуществующему файлу."""

    # Указываем путь к файлу, который ещё не создан.
    audio_file = tmp_path / "missing.mp3"

    validator = AudioValidator()
    is_valid, message = validator.validate(str(audio_file))

    # Валидатор должен сообщить, что файл не найден.
    assert is_valid is False
    assert message == "Файл не найден."


def test_unsupported_format(tmp_path):
    """Проверяет, что файлы с неподдерживаемым расширением отклоняются."""

    # Создаём файл с расширением .txt вместо аудиоформата.
    text_file = tmp_path / "document.txt"

    # Записываем данные, чтобы проверка пустого файла не сработала раньше.
    text_file.write_bytes(b"some text")

    validator = AudioValidator()
    is_valid, message = validator.validate(str(text_file))

    # Валидатор должен отклонить файл из-за неподдерживаемого расширения.
    assert is_valid is False
    assert message == "Неподдерживаемый формат аудиофайла."


def test_empty_audio_file(tmp_path):
    """Проверяет, что пустые аудиофайлы отклоняются."""

    # Создаём MP3-файл, но ничего в него не записываем.
    audio_file = tmp_path / "empty.mp3"
    audio_file.touch()

    validator = AudioValidator()
    is_valid, message = validator.validate(str(audio_file))

    # Валидатор должен обнаружить, что размер файла равен нулю.
    assert is_valid is False
    assert message == "Файл пуст."