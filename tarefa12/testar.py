#!/usr/bin/env python

import sys
from os.path import isfile, join, getsize
from os import listdir
from itertools import count
import re
import codecs
from subprocess import DEVNULL, PIPE, run, TimeoutExpired


class BaseTask:
    SPACES_RE = re.compile(r"\s+", re.M)
    TIME_LIMIT_SECONDS = 5

    def strip_spaces(self, text):
        return self.SPACES_RE.sub(" ", text.strip())

    def read_file(self, file_name):
        try:
            with codecs.open(file_name, encoding="utf-8", errors="strict") as f:
                return f.read()
        except ValueError:
            raise ValueError(f"Enconding inválido em {file_name}. Por favor, use UTF-8.")
        except:
            return ""

    def has_size(self, file_name, size):
        file_size = getsize(file_name)
        assert file_size >= size, f"{file_name} deve ter pelo menos {size} bytes"

    def count_words(self, text):
        words = text.split()
        number_of_words = len(words)
        return number_of_words

    def has_n_words(self, file_name, n_words):
        try:
            text = self.read_file(file_name)
            assert self.count_words(text) >= n_words, f"{file_name} deve ter pelos menos {n_words} palavras"
        except ValueError:
            raise AssertionError(f"Encoding inválido em {file_name}. Use UTF-8.")

    def compare_stripped(self, left, right):
        return self.strip_spaces(left) == self.strip_spaces(right)

    def compare_files(self, out, res):
        left = self.read_file(out)
        right = self.read_file(res)
        return self.compare_stripped(left, right)

    def test_case(self, script, file_name, arguments, output_file=sys.stderr):

        cmd = ["python3", script] + arguments
        cmd = " ".join([c if " " not in c and c != "" else f'"{c}"' for c in cmd])

        print(f"\nExecutando:\n$ {cmd}", file=output_file)

        if file_name != None:
            out_file_name = file_name + ".out"
            res_file_name = file_name + ".res"
            with open(out_file_name, "w") as o:
                try:
                    p = run(["python3", script] + arguments, stdout=o, stderr=DEVNULL, encoding="utf8", errors="ignore", timeout=self.TIME_LIMIT_SECONDS,)
                except TimeoutExpired:
                    assert False, f"comando excedeu o tempo limite de {self.TIME_LIMIT_SECONDS}s"
            assert p.returncode == 0, f'falha ao executar "{cmd}"'
            assert self.compare_files(out_file_name, res_file_name), f'{file_name}: arquivos "{out_file_name}" "{res_file_name}" diferem'
        else:
            try:
                p = run(["python3", script] + arguments, stdout=output_file, stderr=DEVNULL, encoding="utf8", errors="ignore", timeout=self.TIME_LIMIT_SECONDS,)
            except TimeoutExpired:
                assert False, f"comando excedeu o tempo limite de {self.TIME_LIMIT_SECONDS}s"
            assert p.returncode == 0, f'falha ao executar "{cmd}"'

    def exists(self, file_name):
        assert isfile(file_name), f"você deve criar um arquivo {file_name}"

    def input_output(self, script, input_content, expected_output):
        cmd = f"python3 {script}"
        try:
            p = run(["python3", script], input=input_content, stdout=PIPE, stderr=DEVNULL, encoding="utf8", errors="ignore", timeout=5,)
        except TimeoutExpired:
            assert False, f"comando {cmd} excedeu o tempo limite de {self.TIME_LIMIT_SECONDS}s"
        assert p.returncode == 0, f'falha ao executar "{cmd}" com entrada "{input_content}"'
        assert self.compare_stripped(p.stdout, expected_output), f'para entrada "{input_content}", a saída é "{p.stdout.strip()}", mas era esperado "{expected_output}"'

    def run(self, all=False):
        for name in sorted(dir(self)):
            if not name.startswith("teste_"):
                continue
            try:
                test = getattr(self, name)
                test()
                print(f"{name}: OK")
            except AssertionError as e:
                print(f"{name}: FALHOU\n  -> {e}")
                if not all:
                    return


class Task(BaseTask):

    index = count(0)

    def teste_0(self):
        csvfile = "agenda.csv"
        script = "agenda.py"
        self.exists(script)
        args = ["-a", csvfile, "inicializar"]
        self.test_case(script, None, args)
        self.exists(csvfile)

    def teste_1(self):
        csvfile = "agenda.csv"
        script = "agenda.py"
        args = [
            "-a",
            csvfile,
            "criar",
            "--nome",
            "MC102",
            "--data",
            "01/06/2020",
            "--hora",
            "14:00",
            "--descricao",
            "Aula de laboratório",
        ]
        self.test_case(script, None, args)

    def teste_2(self):
        csvfile = "agenda.csv"
        script = "agenda.py"
        args = ["-a", csvfile, "alterar", "--evento", "1", "--hora", "16:00"]
        self.test_case(script, None, args)

    def teste_3(self):
        csvfile = "agenda.csv"
        script = "agenda.py"
        args = ["-a", csvfile, "remover", "--evento", "1"]
        self.test_case(script, None, args)

    def teste_4(self):
        csvfile = "agenda.csv"
        script = "agenda.py"
        args = ["-a", csvfile, "listar", "--data", "01/06/2020"]
        self.test_case(script, join("testes", f"agenda{next(self.index)}"), args)

    def teste_5(self):
        csvfile = "agenda.csv"
        script = "agenda.py"
        args = ["-a", csvfile, "inicializar"]
        self.test_case(script, None, args)
        
        ## cria novos eventos
        args = [
            "-a",
            csvfile,
            "criar",
            "--nome",
            "MC102",
            "--data",
            "01/01/2020",
            "--hora",
            "14:00",
            "--descricao",
            "Aula de laboratório",
        ]
        self.test_case(script, None, args)
        args = ["-a", csvfile, "criar", "--nome", "MC102", "--data", "01/06/2020", "--hora", "14:00", "--descricao", ""]
        self.test_case(script, None, args)

        ## lista eventos
        args = ["-a", csvfile, "listar", "--data", "01/06/2020"]
        self.test_case(script, join("testes", f"agenda{next(self.index)}"), args)

        ## altera descrição do evento
        args = ["-a", csvfile, "alterar", "--evento", "2", "--descricao", "Aula de laboratório"]
        self.test_case(script, None, args)

        ## lista eventos
        args = ["-a", csvfile, "listar", "--data", "01/06/2020"]
        self.test_case(script, join("testes", f"agenda{next(self.index)}"), args)

        ## altera hora do evento
        args = ["-a", csvfile, "alterar", "--evento", "2", "--hora", "16:00"]
        self.test_case(script, None, args)

        ## lista eventos
        args = ["-a", csvfile, "listar", "--data", "01/06/2020"]
        self.test_case(script, join("testes", f"agenda{next(self.index)}"), args)

        ## cria vários novos eventos
        args = ["-a", csvfile, "criar", "--nome", "MC102", "--data", "04/06/2020", "--hora", "16:00", "--descricao", "Aula de laboratório"]
        self.test_case(script, None, args)
        args = ["-a", csvfile, "criar", "--nome", "MC102", "--data", "01/06/2020", "--hora", "10:00", "--descricao", "Aula expositivas"]
        self.test_case(script, None, args)
        args = ["-a", csvfile, "criar", "--nome", "MC102", "--data", "04/06/2020", "--hora", "10:00", "--descricao", "Aula expositivas"]
        self.test_case(script, None, args)
        args = ["-a", csvfile, "criar", "--nome", "MC102", "--data", "15/06/2020", "--hora", "14:00", "--descricao", "Correção da tarefa"]
        self.test_case(script, None, args)
        args = ["-a", csvfile, "criar", "--nome", "MC102", "--data", "13/06/2020", "--hora", "20:00", "--descricao", "Jogar LOL"]
        self.test_case(script, None, args)
        args = ["-a", csvfile, "criar", "--nome", "MC102", "--data", "15/06/2020", "--hora", "14:00", "--descricao", "Correção da tarefa"]
        self.test_case(script, None, args)

        ## altera nome do evento
        args = ["-a", csvfile, "alterar", "--evento", "7", "--nome", "Campeonato"]
        self.test_case(script, None, args)

        ## lista vários eventos
        args = ["-a", csvfile, "listar", "--data", "01/06/2020"]
        self.test_case(script, join("testes", f"agenda{next(self.index)}"), args)
        args = ["-a", csvfile, "listar", "--data", "04/06/2020"]
        self.test_case(script, join("testes", f"agenda{next(self.index)}"), args)
        args = ["-a", csvfile, "listar", "--data", "15/06/2020"]
        self.test_case(script, join("testes", f"agenda{next(self.index)}"), args)
        args = ["-a", csvfile, "listar", "--data", "13/06/2020"]
        self.test_case(script, join("testes", f"agenda{next(self.index)}"), args)

        ## remove evento
        args = ["-a", csvfile, "remover", "--evento", "7"]
        self.test_case(script, None, args)

        ## lista vários eventos
        args = ["-a", csvfile, "listar", "--data", "13/06/2020"]
        self.test_case(script, join("testes", f"agenda{next(self.index)}"), args)

    def teste_6(self):
        self.exists("README.md")
        min = 300
        max = 500
        words = 0
        with open("README.md", "r") as readme:
            for sentence in readme:
                words += len(sentence.split())
        assert min <= words and words <= max, f"O arquivo README.md deverá conter no mínimo {min} palavras e no máximo {max} palavras."


if __name__ == "__main__":
    Task().run()
