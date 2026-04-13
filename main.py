import requests
from datetime import datetime

def get_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    
    response = requests.get(url)

    if response.status_code != 200:
        print("Erro ao buscar dados. Verifique o usuário.")
        return

    events = response.json()

    if not events:
        print("Nenhuma atividade encontrada.")
        return

    print(f"\nAtividades recentes de {username}:\n")

    for event in events[:10]:  # Limite de eventos
        event_type = event["type"]
        repo = event["repo"]["name"]
        created_at = format_date(event["created_at"])

        print(f"{event_type}")
        print(f"Repositório: {repo}")
        print(f"Data: {created_at}")

        # Detalhes do evento
        for event in events[:10]:
            event_type = event.get("type", "Desconhecido")
            repo = event.get("repo", {}).get("name", "Desconhecido")
            created_at = format_date(event.get("created_at"))

            print(f"{event_type}")
            print(f"Repositório: {repo}")
            print(f"Data: {created_at}")

            payload = event.get("payload", {})

            if event_type == "PushEvent":
                commits = payload.get("commits", [])
                if commits:
                    print("Commits:")
                    for commit in commits:
                        print(f"   - {commit.get('message', 'Sem mensagem')}")
                else:
                    print("Nenhum commit disponível")

            elif event_type == "CreateEvent":
                print(f"Criou: {payload.get('ref_type', 'desconhecido')}")

            elif event_type == "IssuesEvent":
                print(f"Issue: {payload.get('action', 'desconhecido')}")

            elif event_type == "ForkEvent":
                print("Fork do repositório")

            print("-" * 10)


def format_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    return date_obj.strftime("%d/%m/%Y %H:%M")


if __name__ == "__main__":
    print("Visualizador de Atividade do GitHub\n")

    username = input("Digite o nome de usuário do GitHub: ")
    get_github_activity(username)