from google_trans_new.google_trans_new import google_translator

translator = google_translator()
Pronounce = translator.translate(
    'Malware', lang_src='en', lang_tgt='vi')
print(Pronounce)
