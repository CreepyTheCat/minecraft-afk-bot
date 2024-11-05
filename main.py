from pycraft import Client
import time

# Connect to the Minecraft server
def connect_to_server(host, port, username):
    client = Client(host, port, username)
    client.connect()
    return client

# Perform a simple AFK action (e.g., move slightly)
def afk_action(client):
    while True:
        client.player.set_motion(0, 0, 1)  # Move forward
        time.sleep(1)                      # Move for 1 second
        client.player.set_motion(0, 0, 0)  # Stop moving
        time.sleep(1)                      # Wait for 1 second
        client.player.set_motion(0, 0, -1) # Move backward
        time.sleep(1)                      # Move for 1 second
        client.player.set_motion(0, 0, 0)  # Stop moving
        time.sleep(1)                      # Wait for 1 second

# Main function to run the bot
def main():
    host = 'localhost'  # Change to your server's IP if needed
    port = 25565        # Default Minecraft port
    username = 'AFKBot' # Username for the bot

    client = connect_to_server(host, port, username)

    time.sleep(5)  # Wait for a few seconds to switch to Minecraft

    try:
        afk_action(client)  # Start performing AFK actions
    except KeyboardInterrupt:
        print("Stopping the bot...")
    finally:
        client.disconnect()  # Disconnect from the server

if __name__ == "__main__":
    main()
