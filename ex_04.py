import requests
from mongoengine import connect, Document, StringField, IntField, ListField, ReferenceField, DateTimeField

# Étape 2 : Créer une classe Student
class Student(Document):
    name = StringField()
    age = IntField()
    email = StringField()

# Étape 3 : Créer une classe Message
class Message(Document):
    content = StringField()
    date = DateTimeField()
    sender = ReferenceField(Student)

# Étape 4 : Créer une classe Channel
class Channel(Document):
    name = StringField()
    channel_id = StringField()

# Étape 5 : Créer une classe Chat
class Chat(Document):
    name = StringField()
    channels = ListField(ReferenceField(Channel))

# Étape 6 : Se connecter à MongoDB
connect('data-pool_j-4')

def get_channels_and_save_to_db(team_id):
    token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IjBTRjA0czBfWU9GeEQxRnVVYmR6clFrWUVtYUdhZEpFVVNlekhCdjFMeFUiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC85MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYvIiwiaWF0IjoxNjk0MTU4MTkwLCJuYmYiOjE2OTQxNTgxOTAsImV4cCI6MTY5NDI0NDg5MCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhVQUFBQVUwd3ZBcVp5eFl6MUdQTDF3QzJsMTgxNjllL0NSMXBCOWxyRDR3ZmFxNHpGUExacHRPNVNCa3l1S0h4dzNUVGU3MHJhbFY0VkdQWmxUYjRwS1lXUFREaytJUUhKTXJRUVp3RXkzVmxwdE04PSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggRXhwbG9yZXIiLCJhcHBpZCI6ImRlOGJjOGI1LWQ5ZjktNDhiMS1hOGFkLWI3NDhkYTcyNTA2NCIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiU2FhZG91bmkiLCJnaXZlbl9uYW1lIjoiSmFkZSIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjE2My41LjIzLjM4IiwibmFtZSI6IkphZGUgU2FhZG91bmkiLCJvaWQiOiI1ZWJjN2IwOS01YWJmLTQwNzEtODllMS0xM2E3NzI3NjVhMTgiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMTU1MjQzNTI3Ny0xNTk2NDk1Nzk1LTMwODk2MTM3MzEtNDc1NDUiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDFGQkQwMjc3QyIsInJoIjoiMC5BWFFBeXJRY2tHSzRLVUNUQnVYTkQyMmZoZ01BQUFBQUFBQUF3QUFBQUFBQUFBQjBBTTguIiwic2NwIjoiR3JvdXAuUmVhZC5BbGwgR3JvdXAuUmVhZFdyaXRlLkFsbCBwcm9maWxlIG9wZW5pZCBlbWFpbCBVc2VyLlJlYWQiLCJzaWduaW5fc3RhdGUiOlsia21zaSJdLCJzdWIiOiJIcjVBMGdwdzBpc2xnaWRPcXVoWWU4cFFwWU8wSWVfZjZhT3paTTFOU0ZVIiwidGVuYW50X3JlZ2lvbl9zY29wZSI6IkVVIiwidGlkIjoiOTAxY2I0Y2EtYjg2Mi00MDI5LTkzMDYtZTVjZDBmNmQ5Zjg2IiwidW5pcXVlX25hbWUiOiJqYWRlLnNhYWRvdW5pQGVwaXRlY2guZGlnaXRhbCIsInVwbiI6ImphZGUuc2FhZG91bmlAZXBpdGVjaC5kaWdpdGFsIiwidXRpIjoidXd1Tk1ScWNVMFNsVFN6ZFJqWjVBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYyI6WyJDUDEiXSwieG1zX3NzbSI6IjEiLCJ4bXNfc3QiOnsic3ViIjoiZDhJWkNPRnR6cm90WEtGUFNzWXlyam1IWmM0RUJ0eFUtV3BpMmdfVnZiSSJ9LCJ4bXNfdGNkdCI6MTQxNzgwNDg4NywieG1zX3RkYnIiOiJFVSJ9.f5TBlc5MaaxzQVQSgsdhem_1wnbuXM8x62QV1-OffX_fnkQQpmCL_elomF-ceKEi4tHmUX9pOEQxsO6AyDcb6lRO9q9y2dY9n0Gl2ZakPj_u_m2cxRQa0Z4_Eu1fOeiPvcATsicF-DA1G743iELyh29UJryfLUmmkTkhxOgmnApQGlCCEzQxBj7AsRYF7lMxONoqCKhTwyM10Sw6qONI8iSd2gkjuMVghiBl97JPAx-IkuprEHPl-4hoYacDAmB21A5tIti33lEllzGoOiFtJtheFxRfLUGcVZHO95ukazAXBhtah25jLp0i7mgxroU9hDpLIKnt5NcMzytPQldpkQ"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f"https://graph.microsoft.com/beta/teams/{team_id}/channels"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        channels_data = response.json()

        # Récupérez la liste des canaux
        channels = channels_data.get('value', [])
        
        for channel_data in channels:
            # Récupérez l'ID et le nom du canal
            channel_id = channel_data.get('id', '')
            channel_name = channel_data.get('displayName', '')

            # Créez une instance de la classe Channel et associez l'ID et le nom
            channel = Channel(name=channel_name, channel_id=channel_id)
            channel.save()  # Enregistrez le canal dans la base de données
            
            print(f"Canal enregistré - ID : {channel.channel_id}, Nom : {channel.name}")

    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête : {response.status_code}")

if __name__ == "__main__":
    team_id = '0f723f30-bd8c-4f25-954c-b4ee29143f25'  # Remplacez par l'ID de votre équipe
    get_channels_and_save_to_db(team_id)