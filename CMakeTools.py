import os
import sys


def source_list(path):
    base = os.path.basename(os.path.dirname(path))

    if not os.path.exists(path):
        raise Exception(f"Path don't exist: {path}")

    def sources():
        for address, dirs, files in os.walk(path):
            for file in files:
                if file[0] != '.':
                    yield os.path.join(base, os.path.join(os.path.relpath(address, path), file))

    return base, sources()


def build_cmake(base, sources):
    with open(base + ".cmake", "w", encoding='utf-8') as cmake_list:
        cmake_list.write("set(" + base + " ${" + base + "}\n")
        for source in sources:
            cmake_list.write(f"\t{source}\n")
        cmake_list.write(")")


if __name__ == '__main__':
    build_cmake(*source_list(sys.argv[1]))

