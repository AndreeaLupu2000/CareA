from google.cloud import texttospeech

from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(
    'C:\\Users\\40732\\Downloads\\tribal-marker-417122-f025dc88eca1.json'
)


def text_to_speech_save(text, output_file):
    # Initialize the Text-to-Speech client
    tts_client = texttospeech.TextToSpeechClient(credentials=credentials)
    print(tts_client.list_voices())

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code and the SSML voice gender
    voice = texttospeech.VoiceSelectionParams(
        language_code='en-US',
        name='en-US-Studio-O',
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=1.5,
    )

    # Perform the Text-to-Speech request on the text input with the selected voice parameters and audio file type
    response = tts_client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Save the audio content to a file
    with open(output_file, 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print(f"Audio content written to file {output_file}")

text_to_speech_save(f"I heard: Where is the hospital cafeteria?", "demo_question.mp3")
# Usage example
text_to_speech_save(f"Exit the room to the right, go to the elevator and take it to the ground floor. "
                    f"The cafeteria will be right infront of you.",  "demo.mp3")
