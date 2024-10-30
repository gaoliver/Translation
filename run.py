import subprocess
import time

def run():
    space = "\n\n"

    # Startup message
    print("Starting translation...")
    print(space)

    # Wait for 5 seconds
    time.sleep(3)

    # Execute the scripts

    # Run translate-dialog-lines.py
    print("Step 1: Copying and translating subtitles contents..." + space)
    subprocess.run(['python', 'utils/translate-dialog-lines.py'])
    print(space*2)

    # Run backup-translated-content.py
    print("Step 2: Formating new translated object...")
    subprocess.run(['python', 'utils/backup-translated-content.py'])
    print(space)

    # Run replace-original.py
    print("Step 3: Replacing the original dialog lines...")
    subprocess.run(['python', 'utils/replace-original.py'])
    print(space)

    # Delete processed files
    print("Step 4: Deleting processed files...")
    subprocess.run(['python', 'utils/delete-processed-files.py'])
    print(space*2)

    # Finish message
    print("All scripts executed successfully.")
    print(space*4)

if __name__ == '__main__':
    run()