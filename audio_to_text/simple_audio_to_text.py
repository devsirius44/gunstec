import openai

openai.api_key = "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"
mp3_file = "audio_snippet.mp3"

def openai_whisper_transcribe(mp3_file):
    snippet_file = open(mp3_file, "rb")
    snippet_transcription = openai.audio.transcriptions.create(model="whisper-1", file=snippet_file, response_format="text")
    print("==>", snippet_transcription)
    return snippet_transcription

meeting_content = openai_whisper_transcribe(mp3_file)
print(meeting_content)

