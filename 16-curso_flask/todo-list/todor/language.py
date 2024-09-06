from language import es, en
#for change language
def get_language(lang):
  if lang == "es":
    return es.messages
  elif lang == "en":
    return en.messages
  else:
    return es.messages