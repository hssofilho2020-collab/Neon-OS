import flet as ft
from google import genai
import json, os, asyncio
import edge_tts

try:
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    HAS_ANDROID = True
except:
    HAS_ANDROID = False

client = genai.Client(api_key="AQ.Ab8RN6L1nP8EZklyUB84cFd2CEPouP8JqFjfF4FwgagxznN2w")

def carregar_programas():
    if os.path.exists("programas.json"):
        with open("programas.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

async def falar(texto):
    try:
        await edge_tts.Communicate(texto, voice="pt-BR-AntonioNeural").save("/tmp/neon.mp3")
    except:
        pass

def abrir_app(pacote):
    if not HAS_ANDROID: return False
    try:
        from jnius import autoclass
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        pm = PythonActivity.mActivity.getPackageManager()
        intent = pm.getLaunchIntentForPackage(pacote)
        if intent:
            PythonActivity.mActivity.startActivity(intent)
            return True
    except:
        pass
    return False

def main(page: ft.Page):
    page.title = "NEON OS"
    page.theme_mode = ft.ThemeMode.DARK
    PROGRAMAS = carregar_programas()
    chat = ft.ListView(expand=True, auto_scroll=True)
    entrada = ft.TextField(hint_text="Fala Chefe...", expand=True)

    async def btn_enviar(e):
        if not entrada.value: return
        cmd = entrada.value
        chat.controls.append(ft.Text(f"Chefe: {cmd}", weight="bold"))
        entrada.value = ""
        page.update()
        cmd_low = cmd.lower()
        for nome, info in PROGRAMAS.items():
            if any(c in cmd_low for c in info.get("comando", [])):
                chat.controls.append(ft.Text(f"NEON: Abrindo {nome}, Chefe!"))
                abrir_app(info["pacote"])
                page.update()
                return
        try:
            resp = client.models.generate_content(model="gemini-2.5-flash", contents=f"Você é a NEON 2.0, chama de Chefe, resposta curta: {cmd}").text
            chat.controls.append(ft.Text(f"NEON: {resp}"))
            await falar(resp)
        except Exception as ex:
            chat.controls.append(ft.Text(f"Erro: {ex}"))
        page.update()

    page.add(chat, ft.Row([entrada, ft.IconButton(ft.icons.SEND, on_click=btn_enviar)]))

ft.app(target=main)
