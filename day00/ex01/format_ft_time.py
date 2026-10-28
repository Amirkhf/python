import time
import datetime

# recupere les secondes ecoulees depuis le 1er janvier 1970
t = time.time()

# f-string pour formater la phrase
result = (f"Seconds since January 1, 1970: {t:,.4f} "
          f"or {t:.2e} in scientific notation")
# recupere la date du jour
now = datetime.datetime.now()
# affiche le resultat
print(result)
# strftime pour formater la date
print(now.strftime("%b %d %Y"))

# https://sites.google.com/site/pythonpasapas/methodes/f-string