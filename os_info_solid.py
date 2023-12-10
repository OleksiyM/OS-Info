from abc import ABC, abstractmethod
from multiprocessing import cpu_count
import platform
import psutil
import subprocess


class SystemInfo(ABC):
    @abstractmethod
    def os_name(self) -> str:
        pass

    @abstractmethod
    def os_version(self) -> str:
        pass

    @abstractmethod
    def os_machine(self) -> str:
        pass


class WindowsInfo(SystemInfo):
    def os_name(self) -> str:
        return "Windows"

    def os_version(self) -> str:
        return platform.version()

    def os_machine(self) -> str:
        arch = platform.architecture()[0]
        return f"Windows {arch} bit"


class LinuxInfo(SystemInfo):
    def os_name(self) -> str:
        return "Linux"

    def os_version(self) -> str:
        os_type, _, _ = platform.uname()
        return os_type.replace("-", " ")

    def os_machine(self) -> str:
        os_type = platform.architecture()[0]

        lsb_info = subprocess.check_output(["lsb_release", "-si", "-sr"]).decode().strip()
        distro, version = lsb_info.split()

        return f"Linux {os_type} {distro} {version}"


class MacOSInfo(SystemInfo):
    def os_name(self) -> str:
        return f"macOS {platform.mac_ver()[0]}"

    def os_version(self) -> str:
        return platform.version() 

    def os_machine(self) -> str:
        return platform.machine()


def current_system_info() -> SystemInfo:
    current_os = platform.system()

    system_info_classes = {
        "Windows": WindowsInfo,
        "Linux": LinuxInfo,
        "Darwin": MacOSInfo,
    }

    info_class = system_info_classes.get(current_os)

    if not info_class:
        raise ValueError(f"Unsupported OS: {current_os}")

    return info_class()


def get_system_info() -> str:
    system_info = current_system_info()
    return f"""OS: {system_info.os_name()}
OS version: {system_info.os_version()}
Machine: {system_info.os_machine()}"""


def get_hardware_info() -> str:
    return f"""CPU Kernels: {cpu_count()}
Total Memory (RAM): {round(psutil.virtual_memory().total / 1024 ** 3, 2)} Gb"""


def main():
    output = "\n".join(
        [
            "Hardware:",
            get_hardware_info(),
            "\nSoftware:",
            get_system_info(),
        ]
    )

    print(output)


if __name__ == "__main__":
    main()
