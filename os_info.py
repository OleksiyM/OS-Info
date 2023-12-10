from multiprocessing import cpu_count
import threading
import platform
import psutil
import subprocess


def current_cpu_count():
    return cpu_count()


def total_memory():
    GB = 1024 ** 3
    return round(psutil.virtual_memory().total / GB, 2)


def get_thread_count():
    return threading.active_count()


def os_version():
    return platform.version()


def os_machine():
    return platform.machine()


def get_windows_info():
    arch = platform.architecture()[0]
    return f"Windows {arch} bit"


def get_linux_info():
    os_type = platform.architecture()[0]

    lsb_info = subprocess.check_output(["lsb_release", "-si", "-sr"]).decode().strip()
    distro, version = lsb_info.split()

    return f"Linux {os_type} {distro} {version}"


def get_mac_info():
    mac_ver = platform.mac_ver()[0]
    return f"macOS {mac_ver}"


def my_os_info():
    current_os = platform.system()

    os_info = {
        "Darwin": get_mac_info,
        "Windows": get_windows_info,
        "Linux": get_linux_info
    }

    info_func = os_info.get(current_os) if current_os in os_info else f"Unknown OS {current_os}"

    # info_func = os_info.get(current_os, lambda: f"Unknown OS {current_os}")

    return info_func()


def current_os_info():
    current_os = platform.system()

    if current_os == "Darwin":
        return f"{get_mac_info()}"

    elif current_os == "Windows":
        return f"{get_windows_info()}"

    elif current_os == "Linux":
        return f"{get_linux_info()}"

    return f"Unknown OS {platform.system()}"


def main():
    output = "\n".join([
        "Hardware:",
        f"  CPU Kernels: {current_cpu_count()}",
        f"  Total Memory (RAM): {total_memory()} Gb",
        "\nSoftware:",
        f"  OS: {my_os_info()}",
        f"  OS ver: {os_version()}",
        f"  Architecture: {os_machine()}"
    ])

    print(output)


if __name__ == "__main__":
    main()
