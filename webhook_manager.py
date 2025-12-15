# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------------------
 DISCORD WEBHOOK MULTITOOL - V.1.0
------------------------------------------------------------------------------
 Autor:      Carliyo
 Fecha:      2025
 Descripción: A professional Python CLI tool to manage, analyse, and audit Discord Webhooks. Built for educational purposes.
 Github:     https://github.com/qpbo/A-Simple-Discord-Webhook-Manager
------------------------------------------------------------------------------
"""

import os
import sys
import json
import time
import requests
import base64
from datetime import datetime, timezone
from typing import Dict, List, Any

# Intentar importar colorama para estética, si no, definir clases vacías
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class Fore:
        CYAN = GREEN = RED = YELLOW = WHITE = RESET = ""
    class Style:
        BRIGHT = RESET_ALL = ""

# --- CONFIG ---
VERSION = "1.0.0"
DEV = "Carliyo"
REPO = "https://github.com/qpbo/A-Simple-Discord-Webhook-Manager"

# --- CONFIGURACIÓN VISUAL ---
BANNER = f"""
{Fore.CYAN}{Style.BRIGHT}
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                            {Fore.WHITE}MULTITOOL V.1.0
                            {Fore.YELLOW}By: Carliyo
{Style.RESET_ALL}"""

# --- CLASE GESTORA (Backend) ---
class DiscordWebhookManager:
    def __init__(self, url: str):
        self.url = url.strip()
        self.session = requests.Session()

    def validate_url(self) -> bool:
        return "discord.com/api/webhooks" in self.url or "discordapp.com/api/webhooks" in self.url

    def get_info(self) -> Dict[str, Any]:
        try:
            r = self.session.get(self.url)
            if r.status_code == 200:
                data = r.json()
                # Calcular fecha creación
                snowflake = int(data['id'])
                timestamp = ((snowflake >> 22) + 1420070400000) / 1000
                date = datetime.fromtimestamp(timestamp, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                
                return {
                    "valid": True,
                    "data": data,
                    "created_at": date,
                    "type": "Bot" if data.get("type") == 1 else "Webhook",
                    "avatar": f"https://cdn.discordapp.com/avatars/{data['id']}/{data['avatar']}.png" if data.get('avatar') else "N/A"
                }
            return {"valid": False, "code": r.status_code}
        except Exception as e:
            return {"valid": False, "error": str(e)}

    def delete(self) -> bool:
        try:
            r = self.session.delete(self.url)
            return r.status_code == 204
        except:
            return False

    def send_message(self, content=None, embeds=None) -> bool:
        payload = {}
        if content: payload["content"] = content
        if embeds: payload["embeds"] = embeds
        
        try:
            r = self.session.post(self.url, json=payload)
            if r.status_code == 204: return True
            if r.status_code == 429: 
                print(f"{Fore.YELLOW}[!] Rate Limit detectado.{Fore.RESET}")
            return False
        except:
            return False

    def modify(self, name=None, avatar_url=None) -> bool:
        payload = {}
        if name: payload['name'] = name
        if avatar_url: payload['avatar'] = avatar_url
        
        try:
            r = self.session.patch(self.url, json=payload)
            return r.status_code == 200
        except:
            return False

# --- UTILS VISUALES ---
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_log(type_log, message):
    if type_log == "success":
        print(f"{Fore.GREEN}[+] ÉXITO: {Fore.WHITE}{message}")
    elif type_log == "error":
        print(f"{Fore.RED}[!] ERROR: {Fore.WHITE}{message}")
    elif type_log == "info":
        print(f"{Fore.CYAN}[i] INFO: {Fore.WHITE}{message}")
    elif type_log == "input":
        return input(f"{Fore.YELLOW}[?] {message}: {Fore.RESET}")

def pause():
    print(f"\n{Fore.LIGHTBLACK_EX}Presiona Enter para continuar...{Fore.RESET}")
    input()

# --- FUNCIONES DEL MENÚ ---
def menu_info():
    url = print_log("input", "Ingresa la URL del Webhook")
    manager = DiscordWebhookManager(url)
    
    print(f"\n{Fore.YELLOW}Analyzando webhook...{Fore.RESET}")
    time.sleep(0.5) # Efecto dramático
    
    info = manager.get_info()
    
    if info['valid']:
        data = info['data']
        print(f"\n{Fore.CYAN}--- REPORTE DE WEBHOOK ---{Fore.RESET}")
        print(f" {Fore.GREEN}Estado:{Fore.WHITE}      ACTIVO")
        print(f" {Fore.GREEN}Nombre:{Fore.WHITE}      {data.get('name')}")
        print(f" {Fore.GREEN}ID:{Fore.WHITE}          {data.get('id')}")
        print(f" {Fore.GREEN}Guild ID:{Fore.WHITE}    {data.get('guild_id', 'Desconocido/DM')}")
        print(f" {Fore.GREEN}Channel ID:{Fore.WHITE}  {data.get('channel_id')}")
        print(f" {Fore.GREEN}Creado:{Fore.WHITE}      {info['created_at']}")
        print(f" {Fore.GREEN}Token:{Fore.WHITE}       {data.get('token')[:10]}... (Oculto)")
        print(f" {Fore.GREEN}Avatar:{Fore.WHITE}      {info['avatar']}")
    else:
        print_log("error", f"Webhook inválido o eliminado. Código: {info.get('code', 'Error')}")

def menu_send():
    url = print_log("input", "URL del Webhook")
    msg = print_log("input", "Mensaje a enviar")
    
    manager = DiscordWebhookManager(url)
    if manager.send_message(content=msg):
        print_log("success", "Mensaje enviado correctamente.")
    else:
        print_log("error", "No se pudo enviar el mensaje.")

def menu_spam():
    # Opción oculta/extra para pruebas de estrés
    url = print_log("input", "URL del Webhook")
    msg = print_log("input", "Mensaje de Spam")
    count = int(print_log("input", "Cantidad de mensajes"))
    
    manager = DiscordWebhookManager(url)
    print(f"{Fore.YELLOW}Iniciando secuencia... (Ctrl+C para parar)")
    
    try:
        for i in range(count):
            if manager.send_message(content=f"{msg}"):
                print(f"{Fore.GREEN}[+] Enviado #{i+1}")
            else:
                print(f"{Fore.RED}[-] Fallo #{i+1}")
            time.sleep(0.5) # Respetar rate limit básico
    except KeyboardInterrupt:
        print("\nDetenido por usuario.")

def menu_delete():
    url = print_log("input", "URL del Webhook a ELIMINAR")
    confirm = print_log("input", f"Escribe {Fore.RED}'DELETE'{Fore.YELLOW} para confirmar").strip()
    
    if confirm == "DELETE":
        manager = DiscordWebhookManager(url)
        if manager.delete():
            print_log("success", "Webhook eliminado permanentemente.")
        else:
            print_log("error", "No se pudo eliminar (o ya no existe).")
    else:
        print_log("error", "Cancelado.")

def action_credits():
    clear()
    print(BANNER)
    print(f"{Fore.CYAN}--- CREDITOS & INFO ---{Fore.RESET}\n")
    print(f" {Fore.GREEN}Dev:      {Fore.WHITE}{DEV}")
    print(f" {Fore.GREEN}Version:  {Fore.WHITE}{VERSION}")
    print(f" {Fore.GREEN}Github:   {Fore.WHITE}{REPO}")
    print(f" {Fore.GREEN}Year:     {Fore.WHITE}2025")
    print(f"\n{Fore.LIGHTBLACK_EX} Herramienta creada con fines educativos.")
    print(f" No me hago responsable del mal uso.")
    pause()

# --- BUCLE PRINCIPAL ---
def main():
    while True:
        clear()
        print(BANNER)
        print(f"{Fore.WHITE}Selecciona una operación:\n")
        print(f"{Fore.CYAN}[1] {Fore.WHITE}Obtener Info (Inspector)")
        print(f"{Fore.CYAN}[2] {Fore.WHITE}Enviar Mensaje Simple")
        print(f"{Fore.CYAN}[3] {Fore.WHITE}Spammer (Posible Rate-Limit si se abusa)")
        print(f"{Fore.CYAN}[4] {Fore.WHITE}Eliminar Webhook")
        print(f"{Fore.CYAN}[5] {Fore.WHITE}Creditos")
        print(f"{Fore.CYAN}[6] {Fore.WHITE}Salir")
        print(f"\n{Fore.CYAN}-----------------------------------")
        
        opcion = input(f"{Fore.YELLOW}root@carliyo's-webhook-tool:~# {Fore.RESET}")
        
        print() # Salto de línea
        
        if opcion == '1':
            menu_info()
        elif opcion == '2':
            menu_send()
        elif opcion == '3':
            menu_spam()
        elif opcion == '4':
            menu_delete()
        elif opcion == '5':
            action_credits()
        elif opcion == '6':
            print(f"{Fore.CYAN}Saliendo... Hasta luego.")
            sys.exit()
        else:
            print_log("error", "Opción no válida.")
            
        pause()

if __name__ == "__main__":
    main()