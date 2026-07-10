class Song:
    def __init__(self, name):
        self.name = name
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    # Add song at the end
    def add_song(self, song_name):
        new_song = Song(song_name)

        if self.head is None:
            self.head = new_song
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_song

        print(song_name, "added to playlist")

    # Insert song at a given position
    def insert_song(self, position, song_name):
        new_song = Song(song_name)

        if position == 1:
            new_song.next = self.head
            self.head = new_song
            print(song_name, "inserted at position", position)
            return

        temp = self.head
        count = 1

        while temp and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid Position")
        else:
            new_song.next = temp.next
            temp.next = new_song
            print(song_name, "inserted at position", position)

    # Delete a song
    def delete_song(self, song_name):
        temp = self.head

        if temp and temp.name == song_name:
            self.head = temp.next
            print(song_name, "deleted from playlist")
            return

        prev = None

        while temp and temp.name != song_name:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Song not found")
        else:
            prev.next = temp.next
            print(song_name, "deleted from playlist")

    # Display playlist
    def display(self):
        if self.head is None:
            print("Playlist is empty")
        else:
            temp = self.head
            print("\nMusic Playlist:")
            while temp:
                print(temp.name, end=" -> ")
                temp = temp.next
            print("None")


# Main Program
playlist = Playlist()

while True:
    print("\n----- MUSIC PLAYLIST MENU -----")
    print("1. Add Song")
    print("2. Insert Song")
    print("3. Delete Song")
    print("4. Display Playlist")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        song = input("Enter song name: ")
        playlist.add_song(song)

    elif choice == 2:
        pos = int(input("Enter position: "))
        song = input("Enter song name: ")
        playlist.insert_song(pos, song)

    elif choice == 3:
        song = input("Enter song name to delete: ")
        playlist.delete_song(song)

    elif choice == 4:
        playlist.display()

    elif choice == 5:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")
