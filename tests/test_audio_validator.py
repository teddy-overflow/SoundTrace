from soundtrace.services.audio_validator import AudioValidator


def test_valid_audio_file(tmp_path):
    audio_file = tmp_path / "song.mp3"
    audio_file.touch()

    validator = AudioValidator()
    is_valid, message = validator.validate(str(audio_file))

    assert is_valid is True
    assert message == "Файл прошёл проверку."


def test_file_does_not_exist(tmp_path):
    audio_file = tmp_path / "missing.mp3"

    validator = AudioValidator()
    is_valid, message = validator.validate(str(audio_file))

    assert is_valid is False
    assert message == "Файл не найден."


def test_unsupported_format(tmp_path):
    text_file = tmp_path / "document.txt"
    text_file.touch()

    validator = AudioValidator()
    is_valid, message = validator.validate(str(text_file))

    assert is_valid is False
    assert message == "Неподдерживаемый формат аудиофайла."