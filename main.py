from asyncio import events

import requests
from datetime import datetime

def get_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")
        return

    events = response.json()

    if not events:
        print("Nenhuma atividade encontrada.")
        return

    print(f"\nAtividades recentes de {username}:\n")

    for event in events[:10]:
        event_type = event.get("type", "Desconhecido")
        repo = event.get("repo", {}).get("name", "Desconhecido")
        created_at = format_date(event.get("created_at"))

        print(f"\n{event_type}")
        print(f"Repositório: {repo}")
        print(f"Data: {created_at}")

        payload = event.get("payload", {})

        if event_type == "PushEvent":
            commits = payload.get("commits", [])
            for commit in commits:
                print(f"   - {commit.get('message', 'Sem mensagem')}")

        elif event_type == "CreateEvent":
            print(f"Criou: {payload.get('ref_type', 'desconhecido')}")

        elif event_type == "IssuesEvent":
            print(f"Issue: {payload.get('action', 'desconhecido')}")

        elif event_type == "ForkEvent":
            print("Fork do repositório")

        print("-" * 20)


def format_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    return date_obj.strftime("%d/%m/%Y %H:%M")


if __name__ == "__main__":
    print("Visualizador de Atividade do GitHub\n")

    username = input("Digite o nome de usuário do GitHub: ")
    get_github_activity(username)