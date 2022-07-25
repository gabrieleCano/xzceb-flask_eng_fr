"""
Python Final Project by Gabriele Cano
"""
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

def init_translator():
    """
    initializing the translator service
    """
    load_dotenv()
    apikey = os.environ['apikey']
    url = os.environ['url']
    local_authenticator = IAMAuthenticator(apikey)
    translator_service = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=local_authenticator
    )
    translator_service.set_service_url(url)

    return translator_service

LANGUAGE_TRANSLATOR = init_translator()

def english_to_french(english_text):
    """
    Translate from English to French
    """
    result = get_translation('en-fr',english_text)
    return manage_result(result)

def french_to_english(french_text):
    """
    Translate from French to English
    """
    result = get_translation('fr-en',french_text)
    return manage_result(result)

def get_translation(translator, text):
    """
    Extract the translated text from Watson response
    """
    success = False

    if text is not None and isinstance(text, str) and len(text) > 0:
        result = translate(translator, text)
        success = result[0]
    else:
        return {"status" : 400,
        "result" : "You have entered an empty text or a number. Please retry."}

    if success:
        result_contains_translations = len(result[1]) > 0 and 'translations' in (result[1])
        if result_contains_translations:
            translations = result[1]['translations']
            translations_contains_translation = (len(translations) > 0 and
            'translation' in (translations[0]))
            if translations_contains_translation:
                translation = translations[0]['translation']
                translation_is_not_empty = len(translation) > 0
                if translation_is_not_empty:
                    successful_translation = translation.casefold() != text.casefold()
                    if successful_translation:
                        return {"status" : 200, "result" : translation}
                    return {"status" : 400,
                    "result" : 'Sorry, I can\'t find a translation for the text: ' + text}
    return {"status" : 500, "result" : "Error"}

def translate(translator, text):
    """
    Translate the textToTranslate with the translator
    """
    try:
        if LANGUAGE_TRANSLATOR is None:
            return (False, "Can not initialize translator service.")
        return (True, LANGUAGE_TRANSLATOR.translate(
            text=text,
            model_id=translator).get_result())
    except ApiException as ex:
        return (False, "Method failed with status code " + str(ex.code) +
                ": " + ex.message, ex.code)

def manage_result(result):
    """
    Manage the result
    """
    manage_status = {
        200 : ('OK', result['result']),
        400 : ('Bad request',result['result']),
        500 : ('Error', 'Sorry, but something went wrong. Please retry later.')
        }
    return manage_status[result['status']][1]
