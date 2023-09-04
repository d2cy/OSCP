# R3c0nX

R3c0nX is a reconnaissance and enumeration tool designed to assist with information gathering, network scanning, and running tools based on services detected. This tool is intended to simplify the reconnaissance process .

## Usage

To use R3c0nX, provide the following mandatory command-line arguments:

- `-p` or `--path`: Path to create folders for organizing results.
- `-m` or `--machine`: Machine name or IP address.
- `-i` or `--ip`: Machine IP address.

### Example Usage:

```bash
python r3c0nX.py -p /path/to/folders -m TargetMachine -i 192.168.1.100
```

## Features
#### Folder Structure

Upon execution, R3c0nX creates a structured folder hierarchy based on the provided machine name:
```
Machine Name Folder (e.g., TargetMachine)
|
|____Enumeration
|
|____Exploits
|
|____Notes
|
|____Screenshots
|
|_____Others

```
#### Nmap Scan

R3c0nX initiates a basic Nmap scan as the initial reconnaissance step. The tool then further refines the scan based on the output.

#### Automated Tools

Based on the services detected during the scan and the configuration files, R3c0nX can automatically run additional tools to gather information, perform enumeration, or execute specific tasks. You can customize and expand the list of tools and wordlists in the configuration files to suit your needs.

#### Benefits

- **Customizable Configurations**: Users can easily edit the configuration files to include more tools, wordlists, and other parameters, allowing for flexibility and customization.
- **Streamlined Reconnaissance**: R3c0nX simplifies the reconnaissance process, automating certain steps and organizing results into a clear folder structure.


