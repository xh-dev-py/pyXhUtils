import os
import stat
from typing import Callable, IO, Optional


class ScriptWriter:
    @staticmethod
    def write_script(file_name: str, op: Callable[[IO], None], executable: bool = False):
        with open(file_name, "w") as f:
            op(f)

        if executable:
            st = os.stat(file_name)
            os.chmod(file_name, st.st_mode | stat.S_IEXEC)

    def write_script_text(self, file_name: str, text: str, executable: bool = False):
        self.write_script(file_name, lambda f: f.write(text), executable=executable)


if __name__ == '__main__':
    ScriptWriter.write_script("test.txt", lambda f: f.write("hi"))
    ScriptWriter.write_script("test.sh", lambda f: f.write("echo hi"), executable=True)
