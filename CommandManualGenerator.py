# class CommandManualGenerator.py
#Name:Mohammad Ataya
#Id:1211555
import os
from CommandManual import CommandManual
from XmlSerializer import XmlSerializer

class CommandManualGenerator:
    def __init__(self, InputFile):
        self.InputFile = InputFile
          # GetCommandDescription  function
    def GetCommandDescription(self, Command):
        result =  os.popen(f"man {Command} | col -b").read().strip()
        return result if result else "No description"
      # GetVersionHistory  function
    def GetVersionHistory(self, Command):
        result =  os.popen(f"{Command} --version").read().strip()
        return result if result else "Version history not found."
          # GetExample  function
    def GetExample(self, Command):
        result = os.popen(f"man {Command} | col -b | grep -A3 'EXAMPLES'").read().strip()
        return result if result else "No example available."
     # GetRelatedCommands  function
    def GetRelatedCommands(self, Command):
        result = os.popen(f"compgen -c {Command}").read().split()
        return result if result else "No related commands found."
       # GenerateXml  function
    def GenerateXml(self, Command, Description, VersionHistory, Example, RelatedCommands):
        manual = CommandManual(Command, Description, VersionHistory, Example, RelatedCommands)
        xml_serializer = XmlSerializer(manual)
        xml_serializer.save_to_file()
    # VerifyContent  function
    def VerifyContent(self, FileXmlcheek,File):
        with open(FileXmlcheek, 'r') as file:
            existingxml= file.read()

        with open(f"{File}_manual.xml", 'r') as file:
            new_xml_content = file.read()

        if existingxml == new_xml_content:
            print("Verification is correct")
        else:
            print("Verification is not correct")

    #Search function
    def Search(self, keyword):
        with open(self.InputFile, 'r') as file:
            commands = [line.strip() for line in file]

        for Command in commands:
            if keyword.lower() in Command.lower():
                print(f"Command: {Command}")
                print(f"Description: {self.GetCommandDescription(Command)}")
                print(f"Example: {self.GetExample(Command)}")
    
    
        #RecommendCommands function
    def RecommendCommands(self, file):
        if os.path.isfile(file):
            with open(file, "r") as f:
                commands = [line.split()[0] for line in f.readlines()]

            recommended = sorted(set(commands), key=commands.count, reverse=True)[:5]
            print(f"Recommended commands: {', '.join(recommended)}")
        else:
            print("File not found")

        #process_commands function
    def process_commands(self):
        with open(self.InputFile, 'r') as file:
            commands = [line.strip() for line in file]

        for Command in commands:
            Description = self.GetCommandDescription(Command)
            VersionHistory = self.GetVersionHistory(Command)
            Example = self.GetExample(Command)
            RelatedCommands = self.GetRelatedCommands(Command)

            self.GenerateXml(Command, Description, VersionHistory, Example, RelatedCommands)
