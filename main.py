import os
import subprocess
import datetime
import json
from colorama import Fore, Style

viod = "              "

#
directories = [
    "/storage/emulated/0/pubgmobile/",
    "/storage/emulated/0/pubgmobile/OutPut/",
    "/storage/emulated/0/pubgmobile/repack/",
    "/storage/emulated/0/PeaceElite/",
    "/storage/emulated/0/PeaceElite/output/",
    "/storage/emulated/0/PeaceElite/repack/"
]

def gradient_text(text, start_color, end_color):
    """Create a gradient text start_color до end_color."""
    start_rgb = [int(start_color[i:i + 2], 16) for i in (0, 2, 4)]
    end_rgb = [int(end_color[i:i + 2], 16) for i in (0, 2, 4)]

    gradient = ''
    for i in range(len(text)):
        ratio = i / len(text)
        rgb = [int(start_rgb[j] + (end_rgb[j] - start_rgb[j]) * ratio) for j in range(3)]
        gradient += f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{text[i]}"
    
    return gradient + Style.RESET_ALL

def get_current_datetime():
    """Returns the current date and time as a format string."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def print_main_menu():
    print(viod + gradient_text("\n\n\n" + " " + get_current_datetime() + " │ 作者：lin │ QQ：2786910486 │ pakobbtool", "0000FF", "00FFFF"))
    print()
    print(viod + gradient_text("┌───────────────────────────────┐", "0000FF", "00FFFF"))
    print(viod + gradient_text("│  PUBG Mobile  │  Peace Elite  │", "0000FF", "00FFFF"))
    print(viod + gradient_text("│───────────────────────────────│", "0000FF", "00FFFF"))
    print(viod + gradient_text("│[1] Unpack OBB │[3] Unpack PAK │", "0000FF", "00FFFF"))
    print(viod + gradient_text("│[2] Repack OBB │[4] Repack PAK │", "0000FF", "00FFFF"))
    print(viod + gradient_text("│───────────────────────────────│", "0000FF", "00FFFF"))
    print(viod + gradient_text("│[5] 帮助        [0] 退出       │", "0000FF", "00FFFF"))
    print(viod + gradient_text("└───────────────────────────────┘", "0000FF", "00FFFF"))
    print()

def print_unpack_menu():
    print()

def print_repack_menu():
    print()

def list_files_in_directory(directory, file_extension):
    """Displays files in a directory with a given extension."""
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"未找到目录: '{directory}'")

        files = os.listdir(directory)
        target_files = [file for file in files if file.endswith(file_extension)]

        if not target_files:
            print(gradient_text(f"未找到扩展名文件 {file_extension} 在目录中 {directory}.", "FF0000", "FFFFFF"))
            return None

        print(gradient_text(f"目录中的文件 {directory}: ", "00FF00", "FFFFFF"))
        for index, file_name in enumerate(target_files, start=1):
            print(gradient_text(f"{index}) {file_name}", "0000FF", "00FFFF"))

        return target_files

    except FileNotFoundError as e:
        print(gradient_text(str(e), "FF0000", "FFFFFF"))
    except PermissionError:
        print(gradient_text(f"拒绝进入目录: '{directory}.", "FF0000", "FFFFFF"))
    except Exception as e:
        print(gradient_text(f"目录访问错误: {e}", "FF0000", "FFFFFF"))

    return None

def execute_command(command):
    """Execute this shell command and output the result or error."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(gradient_text(result.stdout.strip(), "00FF00", "FFFFFF"))  #
    except subprocess.CalledProcessError as e:
        print(gradient_text(f"命令执行错误: {e}\n{e.stderr.strip()}", "FF0000", "FFFFFF"))

def main():
    subprocess.call("chmod +x quickbms", shell=True)

    while True:
        print_main_menu()
        choice = input(gradient_text("输入您的选择: ", "00FF00", "FFFFFF")).strip()

        if choice == '1':
            print_unpack_menu()
            directory = "/storage/emulated/0/pubgmobile/"
            files = list_files_in_directory(directory, '.obb')
            if files:
                index_input = input(gradient_text("输入解包文件的编号(或输入0返回): ", "00FF00", "FFFFFF")).strip()
                if index_input == '0':
                    continue
                if not index_input:
                    print(gradient_text("输入不能是空的 请再试一次", "FF0000", "FFFFFF"))
                    continue
                try:
                    index = int(index_input) - 1
                    if 0 <= index < len(files):
                        command = f"qemu-i386 quickbms pubgm_obb.bms \"{os.path.join(directory, files[index])}\" \"/storage/emulated/0/pubgmobile/OutPut/\""
                        execute_command(command)
                    else:
                        print(gradient_text("无效指数 请再试一次", "FF0000", "FFFFFF"))
                except ValueError:
                    print(gradient_text("请输入一个有效的整数", "FF0000", "FFFFFF"))

        elif choice == '2':
            print_repack_menu()
            directory = "/storage/emulated/0/pubgmobile/"
            files = list_files_in_directory(directory, '.obb')
            if files:
                index_input = input(gradient_text("输入解包文件的编号(或输入0返回）: ", "00FF00", "FFFFFF")).strip()
                if index_input == '0':
                    continue
                if not index_input:
                    print(gradient_text("输入不能是空的 请再试一次", "FF0000", "FFFFFF"))
                    continue
                try:
                    index = int(index_input) - 1
                    if 0 <= index < len(files):
                        command = f"qemu-i386 quickbms -g -w -r -r pubgm_obb.bms \"{os.path.join(directory, files[index])}\" \"/storage/emulated/0/pubgmobile/repack/\""
                        execute_command(command)
                    else:
                        print(gradient_text("无效指数 请再试一次", "FF0000", "FFFFFF"))
                except ValueError:
                    print(gradient_text("请输入一个有效的整数", "FF0000", "FFFFFF"))

        elif choice == '3':
            print_unpack_menu()
            directory = "/storage/emulated/0/PeaceElite/"
            files = list_files_in_directory(directory, '.pak')
            if files:
                index_input = input(gradient_text("输入解包文件的编号(或输入0返回): ", "00FF00", "FFFFFF")).strip()
                if index_input == '0':
                    continue
                if not index_input:
                    print(gradient_text("输入不能是空的 请再试一次", "FF0000", "FFFFFF"))
                    continue
                try:
                    index = int(index_input) - 1
                    if 0 <= index < len(files):
                        command = f"qemu-i386 quickbms chinaNB.bms \"{os.path.join(directory, files[index])}\" \"/storage/emulated/0/PeaceElite/output/\""
                        execute_command(command)
                    else:
                        print(gradient_text("无效指数 请再试一次", "FF0000", "FFFFFF"))
                except ValueError:
                    print(gradient_text("请输入有效整数", "FF0000", "FFFFFF"))

        elif choice == '4':
            print_repack_menu()
            directory = "/storage/emulated/0/PeaceElite/"
            files = list_files_in_directory(directory, '.pak')
            if files:
                index_input = input(gradient_text("输入解包文件的编号(或输入0返回): ", "00FF00", "FFFFFF")).strip()
                if index_input == '0':
                    continue
                if not index_input:
                    print(gradient_text("输入不能是空的 请再试一次", "FF0000", "FFFFFF"))
                    continue
                try:
                    index = int(index_input) - 1
                    if 0 <= index < len(files):
                        command = f"qemu-i386 quickbms -g -w -r -r chinaNB.bms \"{os.path.join(directory, files[index])}\" \"/storage/emulated/0/PeaceElite/repack/\""
                        execute_command(command)
                    else:
                        print(gradient_text("输入不能是空的 请再试一次", "FF0000", "FFFFFF"))
                except ValueError:
                    print(gradient_text("请输入有效整数", "FF0000", "FFFFFF"))

        elif choice == '5':
            print(gradient_text("\n\n这是一个用于PAK (Peace Elite)和OBB (PUBG Mobile)拆解和打包的工具\n\n如何使用:\n1将OBB或PAK文件拖放到相应的目录中\n2使用选定的菜单与文件进行交互\n3OutPut文件夹将包含解压缩的文件\n4都准备好了!该工具已准备好使用!\n详细咨询QQ：2786910486\n制作者QQ: 2786910486\n", "00FFFF", "0000FF"))

        elif choice == '0':
            print(gradient_text("退出...", "FF0000", "FFFFFF"))
            break

        else:
            print(gradient_text("输入不能是空的 请再试一次", "FF0000", "FFFFFF"))

if __name__ == "__main__":
    main()