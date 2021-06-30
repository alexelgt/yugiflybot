import re

cards_info = {
    "NEGACION_PERPETUA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACqrlgq3DaAgbAMdlx-jBjFfBYuvJpWgACjwkAAoIUOFHGDP1O2sYXTR8E",
        "regex": re.compile(r'negaci[oó]n perpetua|no s[eé] de qu[eé] me est[aá]s hablando|no he hecho nada', re.IGNORECASE)
    },
    "DEMUESTRAMELO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACqrpgq3EEFC38-2JgYQYwqFxI621y3AACuwwAAptROVFhiYbhztK1tx8E",
        "regex": re.compile(r'demu[eé]stramelo|sin pruebas no hay delito|si no hay pruebas', re.IGNORECASE)
    },
    "NO_VOLVERA_A_OCURRIR": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACqvhgq4Y71rPyiHN3bz-1CyBV2potPAAC0goAAtGaMFHFpqoIlB3dAAEfBA",
        "regex": re.compile(r'no volver[aá] a ocurrir|un perdón invalida al instante cualquier baneo', re.IGNORECASE)
    },
    "CONTRAATAQUE": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACqwdgq4lUw1Pgc4i4Gs9qAxKyu4vbiQACWQsAAvOxOFHGxm0Px8dcdh8E",
        "regex": re.compile(r'contraataque|pika(chu)? fomenta el( uso de(l)?)? fl[iy]', re.IGNORECASE)
    },
    "CALCULADOR": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACqwlgq4uExqCsXtuO0pMrMxLNvj0m5QAClQoAAptFOFGEWrGFpFfsPh8E",
        "regex": re.compile(r'calculador|solo calculo( los)? iv|solo( lo)? (uso|utilizo)( el fl[iy])? para calcular( (los|el))? iv', re.IGNORECASE)
    },
    "PRIMERA_Y_ULTIMA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACqwpgq4utbMfkasinQ6_vE6W2AUuIAQACIBIAAlcPOVGjcfMCc1avsR8E",
        "regex": re.compile(r'primera y [uú]ltima|solo( lo)? (he usado|use)( el fl[iy])? una vez|solo una vez', re.IGNORECASE)
    },
    "LA_PRINCIPAL": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACqxZgq40hfk7HobhGfCtcRO5mNkeiwgACBgsAAm-aMFFhn4vTLjvNQR8E",
        "regex": re.compile(r'la principal|con la( cuenta)? principal juego legalmente|((hago|uso)( el)? fl[iy]|l[ao] uso) con la( cuenta)? (secundaria|pequeña)', re.IGNORECASE)
    },
    "LESION": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACqxdgq42psr5CYASCNlHfYzuI7ZjVhAACVgkAApnvMFH8Py4Z-5-V8B8E",
        "regex": re.compile(r'lesi[oó]n|tuve una lesi[oó]n', re.IGNORECASE)
    },
    "TIENDA_MALIGNA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACqxhgq48H0x1nupVov0Bja6_bNz3BCQACGgoAAmi3OVFkKs1YwKTI9x8E",
        "regex": re.compile(r'tienda maligna|ven[ií]a( ya)? instalado|(m[oó]vil|tel[eé]fono) a (reparar|arreglar)', re.IGNORECASE)
    },
    "INOCENCIA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACqqZgq2sYgYv0Zi_QZUYtw8bHCRDa0QACpQoAApRMMFHFaikae6k60h8E",
        "regex": re.compile(r'inocencia|tengo( un)? (iphone|ios)|tengo( un)? (iphone|ios)(,)? ah[ií] no se puede instalar( el)? fl[iy]|no puede ser(,)? si uso iphone|yo es que uso iphone y no puedo tener fl[iy]|uso iphone y ah[ií] no se puede usar', re.IGNORECASE)
    },
    "SOBRINO_MAGICO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACqzpgq5IL1xtBlWvROW6LMOWru79oqAACgQoAAik1OVGa_HLAufiS7R8E",
        "regex": re.compile(r'sobrino m[aá]gico|le dej[eé] el (m[oó]vil|tel[eé]fono) a mi', re.IGNORECASE)
    },
    "REGIONALES": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACqztgq5K37P7mQUbKWKCTGAYRMdO4kAAC3AsAAj7jOFG-5Ol3itNH6x8E",
        "regex": re.compile(r'regionales|solo capturo( los)? regionales|solo( lo)? (uso|utilizo)( el fl[iy])? para capturar( los)? regionales', re.IGNORECASE)
    },
    "BONDAD_INNATA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACqzxgq5NeCYAHhJOT-zL34hhnHuEMEQAC3goAAvUgOFGEWF3l7O-AWB8E",
        "regex": re.compile(r'bondad innata|soy( una)? buena persona', re.IGNORECASE)
    },
    "DERECHOS_HUMANOS": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACqz1gq5PNGYxMR-v0bdI6wvAD2QcumAACVgsAAvKMOVGxixc_kjwd9R8E",
        "regex": re.compile(r'derechos (humanos|fundamentales)', re.IGNORECASE)
    },
    "DESCONOCIMIENTO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACqz5gq5RTELlrlNRKpH9e-D0TKMVI4AACdQoAAl_yMVFpsdemqKHdJR8E",
        "regex": re.compile(r'desconocimiento|no sab[ií] que no se pod[ií]a usar', re.IGNORECASE)
    },
    "COCHE_INVISIBLE": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACq2Bgq6hTOxNlJKZjHfyYRqLS0wVeIwACXwoAAl5_MFEUhEqE8qMCyB8E",
        "regex": re.compile(r'coche invisible|iba en coche(,)? por eso no me viste', re.IGNORECASE)
    },
    "COVID-19": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACq2Fgq6kGXk2dUY_qb_2lxb_hLum5KAAC3A0AAuG6MVG2SPk1Z1qvnR8E",
        "regex": re.compile(r'covid(-)?(19)?|cumplir con las restricciones|con covid(-)?(19)? (us[eé]|utilic[eé])( el)? fl[iy]|no (puedo|pod[ií]a) salir de casa', re.IGNORECASE)
    },
    "HIPOCRESIA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACq2Jgq6mgi3tf1xf8OmdVb2tPhBX5nwACSQoAAg2QOFFvHUHdWF5ILx8E",
        "regex": re.compile(r'hipocres[ií]a|todo el mundo (usa|utiliza) fl[iy]', re.IGNORECASE)
    },
    "ALDEA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACq2lgq69TzpOzVblcaZxj9QABFr9Vd5kAAhkMAAKerjlR9PXkzqxlEJMfBA",
        "regex": re.compile(r'aldea|en mi pueblo no hay pok[eé]paradas', re.IGNORECASE)
    },
    "LIBERTAD": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACq2pgq6-Ws0EtdvUdM5AWVcvJZYNrSwACywgAAn8tOFGXj4TkLpw76B8E",
        "regex": re.compile(r'libertad|cada uno juega como quiere', re.IGNORECASE)
    },
    "AMISTAD": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACq2tgq6_KB866mwABls7hc1OyBrvAGJYAAosJAAJ61TlR3Hiv5JX7BRcfBA",
        "regex": re.compile(r'amistad|era la cuenta de un(a)? amig|un(a)? amig[ao] me dej[oó] (su (m[oó]vil|tel[eé]fono)|el suyo)', re.IGNORECASE)
    },
    "EL_QUE_TENGO_AQUI_COLGADO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACq2xgq6_2lqvzYxMDbgG5fZuz37z6fQACwAsAAm_yOVG7YHMWSYAlqB8E",
        "regex": re.compile(r'el que tengo aqu[ií] colgado|voy a poner este tema en manos de mi abogado', re.IGNORECASE)
    },
    "KINDER_SORPRESA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACq21gq7ArDoBYZKcEvo5GVGTEvItzCQACkAoAArBvWFHx-MMChLesjh8E",
        "regex": re.compile(r'kinder sorpresa|me sali[oó] el regional de un huevo', re.IGNORECASE)
    },
    "PRODUCTO_NACIONAL": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACq25gq7BzJqIrnC8Blz5dFHFkcvlHNAAC3wkAAmNUUFFFaIbWr6p91R8E",
        "regex": re.compile(r'producto nacional|solo lo uso por mi (barrio|zona)', re.IGNORECASE)
    },
    "INOCENTE_ILUSTRADO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACq29gq7Ch-rEX5ZgKcNNgrwLXQP8HuAAC2AcAAg3WWVGasMkJtwjG-h8E",
        "regex": re.compile(r'inocente ilustrado|estoy en( un)? grupo(s)? fl[iy](,)?(( solo para) informarme de las (novedades|noticias)| pero (no uso fl[iy]|solo para (que me hagan|hacer) intercambios))', re.IGNORECASE)
    },
    "MUERTE_DEL_MENSAJERO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACq3Bgq7Dn81jcEL4UOMMuPE2DOyCyuQACgQoAAj0GWFH1Jpv9EGzoaB8E",
        "regex": re.compile(r'muerte del mensajero|solo reenvi[eé] una imagen de otra persona', re.IGNORECASE)
    },
    "A_QUIEN_MADRUGA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACrB9grhpar42xUmBMkgLlFIKAz700hAACIwsAAgQkaVG0ITuDWIY_-R8E",
        "regex": re.compile(r'a quien madruga|dios le ayuda|me levanto muy (temprano|pronto)|no tengo tiempo', re.IGNORECASE)
    },
    "GAME_BOOSTER": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACrCBgrhqyDHUCOYEXo7bHy5SgBhqYVgACRQkAArAVaFFD9ISXq8c5YB8E",
        "regex": re.compile(r'game booster|no es un joystick', re.IGNORECASE)
    },
    "FRANKIE_EL_SOPLON": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACrCFgrhtvaS7tjn8KkKMGsMHKnLVUnQAClwoAAruAaVFf_WFhx6c_lx8E",
        "regex": re.compile(r'frankie el sopl[oó]n|te digo qui[eé]n( m[aá]s)? es fl[iy]', re.IGNORECASE)
    },
}

all_regex_text = ""

for card in cards_info:
    all_regex_text += "{}|".format(cards_info[card]["regex"].pattern)

all_regex_text = all_regex_text.rstrip("|")

CHECK_TEXT_REGEX = re.compile(all_regex_text, re.IGNORECASE)
