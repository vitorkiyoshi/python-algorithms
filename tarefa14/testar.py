#!/usr/bin/env python

from os.path import isfile, join, getsize
from os import listdir
import re
import codecs
from subprocess import DEVNULL, PIPE, run, TimeoutExpired


class BaseTask:
    SPACES_RE = re.compile(r'\s+', re.M)
    TIME_LIMIT_SECONDS = 5

    def strip_spaces(self, text):
        return self.SPACES_RE.sub(' ', text.strip())

    def read_file(self, file_name):
        try:
            with codecs.open(file_name, encoding='utf-8', errors='strict') as f:
                return f.read()
        except ValueError:
            raise ValueError(f"Enconding inválido em {file_name}. Por favor, use UTF-8.")
        except:
            return ''

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

    def test_case(self, script, in_file_name):
        out_file_name = in_file_name.replace('.in', '.out')
        res_file_name = in_file_name.replace('.in', '.res')
        cmd = f'python3 {script} < {in_file_name} > {out_file_name}'
        with open(in_file_name) as i, open(out_file_name, 'w') as o:
            try:
                p = run(['python3', script],
                        stdin=i,
                        stdout=o,
                        stderr=DEVNULL,
                        encoding='utf8',
                        errors='ignore',
                        timeout=self.TIME_LIMIT_SECONDS)
            except TimeoutExpired:
                assert False, f'comando {cmd} excedeu o tempo limite de {self.TIME_LIMIT_SECONDS}s'
        assert p.returncode == 0, f'falha ao executar "{cmd}"'
        assert self.compare_files(out_file_name, res_file_name), \
            f'{in_file_name}: arquivos "{out_file_name}" "{res_file_name}" diferem'

    def exists(self, file_name):
        assert isfile(file_name), f'você deve criar um arquivo {file_name}'

    def input_output(self, script, input_content, expected_output):
        cmd = f'python3 {script}'
        try:
            p = run(['python3', script],
                    input=input_content,
                    stdout=PIPE,
                    stderr=DEVNULL,
                    encoding='utf8',
                    errors='ignore',
                    timeout=5)
        except TimeoutExpired:
            assert False, f'comando {cmd} excedeu o tempo limite de {self.TIME_LIMIT_SECONDS}s'
        assert p.returncode == 0, f'falha ao executar "{cmd}" com entrada "{input_content}"'
        assert self.compare_stripped(
            p.stdout, expected_output
        ), f'para entrada "{input_content}", a saída é "{p.stdout.strip()}", mas era esperado "{expected_output}"'

    def run(self, all=False):
        for name in sorted(dir(self)):
            if not name.startswith('teste_'):
                continue
            try:
                test = getattr(self, name)
                test()
                print(f'{name}: OK')
            except AssertionError as e:
                print(f'{name}: FALHOU\n  -> {e}')
                if not all:
                    return


class Task(BaseTask):

    def teste_00_fatorial(self):
        tests = [("0", "1"), ("1", "1"), ("5", "120"), ("11", "39916800"), ("31", "8222838654177922817725562880000000")]
        script = 'fatorial.py'
        self.exists(script)
        for (inputvalue, outputvalue) in tests:
            self.input_output(script, inputvalue, outputvalue)

    def teste_01_maximo(self):
        script = 'maximo.py'
        self.exists(script)
        for i in range(5):
            self.test_case(script, join('testes', f"maximo{i}.in"))

    def teste_02_fibonacci3(self):
        tests = [("0", "0"), ("1", "1"), ("11", "423"), ("31", "83047505"), ("120", "29725355656849404391892131886652")]
        script = 'fibonacci3.py'
        self.exists(script)
        for (inputvalue, outputvalue) in tests:
            self.input_output(script, inputvalue, outputvalue)

    def teste_03_collatz(self):
        tests = [("1", "0"), ("10", "5"), ("15", "12"), ("1246538", "95"), ("372036854775807", "234")]
        script = 'collatz.py'
        self.exists(script)
        for (inputvalue, outputvalue) in tests:
            self.input_output(script, inputvalue, outputvalue)

    def teste_04_mmc(self):
        tests = [("12 9", "36"), ("458 745", "341210"), ("278943861 849435618", "78981616985280366")]
        script = 'mmc.py'
        self.exists(script)
        for (inputvalues, outputvalue) in tests:
            self.input_output(script, inputvalues, outputvalue)

    def teste_05_hanoi(self):
        tests = [("1", "1"), ("2", "3"), ("15", "32767"), ("22", "4194303")]
        script = 'hanoi.py'
        self.exists(script)
        for (inputvalue, outputvalue) in tests:
            self.input_output(script, inputvalue, outputvalue)

    def teste_06_busca_binaria(self):
        script = 'busca_binaria.py'
        self.exists(script)
        for i in range(5):
            self.test_case(script, join('testes', f"busca_binaria{i}.in"))

    def teste_07_potencia(self):
        tests = [("2 3", "8"), ("3 5", "243"), ("25 48", "12621774483536188886587657044524579674771302961744368076324462890625")]
        script = 'potencia.py'
        self.exists(script)
        for (inputvalues, outputvalue) in tests:
            self.input_output(script, inputvalues, outputvalue)

    def teste_08_kesimo(self):
        script = 'k-esimo.py'
        self.exists(script)
        for i in range(5):
            self.test_case(script, join('testes', f"k-esimo{i}.in"))

    def teste_09_menor_ausente(self):
        script = 'menor_ausente.py'
        self.exists(script)
        for i in range(5):
            self.test_case(script, join('testes', f"menor_ausente{i}.in"))

    def teste_10_merge_sort(self):
        script = 'merge_sort.py'
        self.exists(script)
        for i in range(5):
            self.test_case(script, join('testes', f"merge_sort{i}.in"))

    def teste_11_ndigitos(self):
        script = 'n-digitos.py'
        self.exists(script)
        for i in range(5):
            self.test_case(script, join('testes', f"n-digitos{i}.in"))

    def teste_12_menor_caminho(self):
        script = 'menor_caminho.py'
        self.exists(script)
        for i in range(5):
            self.test_case(script, join('testes', f"menor_caminho{i}.in"))

if __name__ == '__main__':
    Task().run(True)