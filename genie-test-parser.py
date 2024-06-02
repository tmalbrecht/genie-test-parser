from pyats_genie_command_parse import GenieCommandParse
import pprint

# Choose one of the following networking operating systems to initialise the command parser
# {'bigip', 'gaia', 'cheetah', 'dnac', 'apic', 'aireos', 'comware', 'iosxe', 'ios', 'nxos', 'linux', 'iosxr', 'asa', 'sros', 'viptela', 'ironware', 'junos'}
parse_obj = GenieCommandParse(nos='iosxe')

# Check the link below to see all available parsed commands in the Genie library.
# https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/?ref=packetswitch.co.uk#/parsers

# Choose a 'show' command and create a text file containing the output of the 'show' command you want to parse.
# The parsed data will be stored as a Python dictionary in the 'data' variable.

data = parse_obj.parse_file(show_command='show license all', file_name_and_path='example_cmd_1.txt')
data2 = parse_obj.parse_file(show_command='show version', file_name_and_path='example_cmd_2.txt')

# Use pretty print to print the parsed data in the terminal
print()
print("*" * 200)
print("Parsing example 1")
print("*" * 200)
print()
pprint.pp(data)
print()
print("*" * 200)
print("Parsing example 2")
print("*" * 200)
print()
pprint.pp(data2)


# Write parsed data to a file
with open("parsed_example_1.txt", "w") as file:
        pprint.pp(data, stream=file)

with open("parsed_example_2.txt", "w") as file:
        pprint.pp(data2, stream=file)

