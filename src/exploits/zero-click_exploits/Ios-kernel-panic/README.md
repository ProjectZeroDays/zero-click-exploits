# CVE-2021-1965

CVE-2021-1965 WiFi Zero Click RCE Trigger PoC

This is a quick&dirty Proof-of-Concept code to verify if your phone is vulnerable. After running the poc code, your phone is supposed to crash & reboot within seconds. In case you need more info about the bug & vulnerable code, here you are:

Description: Possible buffer overflow due to lack of parameter length check during MBSSID scan IE parse

During multiple BSSID scan ie parse, there is memory allocation on new_ie variable of size 1024 which may create buffer overflow in util_gen_new_ie() if ie length is greater than 1024

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Changelog](#changelog)
- [Security](#security)
- [Code of Conduct](#code-of-conduct)
- [Contact](#contact)

## Prerequisites

- A C compiler (e.g., gcc)
- libpcap library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/CVE-2021-1965.git
   cd CVE-2021-1965
   ```

2. Install the required dependencies:
   ```
   sudo apt-get update
   sudo apt-get install -y gcc libpcap-dev
   ```

## Usage

1. Compile the script using a C compiler, for example:
   ```
   gcc -o CVE-2021-1965-poc CVE-2021-1965-poc.c -lpcap
   ```

2. Run the compiled script:
   ```
   ./CVE-2021-1965-poc
   ```

3. Check if the script connects back to `zeroclickexploits.ddns.net` and auto executes as expected.

## Contributing

Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Changelog

See the [CHANGELOG.md](CHANGELOG.md) file for a history of changes made to the project.

## Security

For information on how to report security vulnerabilities, please refer to the [SECURITY.md](SECURITY.md) file.

## Code of Conduct

Please refer to the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file for guidelines on how to interact with the project community.

## Contact

For support or questions, please contact the maintainers or project team.

## Additional Documentation

Additional documentation, such as usage instructions, architecture diagrams, and design documents, can be found in the `docs/` directory.

## Setting up the cron job

To automate the execution of the script, you can set up a cron job to run the script at a specified interval. Follow these steps:

1. Open the crontab file by running `crontab -e` in the terminal.
2. Add a new line with the desired schedule and the command to execute the script. For example, to run the script every minute, add the following line:
   
   ```
   * * * * * /path/to/CVE-2021-1965-poc
   ```

## Testing the script

To test the script, follow these steps:

1. Compile the script using a C compiler, for example:
   
   ```
   gcc -o CVE-2021-1965-poc CVE-2021-1965-poc.c -lpcap
   ```

3. Run the compiled script:
   
   ```
   ./CVE-2021-1965-poc
   ```
   
4. Check if the script connects back to `zeroclickexploits.ddns.net` and auto executes as expected.
