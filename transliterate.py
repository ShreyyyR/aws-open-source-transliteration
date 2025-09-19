# Option 1: Open Source Transliteration
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def en_to_kn_open_source(text: str) -> str:
    return transliterate(text, sanscript.ITRANS, sanscript.KANNADA)

# Option 2: AWS Translate
import boto3

def en_to_kn_aws(text: str) -> str:
    client = boto3.client("translate", region_name="ap-south-1")
    response = client.translate_text(
        Text=text,
        SourceLanguageCode="en",
        TargetLanguageCode="kn"
    )
    return response["TranslatedText"]

