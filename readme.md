## Usage
1. Open a terminal, command prompt or PowerShell terminal
2. Navigate to the directory containing os_info.py using `cd`
3. Run the command

### Windows
```
python os_info.py
```
or
```
python os_info_solid.py
```
### macOS or Linux
```
python3 os_info.py
``` 
or
```
python3 os_info_solid.py
```

This will execute the Python script and print out the system information gathered by the code.

The steps are similar across operating systems - navigate to the file location and run the Python interpreter, passing the script file as an argument.

## Architecture of the os_info.py
This code is gathering system information from the local machine.

It imports several Python modules:

`multiprocessing` - To get the number of CPU cores
`threading` - To get the number of active threads
`platform` - To get OS and hardware details
`psutil` - To get memory usage details
`subprocess` - To run the `lsb_release` command on Linux
It defines several functions:

`current_cpu_count()` - Gets the number of CPU cores
`total_memory()` - Gets the total RAM in GB
`get_thread_count()` - Gets the number of active threads
`os_version()` - Gets the OS version
`os_machine()` - Gets the hardware architecture
`get_windows_info()`, `get_linux_info()`, `get_mac_info()` - Get OS-specific details
`my_os_info()` - Calls the appropriate OS info function
`current_os_info()` - Another way to get OS details
`main()` - Prints a summary of the hardware and software info
The main function joins the output of each info gathering function to print a readable summary. It handles Windows, Linux and macOS.


## Architecture os_info_solid.py
This code is gathering system information using the Solid Principles of Object Oriented Design.

### It imports:

* `abc` for abstract base classes
* `multiprocessing` and `platform` for system info
* `psutil` for memory details
* `subprocess` to run commands
It defines an abstract base class SystemInfo with pure virtual methods for:

* OS name
* OS version
* OS machine
Concrete subclasses are defined for each OS:

* `WindowsInfo`
* `LinuxInfo`
* `MacOSInfo`
Each subclass implements the pure virtual methods specific to that OS.

### The: 
`current_system_info()` function returns the appropriate subclass instance based on the OS.

`get_system_info()` calls the subclass methods to retrieve OS details.

`get_hardware_info()` gets CPU/memory info.

`main()` prints a summary by joining the output of the info functions.

By defining an abstract interface and concrete implementations, new OSes can be added easily while keeping the consumer code unchanged. Let me know if any part needs more explanation!

## Key points:

* **Abstracted system information**: The `SystemInfo` abstract class defines the contract for any class that provides information about the system.
* **Concrete system info classes**: The `WindowsInfo`, `LinuxInfo`, and `MacOSInfo` classes implement the `SystemInfo` abstract class, providing specific information for their respective operating systems.
* **Single point of entry**: The `current_system_info` function retrieves the appropriate `SystemInfo` class based on the current operating system.
* **Separated hardware and software info**: The `get_hardware_info` and `get_system_info` functions are separate, allowing for easier reuse and modification.
* **Improved output readability**: The output is now formatted using f-strings for better readability.

## This code adheres to the SOLID principles by:

* **Single responsibility principle**: Each class has a single, well-defined responsibility.
* **Open/closed principle**: The system is open for extension (adding new operating systems) but closed for modification (changing existing behavior).
* **Liskov substitution principle**: Subclasses can be used wherever their base class is expected.
* **Interface segregation principle**: The `SystemInfo` abstract class defines a clear and concise interface for system information.
* **Dependency inversion principle**: High-level modules depend on abstractions (interfaces), not concrete implementations.