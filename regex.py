# Yu-Gi-Fly Bot Telegram Bot
# Copyright (C) 2025 Alexelgt

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import re

# === Fly groups === #
FLY_GROUPS_REGEX = re.compile(r'pokemongoflymundial100ivs|intercambiospokemongoflymundial|pokemongoflymundial|ayudaflypokemongo|coordenadasunown|laketriopogo|offtopicflymundial|pvpflymundial|codigosamistadflymundial|pokemongofly100|pokemongoflychat|pokemongoflycoords|pokemongoflyraids|pgsharpop|pgsharpk|pgsharpapp|pgsharpofficials|pogoflyitaly2_0|pokemongohackspain|flygpspokemongo|unlimited100pokemon|pogopvpcoordinates|catch100|aerialsurveymisiones|aerialsurveypgo|pokemodespressoapk|top_pvpcoords|nexushub00|toppokego100iv|teamgorocketcoords', re.IGNORECASE)

# ==== Cards ==== #
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
        "regex": re.compile(r'contraataque|pika(chu)? fomenta el( uso del?)? fl[iy]', re.IGNORECASE)
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
        "regex": re.compile(r'\bprincipal\b|con la( cuenta)? principal juego legalmente|((hago|uso)( el)? fl[iy]|l[ao] uso) con la( cuenta)? (secundaria|pequeña)', re.IGNORECASE)
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
        "regex": re.compile(r'inocencia|tengo( un)? (iphone|ios)|tengo( un)? (iphone|ios),? ah[ií] no se puede instalar( el)? fl[iy]|no puede ser,? si uso iphone|yo es que uso iphone y no puedo tener fl[iy]|uso iphone y ah[ií] no se puede usar', re.IGNORECASE)
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
        "regex": re.compile(r'desconocimiento|no sab[ií] que no se (pod[ií]a|pudie(ra|se)) usar', re.IGNORECASE)
    },
    "COCHE_INVISIBLE": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACq2Bgq6hTOxNlJKZjHfyYRqLS0wVeIwACXwoAAl5_MFEUhEqE8qMCyB8E",
        "regex": re.compile(r'coche invisible|iba en coche,? por eso no me viste', re.IGNORECASE)
    },
    "COVID-19": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACq2Fgq6kGXk2dUY_qb_2lxb_hLum5KAAC3A0AAuG6MVG2SPk1Z1qvnR8E",
        "regex": re.compile(r'covid-?(19)?|cumplir con las restricciones|con covid-?(19)? (us[eé]|utilic[eé])( el)? fl[iy]|no (puedo|pod[ií]a) salir de casa', re.IGNORECASE)
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
        "regex": re.compile(r'libertad|cada uno (juega|que juegue) como quier[ae]|a ratos fl[iy] a ratos normal', re.IGNORECASE)
    },
    "AMISTAD": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACq2tgq6_KB866mwABls7hc1OyBrvAGJYAAosJAAJ61TlR3Hiv5JX7BRcfBA",
        "regex": re.compile(r'amistad|era la cuenta de una? amig|una? amig[ao] me dej[oó] (su (m[oó]vil|tel[eé]fono)|el suyo)', re.IGNORECASE)
    },
    "EL_QUE_TENGO_AQUI_COLGADO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACq2xgq6_2lqvzYxMDbgG5fZuz37z6fQACwAsAAm_yOVG7YHMWSYAlqB8E",
        "regex": re.compile(r'el que tengo aqu[ií] colgado|abogado', re.IGNORECASE)
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
        "regex": re.compile(r'inocente ilustrado|estoy en( un)? grupos? fl[iy],?(( solo para) informarme de las (novedades|noticias)| pero (no uso fl[iy]|solo para (que me hagan|hacer) intercambios))', re.IGNORECASE)
    },
    "MUERTE_DEL_MENSAJERO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACq3Bgq7Dn81jcEL4UOMMuPE2DOyCyuQACgQoAAj0GWFH1Jpv9EGzoaB8E",
        "regex": re.compile(r'muerte del mensajero|solo reenvi[eé] una imagen de otra persona', re.IGNORECASE)
    },
    "A_QUIEN_MADRUGA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACrB9grhpar42xUmBMkgLlFIKAz700hAACIwsAAgQkaVG0ITuDWIY_-R8E",
        "regex": re.compile(r'a quien madruga|dios le ayuda|me levanto muy (temprano|pronto)|no tengo tiempo|mi jornada empieza pronto', re.IGNORECASE)
    },
    "GAME_BOOSTER": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACrCBgrhqyDHUCOYEXo7bHy5SgBhqYVgACRQkAArAVaFFD9ISXq8c5YB8E",
        "regex": re.compile(r'game booster|no es un joystick', re.IGNORECASE)
    },
    "FRANKIE_EL_SOPLON": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACrCFgrhtvaS7tjn8KkKMGsMHKnLVUnQAClwoAAruAaVFf_WFhx6c_lx8E",
        "regex": re.compile(r'frankie el sopl[oó]n|te digo qui[eé]n( m[aá]s)? es fl[iy]', re.IGNORECASE)
    },
    "ENVIDIA_GALOPANTE": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACuWZg3ytSwaP14kqW03t0A5VsXg54KwAC-woAAmJtkFHnGxMVp7RkdSAE",
        "regex": re.compile(r'envidia galopante|ten[eé]is pesar por el bien ajeno', re.IGNORECASE)
    },
    "SOBRINO_MAGICO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACuWdg3yuzobMvcS4Z4ezjWHic4ftPxwACcQgAArIzkVER7qY32UmVKiAE",
        "regex": re.compile(r'sobrino m[aá]gico|le dej[eé] el (m[oó]vil|tel[eé]fono) a mi', re.IGNORECASE)
    },
    "MULTIPLE_PERSONALIDAD": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACuWpg3yxLs50esY6JXoqFGvJs-ou1ZAAC4goAAk35kVGUnmH50-EtjSAE",
        "regex": re.compile(r'm[uú]tiple personalidad|se han metido varias personas en mi m[oó]vil', re.IGNORECASE)
    },
    "REGALO_ENVENENADO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACuWtg3yzgFy0yzP7pn_jMwQ2Xls6YOgAC0wkAAkZgmFEpJZUPcznP6iAE",
        "regex": re.compile(r'regalo envenenado|me han regalado una cuenta que est([aá]|aba) baneada', re.IGNORECASE)
    },
    "ESPRINT_PERPETUO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACuWxg3y0rGkPgJBsitYA3s4nIhwo2IgAC5wgAAoZgoVEybFVX3oJZzSAE",
        "regex": re.compile(r'sprint perpetuo|me han baneado( solo) por tener demasiados (km|kil[oó]metros)', re.IGNORECASE)
    },
    "OLD_SCHOOL": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACuW1g3y2UxemhKYuqE79WS2-V_dBhcwACiAwAAo3CmFGEi74VMTubVCAE",
        "regex": re.compile(r'old school|mi cuenta es de 2016', re.IGNORECASE)
    },
    "HACKER_MALICIOSO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACuW5g3y3DOFb_hQcRmAFmk58s1SChuQACcgoAAiSnsVHqzq78jyNXUSAE",
        "regex": re.compile(r'hacker malicioso|se metieron en mi cuenta', re.IGNORECASE)
    },
    "NAVE_FALSA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACuW9g3y3vT0Fib8MYm50QBoa1mMs-NwACsAkAAnqQuFGqlZu8CkxFIiAE",
        "regex": re.compile(r'nave falsa|alguien ha colocado ese icono en mi juego', re.IGNORECASE)
    },
    "PA_HACERME_EL_CHULO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACuXBg3y4zE8FFkZB3a76izmQzpLaJMAACghcAAtFwuVE3GdIwsaeJxSAE",
        "regex": re.compile(r'hacerme el chulo|lo instal[eé] para presumir', re.IGNORECASE)
    },
    "ERA_BROMI": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACuXFg3y6V8VOKUeEa5wuJZ8lDgTVPMgACgAoAAnS76VJNDQrbZQSmViAE",
        "regex": re.compile(r'era brom[ai]|la confesión( p[uú]blica) que hice fue ir[oó]nica', re.IGNORECASE)
    },
    "YA_TENGO_UNA_EDAD": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACuXJg3y7eomAbA4FE7GOL1jfkGlzhUAACIAsAAua36VJApSJwwSP6iiAE",
        "regex": re.compile(r'ya tengo una edad|tengo muchos años como para ponerme a hacer trampas', re.IGNORECASE)
    },
    "PAULO_COELHO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACuXNg3y8VQfcBxrRUjVQL1PjRaRZKygACAQwAAonH6FKfU3zCSPqPxiAE",
        "regex": re.compile(r'paulo coelho|lo importante es estar feliz con lo que hagas', re.IGNORECASE)
    },
    "DERROCHADOR": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACvp5hFP6Kx1rM06GSVAfyQpuhfD-K4AAC9AsAAoNuoVDINRFVEtkAAUggBA",
        "regex": re.compile(r'derrochador|dinero', re.IGNORECASE)
    },
    "UNILINGUE": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACvp9hFP7ZI75hdTTYb5EWp4nC96TeJQACLwoAAmHZqVCiQjof7ZoaiiAE",
        "regex": re.compile(r'uniling[uü]e|pgsharp|españ(a|ol)', re.IGNORECASE)
    },
    "NOS_TIENEN_MANIA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACvqFhFP_von2CY1Cl5x6Jsx5iLQRDrwAC-wkAAkFIqFCQklDzk7rRciAE",
        "regex": re.compile(r'\bman[ií]a\b|temas personales|baneado del boo?t', re.IGNORECASE)
    },
    "COMPARTIR_ES_VIVIR": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACvqJhFQABDCyIkrC0biGbwsxYH4WE77QAAsAIAAK15KlQKYsKJWEqNW8gBA",
        "regex": re.compile(r'compartir|compartir es vivir', re.IGNORECASE)
    },
    "VICTIMA_DEL_SISTEMA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACvqRhFQFaP-MMGzcH_s6vo18exoHUxAACRQsAAnvYqVAjUIxcIR5pxiAE",
        "regex": re.compile(r'v[ií]ctima del sistema|grupo baneado|bane[oó] a( mi|l) grupo', re.IGNORECASE)
    },
    "INFILTRADO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACvqdhFQHUvIkMeXe0g4a3E9dqRVMX2QACcwsAAh9eoVBfwb4UKsQKpCAE",
        "regex": re.compile(r'infiltrado|reportar a otros', re.IGNORECASE)
    },
    "MONTAÑA_VA_A_MAHOMA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACvqhhFQILG72ZrVg3ihR46Y9RucUF1AAC3AwAAqgOqFBIFFsesauuQSAE",
        "regex": re.compile(r'montaña va a mahoma|incienso', re.IGNORECASE)
    },
    "EL_PODER_DE_LA_AMISTAD": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACvqphFQKCQ_7RyXq1ECEh_WUy54kT9wACugsAAmeyqFD89DdKevBqvCAE",
        "regex": re.compile(r'amistad|amigo', re.IGNORECASE)
    },
    "MIGUEL_BOTSE": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACvqthFQL8XBMYqJbWM4e-QXwvWK28SAAC7AkAAtJWqVCVYoAyZbJGMSAE",
        "regex": re.compile(r'boo?ts[eé]|contagi(arno|o)', re.IGNORECASE)
    },
    "CONTROL_PARENTAL": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACvqxhFQOPLvQgPjzVeO562bxHaLCt8wACeAsAAv-ZqVBEctTil5lbOyAE",
        "regex": re.compile(r'control parental|monitorizado', re.IGNORECASE)
    },
    "SIEMPRE_HUBO_CLASES": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACvq1hFQPQ0HzG4V0SI-t7wzqbJSHEhwAC_QkAAoM2qVAFHJU2tD3xAiAE",
        "regex": re.compile(r'siempre hubo clases|no se les? banea', re.IGNORECASE)
    },
    "HEROE_SIN_KAPPA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACvq5hFQQCtTioo2aB1k__UZBNisez2QACZAoAAsudqVCDd9DtBhB61SAE",
        "regex": re.compile(r'h[eé]roe|(tumbar|tirar) (gym|gimnasio)', re.IGNORECASE)
    },
    "ENTRE_LA_ESPADA_Y_LA_PARED": {
        "sticker_id": "CAACAgQAAx0CR9kKNwACxz1hOep4MU8AAQ1WeUibWy-NEmI8DIcAAi4MAAJaaclR3S9eNv_YIm8gBA",
        "regex": re.compile(r'\bespadas?\b|\bpared(es)?\b|sobreviv|supervivencia|\bvida\b', re.IGNORECASE)
    },
    "DISCIPULO_ENTREGADO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC0IRhxFXRkFCX_tc_1BZQ4oqMt6CtugACaQsAAg7u-FAbDvLMy5HZLSME",
        "regex": re.compile(r'disc[ií]pul|estudi', re.IGNORECASE)
    },
    "SMI": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC0IVhxFcUOYbuMsnqbMbxq-AwAgxFawACUgoAAgvLAVEAAW2wC3JF6rcjBA",
        "regex": re.compile(r'smi|sueldo|\bpases?\b', re.IGNORECASE)
    },
    "SECRETO_A_VOCES": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC0IZhxFglW6W4XXdoHFBakqvr9rJXCwACJgsAAoGFAAFRSScAARQzV6j0IwQ",
        "regex": re.compile(r'secreto|entre t[uú] y yo|entre nosotros', re.IGNORECASE)
    },
    "REY_SIN_CORONA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC0IdhxFhesr8jFehts01_UjjFbLY71wACcwkAAtFW-VB-_HWxnU5EmSME",
        "regex": re.compile(r'\brey\b|\breina\b|\badmin|no (estar|tener) ban', re.IGNORECASE)
    },
    "CHIVO_EXPIATORIO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC0IhhxFi5v8ywENVf2EOQF8ByO7KBAQAC8AwAAhIoAVFUhAABjFboJ0ojBA",
        "regex": re.compile(r'chivo expiatorio|(m[oó]vil|tel[eé]fono|dispositivo) (viejo|antiguo)', re.IGNORECASE)
    },
    "WORKAHOLIC": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC0IlhxFko7bGiRW0LOT4vnknfQaFATwACQAoAAhhdAVGjkCEPZTyUjiME",
        "regex": re.compile(r'workaholic|trabaj(o|ar?)', re.IGNORECASE)
    },
    "TARIFA_INSUFICIENTE": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC0IphxFmA2CaMltd_3sdd40au3Lm9TwAC6wsAAmEb-VBS0RQLWgmELSME",
        "regex": re.compile(r'tarifa|datos', re.IGNORECASE)
    },
    "PLAN_B": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC0IthxFmw0l2CnoReVqRvPp7vzywnBwACYg0AAl5L-FAkCzmZJdoJHiME",
        "regex": re.compile(r'plan b|pobre|datos', re.IGNORECASE)
    },
    "JUMPER": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC0IxhxFnb5PwX8k6S5F5BlruFoaXrKAACYAoAAiglAAFRulGd0u9GN7cjBA",
        "regex": re.compile(r'jumper|saltar|salto|coger|volver', re.IGNORECASE)
    },
    "TU_FLY_DE_CONFIANZA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC0I1hxFoVI0fCcoYukVLY9NNgK7sqmQACrwwAAvgkaVHWjPH7-9dveSME",
        "regex": re.compile(r'confi(anza|ar|o)', re.IGNORECASE)
    },
    "PACIENTE_CERO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC4KViyw11ep4SsPsq2UplxEGiua2XFQACsAwAAnNtGFJT3vHD0Bs4likE",
        "regex": re.compile(r'paciente (cero|0)|pesad[ao]|imposible jugar', re.IGNORECASE)
    },
    "ESTABILIZADOR_GPS": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC4Khiyw4Xc5iVpseVn_fsF3NZtPnJvgACHRAAAjnRGFIdoipts00xJikE",
        "regex": re.compile(r'gps|se le pira', re.IGNORECASE)
    },
    "EPILEPSIA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC4Kliyw5uwM4MRSHjYJSTv0tJUiZh_QACqwwAAvBkGFKPn-3Z5ezMFikE",
        "regex": re.compile(r'epilepsia|epil[eé]ptico', re.IGNORECASE)
    },
    "CON_LA_IGLESIA_HEMOS_TOPADO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC4Kpiyw6j5gjq4TNntaLk75Q7yPjATQACjA0AAjlGIFLFiB_RWflKyCkE",
        "regex": re.compile(r'iglesia|desconocid[ao]', re.IGNORECASE)
    },
    "PIEDAD": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC4Ktiyw8EFvmL-T-2HZy3ykseDJVZ2AACWQoAAsf4GFKJDvvwXI_ZIikE",
        "regex": re.compile(r'piedad', re.IGNORECASE)
    },
    "AMENAZA_CONFUSA": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC4Kxiyw8vohsRkWvv46gq-xm1N8rvqwACjQ0AAuySGFI-6VTDuXR7QSkE",
        "regex": re.compile(r'amenaza|instalar', re.IGNORECASE)
    },
    "ESPIRITU_NAVIDEÑO": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC4K5iyw_VPc2tR006uUZBRBoAAUkrvrwAAtEPAAKjvRlS91mBptbxU5spBA",
        "regex": re.compile(r'esp[ií]ritu navideño', re.IGNORECASE)
    },
    "ESTATUTOS": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC4K9iyxAFQM0He2wJqj1SYc4FJ_RpEAAC8woAAjLAIFLHCfKjLgpkOCkE",
        "regex": re.compile(r'estatuto|lucro', re.IGNORECASE)
    },
    "TIRANDO_DE_CONTACTOS": {
        "sticker_id": "CAACAgQAAx0CR9kKNwAC4LBiyxA5L3fbjJquQQzfx2VsHBp3OgAC5gwAAjpBGFIGwA5OqUbwNykE",
        "regex": re.compile(r'contacto|confianza', re.IGNORECASE)
    },
    "LA_EX": {
        "sticker_id": "CAACAgQAAxkBAANsaInDoTQMVGgFNR-hdfLMnGOG-JQAAucaAALWu1BQorM83Yqpb5M2BA",
        "regex": re.compile(r'\bex\b', re.IGNORECASE)
    },
    "FLY_EXPANSION": {
        "sticker_id": "CAACAgQAAxkBAANuaInDp7qoh0AxdouM2RhjN2HN0q0AAkYZAAKFUVBQVNYSpT6ft6I2BA",
        "regex": re.compile(r'fly expansion|big bang|siempre ha habido fly', re.IGNORECASE)
    },
}

all_cards_regex_text = "|".join(
    [card_value["regex"].pattern for card_value in cards_info.values()])

CARDS_TEXT_REGEX = re.compile(all_cards_regex_text, re.IGNORECASE)
# == Cards == #

# ==== Animations ==== #
animations_info = {
    "NAZI_WALKER": {
        "animation_id": "CgACAgQAAx0CR9kKNwACypxhdbvZGu9VoMqm5UPXdn8o5GqyXAACSgEAArnhmVOk22WpWiz84yEE",
        "regex": re.compile(r'\bnazi(walker)?(s)?\b|grupo de reportes', re.IGNORECASE)
    },
    "POCO_ME_PARECE": {
        "animation_id": "CgACAgQAAx0CR9kKNwAC0MVhx4TjMJi4AAEOSf5rbOKbpIArmdIAAgkLAAJZ3jhSIhuVn6minn4jBA",
        "regex": re.compile(r'poco me parece|[1-9]\d{2,} ?(€|\$|£|pavos)', re.IGNORECASE)
    },
    "ESPAÑITA": {
        "animation_id": "CgACAgQAAx0CR9kKNwAC0e5h0FoQbXduHm63E4lUntmQ2uSkJwACMgIAAjvs3FIty-uxlI8iLyME",
        "regex": re.compile(r'españita', re.IGNORECASE)
    },
}

photos_info = {
    "IGREJA": {
        "photo_name": "igreja.jpeg",
        "output_text": "Igreja",
        "regex": re.compile(r'\bpois+\b|\bigreja\b', re.IGNORECASE)
    },
}

all_animations_photos_regex_text = "|".join([animation_value["regex"].pattern for animation_value in animations_info.values()] + [
                                            photo_value["regex"].pattern for photo_value in photos_info.values()])

ANIMATION_PHOTOS_TEXT_REGEX = re.compile(
    all_animations_photos_regex_text, re.IGNORECASE)
# == Animations == #
