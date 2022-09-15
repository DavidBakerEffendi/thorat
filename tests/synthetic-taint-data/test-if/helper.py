import subprocess
import json

def run_cmd(cmd, msg="Failed to run command"):
    print('Running ' + ' '.join(cmd))
    if subprocess.check_call(cmd):
        print(msg)
        exit(1)

def read_character_file(path):
    character_file = open(path)
    char_dict = json.load(character_file)
    character_file.close()
    return char_dict