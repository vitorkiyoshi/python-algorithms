#!/usr/bin/env python

from os.path import isfile, join, getsize
from os import listdir
import re
import codecs
from subprocess import DEVNULL, PIPE, run, TimeoutExpired

import tempfile

from contextlib import contextmanager
import threading
import _thread

class TimeOutException(Exception):
    def __init__(self, message):
        super(TimeOutException, self).__init__(message)

@contextmanager
def time_limit(seconds, msg=''):
    timer = threading.Timer(seconds, lambda: _thread.interrupt_main())
    timer.start()
    try:
        yield
    except KeyboardInterrupt:
        raise TimeOutException("Timed out for operation {}".format(msg))
    finally:
        timer.cancel()


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

    def compare_stripped(self, left, right):
        return self.strip_spaces(left) == self.strip_spaces(right)

    def compare_files(self, out, res):
        left = self.read_file(out)
        right = self.read_file(res)
        return self.compare_stripped(left, right)

    def test_case(self, script, in_file_name):
        out_file_name = in_file_name.replace(".in", ".out")
        res_file_name = in_file_name.replace(".in", ".res")
        cmd = f"python3 {script}"
        with tempfile.TemporaryFile(mode="a") as i, open(out_file_name, "w") as o:
            i.write(f"{in_file_name}\n{out_file_name}")
            i.seek(0, 0)
            try:
                p = run(
                    ["python3", script],
                    stdin=i,
                    stdout=o,
                    stderr=DEVNULL,
                    encoding="utf8",
                    errors="ignore",
                    timeout=self.TIME_LIMIT_SECONDS,
                )
            except TimeoutExpired:
                assert False, f"comando {cmd} excedeu o tempo limite de {self.TIME_LIMIT_SECONDS}s"
        assert p.returncode == 0, f'falha ao executar "{cmd}"'
        assert self.compare_files(
            out_file_name, res_file_name
        ), f'{in_file_name}: arquivos "{out_file_name}" "{res_file_name}" diferem'

    def test_clousure(self, clousure):
        import traceback
        with time_limit(self.TIME_LIMIT_SECONDS):
            try:
                clousure()
            except TimeOutException:
                assert False, f"comando excedeu o tempo limite de {self.TIME_LIMIT_SECONDS}s"
            except Exception:
                tb = traceback.format_exc()
                assert False, f"algum erro ocorreu durante a execução:\n{tb}"

    def unittest_case(self, case, in_file_name):
        if case == "encode":
            out_file_name = in_file_name.replace(".pbm", ".out")
            res_file_name = in_file_name.replace(".pbm", ".p1c")
        else:
            out_file_name = in_file_name.replace(".p1c", ".out")
            res_file_name = in_file_name.replace(".p1c", ".pbm")

        open(out_file_name, "w").close()

        def encode_clousure():
            from modulo import (
                carregar_imagem_decodificada,
                codificar,
                escrever_imagem_codificada,
            )

            m, n, imagem = carregar_imagem_decodificada(in_file_name)
            codificacao = codificar(m, n, imagem)
            escrever_imagem_codificada(m, n, codificacao, out_file_name)

        def decode_closure():
            from modulo import (
                carregar_imagem_codificada,
                decodificar,
                escrever_imagem_decodificada,
            )

            m, n, codificacao = carregar_imagem_codificada(in_file_name)
            imagem = decodificar(m, n, codificacao)
            escrever_imagem_decodificada(m, n, imagem, out_file_name)

        if case == "encode":
            self.test_clousure(encode_clousure)
        else:
            self.test_clousure(decode_closure)

        message = f'{in_file_name}: arquivos "{out_file_name}" "{res_file_name}" diferem'
        assert self.compare_files(out_file_name, res_file_name), message

    def exists(self, file_name):
        assert isfile(file_name), f"você deve criar um arquivo {file_name}"

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
    def teste_0_codificacao(self):
        self.exists("modulo.py")
        for in_file_name in ["toy.pbm", "feep.pbm", "disquete.pbm"]:
            self.unittest_case("encode", join("testes", in_file_name))

    def teste_1_decodificacao(self):
        self.exists("modulo.py")
        for in_file_name in ["toy.p1c", "feep.p1c", "disquete.p1c"]:
            self.unittest_case("decode", join("testes", in_file_name))

    def teste_2_bordas(self):
        script = "bordas.py"
        self.exists(script)
        for test_file in ["cross.in", "elefant.in", "llama.in", "person.in", "teddy.in"]:
            self.test_case(script, join("testes", test_file))


if __name__ == "__main__":
    Task().run()
