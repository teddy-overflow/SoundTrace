import math
import wave

from soundtrace.services.fingerprint_generator import FingerprintGenerator

def create_test_audio(file_path):
    """Создаёт WAV-файл с искусственным звуковым сигналом."""

    sample_rate = 44100
    duration = 10
    frequency = 440

    with wave.open(str(file_path), "wb") as audio_file:
        audio_file.setnchannels(1)
        audio_file.setsampwidth(2)
        audio_file.setframerate(sample_rate)

        audio_data = bytearray()

        for i in range(sample_rate * duration):
            sample = int(
                32767 * math.sin(
                    2 * math.pi * frequency * i / sample_rate
                )
            )

            audio_data.extend(sample.to_bytes(2, byteorder="little", signed=True))

        audio_file.writeframes(audio_data)

def test_generate_returns_fingerprint(tmp_path):
    """Проверяет создание акустического отпечатка из WAV-файла."""

    # Создаём путь к временному аудиофайлу.
    audio_file = tmp_path / "test.wav"

    # Генерируем искусственный WAV-файл.
    create_test_audio(audio_file)

    # Создаём генератор акустических отпечатков.
    generator = FingerprintGenerator()

    # Получаем длительность и акустический отпечаток.
    duration, fingerprint = generator.generate(str(audio_file))

    # Проверяем, что длительность положительная.
    assert duration > 0

    # Проверяем, что отпечаток является строкой.
    assert isinstance(fingerprint, str)

    # Проверяем, что отпечаток не пустой.
    assert len(fingerprint) > 0