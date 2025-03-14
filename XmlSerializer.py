# XmlSerializer.py
#Name:Mohammad Ataya
#Id:1211555
import xml.etree.ElementTree as ET

class XmlSerializer:
    def __init__(self, command_manual):
        self.command_manual = command_manual

    def save_to_file(self):
        root = ET.Element("Manuals")
        command_manual = ET.SubElement(root, "CommandManual")
        ET.SubElement(command_manual, "CommandName").text = self.command_manual.Command
        ET.SubElement(command_manual, "CommandDescription").text = self.command_manual.Description
        ET.SubElement(command_manual, "VersionHistory").text = self.command_manual.VersionHistory
        ET.SubElement(command_manual, "Example").text = self.command_manual.Example
        ET.SubElement(command_manual, "RelatedCommands").text = ", ".join(self.command_manual.RelatedCommands)
        ET.SubElement(command_manual, "SyntaxAndUsage").text = "Syntax and usage information here."
        ET.SubElement(command_manual, "DocumentationLinks").text = "Documentation links here."

        tree = ET.ElementTree(root)
        tree.write(f"{self.command_manual.Command}_manual.xml")
