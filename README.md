### Simple Python Keylogger

This Python script is a basic keylogger designed to capture keystrokes on a system and log them to a text file. It utilizes the `pynput` library to monitor keyboard events and record them along with timestamps.

#### Features:

- **Keystroke Logging**: The keylogger captures each keystroke made by the user.
- **Timestamping**: Each keystroke is logged with a timestamp indicating when it was captured.
- **Platform Detection**: The script includes functionality to detect whether it is running on a physical machine or a virtual machine. If running on a virtual machine, the script deletes itself to avoid unintended consequences.

#### Usage:

1. Clone the repository or download the script.
2. Run the script on the target machine.
3. The keylogger will start capturing keystrokes and saving them to a file named `keyloggeroutput.txt`.
4. To stop the keylogger, terminate the script.

#### Note:

- This keylogger is intended for educational purposes only.
- While the script includes detection for Windows virtual machines, it has not been tested in this environment.

#### Testing:
- The Script executes and begins capture on a Physical Machine running Windows 10.
- The Script executes and deletes itself on a VM Ware Virtual Machine running Debian Linux.
